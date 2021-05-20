# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# 
#  
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:
# 
# Input: root = []
# Output: []
# Example 3:
# 
# Input: root = [1]
# Output: [1]
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [2,1]
# Example 5:
# 
# 
# Input: root = [1,null,2]
# Output: [2,1]
#  
# 
# Constraints:
# 
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#  
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import List

from common.utils import TreeNode, stringToTreeNode

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        return res


if __name__ == '__main__':
    a = Solution()
    root = '[1,null,2,3]'
    print(a.postorderTraversal(stringToTreeNode(root)))
