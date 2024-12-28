from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        

        d=defaultdict(int)
        for num in arr:
            d[num]+=1
        freqs=list(d.values())
        return len(freqs)==len(set(freqs))
        