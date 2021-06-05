##################################################################################################
# diff(expression) Devuelve una simplificacion elemental de expression en notacion SQRPN
# expression es una expresion en notacion SQRPN
##################################################################################################
def simplify(expression):
    
    if not isinstance(expression,list):
        return expression
        
    else:
        if is_function(expression[0]):
            return  [expression[0], simplify(expression[1])]

        else: 
            if expression[0] == '*':
                if expression[1] == '1':
                    return simplify(expression[2])
                elif expression[2] == '1':
                    return simplify(expression[1])
                elif expression[1] == '0':
                    expression = '0'
                    return expression
                elif expression[2] == '0':
                    expression = '0'
                    return expression
                elif expression[2] == expression[1]:
                    return ['^',  simplify(expression[1]),'2']
                else:
                    return [expression[0],simplify(expression[1]), simplify(expression[2])]

            elif expression[0] == '+':
                if isinstance(expression[1], str) and isinstance(expression[2], str) and expression[1].isnumeric() and expression[2].isnumeric():
                    return str(int(expression[1])+int(expression[2]))
                elif expression[1] == '0':
                    return simplify(expression[2])
                elif expression[2] == '0':
                    return simplify(expression[1])
                elif expression[2] == expression[1]:
                    return ['*', '2', simplify(expression[1])]
                else:
                    return [expression[0],simplify(expression[1]), simplify(expression[2])]

            elif expression[0] == '-':
                if isinstance(expression[1], str) and isinstance(expression[2], str) and expression[1].isnumeric() and expression[2].isnumeric() and int(expression[1])>=int(expression[2]):
                    return str(int(expression[1])-int(expression[2]))
                if expression[1] == '0' and expression[2] == '0':
                    expression = '0'
                    return expression
                if expression[2] == '0':
                    return simplify(expression[1])
                else:
                    return [expression[0],simplify(expression[1]), simplify(expression[2])]
            else:
                    return [expression[0],simplify(expression[1]), simplify(expression[2])]
  

    

def is_function(car):
    function_list = ["cos", "sin", "tan", "exp", "log"]
    if car in function_list:
        return 1
    else:
        return 0