#!/usr/bin/python3
from urllib.request import urlopen
"""What's my status?"""

if __name__ == '__main__':
    with urlopen('http://madaralx.tech') as response:
        body = response.read()
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf8"))
