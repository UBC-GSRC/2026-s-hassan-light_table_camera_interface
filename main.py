import os
import cv2
import threading
import queue
import time
import toml
import tkinter as tk
from tkinter import filedialog
from harvesters.core import Harvester
import logging

# ===============================
# --- QUIET HARVESTER LOGGING ---
# ===============================
logging.getLogger('harvesters.core').setLevel(logging.CRITICAL)

# ===============================
# --- LOAD CONFIG ---
# ===============================
config = toml.load('config.toml')

CTI_FILE = config['driver']['cti_path']

OFFSET_X = config['roi']['offset_x']
OFFSET_Y = config['roi']['offset_y']
WIDTH = config['roi']['width']
HEIGHT = config['roi']['height']

FRAME_RATE = config['camera']['frame_rate']
EXPOSURE_TIME = config['camera']['exposure_time']

HOURS = config['capture']['hours']
MINUTES = config['capture']['minutes']
SECONDS = config['capture']['seconds']
MAX_FRAMES = config['capture']['max_frames']
SAVE_IMAGES = config['capture']['save_images']

# ===============================
# --- DIRECTORY PICKER ---
# ===============================
if SAVE_IMAGES:
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    SAVE_DIR = filedialog.askdirectory(title="Select folder to save images")
    root.destroy()

    if not SAVE_DIR:
        print("No directory selected. Exiting.")
        exit()

    print(f"Saving images to: {SAVE_DIR}")
    os.makedirs(SAVE_DIR, exist_ok=True)
else:
    SAVE_DIR = None
    print("Image saving disabled.")

# ===============================
# --- CAPTURE LIMIT SETUP ---
# ===============================
MAX_DURATION_SEC = HOURS * 3600 + MINUTES * 60 + SECONDS

print(f"Max duration: {'UNLIMITED' if MAX_DURATION_SEC == 0 else MAX_DURATION_SEC}")
print(f"Max frames: {'UNLIMITED' if MAX_FRAMES == -1 else MAX_FRAMES}")

# ===============================
# --- QUEUE + WRITER THREAD ---
# ===============================
if SAVE_IMAGES:
    img_queue = queue.Queue(maxsize=1000)

    def disk_writer():
        while True:
            item = img_queue.get()
            if item is None:
                break
            img, filename = item
            cv2.imwrite(filename, img)
            img_queue.task_done()

    writer_thread = threading.Thread(target=disk_writer, daemon=True)
    writer_thread.start()
else:
    img_queue = None

# ===============================
# --- HARVESTER SETUP ---
# ===============================
h = Harvester()
h.add_file(CTI_FILE)
h.update()
ia = h.create()
nm = ia.remote_device.node_map

# ===============================
# --- APPLY CAMERA SETTINGS ---
# ===============================
try:
    nm.OffsetX.value = 0
    nm.OffsetY.value = 0
    nm.Width.value = WIDTH
    nm.Height.value = HEIGHT
    nm.OffsetX.value = OFFSET_X
    nm.OffsetY.value = OFFSET_Y

    print(f"ROI Set: {WIDTH}x{HEIGHT} at ({OFFSET_X}, {OFFSET_Y})")

    if hasattr(nm, "ExposureAuto"):
        nm.ExposureAuto.value = "Off"
    nm.ExposureTime.value = EXPOSURE_TIME

    if hasattr(nm, "AcquisitionFrameRateEnable"):
        nm.AcquisitionFrameRateEnable.value = True
    nm.AcquisitionFrameRate.value = FRAME_RATE

    print(f"Exposure: {EXPOSURE_TIME} us")
    print(f"Frame Rate: {FRAME_RATE} Hz")

except Exception as e:
    print(f"Camera setup warning: {e}")

# ===============================
# --- START ACQUISITION ---
# ===============================
ia.start()
print("Press 's' to start, 'e' to stop, 'q' to quit.")

# Fix OpenCV window
cv2.destroyAllWindows()

aspect_ratio = WIDTH / HEIGHT
display_height = 600
display_width = int(display_height * aspect_ratio)

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow("Camera", display_width, display_height)

# ===============================
# --- RUNTIME STATE ---
# ===============================
count = 0
record_count = 0
running = True
saving_enabled = False
record_start_time = None
last_display = time.perf_counter()

# ===============================
# --- MAIN LOOP ---
# ===============================
try:
    while running:

        # TIMER ONLY ACTIVE DURING RECORDING
        if saving_enabled and record_start_time is not None:
            elapsed = time.perf_counter() - record_start_time
        else:
            elapsed = 0

        # STOP CONDITIONS
        if SAVE_IMAGES and saving_enabled and MAX_DURATION_SEC > 0:
            if elapsed >= MAX_DURATION_SEC:
                print("Time limit reached.")
                saving_enabled = False
                record_start_time = None
                continue

        if MAX_FRAMES != -1 and count >= MAX_FRAMES:
            print("Frame limit reached.")
            break

        try:
            buffer = ia.fetch()
        except KeyboardInterrupt:
            print("\nUser interrupted.")
            break
        except Exception:
            break

        with buffer:

            count += 1

            # ALWAYS CHECK KEYS
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                running = False

            elif key == ord('s'):
                if SAVE_IMAGES:
                    saving_enabled = True
                    record_count = 0
                    record_start_time = time.perf_counter()
                    print(">>> Recording STARTED")
                else:
                    print("Saving disabled in config")

            elif key == ord('e'):
                if saving_enabled:
                    print(f">>> Recording STOPPED ({record_count} frames)")
                saving_enabled = False
                record_start_time = None

            # RAW IMAGE
            component = buffer.payload.components[0]
            raw = component.data.reshape(component.height, component.width)

            # DISPLAY IMAGE (copy)
            display_img = raw.copy()

            now = time.perf_counter()

            if now - last_display > 0.03:

                # OVERLAY
                if saving_enabled:
                    blink = int(now * 2) % 2 == 0
                    if blink:
                        cv2.putText(display_img, "REC", (20, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,), 3)
                        cv2.circle(display_img, (110, 30), 10, (255,), -1)
                else:
                    cv2.putText(display_img, "LIVE", (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (200,), 2)

                # INFO
                cv2.putText(display_img, f"Frames: {record_count}", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,), 2)

                if saving_enabled:
                    cv2.putText(display_img, f"{elapsed:.1f}s", (20, 110),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,), 2)

                cv2.imshow("Camera", display_img)
                last_display = now

                # Window fix
                try:
                    _, _, _, h = cv2.getWindowImageRect("Camera")
                    if h < 100:
                        cv2.resizeWindow("Camera", display_width, display_height)
                except:
                    pass

            # SAVE RAW ONLY
            if SAVE_IMAGES and saving_enabled:
                if not img_queue.full():
                    
                    ns = time.time_ns()
                    sec = ns // 1_000_000_000
                    sub = ns % 1_000_000_000

                    filename = os.path.join(SAVE_DIR, f"{sec}_{sub:09d}.jpg")

                    img_queue.put((raw.copy(), filename))
                    record_count += 1

except KeyboardInterrupt:
    print("\nUser interrupted (outer).")

# ===============================
# --- CLEAN SHUTDOWN ---
# ===============================
print("Shutting down...")

try:
    if ia.is_acquiring():
        ia.stop()
except:
    pass

try:
    ia.destroy()
except:
    pass

if SAVE_IMAGES:
    try:
        img_queue.put(None)
        writer_thread.join()
    except:
        pass

cv2.destroyAllWindows()
print("Done!")