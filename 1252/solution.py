class Solution:
    def oddCells(self, n: int, m: int, indices: [[int]]) -> int:
      result = 0
      matrix = [[0 for i in range(n)] for j in range(m)]

      for index in indices:
        row = index[0]  
        col = index[1]

        [[m[row] + 1, m[1]] for m in matrix]

      return result

if __name__ == '__main__':
  so = Solution()

  assert 6 == so.oddCells(2, 3, [[0,1],[1,1]])
  assert 0 == so.oddCells(2, 2, [[1,1],[0,0]])
