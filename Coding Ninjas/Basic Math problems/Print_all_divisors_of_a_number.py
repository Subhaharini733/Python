# https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188
# time comp: O(n)
# space comp: O(1)

from typing import List
def printDivisors(n: int) -> List[int]:
    div = []  
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i) 
    return div 

n = int(input("Enter a number: "))
divisors = printDivisors(n)
print(divisors)  

# from typing import list is a method used to give hints on inputs and what to be returned as result
