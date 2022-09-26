linha_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
coluna_matriz_a = int(input("Digite a quantidade de elementos de cada linhaA: "))
linha_matriz_b = int(input("\nDigite a quantidade de linhas da matriz B: "))
coluna_matriz_b = int(input("Digite a quantidade de elementos de cada linha B: "))
if linha_matriz_a == linha_matriz_b and coluna_matriz_a == coluna_matriz_b:
    matriz_a = []
    for contador_linha_a in range(linha_matriz_a):
        linha_a = []
    for contador_coluna_a_a in range(coluna_matriz_a):
        elemento_a = int(input("Digite um número para atribuir a matriz A:"))
        linha_a.append(elemento_a)
        matriz_a.append(linha_a)
        matriz_b = []
    for contador_linha_b in range(linha_matriz_b):
        linha_b = []
    for contador_coluna_b in range(coluna_matriz_b):
        elemento_b = int(input("Digite um número para atribuir a matriz B:"))
        linha_b.append(elemento_b)
    matriz_b.append(linha_b)
    print(f"Matriz A - Dimensão ({linha_matriz_a}x{coluna_matriz_a})")
    for aux1 in range(linha_matriz_a):
        print(matriz_a[aux1])
        print(f"\nMatriz B - Dimensão ({linha_matriz_b}x{coluna_matriz_b})")
    for aux2 in range(linha_matriz_b):
        print(matriz_b[aux2])
    if linha_matriz_a == linha_matriz_b and coluna_matriz_a == coluna_matriz_b :
        linha_matriz_c = (linha_matriz_a + linha_matriz_b) // 2
        coluna_matriz_c = (coluna_matriz_a + coluna_matriz_b) // 2
        matriz_c = []
    for contador_linha_c in range(linha_matriz_c):
        linha_c = []
        for contador_coluna_c in range(coluna_matriz_c):
            elemento_c = matriz_a[contador_linha_c][contador_coluna_c] + matriz_b[contador_linha_c][contador_coluna_c]
            linha_c.append(elemento_c)
        matriz_c.append(linha_c)
    print(f"\nMatriz C - Soma das Matrizes")
    for aux3 in range(linha_matriz_c):
        print(matriz_c[aux3])
else:
    print(f"\nA SOMA NÃO É POSSÍVEL, POIS, AS DIMENSÕES DAS MATRIZES NÃO SÃO IGUAIS!")
