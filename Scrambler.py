#найти в интернет как перемешивать массивы

import random

alfabet = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZабвгдеёжзиклмнопрстуфхцчшщьъыэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"

listAlfabet = set()

for c in alfabet:
	listAlfabet.add(c)

print (listAlfabet)

codeString = ""
for c in listAlfabet:
	codeString = codeString + c
	
print ("codesting is: ", codeString)
print ("length of codesting is: ", len(codeString))



n = len(alfabet)

for c in range(n):
	#mixchats()
	#print (alfabet[c])
	alfabet[c]

print ("alfabet is: ", alfabet)
print ("length of alfabet is: ", len(alfabet))

#print(sorted(codeString))

	