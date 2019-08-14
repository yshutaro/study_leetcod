class Solution:
  def removeOuterParentheses(self, S: str) -> str:
    count = 0
    list = []
    for i in range(len(S)):
      if S[i] == "(":
        count += 1
        if count != 1:
          list.append(S[i])
      if S[i] == ")":
        count += -1
        if count != 0:
          list.append(S[i])
      

    print(list)
    return "".join(list)


if __name__ == '__main__':
  so = Solution()
  assert "()()()" == so.removeOuterParentheses("(()())(())")

  assert "()()()()(())" ==  so.removeOuterParentheses("(()())(())(()(()))")

  assert "" ==  so.removeOuterParentheses("()()")
