inicio = int(input("digite numero inicial : "))
fim = int(input("digite o numero final : "))
for n in range(inicio, fim + 1, 1):
    print("taboada de %i" % n)
    for nn in range(1, 10, 1):
        print("%i X %i = %i" % (n, nn, (n * nn)))
