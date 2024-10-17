# # https://www.geeksforgeeks.org/problems/odd-or-even3618/1
# time comp: O(1)
# space comp: O(1)

class Solution:
    def oddEven(self, n):
        return 'even' if n % 2 == 0 else 'odd'

if __name__ == '__main__':
    N = int(input())
    ob = Solution()
    print(ob.oddEven(N))
