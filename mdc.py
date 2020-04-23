def mdc(a,b):
	r = a % b #essa operacao me parece estar com defeito...!!!!!!!!!
	print('r , a/b, b/r =>',r,(a/b),(b/r))
	if r == 0:
		print('MDC = ',n1)
	elif (a/b) == (b/r):
		print('MDC = ',r)
	else:
		print('ou nao existe ou ainda nao encontrei...!')


key = 'y'
while (key == 'y'):
	n1 = float(input('numero 1 : '))
	n2 = float(input('numero 2 : '))
	if (n1 > n2):
		n1, n2 = n2, n1
	mdc(n1,n2)
	key = input('continuar digite y : ')
