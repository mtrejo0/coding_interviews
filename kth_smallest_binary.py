


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kth_smallest(self, node, k):
        sorted = self.recurse(node)
        return sorted[k-1]

    def recurse(self, node, order=[]):
        left = []
        if node.left:
            left = self.recurse(node.left, order)
        right = []
        if node.right:
            right = self.recurse(node.right, order)
        return left + [node.val] + right


if __name__ == "__main__":
    
    tests = [
        [
            [TreeNode(8,TreeNode(3),TreeNode(9)), 2], 8
        ],
        [
            [TreeNode(8,TreeNode(3),TreeNode(9, TreeNode(8.5), TreeNode(10))), 4], 9
        ],
    ]

    solution = Solution()
    for test in tests:

        input, expected = test
        actual = solution.kth_smallest(input[0], input[1]) 

        print(actual, expected)
        assert actual == expected
    
    print("Passed!")

        
