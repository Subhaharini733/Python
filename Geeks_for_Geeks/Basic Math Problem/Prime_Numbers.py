# https://www.geeksforgeeks.org/problems/prime-number2314/1
# time comp: O(sqrt(n))
# space comp: O(1)

class Solution:
    def isPrime (self, N):
        if N <= 1:
            return 0
        for i in range (2, int(N**0.5) + 1):
            if N % i == 0:
                return 0
        return 1

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isPrime(N))
