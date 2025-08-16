class Solution:
    def containsDuplicate(self, nums):
        seen = set()  #initializing empty hash set
        for i in nums:  #iterating thru each numbr in nums
            if i in seen:  #if numbr is already in set
                return True  # return true
            seen.add(i)  #otherwise add num to set
        return False  # if i finish loop w/o finding duplicate, return false

sol = Solution()
nums = [1,2,3,1]
print(sol.containsDuplicate( nums))


        