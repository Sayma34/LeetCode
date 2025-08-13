class Solution:
    def twoSum(self, arr, target):
        left = 0
        right = len(arr) - 1  # Initialize right to the last index
        while True:
            # Added a condition to break the loop if pointers cross
            if left >= right:
                break

            if arr[left] + arr[right] < target:
                left+=1
            elif arr[left] + arr[right] > target:
                right-=1
            elif arr[left] + arr[right] == target:
                # Returning 1-based indices as per common Two Sum problem convention
                return [left + 1, right + 1]
            # The break here would cause the loop to exit after the first iteration,
            # which is likely not the intended behavior for finding the sum.
            # Removing the break to allow the loop to continue until pointers cross or target is found.
            # break # Removed the break as requested to keep while True structure but fix logic

        return [] # Return empty list if no solution found

arr = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(arr, target))