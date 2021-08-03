# dymo-scale-ros

## Installation

1. Install Python and Libusb
```
sudo apt-get install python libusb-1.0-0
```
2. Create text file `/etc/udev/rules.d/99-garmin.rules` with contents:
```
SUBSYSTEM=="usb", ATTR{idVendor}=="0922", ATTR{idProduct}=="8003", MODE="666"
```
3. Install python-dymo-scale
```
pip install python-dymo-scale
```

## Running
```
python scripts/dymo_scale_publisher.py
```