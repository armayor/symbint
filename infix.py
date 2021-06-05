##################################################################################################
# infix(expr) Convierte la notacion SQRPN a una cadena de texto
# expr es la expresion en notacion SQRPN
##################################################################################################
def infix(expr):
    for i in range(len(expr)):
        if is_operator(expr[i]):
            return  "(" + infix(expr[i+1]) + expr[i] + infix(expr[i+2]) + ")"
        elif is_function(expr[i]):
            return   expr[i] + "(" + infix(expr[i+1]) + ")"
        else:
            return expr


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

