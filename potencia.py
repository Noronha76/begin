
def div(a,b):
	if a % b == 0:
		return a/b
	else:
		print('divisao nao inteira')
		return 0

def is_power(a,b):
	if a % b == 0:
		if div(a,b) % b == 0:
			print('Potencia')
		else:
			print('Nao e Potencia')
	else:
		print('Nao e Potencia')

key = 'y'
while (key == 'y'):
	n = int(input('base : '))
	p = int(input('potencia : '))
	is_power(p,n)
	key = input('continuar digite y : ')
