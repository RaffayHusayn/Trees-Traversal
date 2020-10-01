class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack = [root] #not actually a stack, can also use deque
        preorderArray =[]

        while stack:
            node = stack.pop(0)# poping the first element, not the last element because of preorder
            preorderArray.append(node.val)
            stack = node.children + stack
        return preorderArray
