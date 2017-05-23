#!/usr/bin/env python3.6
"""
Jack Kerr | 43561834
"""
import re
from sys import argv
import urllib.request
from urllib.parse import urlparse
from ftplib import FTP

def downloadHttp(url):
    segments = urlparse(url)
    filename = 'index' if segments.path == '' or segments.path == '/' else segments.path.split('/')[-1]
    site = None
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.HTTPError as g:
        print(g)
        return
    except urllib.error.URLError as e:
        print('URL Error: Hostname Not Found')
        return
    
    with open(filename, 'wb') as f:
        f.write(site.read())

def downloadFtp(url):
    segments = urlparse(url)
    path_segments = segments.path.strip('/').rsplit('/', 1)
    filename = path_segments[-1]
    folder = path_segments[0] if path_segments[0] != path_segments[-1] else None
    try:
        ftp = FTP(segments.netloc)
    except:
        print('Incorrect hostname')
        return
    ftp.login('anonymous','coms3200@uq.edu.au')
    if folder is not None:
        try:
            ftp.cwd(folder)
        except:
            print("The folder does not exist on the FTP server")
            return
    try:
        ftp.retrbinary(f'RETR {filename}', open(filename, 'wb').write)
    except:
        print("The file could not be found on the FTP server")


def main():
    # Do some arg checking
    assert len(argv) == 2
    url = argv[1]

    if re.match("http:\/\/(.*)", url):
        downloadHttp(url)
    elif re.match("ftp:\/\/(.*)", url):
        downloadFtp(url)
    else:
        print("Invalid Protocol")

if __name__ == "__main__":
    main()
