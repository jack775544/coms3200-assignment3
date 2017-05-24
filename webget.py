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
    # Segment up the url
    segments = urlparse(url)
    filename = 'index' if segments.path == '' or segments.path == '/' else segments.path.split('/')[-1]
    site = None
    try:
        # Attempt to download the site
        site = urllib.request.urlopen(url)
    except urllib.error.HTTPError as g:
        # Invalid file (404), throw error
        print(g)
        return
    except urllib.error.URLError as e:
        # Invalid hostname, throw error
        print('URL Error: Hostname Not Found')
        return
    
    # Save the file
    with open(filename, 'wb') as f:
        f.write(site.read())

def downloadFtp(url):
    # Segment the url
    segments = urlparse(url)
    path_segments = segments.path.strip('/').rsplit('/', 1)
    filename = path_segments[-1]
    folder = path_segments[0] if path_segments[0] != path_segments[-1] else None

    try:
        # Set up ftp connection
        ftp = FTP(segments.netloc)
    except:
        # If this fails the hostname is wrong
        print('Incorrect hostname')
        return
    # Login as anon
    ftp.login('anonymous','coms3200@uq.edu.au')
    if folder is not None:
        try:
            # Change to the specified folder
            ftp.cwd(folder)
        except:
            # Error if the folder does not exist
            print("The folder does not exist on the FTP server")
            return
    try:
        # Download and save the file
        ftp.retrbinary(f'RETR {filename}', open(filename, 'wb').write)
    except:
        # Error if the file is not there
        print("The file could not be found on the FTP server")


def main():
    # Do some arg checking
    assert len(argv) == 2
    url = argv[1]

    # Match the protocol
    if re.match("http:\/\/(.*)", url):
        downloadHttp(url)
    elif re.match("ftp:\/\/(.*)", url):
        downloadFtp(url)
    else:
        # Error if the wrong protocol is given
        print("Invalid Protocol")

if __name__ == "__main__":
    main()
