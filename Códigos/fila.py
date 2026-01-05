from queue import Queue
from collections import deque

q = Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())

# get() remove o elemento da frente da fila e retorna esse elemento