class TreeNode:
    def _int_(self , val)：
        self.val = val
        self.left = None
        self.right = None
        
    def search(root, target):
        if not root:
            return False
        elif root.val > target:
            return search(root.left, target)
        elif root.val < target:
            return search(root.right, target)
        else:
            return True
