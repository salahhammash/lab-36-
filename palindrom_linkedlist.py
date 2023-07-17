class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        sec = head
        #Finding the Mid of the linked list
        while first and first.next:
            first = first.next.next
            sec = sec.next
        # Reversing the second half of the linked list
        node = None
        # This variable will keep track of the previous node as we reverse the pointers.
        while sec:
            n = sec.next
            sec.next = node
            #to everses the pointer direction 
            node = sec
            sec = n
        # Comparing the First and the Second Half
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True