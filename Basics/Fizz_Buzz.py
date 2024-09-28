# Leetcode - 412 - Fizz Buzz
# time comp: O(n)
# space comp: O(n)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += "Buzz"
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            output.append(ans)
        return output

# we are asked to submit output in list , output list is created.
# lets loop to get every number of n.
# check if i is divisible by 3 , if yes then store 'Fizz' in ans and 
#    then check for 5, if yes append 'Buzz' to ans.
# then in elif check if i divisible by 5 alone, if yes store 'Buzz' to ans .
# else store string of i in ans (for 1, 2 , 4, 6, 7....)
# then append everything to output and return output.
    
        
