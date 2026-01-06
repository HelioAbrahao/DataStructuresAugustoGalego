class Solution:
    def firstUniqChar(self, s:str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else: 
                d[ch][1] += 1

        for ch, val in d.items():
            if val[1] == 1:
                return val[0]

        return -1
    

# enumerate é uma função do Python que permite percorrer um iterável (lista, string, etc) tendo acesso ao índice e ao valor ao mesmo tempo. 
# De forma geral, o enumerate(iteravel) retorna pares: (indice, valor)

# .get() é um método de dicionários usado para buscar um valor por chave, sem causar erro se a chave não existir. 
# Forma geral: d.get(chave) (retorna None se a chave não existir)

# .items() é um método de dicionários que retorna pares de chave e valor. Para cada elemento do dicionário, você recebe uma tupla (chave, valor). Isso é muito útil para percorrer o dicionário e ter acesso aos dois ao mesmo tempo. 

# Criação de um dicionário 
# iterando através da string por meio do enumerate, que retorna um par com o índice e o caractere