soursce = "This is the string to code! А это просто так, тексты, с буквой Ы"
result = ""

alphabet = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZабвгдеёжзиклмнопрстуфхцчшщьъыэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
alphabet2 = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯабвгдеёжзиклмнопрстуфхцчшщьыъэюя"


def code(charS):
	pos = alphabet.find(charS)
	if pos >= 0: 
		return alphabet2[pos]
	return charS
	'''
	count = 0
	for c in alphabet:
		if c == charS:
			return alphabet2[count]
		count += 1

	return charS
	'''

for charSource in soursce:
	result = result + code(charSource)

print (soursce)
print (result)

