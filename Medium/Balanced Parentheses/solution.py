def is_parentheses_balance(seq: str):
    pass
    count = 0
    for l in seq:
        if l == "(":
            count += 1
        elif l == ")":
            count -= 1
        else:
            return False
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False

# "(())()", “()”, and "(()(()))" are balanced, while "(()" and "(()))(" are not.
# True
print(is_parentheses_balance("(())()"))
print(is_parentheses_balance("(()(()))"))
print(is_parentheses_balance("()"))

# False:
print(is_parentheses_balance("(()"))
print(is_parentheses_balance("(()))("))