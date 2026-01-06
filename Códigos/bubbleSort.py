def bubble_sort(arr):
    n = len(arr)
    
    # n = 5
    
    for i in range(n - 1):    # 0 1 2 3 (quando tenta ir para o 4, o loop para) 
        for j in range(n - 1 - i):  
            if arr[j] > arr[j + 1]:
                # troca
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Basicamente um swap
    
    return arr


vetor = [4, 5, 2, 3, 1]
ordenado = bubble_sort(vetor)

print(ordenado)
