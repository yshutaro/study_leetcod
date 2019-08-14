class Solution:
  def numJewelsInStones(self, J: str, S: str) -> int:
    j = [s[i] for i in range(0, len(J))]
    print(j)

if __name__ == '__main__':
  solusion = Solution()
  solusion.numJewelsInStones("aA", "aAAbbbb")
