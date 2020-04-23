def fibonacci(n):
    if n < 2:
        print(' 0 , fim')
    else:
        print('Sequencia de fibonacci...')
        print(' 0 , 1 , ', end='')
        fibNovo = 1
        fibAntigo = 1
        for i in range(1, n - 1, 1):
            soma = fibNovo + fibAntigo
            print(soma, ', ', end='')
            fibAntigo = fibNovo
            fibNovo = soma
        print(' fim.')


while True:
    try:
        num = int(input("digite numero para a sequencia de fibonacci : "))
        fibonacci(num)
        c = input("deseja continuar? y->sim : ")
        if c == 'y':
            pass
        else:
            break
    except ValueError:
        print('Ops! Isto não é um número válido. Tente Novamente...')
