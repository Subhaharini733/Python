# https://www.geeksforgeeks.org/problems/reverse-digit0316/1
# time comp: O(log n)
# space comp: o(1)

class Solution:
	def reverse_digit(self, n):
	    rev = 0
		while n > 0:
		    dig = n % 10
		    rev = (rev * 10) + dig
		    n //= 10
		return rev

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
