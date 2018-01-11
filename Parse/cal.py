def testFunction(a):
    return a
def main():
    testFunc = testFunction3
    TIPS_T = "EXPR: %s RESULT: %d\n"
    expr = "1+1*3+5-6#"
    post = [None] * 1000
    ss = [None] * 1000
    ch = None
    sum = None
    i = None
    t = None
    z = None
    error = 0
    top = 0
    sum = expr
    t = 1
    i = 0
    ch = expr[i]
    i = i + 1
    while ch != '#':
        if ch == '+' or ch == '-':
            while top != 0 and ss[top] != '(':
                post[t] = ss[top]
                top = top - 1
                t = t + 1
            top = top + 1
            ss[top] = ch
        elif ch == '*' or ch == '/':
            while ss[top] == '*' or ss[top] == '/':
                post[t] = ss[top]
                top = top - 1
                t = t + 1
            top = top + 1
            ss[top] = ch
        elif ch == '(':
            top = top + 1
            ss[top] = ch
        elif ch == ')':
            while ss[top] != '(':
                post[t] = ss[top]
                top = top - 1
                t = t + 1
            top = top - 1
        elif ch == ' ':
            z = 1
        else:
            while ch.isdigit() or ch == '.':
                post[t] = ch
                t = t + 1
                ch = expr[i]
                i = i + 1
            i = i - 1
            post[t] = ' '
            t = t + 1
        ch = expr[i]
        i = i + 1
    while top != 0:
        post[t] = ss[top]
        t = t + 1
        top = top - 1
    post[t] = ' '
    newstack = [None] * 100
    newstr = [None] * 100
    t = 1
    top = 0
    ch = post[t]
    t = t + 1
    temp = None
    tempTop = None
    while ch != ' ' and error == 0:
        if ch == '+':
            tempTop = top - 1
            newstack[tempTop] = newstack[tempTop] + newstack[top]
            top = top - 1
        elif ch == '-':
            tempTop = top - 1
            newstack[tempTop] = newstack[tempTop] - newstack[top]
            top = top - 1
        elif ch == '*':
            tempTop = top - 1
            newstack[tempTop] = newstack[tempTop] * newstack[top]
            top = top - 1
        elif ch == '/':
            if newstack[top] != 0:
                tempTop = top - 1
                newstack[tempTop] = newstack[tempTop] / newstack[top]
            else:
                error = 1
            top = top - 1
        else:
            i = 0
            while ch.isdigit() or ch == '.':
                newstr[i] = ch
                i = i + 1
                ch = post[t]
                t = t + 1
            temp = 0
            newstr[i] = temp
            top = top + 1
            newstack[top] = int("".join(newstr[:newstr.index(0)]))
        ch = post[t]
        t = t + 1
    result = None
    result = newstack[top]
    if error == 0:
        print(TIPS_T % (expr,result,))
    else:
        print("error\n")
    return 0

if __name__ == '__main__':
    main()