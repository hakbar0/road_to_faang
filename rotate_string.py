class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        for i in range(len(s)):
            if goal != s[i:] + s[:i]:
                continue

            return True
        
        return False
