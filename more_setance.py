class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        w1 = setence1.split()
        w2 = sentence2.split()

        if len(w1) > len(w2):
            w1, w2 = w2, w1

        left, right = 0, 0

        while left < len(w1) and w1[left] == w2[left]:
            left += 1

        while right < len(w1) and w1[-(right + 1)] == w2[-(right + 1)]:
            right += 1
        
        return left + right >= len(w1)