class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(curList):
            if len(curList) == len(nums):
                res.append(curList[:])
                return
            
            for num in nums:
                if num not in curList:
                    curList.append(num)
                    solve(curList)
                    curList.pop()
            return
        
        solve([])
        return res