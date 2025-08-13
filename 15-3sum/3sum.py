#threesum
class Solution:
    def threeSum(self, arr, threesum = 0):
        res = []
        arr.sort()
        for i,a in enumerate(arr):
            if i>0 and a == arr[i-1]:
                continue
            left = i+1
            right = len(arr)-1
            while left<right:
                threesum = a + arr [left] + arr[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([a, arr[left], arr[right]])
                    #updating pointer
                    left +=1
                    while arr[left]== arr[left-1] and left<right:
                        left+=1

        return res

arr = [-1,0,1,2,-1,-4]
threesum = 0
thrs = Solution()

print(thrs.threeSum(arr, threesum))