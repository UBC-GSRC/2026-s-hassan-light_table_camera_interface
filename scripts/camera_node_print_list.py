from harvesters.core import Harvester
import toml

# --- LOAD CONFIG ---
config = toml.load('camera_configuration.toml')
CTI_FILE = config['driver']['cti_path']

# --- SETUP ---
h = Harvester()
h.add_file(CTI_FILE)
h.update()

ia = h.create()
nm = ia.remote_device.node_map

# ✅ Helper to convert numeric access → readable text
def access_to_str(val):
    return {
        0: "Not Implemented",
        1: "Not Available",
        2: "Write Only",
        3: "Read Only",
        4: "Read/Write"
    }.get(val, f"Unknown ({val})")

print("\n=== NODE DETAILS ===\n")

for name in dir(nm):
    if name.startswith("_"):
        continue

    try:
        node = getattr(nm, name)

        # Ensure it's a real GenICam feature
        if not hasattr(node, "value"):
            continue

        # Get current value safely
        try:
            val = node.value
        except Exception:
            val = "N/A"

        # Get access mode safely
        try:
            access = access_to_str(node.get_access_mode())
        except Exception:
            access = "Unknown"

        print(f"{name:30} | Value: {val} | Access: {access}")

    except Exception:
        pass

ia.destroy()