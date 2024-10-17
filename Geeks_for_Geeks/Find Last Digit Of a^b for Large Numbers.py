# https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1
# time comp: O(1)
# space comp: O(1)

class Solution:
    def getLastDigit(self, a, b):
        a = int (a) % 10
        b = int (b)
        if b == 0:
            return 1
        cycles = {
            0 : [0],
            1 : [1],
            2 : [2, 4, 8, 6],
            3 : [3, 9, 7, 1],
            4 : [4, 6],
            5 : [5],
            6 : [6],
            7 : [7, 9, 3, 1],
            8 : [8, 4, 2, 6],
            9 : [9, 1]
        }
        cycle = cycles[a]
        cycle_length = len(cycle)
        index = (b-1) % cycle_length
        return cycle[index]
      
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
