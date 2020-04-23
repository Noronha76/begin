t = '-' * 4
s = ' ' * 4
l1 = '+' + t + '+' + t + '+'
l2 = '|' + s + '|' + s + '|'
def repLinhas(l,n):
	for i in range(n):
		print(l)
print(l1)
for i in range(2):
	repLinhas(l2,4)
	print(l1)
