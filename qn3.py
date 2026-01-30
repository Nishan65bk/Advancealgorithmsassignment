class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_service_centers(root):
    count = 0

    def dfs(node):
        nonlocal count
        if not node:
            return 2

        left = dfs(node.left)
        right = dfs(node.right)

        if left == 0 or right == 0:
            count += 1
            return 1

        if left == 1 or right == 1:
            return 2

        return 0

    if dfs(root) == 0:
        count += 1

    print("Time Complexity: O(n)")
    return count
