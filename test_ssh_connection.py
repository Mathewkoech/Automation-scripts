#python script to test ssh connection to server
import paramiko  # Import paramiko library

# Replace with your server details
server_ip = "" #server ip
username = "" #user
key_filename = ""#path to ssh keys 
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.Auto>
    client.connect(hostname=server_ip, username=user>
    print("SSH connection successful!")
    client.close()
except paramiko.AuthenticationException:
    print("Authentication failed!")