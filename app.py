from netmiko import ConnectHandler
import time,os

# Define the SSH connection parameters
hostname = '192.168.1.1'
port = 2210  # Default SSH port
username, password = os.getenv('WIFI_ADMIN').split(":")
timeout = 10  # Specify the timeout value in seconds

#First create the device object using a dictionary
CSR = {
    'device_type': 'zyxel_os',
    'ip': hostname,
    'port':port,
    'username': username,
    'password': password
}

# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)

# Then send the command and print the output
output = net_connect.send_command("zycli wan show")
lines = output.strip().split('\n')
row = [s for s in lines if 'Cellular WAN 1' in s]
if not 'Connected' in row[0]:
    net_connect.send_command("zycli reboot")
    time.sleep(60*5)
else:
    print('Connected')

# Finally close the connection
net_connect.disconnect()