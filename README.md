# lab 36

---

## 1-  Middle of the Linked List
        
## Given the head of a singly linked list, 
## arguments: head
## returns: the middle node of the linked list

---


## Whiteboard Process 
[Whiteboard Process](./assests/leet%20code%201.png)
<!-- [Whiteboard Process](./assests/leet%20code%201.png) -->

---

## Approach & Efficiency

---  

## left_join method
## O(n) Time performance 
## O(n) Space performance 



soulution 

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        length=0
        while current :
            length +=1
            current = current.next

        midel_index = length // 2
        new_head = head
        for i in range(midel_index):
            new_head = new_head.next
        return new_head    
