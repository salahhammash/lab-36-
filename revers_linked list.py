# Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        initialize 3 variables 
        previpus = none
        current = head 
        next = current .next 
        '''
        pre = None
        current = head
        while current is not None :
            n = current.next 
            current.next = pre
            pre = current
            current = n
        return pre  

'''
افرض عندي ليست فيها 
1->2->3->4->5

pre = None
current = 1 
n =2 

بالعادة الكارنت .نيكست بتكون 4
انا بدي اعكسها اخليها ال2 
عن طريق اني اخلي 
current.next = p
p = current 
current = n

result 
5->4->3->2->1

'''