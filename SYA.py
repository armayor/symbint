def SYA(expr):
    stack = []
    queue = []
    
    for i in range (len(expr)):
        token = expr[i]
        #print("cola: ", queue)
        #print("stack", stack)
        if not is_operator(token) and not is_function(token) and not is_symbol(token):
            queue.append(token)
        elif is_operator(token):

            while precedence(token, stack):
                queue.append(stack[-1])
                stack.pop(-1)
            stack.append(token)
        elif is_function(token):
            stack.append(token)

        elif is_symbol(token):

            if token in ["(", "["]:
                stack.append(token)
            else:
                while not (stack[-1] in ["(", "["]):
                    queue.append(stack[-1])
                    stack.pop(-1)
                stack.pop(-1)
                if not(not stack):
                    while is_function(stack[-1]):
                        queue.append(stack[-1])
                        stack.pop(-1)
                        if (not stack):
                            break
                
    while not(not stack):
        queue.append(stack[-1])
        stack.pop(-1)
    return queue

##################################################################################################
# Funciones Auxiliares
##################################################################################################
def is_operator(car):
    operator_list = ["+", "-", "*", "/", "^"]
    if car in operator_list:
        return 1
    else:
        return 0
    
def is_function(car):
    function_list = ["cos", "sin", "tan", "exp", "log"]
    if car in function_list:
        return 1
    else:
        return 0

def is_symbol(car):
    symbol_list = ["(", ")", "[", "]"]
    if car in symbol_list:
        return 1
    else:
        return 0

def precedence(token, stack):
    if not stack:
        return 0
    else:
        element = [token, stack[-1]]
        priority = [0,0]

        for i in range(len(element)):
            if element[i]== "^":
                priority[i] = 4
            elif element[i] in ["*", "/"]:
                priority[i] = 3
            elif element[i] in ["+", "-"]:
                priority[i] = 2
        
        if priority[1]>=priority[0]:
            return 1
        else:
            return 0

