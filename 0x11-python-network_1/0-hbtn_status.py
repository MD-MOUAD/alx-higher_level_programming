#!/usr/bin/python3
from urllib.request import urlopen
"""What's my status?"""

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
    print(f"\t- type: {type(body)}\n\t- content: {body} \n\t\
        - utf8 content: {body.decode('utf8')}")
