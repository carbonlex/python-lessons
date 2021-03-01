from urllib import request, parse
import sys

myURL = "http://www.google.com/search?"
value = {'q': 'Royksopp'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myURL = myURL + mydata
    req = request.Request(myURL, headers=myheader)
    response = request.urlopen(req)
    response = response.readlines()
    for line in response:
        print(line)

except Exception:
    print("Error occurred during web request!!")
    print(sys.exc_info()[1])