# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





def get_links():
    url = input("Enter url: ")
    position = int(input("Enter position: "))
    repeat = int(input("Enter Repetition: "))
    all_url = []
    print("Retrieved: {}".format(url))
    for i in range(repeat):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        url = ""
        # Retrieve all of the anchor tags
        tags = soup('a')
        url_list = []
        for tag in tags:
            url_list.append(tag.get("href", None))
                       
        url = url_list[position - 1]
        all_url.append(url)
        print("Retrieved: {}".format(url))

get_links()
    
        #print(tag.get('href', None))
        #print('TAG:', tag)
        #print('URL:', tag.get('href', None))
        #print('Contents:', tag.contents[0])
        #print('Attrs:', tag.attrs)

    
        

        
