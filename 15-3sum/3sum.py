class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Approach:
        - Sort the array.
        - Fix one number nums[i].
        - Use two pointers (l and r) to find two numbers whose sum with nums[i] is 0.
        - If the sum is too big → move r left.  
        - If the sum is too small → move l right.
        - If sum = 0 → store the triplet.
        - Skip duplicates to avoid repeating triplets."""
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l , r = i + 1 , len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l] , nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


cleaner version->
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                     
                elif total < 0:
                    l += 1
                else:
                    r -= 1    
        return res

       

            

        



            

        
