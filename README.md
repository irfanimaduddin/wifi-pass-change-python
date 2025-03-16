# WiFi Password Changer (Python)

An automated tool built with Python and Selenium WebDriver to change WiFi passwords on router web interface.

## Description

This script automates the process of changing WiFi passwords for both 2.4GHz and 5GHz networks on supported routers. It uses Selenium WebDriver to interact with the router's web interface.

## Prerequisites

- Python 3
- Selenium (v4.25.0 or higher)

## Installation

1. Clone the repository
```bash
git clone https://github.com/irfanimaduddin/wifi-pass-change-python.git
cd wifi-pass-change-python
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Update the ChromeDriver path in the script to match your system setup

## Usage

Run the script with the following command:

```bash
python change_pass.py --ip="192.168.1.1" --auser="admin" --apass="admin123" --nwpass="new_wifi_password"
```

### Arguments

- `--ip`: Router IP address (required)
- `--auser`: Admin username for router login (required)
- `--apass`: Admin password for router login (required)
- `--nwpass`: New WiFi password to set (required)

### Help

To see all available options:

```bash
python change_pass.py --help
```

## Features

- Automated login to router interface
- Changes password for both 2.4GHz and 5GHz networks
- Headless operation (runs in background)
- Validation of current and new passwords
- Password visibility toggle handling
- Automatic iframe navigation
- Console output of changes made

## Example Output

```
Changing pass for SSID: MyNetwork_2G
Current Password: oldpassword123
New Password: newpassword123

Changing pass for SSID: MyNetwork_5G
Current Password: oldpassword123
New Password: newpassword123
```

## Notes

- The script is configured to run in headless mode by default
- Includes wait times to account for page loading
- Automatically handles iframe switching
- Validates password changes before completing

## Security Considerations

- Avoid storing credentials in the script
- Use secure passwords
- Run on trusted networks only

## Known Limitations
- Specific to routers with similar web interface structure
- Requires Chrome browser and ChromeDriver
- No error handling for invalid credentials
- Fixed wait times may need adjustment

## You may see
- [Wifi Pass Change with JavaScript](https://github.com/irfanimaduddin/wifi-pass-change-js)

## Author

Irfan Imaduddin
