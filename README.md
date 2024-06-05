# Zyxel-NR5103-5G-THREE-WIFI-Router-checker
This is a python script to check the WAN connectivity of  5G THREE WIFI 6 Home Router 2022 (Zyxel NR5103) Dual Band

# WAN Connectivity Checker for 5G THREE WIFI 6 Home Router (Zyxel NR5103)

<img src="https://i.ebayimg.com/images/g/pvwAAOSwpBZkAdxV/s-l1600.webp" alt="5G THREE WIFI 6 Home Router 2022 (Zyxel NR5103)" width="300"/>

This Python script checks the WAN connectivity of the "5G THREE WIFI 6 Home Router 2022 (Zyxel NR5103) Dual Band" wifi router.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Access to the router's administrative interface via SSH.
- The `paramiko` library for SSH connections. You can install it using pip:

```bash
pip install paramiko
```

## Setting Up Environment Variables

You need to set the WIFI_ADMIN environment variable, which should contain the admin username and password for the router in the format username:password. For example:

```bash
export WIFI_ADMIN='admin:yourpassword'
```
## Script Configuration

Define the SSH connection parameters in the script:
```python
# Define the SSH connection parameters
hostname = '192.168.1.1'
port = 2210  # Default SSH port
username, password = os.getenv('WIFI_ADMIN').split(":")
timeout = 10  # Specify the timeout value in seconds
```
