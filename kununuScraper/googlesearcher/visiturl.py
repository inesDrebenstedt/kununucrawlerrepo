import time
# read the data from the URL and print it Python 3 variant
#
import urllib.request
# open a connection to a URL using urllib
global htmlResultBody
def makeUrlRequest(url):
    time.sleep(10)
    webUrl  = urllib.request.urlopen(url)

    #get the result code and print it
    print ("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    htmlResultBody = webUrl.read()
    if isinstance(htmlResultBody, str):
        print('htmlResultBody is of type string!')
    return htmlResultBody


