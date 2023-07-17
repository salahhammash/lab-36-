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
