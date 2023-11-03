def check_brackets(s):
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}',
    }
    stack = [] # (bracket, index)[]
    
    for i in range(len(s)):
        if len(stack) != 0 and s[i] == brackets[stack[-1][0]]: # closes the last bracket
            stack.pop()
        elif s[i] in brackets: # is an opening bracket
            stack.append((s[i], i))
        else: # closing, but not for the last bracket
            return i
    if len(stack) != 0:
        return stack[0][1] # return index of the first unclosed bracket
    return -1 # success

print(check_brackets('[()]()({})'))  # -1
print(check_brackets('[()]]()({})')) # 4
print(check_brackets('[()](()({})')) # 4

