"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of the two numbers such that they add up to target.

        Approach:
        - Use a hashmap (dictionary) to store numbers we have already seen
          along with their indices.
        - For each number, check if the complement (target - current number)
          already exists in the hashmap.
        - If it exists, we have found the required pair.
        """
        
        mp = {}                                       
        for i in range(len(nums)):                    
            rem = target - nums[i]                    
            if rem in mp:
                return [mp[rem], i]   
            mp[nums[i]] = i

alternative code ->

 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Same logic as above, but using enumerate() for cleaner Python syntax.

        enumerate(nums) gives:
        - i   -> index
        - num -> value at that index
        """

        mp = {}
        for i , num in enumerate(nums):
            if target - num in mp:
                return [mp[target - num], i]
            mp[num] = i
                
        
        
