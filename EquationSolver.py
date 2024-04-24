from DSAStack import DSAStack,DSAQueue
def solve(equation):
    postfix=_parseInfixToPostfix(equation)
    result=_evaluatePostfix(postfix)
    return result
def precedenceOf(the_op):
    if the_op == '+' or the_op =='-':
        return 1
    elif the_op =='*' or the_op=='/':
        return 2
    
def _parseInfixToPostfix(equation):
    postfix=""
    opStack=DSAStack()
    for term in equation:
        if term =='(':
            opStack.push(term)
        elif term ==')':
            while opStack.top() !='(':
                postfix +=opStack.pop()
            opStack.pop()
        elif term == '*' or term =='-' or term =='+' or term =='/':
            while (not opStack.is_empty()) and (opStack.top() !='(') and precedenceOf(opStack.top()) >= precedenceOf(term):
                    postfix+=opStack.pop()
            opStack.push(term)
        else:
            postfix+=term
    while (not opStack.is_empty()):
        postfix +=opStack.pop()
    return postfix
def _evaluatePostfix(postfixQueue):
    numStack =DSAStack()
    answer =0.0
    print(postfixQueue)
    for i in postfixQueue:
        if i.isdigit():
            numStack.push(i)
        elif i =='+' or i=='-' or i=='*' or i=='/':
            op1 = float(numStack.pop())
            op2 = float(numStack.pop())
            num = _executeOperation(i,op1,op2)
            numStack.push(num)
    answer = numStack.pop()
    return answer
def _executeOperation(op,op1,op2):
    if op == '+':
        return op1+op2
    if op =='-':
        return op1-op2
    if op =='*':
        return op1*op2
    if op =='/':
        return op1/op2

