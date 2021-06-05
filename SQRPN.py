##################################################################################################
# SQRPN(expr) Devuelve la forma con corchetes de la RPN (Reverse Polish Notation)
# expr es una lista que contiene los tokens de la RPN
##################################################################################################
def SQRPN(expr):

    # Primer punto de iteracion en la lista
    i = 0 

    # Itero hasta que llegue al final
    while i < len(expr):

        # Si tengo un operador ..., el1, el2, operador, ... lo concateno en  [operador, el1, el2]
        if is_operator(expr[i]):
            
            expr[i] = [expr[i], expr[i-2], expr[i-1]]
            expr.pop(i-2) # Elimino el1 y muevo indice
            i = i-1
            expr.pop(i-1) # Elimino el2 y muevo indice
            i = i-1            
            
        # Si tengo una funcion ..., arg, funcion, ... lo concateno en  [funcion, arg]
        elif is_function(expr[i]):
            
            expr[i] = [expr[i], expr[i-1]]
            expr.pop(i-1) # Elimino arg y muevo indice
            i = i-1
        
        i = i + 1 # Siguiente iteracion
        
    return expr[0] # Devuelvo lista con sublistas

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

