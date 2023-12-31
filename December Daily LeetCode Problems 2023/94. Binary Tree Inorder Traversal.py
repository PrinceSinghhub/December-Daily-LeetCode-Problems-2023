# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # morish Travesrsal

        inOrder = []

        currNode = root

        while currNode != None:
            if currNode.left == None:
                inOrder.append(currNode.val)
                currNode = currNode.right

            else:
                prevNode = currNode.left
                while prevNode.right != None and prevNode.right != currNode:
                    prevNode = prevNode.right

                # create a thread
                if prevNode.right == None:
                    prevNode.right = currNode
                    currNode = currNode.left

                else:
                    prevNode.right = None
                    inOrder.append(currNode.val)
                    currNode = currNode.right
        return inOrder

    def preOrderTraversal(self, root):
        # morish Travesrsal

        preOrder = []

        currNode = root

        while currNode != None:
            if currNode.left == None:
                preOrder.append(currNode.val)
                currNode = currNode.right

            else:
                prevNode = currNode.left
                while prevNode.right != None and prevNode.right != currNode:
                    prevNode = prevNode.right

                # create a thread
                if prevNode.right == None:
                    prevNode.right = currNode
                    preOrder.append(currNode.val)
                    currNode = currNode.left

                else:
                    prevNode.right = None
                    currNode = currNode.right
        return preOrder
