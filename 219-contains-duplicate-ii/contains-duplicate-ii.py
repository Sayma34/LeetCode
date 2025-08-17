class Solution:
    def containsNearbyDuplicate(self, nums, k):
        recent_idx = {} 
        #storing num as keys. and their last seen index as values.
        # if we see 3 at index 2, we store {3: 2}.  
        for idx, num in enumerate(nums):
            #If the current index minus the previous index of this number is ≤ k, then the two duplicates are close enough.
            if num in recent_idx and idx - recent_idx [num] <= k:
                return True
            recent_idx[num] = idx  # updating last seen index
        return False

sol = Solution()
nums = [1,2,3,1]
k = 3
print(sol.containsNearbyDuplicate( nums, k))

# K = maximum allowed distance between two duplicate numbers.
               