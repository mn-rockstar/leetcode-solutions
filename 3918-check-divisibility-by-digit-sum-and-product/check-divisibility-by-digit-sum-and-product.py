class Solution:
    def checkDivisibility(self, n: int) -> bool:
        numbers = []
        for i in str(n):
            numbers.append(i)
        sum1 = 0
        product = 1
        for i in numbers:
            sum1 += int(i)
            product *= int(i)
        check = (sum1 + product)
        if n % check == 0:
            return True
        else: 
            return False
