#!/usr/bin/env python3

import json
from base64 import b64encode

import requests
import urllib3
from requests.auth import HTTPBasicAuth

# Configuration
# endpoint = '/agents?select=lastKeepAlive&select=id&status=disconnected'
# {protocol}://{host}:{port}/syscollector/{agent_id}/packages
endpoint = '/agents'

protocol = 'https'
host = '10.250.0.203'
port = '55000'
user = 'wazuh-wui'
password = 'wazuh-wui'

# Disable insecure https warnings (for self-signed SSL certificates)
requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Functions
def get_response(url, headers, verify=False):
    """Get API result"""
    request_result = requests.get(url, headers=headers, verify=verify)

    if request_result.status_code == 200:
        return json.loads(request_result.content.decode())
    else:
        raise Exception(f"Error obtaining response: {request_result.json()}")

# Variables
base_url = f"{protocol}://{host}:{port}"
login_url = f"{base_url}/security/user/authenticate"
basic_auth = f"{user}:{password}".encode()
headers = {'Authorization': f'Basic {b64encode(basic_auth).decode()}'}
headers['Authorization'] = f'Bearer {get_response(login_url, headers)["data"]["token"]}'
print("\nLogin request ...\n")

#Request
response = get_response(base_url + endpoint, headers)

# WORK WITH THE RESPONSE AS YOU LIKE
print(json.dumps(response, indent=4, sort_keys=True), file=open('output.txt', 'w'))

