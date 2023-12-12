class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces=0
        visited=set()
        n=len(isConnected)
    # helper fnction
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        
        for x in range(n):
            if x not in visited:
                dfs(x)
                provinces+=1



        
        return provinces
