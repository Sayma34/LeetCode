class Solution:
    def threeSumClosest(self, arr,  target):
        arr.sort()
        n = len(arr)
        closest = float('inf')
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                total = arr[i]+ arr[left]+ arr[right]
                if abs(total-target) < abs(closest - target):
                    closest = total
                if total < target:
                    left +=1
                elif total > target:
                    right -=1
                else:
                    return total

  
        return closest

sol = Solution()
arr = [-1,2,1,-4]
target = 1
print(sol.threeSumClosest(arr,  target))  