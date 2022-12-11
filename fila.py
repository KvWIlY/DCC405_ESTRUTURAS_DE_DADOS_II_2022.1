# n = indicando o número de pessoas na fila inicial
n = int(input())
#Alturas de cada pessoa da fila
alturas = input().split()

fila = []
out = []


for i in range(n):
    fila.insert(0, int(alturas[i]))

# q = ndicando o número de operações
q = int(input())

for i in range(q):
    # entrada de  três números inteiros T, I e X, descrevendo uma operação:
    # onde T indica o tipo da operação, I representa uma posição na fila e X é a 
    # altura H do novo competidor (na operação tipo 0) ou o parâmetro D (na operação do tipo 1). 
    in_info = input().split(' ')
    op = int(in_info[0])

    if op == 0:
        posicao = int(in_info[1])
        altura = int(in_info[2])
        fila.insert(len(fila) - posicao, altura)
    else:
        vt = 0
        posicao = int(in_info[1]) - 1
        T_A = fila[len(fila) - posicao - 1] + int(in_info[2])

        for i in range(len(fila) - posicao - 1, len(fila)):
            if (fila[i] > T_A):
                vt = len(fila) - i
                break
        out.append(vt)

for i in out:
    print(i)
