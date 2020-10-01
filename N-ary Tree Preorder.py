""""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if root is None:
            return []
        else:
            final = [root.val]
            for child in root.children:
                final += self.preorder(child)
            return final
