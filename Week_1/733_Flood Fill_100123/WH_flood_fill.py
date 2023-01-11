class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial = image[sr][sc]
        if initial == color:
            return image
        r = len(image)
        c = len(image[0])

        def dfs(n, m):
            if (n < 0) or (m < 0) or (n >= r) or (m >= c) or (image[n][m] != initial):
                return
            image[n][m] = color
            dfs(n+1, m)
            dfs(n-1, m)
            dfs(n, m+1)
            dfs(n, m-1)

        dfs(sr, sc)
        return image
