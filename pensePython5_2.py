print('teste de teorema de Fermat')
print('a**n+b**n!=c**n para n maior que dois')
def rec_n():
	n = int(input('digite n inteiro maior que 2 : '))
	if n > 2:
		print('ok')
		return n
	else:
		print('errado')
		rec_n()
def rec_a():
	a = int(input('digite A inteiro positivo : '))
	if a > 0:
		print('ok')
		return a
	else:
		print('errado')
		rec_a()
def rec_b():
	b = int(input('digite B inteiro positivo : '))
	if b > 0:
		print('ok')
		return b
	else:
		print('errado')
		rec_b()
def rec_c():
	c = int(input('digite C inteiro positivo : '))
	if c > 0:
		print('ok')
		return c
	else:
		print('errado')
		rec_c()

vn = rec_n()		
va = rec_a()
vb = rec_b()
vc = rec_c()
if (va**vn + vb**vn != vc**vn):
	print('teste de teorema de Fermat CONFIRMADO !!!')
else:
	print('teste de teorema de Fermat REPROVADO !!!')