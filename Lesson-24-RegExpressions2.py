import re

input_filename = "dumpfile.json"
result_filename = "results.json"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[\w._-]+@[\w._-]+\.[\w.]+"


results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")



print("Total: " + str(len(results)))