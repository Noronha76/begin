def fatorial(n):
    if not isinstance(n, int):
        print('somente numeros inteiros positivos')
        return
    elif n < 0:
        print('somente numeros inteiros positivos')
        return
    elif n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


while True:
    try:
        n = int(input("digite numero para o fatorial : "))
        print(fatorial(n))
        c = input("deseja continuar? y->sim : ")
        if c == 'y':
            pass
        else:
            break
    except ValueError:
        print('Ops! Isto não é um número válido. Tente Novamente...')
