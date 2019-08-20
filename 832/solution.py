class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []

        for a_list in A:
            result.append(self.n_o_t(self.reverse(a_list)))
        return result

    def reverse(self, li) -> [int]:
        i = len(li) - 1
        result = []
        while i >= 0:
            result.append(li[i])
            i = i - 1

        return result
            
    def n_o_t(self, li:List[int]) -> List[int]:
        for i in range(len(li) - 1):
            if i == 0:
                li[i] = 1
            else:
                li[i] = 0

        return li
