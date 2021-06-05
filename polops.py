from CONVERT import convert
from fracops import fracsum, fracprod, fracdiv, fracgcd
#####################################################################
# Un polinomio es una lista ['el0', 'el1',..., 'eln' ] de n+1 elemen-
# tos. Al ser una lista con corchetes es mutable. Cada coeficiente
# puede ser una fraccion o un numero que esten en formato adecuado
# para que fracops opere con ellos
#####################################################################


#####################################################################
# Comprueba si es un polinomio
#####################################################################
def ispol(p):
    if not isinstance(p,list):
        return 0
    elif p[0] != '/' and p[0] != '-':
        return 1
    else:
        return 0

#####################################################################
# Elimina ceros innecesarios
#####################################################################
def quitaceros(p):
    pol = p.copy()

    while pol[0] == '0' and len(pol) > 1:
        pol.pop(0)
    
    return pol
        
#####################################################################
# Devuelve la suma de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################
def polsum(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    grado1 = len(p1)-1
    grado2 = len(p2)-1

    if grado1 >= grado2:
        polsuma = p1.copy()

        for i in range(len(p2)):
            polsuma[len(p1)-len(p2)+i] =  fracsum(polsuma[len(p1)-len(p2)+i], p2[i])
    else:
        polsuma = p2.copy()

        for i in range(len(p1)):
            polsuma[len(p2)-len(p1)+i] =  fracsum(polsuma[len(p2)-len(p1)+i], p1[i])
    
    return quitaceros(polsuma)

#####################################################################
# Devuelve el producto de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################

def polprod(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    prod = ['0']*(len(p1)+len(p2)-1) # Inicializo el producto como
                                        # un polinomio nulo

    for i in range(len(p1)):
        for j in range (len(p2)):
            prod[i+j] = fracsum(prod[i+j], fracprod(p1[i],p2[j]))


    return quitaceros(prod)

#####################################################################
# Devuelve la resta de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################

def poldif(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    return polsum(p1, polprod(p2, '-1'))


#####################################################################
# Devuelve la division de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################

def poldiv(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    if p2 == ['0']:
        raise ValueError("Division por cero:", p2)

    Q = ['0']
    R = p1.copy()    
    
    while R != ['0'] and (len(R)-len(p2)) >= 0:
        T = ['0']*(len(R)-len(p2)+1)
        T[0] = fracdiv(R[0], p2[0])
        Q = polsum(Q, T)
        R = poldif(R, polprod(p2,T))


    return [quitaceros(Q), quitaceros(R)]

#####################################################################
# Devuelve la pseudodivision de dos polinomios o de un polinomio y 
# una constante o de dos constantes
#####################################################################

def polpdiv(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    if p2 == ['0']:
        raise ValueError("Division por cero:", p2)

    Q = ['0']
    R = p1.copy()    
    N = len(p1)-len(p2)+1
    b = p2[0]

    while R != ['0'] and (len(R)-len(p2)) >= 0:
        T = ['0']*(len(R)-len(p2)+1)
        T[0] = R[0]
        N = N-1
        Q = polsum(polprod(b,Q), T)
        R = poldif(polprod(b,R), polprod(p2,T))


    return [quitaceros(polprod(polpot(b,N),Q)), quitaceros(polprod(polpot(b,N),R))]



#####################################################################
# Devuelve la potencia  de un polinomio y una constante o de dos 
# constantes
#####################################################################

def polpot(pol1,n):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not isinstance(n,int):
        if isinstance(n,str):
            pot = int(n)
        elif isinstance(n,list):
            if n[0] == '-':
                pot = -1*int(n[2])
            else:
                raise ValueError('Exponente incorrecto:', n)
        else:
            raise ValueError('Exponente incorrecto:', n)
    else:
        pot = n
    
    if pot == 0 and p1  == ['0']:
        raise ValueError('0^0:', p1, n)
    
    if pot == 0:
        polpot =  ['1']
    elif pot > 0:
        polpot = ['1']
        for i in range(pot):
            polpot = polprod(polpot, p1)
    else:
        polpot = ['1']
        for i in range (abs(pot)):
            polpot = polprod(polpot, p1)
        polpot = ['q', ['1'], polpot]

    return quitaceros(polpot)

#####################################################################
# Devuelve la derivada formal de un polinomio 
#####################################################################

def poldiff(pol1):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if len(p1) == 1: # Si el polinomio es una constante
        return ['0']

    deriv = ['0']*(len(p1)-1)
    for i in range(len(p1)-1):
        deriv[i] = fracprod(p1[i], str(len(p1)-1-i))
    return quitaceros(deriv)

#####################################################################
# Devuelve la integral formal de un polinomio 
#####################################################################

def polint(pol1):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial


    pint = ['0']*(len(p1)+1)
    for i in range(len(p1)):
        pint[i] = fracdiv(p1[i], str(len(p1)-i))
    return quitaceros(pint)

#####################################################################
# Devuelve el contenido de un polinomio
#####################################################################

def polcont(pol1):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if len(p1) == 1: # Si el polinomio es una constante
        if isinstance(p1[0], list):
            if p1[0][0] == '-':
                return p1[0][2]
            elif p1[0][0] == '/' and isinstance(p1[0][1], list):
                return fracprod(p1[0], ['-', '0', '1'])
        else:
            return p1[0]

    contenido = fracgcd(p1[0], p1[0])
    for i in range(len(p1)):
        contenido = fracgcd(contenido, p1[i])
    return contenido

#####################################################################
############################## TESTING ##############################
#####################################################################

#p1 = convert(['1', '0', '-1', '0', '-2'])
#p2 = convert(['-1','3','9', '-27'])

#print(polcont(convert(['(-1)/2'])))