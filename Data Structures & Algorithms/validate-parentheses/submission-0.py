class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_mp = {")" : "(" , "]" : "[", "}" : "{"}
        for c in s:
            if c in close_open_mp:
                if stack and stack[-1] == close_open_mp[c]: #check the last open bracket. 
                    stack.pop() #remove that open bracket.
                else:
                    return False # the corresponding open bracket for that closed bracket is not in the stack. 
            else:
                stack.append(c) # if an open bracket, add to stack.
        return True if not stack else False
        

        