class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return end + 1
    
        

#Time Complexity: O(log N)
#Auxiliary Space: O(1)
