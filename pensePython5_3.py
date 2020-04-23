def rec_a():
	a = int(input('digite lado A inteiro positivo : '))
	if a > 0:
		print('ok')
		return a
	else:
		print('errado')
		rec_a()
def rec_b():
	b = int(input('digite lado B inteiro positivo : '))
	if b > 0:
		print('ok')
		return b
	else:
		print('errado')
		rec_b()
def rec_c():
	c = int(input('digite lado C inteiro positivo : '))
	if c > 0:
		print('ok')
		return c
	else:
		print('errado')
		rec_c()


va = rec_a()
vb = rec_b()
vc = rec_c()

if vb < va > vc:
	#print('A maior')
	if va < (vb+vc):
		print('forma TRIANGULO')
	else:
		print('Nao forma TRIANGULO')
elif va < vb > vc:
	#print('B maior')
	if vb < (va+vc):
		print('forma TRIANGULO')
	else:
		print('Nao forma TRIANGULO')
else:
	#print('C maior')
	if vc < (vb+va):
		print('forma TRIANGULO')
	else:
		print('Nao forma TRIANGULO')