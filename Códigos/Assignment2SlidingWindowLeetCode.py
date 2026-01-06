# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         for left in range(n): 
#             for right in range(left + 1, n): 
#                 if nums[left] == nums[right] and abs(left - right) <= k: 
#                     return True

#         return False
    
#     nums = [1, 2, 3, 1]
#     k = 3
#     print(containsNearbyDuplate(nums, k))

# Esse código acima mesmo dando certo, gera um timeout error pela complexidade de O(n^2)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ultimo_indice = {}

        for indice_atual, valor in enumerate(nums):
            if valor in ultimo_indice:
                if indice_atual - ultimo_indice[valor] <= k:
                    return True

            ultimo_indice[valor] = indice_atual

        return False

