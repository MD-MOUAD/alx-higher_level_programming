#!/usr/bin/python3
"""module doc"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(f"\t- type: {type(response.text)}\n\t- content: {response.text}")
