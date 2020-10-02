class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack = [root] #not actually a stack, can also use deque
        preorderArray =[]

        while stack:
            node = stack.pop()# poping the last element because of postorder
            preorderArray.append(node.val)
            stack = node.children + stack
        return preorderArray
