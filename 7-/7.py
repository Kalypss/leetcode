"""7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))  # Output: 321
    print(sol.reverse(-123)) # Output: -321
    print(sol.reverse(120))  # Output: 21
    