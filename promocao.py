#n = representando o número de cidades da Linearlândia
n = int(input())
grafh = [[] for i in range(n)]
vt = [[-1]*n, [-1]*n]

for i in range(n-1):
    # três inteiros A, B e E, indicando que existe 
    # uma rodovia entre as cidades A e B e E que a linha de ônibus entre elas
    a,b,e = map(int,input().split())
    grafh[a - 1].append((b - 1, e))
    grafh[b - 1].append((a - 1, e))

# maior caminho
def max_way(vertice, empresa_anterior):
    m = 0 
    for vizinho, empresa in grafh[vertice]:
        if empresa != empresa_anterior:
            caminho = vt[empresa][vizinho]
            if caminho == -1: 
                caminho = max_way(vizinho, empresa)
                vt[empresa][vizinho] = caminho        
            if caminho > m : m = caminho
    
    return m + 1

resultado = 0
for i in range(n):
    caminho = max_way(i, None)
    if caminho > resultado: resultado = caminho

print(resultado)