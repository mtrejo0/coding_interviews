


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.recurse(root)
        
    def recurse(self, root, count=0):
        if root == None:
            return 0
        left = 0
        if root.left:
            left = self.recurse(root.left, count)
        right = 0
        if root.right:
            right = self.recurse(root.right, count)
        return left  + right + 1


if __name__ == "__main__":
    
    tests = [
        [
            [TreeNode(8,TreeNode(3),TreeNode(9))], 3
        ],
        [
            [TreeNode(8,TreeNode(3),TreeNode(9, TreeNode(8.5), TreeNode(10)))], 5
        ],
    ]

    solution = Solution()
    for test in tests:

        input, expected = test
        actual = solution.countNodes(input[0]) 

        print(actual, expected)
        assert actual == expected
    
    print("Passed!")

        
