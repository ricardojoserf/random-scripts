import sys

dict = [{'n':'222','c':'c'},{'n':'333','c':'f'},{'n':'444','c':'i'},{'n':'555','c':'l'},{'n':'666','c':'o'},{'n':'7777','c':'s'},{'n':'777','c':'r'},{'n':'888','c':'v'},{'n':'9999','c':'z'},{'n':'999','c':'y'},{'n':'22','c':'b'},{'n':'33','c':'e'},{'n':'44','c':'h'},{'n':'55','c':'k'},{'n':'66','c':'n'},{'n':'77','c':'q'},{'n':'88','c':'u'},{'n':'99','c':'x'},{'n':'2','c':'a'},{'n':'3','c':'d'},{'n':'4','c':'g'},{'n':'5','c':'j'},{'n':'6','c':'m'},{'n':'7','c':'p'},{'n':'8','c':'t'},{'n':'9','c':'w'}]
text = sys.argv[1]

for i in dict:
	if i['n'] in text:
		text = text.replace(i['n'],i['c'])
print text
