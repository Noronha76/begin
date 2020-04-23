word = 'banana'
if 'a' in word:
	print('existe a letra a na strig banana')
count = 0
for letter in word:
	if letter == 'a':
		count += 1
print('ocorrencias de a na string banana : ',count)
count = word.find('a')
print('primeira posicao de a na string : ',count)
count = word.find('na')
print('primeira posicao da seq. NA na string : ',count)
count = word.find('na',3)
print('posicao da seq. NA na string a partir da posicao 3 : ',count)
