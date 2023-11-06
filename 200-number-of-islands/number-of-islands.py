class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        rows,cols=len(grid),len(grid[0])
        island=0
        visit=set()

        def dfs (r,c):
            if r in range(rows) and c in range(cols) and  grid[r][c]=="1" and (r,c) not in visit :

                grid[r][c]=="0"
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]=="1" and (x,y) not in visit:
                    
                    island+=1
                    dfs(x,y)
        return island
            


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid :
#             return 0
#         rows,cols=len(grid),len(grid[0])
#         visit=set()
#         island=0

        
#         def BFS(r,c):
#             q=[]
#             visit.add((r,c))
#             q.append((r,c))
#             while q:
#                 row , col =q.pop(0)
#                 direction=[[1,0],[-1,0],[0,1],[0,-1]]
#                 for dr ,dc in direction :
#                     r,c=row+dr ,col+dc
#                     if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit :
#                         q.append((r,c))
#                         visit.add((r,c))


#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]=="1" and (r,c) not in visit :
#                     BFS(r,c)
#                     island+=1
#         return island