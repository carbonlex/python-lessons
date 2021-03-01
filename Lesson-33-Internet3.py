from urllib import request
import sys

myURL = "http://adv400.tripod.com/kartinka.jpg"
myFile = "flamingo.jpg"
myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'


try:
        print("Start Downloading file from: " + myURL)
        request.urlretrieve(myURL, myFile)
except Exception :
    print("Warning!")
    print(sys.exc_info()[1])
    exit

print("File Downloaded and saved at:" + myFile)