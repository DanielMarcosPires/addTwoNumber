from functools import reduce

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = list(l1)
        listInt1 = [int(x) for x in list1]
        list2 = list(l2)
        listInt2 = [int(y) for y in list2]
        sumList = [x+y for x,y in zip(listInt1,listInt2)]
        print(listInt1)
        print(listInt2)
        
        print(sumList)
        

solution = Solution()

Inp1 = input("l1 = ")
Inp2 = input("l1 = ")

solution.addTwoNumbers(Inp1,Inp2)