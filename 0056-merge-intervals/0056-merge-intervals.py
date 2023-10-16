class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        res = [intervals[0]]

        for l,r in intervals:
            top = res[-1][1]

            if l <= top:
                res[-1][1] = max(top,r)
            else:
                res.append([l,r])
        return res
        