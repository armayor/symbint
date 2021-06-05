from polops import ispol, polsum, poldiv, polprod
from CONVERT import convert
#####################################################################
# Realiza operaciones en una extension Q[t][X] del anillo de polino-
# mios Q[X]. Ahora los coeficientes de polinomios son polinomios en
# Q[t]. t puede ser algebraico o transcendente. Si no se especifica
# el polinomio minimo se entiende t transcendente
#####################################################################

#####################################################################
# Elimina ceros innecesarios
#####################################################################
def FEquitaceros(p):
    pol = p.copy()

    while pol[0] == ['0'] and len(pol) > 1:
        pol.pop(0)
    
    return pol
        
#####################################################################
# Devuelve la suma de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################
def FEpolsum(pol1, pol2, t="trans"):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

    for i in range(len(p2)):
        if not ispol(p2[i]):
            p2[i] = [p2[i]]

    grado1 = len(p1)-1
    grado2 = len(p2)-1

    if grado1 >= grado2:
        polsuma = p1.copy()

        for i in range(len(p2)):
            polsuma[len(p1)-len(p2)+i] =  polsum(polsuma[len(p1)-len(p2)+i], p2[i])
            if t != "trans":
                [cociente, resto] = poldiv(polsuma[len(p1)-len(p2)+i], t)
                polsuma[len(p1)-len(p2)+i] = resto
    else:
        polsuma = p2.copy()

        for i in range(len(p1)):
            polsuma[len(p2)-len(p1)+i] =  polsum(polsuma[len(p2)-len(p1)+i], p1[i])
            if t != "trans":
                [cociente, resto] = poldiv(polsuma[len(p1)-len(p2)+i], t)
                polsuma[len(p1)-len(p2)+i] = resto
   
    return FEquitaceros(polsuma)

#####################################################################
# Devuelve el producto de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################
def FEpolprod(pol1, pol2, t="trans"):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

    for i in range(len(p2)):
        if not ispol(p2[i]):
            p2[i] = [p2[i]]

    prod = [['0']]*(len(p1)+len(p2)-1) # Inicializo el producto como
                                        # un polinomio nulo

    for i in range(len(p1)):
        for j in range (len(p2)):
            prod[i+j] = polsum(prod[i+j], polprod(p1[i],p2[j]))
            
            if t != 'trans':
                prod[i+j] = poldiv(prod[i+j],t)[1]

    return FEquitaceros(prod)

#####################################################################
# Devuelve la resta de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################

def FEpoldif(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

    for i in range(len(p2)):
        if not ispol(p2[i]):
            p2[i] = [p2[i]]

    return FEpolsum(p1, FEpolprod(p2, '-1'))

#####################################################################
# Devuelve la potencia  de un polinomio y una constante o de dos 
# constantes
#####################################################################

def FEpolpot(pol1,n):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

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
    
    if pot == 0 and p1  == [['0']]:
        raise ValueError('0^0:', p1, n)
    
    if pot == 0:
        polpot =  [['1']]
    elif pot > 0:
        polpot = [['1']]
        for i in range(pot):
            polpot = FEpolprod(polpot, p1)
    else:
        polpot = [['1']]
        for i in range (abs(pot)):
            polpot = FEpolprod(polpot, p1)
        polpot = ['q', [['1']], polpot]

    return FEquitaceros(polpot) 

#####################################################################
# Devuelve la pseudodivision de dos polinomios o de un polinomio y 
# una constante o de dos constantes
#####################################################################

def FEpolpdiv(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

    for i in range(len(p2)):
        if not ispol(p2[i]):
            p2[i] = [p2[i]]

    if p2 == [['0']]:
        raise ValueError("Division por cero:", p2)

    Q = [['0']]
    R = p1.copy()    
    N = len(p1)-len(p2)+1
    b = [p2[0]] # tengo que poner b como un polinomio

    while R != [['0']] and (len(R)-len(p2)) >= 0:
        T = ['0']*(len(R)-len(p2)+1)
        T[0] = R[0] # T ya tiene forma de polinomio, no tengo que volver a poner [ ]
        N = N-1
        Q = FEpolsum(FEpolprod(b,Q), T)
        R = FEpoldif(FEpolprod(b,R), FEpolprod(p2,T))


    return [FEquitaceros(FEpolprod(FEpolpot(b,N),Q)), FEquitaceros(FEpolprod(FEpolpot(b,N),R))]

#####################################################################
# Devuelve la division de dos polinomios o de un polinomio y una 
# constante o de dos constantes
#####################################################################

def FEpoldiv(pol1,pol2):
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    # Convierto los coeficientes a polinomios, si hiciera falta
    for i in range(len(p1)):
        if not ispol(p1[i]):
            p1[i] = [p1[i]]

    for i in range(len(p2)):
        if not ispol(p2[i]):
            p2[i] = [p2[i]]

    if p2 == [['0']]:
        raise ValueError("Division por cero:", p2)

    Q = [['0']]
    R = p1.copy()    
    
    while R != [['0']] and (len(R)-len(p2)) >= 0:
        T = [['0']]*(len(R)-len(p2)+1)
        [quot, rem] = poldiv(R[0], p2[0])
        T[0] = quot
        Q = FEpolsum(Q, T)
        R = FEpoldif(R, FEpolprod(p2,T))


    return [FEquitaceros(Q), FEquitaceros(R)]

#####################################################################
############################## TESTING ##############################
#####################################################################


#a1 = convert(['3', '0'])
#a2 = convert(['-1', '0', '0', '0'])
#a3 = convert(['1', '0', '0', '0'])
#p1 = [['1']]
#p2 = [['1']]
#t  = ['1', '0', '1']
#print(FEpolprod(p1,p2))

