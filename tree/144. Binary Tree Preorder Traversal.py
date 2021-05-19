# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]
# Example 4:
# Input: root = [1,2]
# Output: [1,2]
# Example 5:
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
# Constraints:
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#  
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
from typing import List

from common.utils import TreeNode, stringToTreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res



if __name__ == '__main__':
    a = Solution()
    root = '[1,null,2,3]'
    print(a.preorderTraversal2(stringToTreeNode(root)))
