def atoi(str):
    i = 0
    while(str[i] != 0):
        i = i + 1
    temp_str = str[:i]
    return int(''.join(temp_str))

def main():
    
    
    
    expr = "1+1*3/2+(9-1*2)#"
    
    post = [0] * 100
    ss = [0] * 100
    
    
    
    
    
    error = 0
    top = 0
    sum = len(expr)
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
            
            top = top -1
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
    newstack = [0] * 100
    newstr = [''] * 100
    t = 1
    top = 0
    ch = post[t]
    t = t + 1
    
    while ch != ' ' and error == 0:
        if ch == '+':
            newstack[top - 1] = newstack[top - 1] + newstack[top]
            top = top - 1
        elif ch == '-':
            newstack[top - 1] = newstack[top - 1] - newstack[top]
            top = top - 1
        elif ch == '*':
            newstack[top - 1] = newstack[top - 1] * newstack[top]
            top = top - 1
        elif ch == '/':
            if newstack[top] != 0:
                newstack[top - 1] = newstack[top - 1] // newstack[top]
            else:
                error = 1
            top = top - 1
        else:
            i = 0
            while ch.isdigit() or ch == '.':
                newstr[i] = ch
                i = i + 1
                ch = post[t]
                t += 1
            
            temp = 0
            newstr[i] = temp
            top = top + 1
            newstack[top] = atoi(newstr)#int(''.join(newstr))
        
        ch = post[t]
        t = t + 1
    
    if error == 0:
        print(newstack[top])
    else:
        print('wrong')


main()



    














