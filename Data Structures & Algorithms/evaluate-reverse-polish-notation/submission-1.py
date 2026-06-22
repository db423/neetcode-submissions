class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for t in tokens:
            if t not in "+-*/":
                num_stack.append(int(t))
            if num_stack and t in "+-*/":
                a = num_stack.pop()
                b = num_stack.pop()
                if t == '+':
                    num_stack.append(a+b)
                elif t == '-':
                    num_stack.append(b-a)
                elif t == '*':
                    num_stack.append(a*b)
                elif t == '/':
                    num_stack.append(int(b/a))
        return num_stack.pop()

            