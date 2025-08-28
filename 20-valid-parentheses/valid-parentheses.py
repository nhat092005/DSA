class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(',
                '}': '{',
                ']': '['}

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs.get(ch):
                    return False
                stack.pop()

        return not stack