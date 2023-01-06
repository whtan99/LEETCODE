class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        if not s:
            return True
        for b in s:
            print(b)
            if (b == '(') or (b == '{') or (b == '['):
                temp.append(b)
            elif (b == ')'):
                if not temp or temp[-1] != '(':
                    return False
                temp = temp[:-1]
            elif (b == '}'):
                if not temp or temp[-1] != '{':
                    return False
                temp = temp[:-1]
            elif (b == ']'):
                if not temp or temp[-1] != '[':
                    return False
                temp = temp[:-1]
        return len(temp) == 0
