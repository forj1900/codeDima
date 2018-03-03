file = open("textToCode.txt")
soursce = file.read()
result = ""

alphabet = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZабвгдеёжзиклмнопрстуфхцчшщьъыэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
alphabet2 = "IпtЖTGRkдчecШМУlxwХцлсOщЬДQИЧГmЕгЁSэMbCоKXеDкжЫхьPыЭЯъuLgWHЗтФфpуiНОdВвКYNшАyяZаЛТбzhнЩEрrюBБoмСиЦЪAЮVзРqПaёnfvUsF"


def code(charS):
	count = 0
	for c in alphabet:
		if c == charS:
			return alphabet2[count]
		count += 1

	return charS

for charSource in soursce:
	result = result + code(charSource)

print (soursce)
print (result)

file.close()
file = open("ResultOfCode.txt", 'w')
file.write(result)
file.close()

