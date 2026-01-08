def find_middle(head):
    slow = head
    fast = head.next
    
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2): # Função do merge é basicamente receber duas listas ligadas já ordenadas (l1 e l2) e juntá-las em uma única lista ordenada. 
    head = Node() # head é um nó fictício (dummy)
    tail = head 

    while l1 and l2: # Loop roda enquanto as duas listas ainda tem elementos 
        if l1.val < l2.val: # Comparação dos primeiros nós de cada lista
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next 
        tail = tail.next
        
    tail.next = l1 or l2
    return head.next

def mergesort(head):
    if not head or not head.next:
        return head
    
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None
    left = mergesort(head)
    right = mergesort(after_middle)
    
    sorted_list = merge(left, right)
    
    return sorted_list


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)

my_list = mergesort(node_9)

curr = my_list
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next 
    