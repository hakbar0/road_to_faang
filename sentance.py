class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        split_s_1 = sentence1.split()
        split_s_2 = sentence2.split()

        short_search = split_s_1 if len(split_s_1) <= len(split_s_2) else split_s_2
        long_search = split_s_2 if len(split_s_1) <= len(split_s_2) else split_s_1

        while short_search and short_search[0] == long_search[0]:
            short_search.pop(0)
            long_search.pop(0)
        
        while short_search and short_search[-1] == long_search[-1]:
            short_search.pop()
            long_search.pop()


        return len(short_search) == 0