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

        mid = length // 2
        new_head = head
         # count = 0
        for i in range(mid):
        # while count != midel_index:
            # count +=1
            new_head = new_head.next
        return new_head    
