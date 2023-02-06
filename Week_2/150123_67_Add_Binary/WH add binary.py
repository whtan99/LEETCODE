class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) -1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            s = carry
            if i >= 0:
                s += ord(a[i]) - ord('0')
            if j >= 0:
                s += ord(b[j]) - ord('0')
            if s > 1:
                carry = 1
            else:
                carry = 0
            res += str(s % 2)
            i -= 1
            j -= 1
        if carry != 0:
            res += str(carry)
        return res[::-1]
