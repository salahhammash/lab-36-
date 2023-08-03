def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False   
        if p.val != q.val:
            return False    
        check_left = isSameTree(p.left, q.left)
        check_right = isSameTree(p.right, q.right)
        return check_left and check_right