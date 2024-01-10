#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv
"""Response header value"""

if __name__ == '__main__':
    with urlopen(argv[1]) as response:
        header = response.headers  # headers atribute or info() method
    print(header["X-Request-Id"])
