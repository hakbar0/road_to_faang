newspapers = [
    ["the", "cat", "sat", "on", "the", "mat"],
    ["dog", "ran", "fast", "the"],
    ["big", "cat", "jumped", "over"]
]

target = ["the", "cat", "ran"]

# # True 

# newspapers = [
#     ["the", "cat", "sat"],
#     ["dog", "ran", "fast"]
# ]
# target = ["the", "the", "the"]

# # False

# newspapers = [
#     ["the", "big", "the"],
#     ["the", "small", "dog"],
#     ["ran", "the", "fast"]
# ]
# target = ["the", "the", "the", "the"]

# True

# newspapers = [["hello", "world"]]
# target = []

#  True

def find_target( newspapers, target) -> bool:
    if target == []:
        return True
    targetCount, newspaperCount = {}, {}

    for word in target:
        targetCount[word] = targetCount.get(word, 0) + 1
    
    for array in newspapers:
        for word in array:
            newspaperCount[word] = newspaperCount.get(word, 0) + 1

    for key in targetCount:
        if targetCount[key] > newspaperCount.get(key, 0):
            return False

    return True

print(find_target(newspapers=newspapers, target=target)) 

