class Solution:
    def oddCells(self, n: int, m: int, indices: [[int]]) -> int:
      result = 0
      matrix = [[0 for i in range(n)] for j in range(m)]
      #print("matrix step0:",  matrix) 

      for index in indices:

        row = index[0]  
        col = index[1]
        #print(row)
        #print(col)

        for mat in matrix:
          mat[row] = mat[row] + 1
        #print("matrix_step1:", matrix)
        matrix = [[ mat + 1 for mat in val] if ind == col else val for ind, val in enumerate(matrix)]
      
      #print("matrix:",  matrix) 
      result = sum([len(list(filter(lambda x:x%2==1,m))) for m in matrix])
      #print("result:", result)
      return result

if __name__ == '__main__':
  so = Solution()

  assert 6 == so.oddCells(2, 3, [[0,1],[1,1]])
  assert 0 == so.oddCells(2, 2, [[1,1],[0,0]])
