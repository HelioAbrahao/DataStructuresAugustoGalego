class Solution:
    def hammingWeight(self, n: int) -> int:
        cont = 0
        while n > 0:
            if n & 1:
                cont += 1
            n = n >> 1
        
        return cont