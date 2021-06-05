def tokenize(expr):

    expr = list(expr)
    tokexp = []
    i = 0
    while i < (len(expr)):

        char = expr[i]
        if char in ["(", ")", "[", "]", "*", "^", "/"]:

            tokexp.append(char)
        
        elif char in ["+", "-"]:
            
            if i == 0:
                tokexp.append("0")
                tokexp.append(char)

            elif expr[i-1] in ["(", "["]:
                tokexp.append("0")
                tokexp.append(char)
            
            else:
                
                tokexp.append(char)

        elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            
            if i == 0:
                tokexp.append(char)
            elif expr[i-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                tokexp[-1]= tokexp[-1]+char
            else:
                tokexp.append(char)
        elif char == " ":
            print("La expresion contiene espacios. Se eliminaran.")

        elif char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]: 
            if i == 0:
                tokexp.append(char)
            elif expr[i-1] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
                tokexp[-1]= tokexp[-1]+char
            else:
                tokexp.append(char)
        else:
            print("Caracter no permitido en la posicion: ", i)
            return -1
        i = i+1
    return tokexp


