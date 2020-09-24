class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup_table = {}
        
        
        for i in range(len(nums)):
            
            if nums[i] not in lookup_table:
                
                lookup_table[nums[i]] = i
                
            
        # loop through nums array and then subtract each current
        # element from target and see if that number exists in the
        # look up table, once done with that, you can see if you return a 
        # pair or not.
        
        for j in range(len(nums)):
            
            
            if (target - nums[j]) in lookup_table and j != lookup_table[target - nums[j]]:
                
                return [j, lookup_table[(target - nums[j])]]
        
        return False