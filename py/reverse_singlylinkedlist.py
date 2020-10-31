from singlylinkedlist import Node, LinkedList

def reverse_loop(lst):
    """Reverse the list using loop.
    """
    if not lst.head:
        return
    frst = lst.head
    scnd = lst.head.next
    while scnd:
        tmp = scnd.next
        scnd.next = frst
        frst = scnd
        scnd = tmp
            
    tmp = lst.head
    lst.head = lst.last
    lst.last = tmp
    lst.last.next = None
        
def _reverse(lst, this_node, next_node):
    if next_node.next:
        _reverse(lst, next_node, next_node.next)
        
    next_node.next = this_node
    this_node.next = None

def reverse_rec(lst):
    """Reverse the list using recurssion.
    """
    if not (lst.head and lst.head.next):
        return
    _reverse(lst, lst.head, lst.head.next)
    temp = lst.head
    lst.head = lst.last
    lst.last = temp
        
def test_slinked_list():
    print('test list with multiple items')
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    sl = LinkedList()
    sl.add(n1)
    sl.add(n2)
    sl.add(n3)
    sl.add(n4)
    sl.add(n5)
    sl.add(n6)
    sl.add(n7)
    sl.add(n8)
    sl.add(n9)
    print(sl.traverse())
    reverse_rec(sl)
    print(sl.traverse())
    reverse_rec(sl)
    print(sl.traverse())
    reverse_loop(sl)
    print(sl.traverse())
    reverse_loop(sl)
    print(sl.traverse())

def test_slinked_list_empty():
    print('test empty list')
    sl = LinkedList()
    print(sl.traverse())
    reverse_rec(sl)
    print(sl.traverse())
    reverse_loop(sl)
    print(sl.traverse())

def test_slinked_list_single():
    print('test a single item in list')
    n1 = Node(1)
    sl = LinkedList()
    sl.add(n1)
    print(sl.traverse())
    reverse_rec(sl)
    print(sl.traverse())
    reverse_loop(sl)
    print(sl.traverse())

test_slinked_list()
test_slinked_list_empty()
test_slinked_list_single()


