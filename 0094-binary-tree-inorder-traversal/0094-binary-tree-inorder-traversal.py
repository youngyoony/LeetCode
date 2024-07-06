class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode], result: List[int]) -> None:
            if node:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)
        
        result = []
        inorder(root, result)
        return result