from functools import reduce
custom = 40

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
        print(f"l2 = {listInt2}\n")
        
        sumList = [x+y for x,y in zip(listInt1,listInt2)]
        index = sumList.__len__()-1
        
        print(f"while 0 <={index}")
        test = []
        while 0<=index :
            print(f"List = {sumList} index={index}")
            if(sumList[index] > 9):
                numeroSelecionado = sumList[index]
                separador = [int(digito) for digito in str(numeroSelecionado)]
                print(separador)
                sumList[index] = separador[-1]
                
                if(index > 0 ):
                 sumList[index-1] = sumList[index-1] + separador[0] 
             
            
            index -= 1;
        print(f"resposta = {sumList}")
            

        

solution = Solution()
print("="*custom)
Inp1 = input("l1 = ")
Inp2 = input("l2 = ")
#243
#564

print("-"*custom)
solution.addTwoNumbers(Inp1,Inp2)
print("-"*custom)

print("="*custom)