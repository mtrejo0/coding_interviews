import random

class Solution:
    def __init__(self,songs):
        self.songs = songs
        self.songs_left = songs
  
    def random_song(self):
        if len(self.songs_left) == 0:
            self.songs_left = self.songs
        i = random.randint(0,len(self.songs_left)-1)
        n = len(self.songs_left)-1
        if i != n:
            temp = self.songs_left[i]
            self.songs_left[i] = self.songs_left[n]
            self.songs_left[n] = temp
        return self.songs_left.pop()


if __name__ == "__main__":
    
    tests = [
        [
            [1,2,3]
        ],
        [
            [1,3]
        ]
    ]

    
    for test in tests:
        solution = Solution(test.copy())
        actual = []
        for i in range(len(test)):
            actual.append(solution.random_song())
        print(actual, test)
        assert sorted(actual) == sorted(test)
    
    print("Passed!")

        
