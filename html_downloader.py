import urllib.request
from urllib.parse import quote
import string

class Html_Downloader(object):

    def download(self,url):
        if url is None:
            return None
        
        s = quote(url,safe=string.printable)#中文转
        response = urllib.request.urlopen(s)

        if response.getcode() != 200:
        	return None

        return response.read()
