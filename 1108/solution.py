class Solution:
  def defangIPaddr(self, address: str) -> str:
    return address.replace('.' , '[.]')

if __name__ == '__main__':
  solusion = Solution()
  s = solusion.defangIPaddr("1.2.2.3")
  print(s)
