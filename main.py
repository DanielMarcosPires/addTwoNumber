from functools import reduce
custom = 40

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = list(map(int, reversed(l1)))
        b = list(map(int, reversed(l2)))
        
        print(a)
        print(b)
        
solution = Solution()

solution.addTwoNumbers([123456789],[123])        