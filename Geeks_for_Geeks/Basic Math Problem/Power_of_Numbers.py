# https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1
# time comp: O(log n)
# space comp: O(log n)

class Solution:
    def power(self,N,R):
        return pow(N, R, 1000000007)
      
import math
def main():
    T=int(input())
    while(T>0): 
        N=input()
        R=N[::-1]
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        T-=1
if __name__=="__main__":
    main()

# pow(n,r, 1000000007): This efficiently computes n^r mod 1000000007 using modular exponentiation, 
# which is efficient even for large values of 𝑟.
