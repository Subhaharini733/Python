# https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
# time comp: O(log(min(a,b)))
# space comp: O(1)

class Solution:
    def gcd(self, a : int, b : int) -> int:
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)
      
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.gcd(a, b)
        print(res)
