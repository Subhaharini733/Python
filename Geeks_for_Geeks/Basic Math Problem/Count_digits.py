# https://www.geeksforgeeks.org/problems/count-digits5716/1
# time comp: O(n)
# space comp: O(1)

class Solution:
    def evenlyDivides (self, N):
        num = str (N)
        cnt = 0
        for digit in num:
            dig = int (digit)
            if dig != 0 and N % dig == 0:
                cnt += 1
        return cnt
      
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.evenlyDivides(N))
