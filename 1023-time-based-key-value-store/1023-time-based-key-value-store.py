class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        temp = self.hm.get(key,[])
        l, r = 0, len(temp)-1
        while(l<=r):
            mid = (l + r) // 2
            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
