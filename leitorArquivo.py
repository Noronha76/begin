texto = open('arquivo.txt')
for palavras in texto:
    palavra = palavras.split()
    for p in palavra:
        if len(p) > 13:
            print(p, 'maior que 13')
