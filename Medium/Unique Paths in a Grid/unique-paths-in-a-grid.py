#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):        
        t = [[0 for _ in range(m)] for _ in range(n)]
        
        mod = 10**9 + 7
        for i in range(m):
            if grid[0][i] == 0:
                break
            t[0][i] = 1
        for j in range(n):
            if grid[j][0] == 0:
                break
            t[j][0] = 1
        
        for i in  range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1:
                    t[i][j] = (t[i-1][j] + t[i][j-1])%mod
        return t[n-1][m-1]%mod
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        grid=[]
        for i in range(n):
            col = list(map(int,input().split()))
            grid.append(col)
        
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
# } Driver Code Ends