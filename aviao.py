# nf = o número total de fileiras no avião
# npf = o número de posições por fileira
# npe = o número da primeira fileira da classe econômica
# pfe = posição na fila de embarque do Sr. Zuki

nf,npf,npe,pfe = map(int,input().split())

if ((npe + pfe // npf) > nf):
    print('PROXIMO VOO')
else:
    print(int(npe + (pfe-1)/npf),chr(((pfe-1)%npf+ ord('A'))))