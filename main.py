from functools import reduce

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = list(l1)
        list1.reverse()
        listInt1 = [int(x) for x in list1]
        list2 = list(l2)
        list2.reverse()
        listInt2 = [int(y) for y in list2]
        
        print(f"l1 = {listInt1}")
        print(f"l2 = {listInt2}")
        
        sumList = [x+y for x,y in zip(listInt1,listInt2)]
        
        for value in sumList:
            print(value)
            if(value >= 10):
                separator = [x for x in str(value)]
                print(f"list={separator} length={separator.__len__()}")

        

solution = Solution()

Inp1 = input("l1 = ")
Inp2 = input("l2 = ")
#243
#564

solution.addTwoNumbers(Inp1,Inp2)