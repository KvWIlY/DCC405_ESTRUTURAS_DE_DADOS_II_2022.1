# Radix sort in Python

def countingSort(array, size, col, base, max_len):
  output   = [0] * size
  count    = [0] * (base + 1)
  min_base = ord('a') - 1

  for item in array: # generate Counts
    # Obtenha a letra da coluna se estiver dentro da string, caso contrário, use a posição fictícia de 0
    letter = ord(item[col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1):# Accumulate counts
      count[i + 1] += count[i]

  for item in reversed(array):
    # Obtenha o índice da letra atual do item no índice coluna na matriz de contagem
    letter = ord(item[col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1

  return output

def radixSort(array, max_col = None):
  if not max_col:
    max_col = len(max(array, key = len)) # edit to max length

  for col in range(max_col-1, -1, -1): # max_len-1, max_len-2, ...0
    array = countingSort(array, len(array), col, 26, max_col)

  return array

# ler as strings do arquivo e adiciona na lista dna_Nseq
dna_Nseq = []
with open("ordena.txt","r") as arquivo:
    texto = arquivo.readlines()
    for frase in texto:
        dna_Nseq.append(frase.replace('\n','')) 

arquivo.close

# salva os valores ordenados e adicona os escreve no arquivo dna_seq_Ord
DS = radixSort(dna_Nseq)
with open('dna_seq_Ord.txt', 'w+') as arquivOrd:    
    for items in DS: 
        arquivOrd.write('%s\n' %items) 
arquivOrd.close()

# obs: O Codigo do RadixSort não é de minha autoria. tenha um bom dia!