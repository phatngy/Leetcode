class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode)->ListNode:
    result = ListNode(0)
    curr = result
    carry = 0 

    while l1 or l2 or carry:
        val = carry
        
        if l1:
            val += l1.val
            l1 = l1.next
        
        if l2:
            val += l2.val
            l2 = l2.next
    
        curr.next =  ListNode(val % 10)
        carry = int(val / 10)

        curr = curr.next

    return result.next
