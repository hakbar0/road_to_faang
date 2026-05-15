class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        countR, countM = {}, {}

        for letter in ransomNote:
            countR[letter] = countR.get(letter, 0) + 1

        for letter in magazine:
            countM[letter] = countM.get(letter, 0) + 1
        
        for key in countR:
            if countR[key] != countM.get(key, 0):
                return False
        
        return True

