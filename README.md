# 2026-s-hassan-light_table_camera_interface
The interface needed to view images and save images from the SVS-Vistek EXO cameras. They are GenICam based USB3 Vision cameras which has proven to be an annoyance for premade camera configuration tools.

## Installing the Dependencies

Make a virtual environment from the `requirements.txt` file if not done already.
```
python -m venv .venv_lighttable
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Operating the Camera

Edit the config.toml file as necessary, then Run 

```
python main.py

# Select the folder to save images to
# Press 's' to start saving, 'e' to stop, 'q' or 'Ctrl+C' to quit. Make sure to click the camera feed window before using keyboard controls.
```

Press 

## Camera Configuration

The current script offers the following adjustments:

1. Frame rate
2. Exposure time
3. Crop width / height
4. Crop offset x and y

Other adjustments are possible... check the 'Available Nodes' below to see if you need to have other adjustablility available. 

## Available Nodes 

| Node Name | Value | Writability | 
| --- | --- | --- |
AccessPrivilegeAvailable       | Value: False | Read Only
AcquisitionFrameRate           | Value: 5.0 | Read/Write
AcquisitionMode                | Value: Continuous | Read/Write
BinningHorizontal              | Value: 1 | Read/Write
BinningVertical                | Value: 1 | Read/Write
BlackLevelRaw                  | Value: 0 | Read/Write
BlackLevelSelector             | Value: All | Read/Write
CustomerDataIndex              | Value: 0 | Read/Write
CustomerDataValue              | Value: 4294967295 | Read/Write
CustomerID                     | Value: 0 | Read/Write
CustomerIDKey                  | Value: 0 | Read/Write
CustomerValue                  | Value: 0 | Read/Write
CustomerValueKey               | Value: 0 | Read/Write
DebounceDuration               | Value: 66666 | Read/Write
DefectPixelCorrectionEnable_Control | Value: Off | Read/Write
DefectPixelCorrectionMark_Control | Value: Off | Read/Write
DefectPixelCorrection_MapMaxSize | Value: 32750 | Read Only
DefectPixelCorrection_MapSelect | Value: factory | Read/Write
DefectPixelCorrection_MapSize  | Value: 3110 | Read Only
DefectPixelCorrection_Revision | Value: 3 | Read Only
DeviceFirmwareVersion          | Value: Build 2963 Firmware Dec  2 2020 11:27:51 | Read Only
DeviceID                       | Value: 58469 | Read Only
DeviceManufacturerInfo         | Value: Build 2963 Firmware Dec  2 2020 11:27:52 | Read Only
DeviceModelName                | Value: exo304MU3 | Read Only
DeviceTapGeometry              | Value: Geometry_1X_1Y | Read/Write
DeviceTemperature              | Value: 47.0 | Read Only
DeviceTemperatureSelector      | Value: Mainboard | Read/Write
DeviceUserID                   | Value:  | Read/Write
DeviceVendorName               | Value: SVS-VISTEK GmbH | Read Only
DeviceVersion                  | Value: 1.7.2 | Read Only
EndianessRegistersSupported    | Value: True | Read Only
ExposureAuto                   | Value: Off | Read/Write
ExposureAutoOrder              | Value: True | Read/Write
ExposureMode                   | Value: Timed | Read/Write
ExposureTime                   | Value: 20000.0 | Read/Write
ExposureTimeMax                | Value: 30000.0 | Read/Write
ExposureTimeMin                | Value: 1000.0 | Read/Write
FB_Critical_Reset              | Value: 250 | Read Only
FB_Critical_Set                | Value: 1500 | Read Only
FB_Critical_Watermark          | Value: 1856 | Read Only
FB_Discard_Count               | Value: 0 | Read Only
FB_Statistic                   | Value: 2 | Read Only
FB_UsedDW_Max                  | Value: 80 | Read Only
FamilyRegisterAvailable        | Value: True | Read Only
Gain                           | Value: 0.0 | Read/Write
GainAuto                       | Value: Off | Read/Write
GainAutoLevel                  | Value: 100 | Read/Write
GainAutoMax                    | Value: 48.0 | Read/Write
GainAutoMin                    | Value: 0.0 | Read/Write
GainRaw                        | Value: 0 | Read/Write
GainSelector                   | Value: All | Read/Write
GainSpeed                      | Value: Standard | Read/Write
GainSpeedTime                  | Value: 60 | Read/Write
Gamma                          | Value: 1.0 | Read/Write
GenCPVersionMajor              | Value: 1 | Read Only
GenCPVersionMinor              | Value: 3 | Read Only
Height                         | Value: 2000 | Read/Write
HeightMax                      | Value: 3000 | Read Only
LUTEnable                      | Value: False | Read/Write
LUTIndex                       | Value: 0 | Read/Write
LUTSelector                    | Value: Luminance | Read/Write
LUTValue                       | Value: 0 | Read/Write
LensControlFocus               | Value: 0 | Read/Write
LensControlIris                | Value: 0 | Read/Write
LensControlType                | Value: none | Read/Write
LineFormat                     | Value: Undefined | Read Only
LineInverter                   | Value: False | Read/Write
LineMode                       | Value: Output | Read Only
LineSelector                   | Value: Line1 | Read/Write
LineSource                     | Value: Strobe0 | Read/Write
LineStatus                     | Value: False | Read Only
LineStatusAll                  | Value: 244813135920 | Read Only
LogicFunction                  | Value: AND_Function | Read/Write
MessageChannelSupported        | Value: False | Read Only
OffsetX                        | Value: 1000 | Read/Write
OffsetY                        | Value: 1000 | Read/Write
PWMChange0                     | Value: 0 | Read/Write
PWMChange1                     | Value: 0 | Read/Write
PWMChange2                     | Value: 0 | Read/Write
PWMChange3                     | Value: 0 | Read/Write
PWMEnable                      | Value: False | Read/Write
PWMMax                         | Value: 66666 | Read/Write
PayloadSize                    | Value: 6000000 | Read Only
PixelColorFilter               | Value: None | Read Only
PixelDynamicRangeMax           | Value: 255 | Read Only
PixelDynamicRangeMin           | Value: 1 | Read Only
PixelFormat                    | Value: Mono8 | Read/Write
PixelSize                      | Value: Bpp8 | Read Only
PrescaleDivisor                | Value: 2 | Read/Write
RegisterAddress                | Value: 0 | Read/Write
ReverseX                       | Value: False | Read/Write
ReverseY                       | Value: False | Read/Write
SBRMSupported                  | Value: True | Read Only
SensorHeight                   | Value: 3000 | Read Only
SensorShutterMode              | Value: Global | Read/Write
SensorWidth                    | Value: 4096 | Read Only
SeqCount                       | Value: 1 | Read/Write
SeqEnable                      | Value: False | Read/Write
SeqInterval                    | Value: 0 | Read/Write
SeqLoop                        | Value: False | Read/Write
SeqPulseAStart                 | Value: 0 | Read/Write
SeqPulseAStop                  | Value: 0 | Read/Write
SeqPulseBStart                 | Value: 0 | Read/Write
SeqPulseBStop                  | Value: 0 | Read/Write
SeqSelector                    | Value: 0 | Read/Write
SeqTriggermode                 | Value: RisingEdge | Read/Write
Shading_Control                | Value: Off | Read/Write
Shading_MapSelect              | Value: ShadingMap0 | Read/Write
Shading_Revision               | Value: 2 | Read Only
StringEncoding                 | Value: 0 | Read Only
StrobeDelay                    | Value: 0.0 | Read/Write
StrobeDuration                 | Value: 0.0 | Read/Write
StrobePolarity                 | Value: negative | Read/Write
StrobeSelector                 | Value: Strobe0 | Read/Write
TLParamsLocked                 | Value: 0 | Read/Write
TestPendingAck                 | Value: 3000 | Read/Write
TimestampSupported             | Value: True | Read Only
TriggerActivation              | Value: RisingEdge | Read/Write
TriggerDelay                   | Value: 0.0 | Read/Write
TriggerMode                    | Value: Off | Read/Write
TriggerSelector                | Value: AcquisitionStart | Read/Write
TriggerSource                  | Value: Software | Read/Write
U3VCPCapability                | Value: 0 | Read Only
U3VCPCapabilityHigh            | Value: 0 | Read Only
U3VCPCapabilityLow             | Value: 0 | Read Only
U3VCPConfigurationHigh         | Value: 0 | Read/Write
U3VCPConfigurationLow          | Value: 0 | Read/Write
U3VCPEIRMAvailable             | Value: False | Read Only
U3VCPIIDC2Available            | Value: False | Read Only
U3VCPSIRMAvailable             | Value: True | Read Only
U3VCurrentSpeed                | Value: 8 | Read Only
U3VDeviceCapability            | Value: 0 | Read Only
U3VDeviceCapabilityHigh        | Value: 0 | Read Only
U3VDeviceCapabilityLow         | Value: 0 | Read Only
U3VDeviceConfigurationHigh     | Value: 0 | Read/Write
U3VDeviceConfigurationLow      | Value: 0 | Read/Write
U3VMaxAcknowledgeTransferLength | Value: 1024 | Read Only
U3VMaxCommandTransferLength    | Value: 1024 | Read Only
U3VMaxDeviceResponseTime       | Value: 6000 | Read Only
U3VNumberOfStreamChannels      | Value: 1 | Read Only
U3VVersionMajor                | Value: 1 | Read Only
U3VVersionMinor                | Value: 1 | Read Only
UserNameAvailable              | Value: True | Read Only
UserOutputSelector             | Value: UserOutput0 | Read/Write
UserOutputValue                | Value: False | Read/Write
UserOutputValueAll             | Value: 0 | Read/Write
UserOutputValueAllMask         | Value: 31 | Read/Write
UserSetDefault                 | Value: UserSet1 | Read/Write
UserSetSelector                | Value: UserSet1 | Read/Write
Width                          | Value: 3000 | Read/Write
WidthMax                       | Value: 4096 | Read Only
WrittenLengthFieldSupported    | Value: True | Read Only