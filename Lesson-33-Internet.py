from urllib import request

myURL = "https://google.com"

response = request.urlopen(myURL)
mytext1 = response.readlines()
mytext2 = response.read()


print(response)
print(mytext2)

for line in mytext1:
    print(line)


