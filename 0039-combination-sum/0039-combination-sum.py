class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(start, target, curList):
            if target == 0:
                return res.append(curList[:])
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    curList.append(candidates[i])
                    solve(i, target-candidates[i], curList)
                    curList.pop()
        solve(0, target, [])
        return res