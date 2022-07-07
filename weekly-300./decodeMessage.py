class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        h = 0
        map = {}
        for char in key:
            if char not in alpha: continue
            if char not in map:
                map[char] = alpha[h]
                h += 1
        d = ""
        for char in message:
            if char not in map:
                d += char
            else:
                d += map[char]
        return d
