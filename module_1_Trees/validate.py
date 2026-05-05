class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        io_list = []

        self.helper(root, io_list)

        is_bst = True
        prev = io_list[0]

        for i in range(1, len(io_list)):
            if io_list[i] <= prev:
                is_bst = False
            prev = io_list[i]

        return is_bst

    def helper(self, tree_node, io_list):
        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)
