import re

mytext = "Vasya aaaaaa< Kolya-1991: Olesya 1981, aaaa@gmail.com" \
         "bbbbbbbbbbbb@gmail.com, Petya, gggggg, 1991, fkddsjfksjdf@com" \
         "piska, 2001, Lena Golovach, kfjskdfj@hooooolu.com, djihurda, olo" \
         "aloe@gmail.com, arbue@huli.com. bebebebebebebbebe, govno@com"

"""
\d = Any Digit 0-9
\D = Any non Digit
\w = Any Aphpabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = breakspace
\S = non breakspace

[0-9]{4}
[A-Z][a-z]+


"""

textlookfor = r"[0-9]{4}"
textlookfor = r"\w{6}\s"
textlookfor = r"[A-Z][a-z]+"
textlookfor = r"@\w+\.\w+"

allresults = re.findall(textlookfor, mytext)
print(allresults)
