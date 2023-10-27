class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r, ind = 0, len(nums)-1, 0
        while(ind <= r):
            if nums[ind] == 0:
                nums[l], nums[ind] = nums[ind],nums[l]
                l += 1
                ind += 1
            elif nums[ind] == 2:
                nums[r], nums[ind] = nums[ind],nums[r]
                r -= 1
            else:
                ind += 1
        return 


    