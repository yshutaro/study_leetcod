class Solution:
  def uniqueMorseRepresentations(self, words: str) -> int:

    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    morse_dict = {}
    for i in range(0,26):
      morse_dict[alphabet[i]] = morse[i]

    morse_result = []
    for word in words:
      str = '';
      for i in range(0,len(word)):
        str += morse_dict[word[i]]
      morse_result.append(str)
      
    result = len(list(set(morse_result)))
    return result


if __name__ == '__main__':
  so = Solution()
  assert so.uniqueMorseRepresentations(["gin","zen","gig","msg"]) == 2
