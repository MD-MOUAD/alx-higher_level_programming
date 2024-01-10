#!/usr/bin/python3
from urllib.request import urlopen
"""What's my status?"""

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf8"))
