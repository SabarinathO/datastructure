def longestValidParentheses(s) :
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s): # This creates an iterable that produces pairs of (index, element) for each element in s
        if char == '(':
            stack.append(i)
        elif char == ')':
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)
        else:
            exit(0)
    return max_length


s=(input("enter the character"))
print(longestValidParentheses(s))  # Output: 6
