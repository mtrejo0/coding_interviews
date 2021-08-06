


class Solution():

    def isPalindrome(self, string):

        if len(string) < 2:
            return True

        if string[0] == string[-1]:
            return self.isPalindrome(string[1:-1])
        return False


if __name__ == "__main__":
    
    tests = [
        [
            "aba", True
        ],
        [
            'aas', False
        ],
        [
            'a', True
        ]
    ]

    solution = Solution()
    for test in tests:

        input, expected = test

        assert solution.isPalindrome(input) == expected
    
    print("Passed!")

        
