# Input:
available = "AABNNC"
word = "Banana"

# Output: True

def count_words(available: str, word: str) -> bool:
    if word == "":
        return True
    
    countW, countA = {}, {}

    for letter in word: 
        up = letter.upper()
        countW[up] = countW.get(up, 0) + 1
    
    for letter in available: 
        up = letter.upper()
        countA[up] = countA.get(up, 0) + 1
    
    print(countA)
    print(countW)

    for key in countW:
        if countW[key] > countA.get(key, 0):
            return False
    
    return True

print(count_words(available=available, word=word))
    
