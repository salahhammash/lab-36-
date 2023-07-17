# lab 36

---

## 1-  Middle of the Linked List
        
## Given the head of a singly linked list, 
## arguments: head
## returns: the middle node of the linked list

---


## 2-  Palindrome Linked List
        
## Given the head of a singly linked list, 
## arguments: head
## returns: rue if it is a palindrome false otherwise.
 

## Whiteboard Process 
[middle ](./assests/leet%20code%201.png)
[palindrom](./assests/palindrom.png)

---

## Approach & Efficiency

---  

## O(n) Time performance 
## O(n) Space performance 



soulution 

### middle 
class Solution(object):
    def middleNode(self, head):
     
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
### palindrom

class Solution(object):
    def isPalindrome(self, head):
      
        first = head
        sec = head
        #Finding the Mid of the linked list
        while first and first.next:
            first = first.next.next
            sec = sec.next

        # Reversing the second half of the linked list
        node = None
        while sec:
            n = sec.next
            sec.next = node
            node = sec
            sec = n

        # Comparing the First and the Second Half
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
