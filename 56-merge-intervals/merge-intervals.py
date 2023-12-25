class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting eh the array with ist elenem
        def get_first(x):
            return x[0]
        intervals.sort(key=get_first)
        result=[]
        for interval in intervals:
            if not result or result[-1][1] <  interval[0]    :
                result.append(interval)
            else:
                result[-1][1]=max(result[-1][1],interval[1])
        return result
                
  

