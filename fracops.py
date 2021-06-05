from CONVERT import convert
from gcd import gcd
#####################################################################
# Devuelve el numerador de una fraccion en formato int
#####################################################################
def getnum(fraccion):
    num = fraccion[1] # numerador
    if isinstance(num, list): # si es un numero negativo
        return int(-1*int(num[2]))
    else:
        return int(num)

#####################################################################
# Devuelve el denominador de una fraccion en formato int
#####################################################################
def getden(fraccion):
    den = fraccion[2] # denominador
    return int(den)

#####################################################################
# Convierte a forma de fraccion si es preciso
#####################################################################
def put_in_frac_form(elemento):
    if not isinstance(elemento, list): # si me dan un numero positivo
        return ['/', elemento, '1']
    else:
        if elemento[0] == '-': # si me dan un numero negativo
            return ['/', elemento, '1']
        elif elemento[0] == "/": # si ya me dan una fraccion
            return elemento
        else:
            raise ValueError("El formato del elemento a convertir en fraccion no es el correcto:", elemento)

#####################################################################
# Suma dos fracciones
#####################################################################
def fracsum(f1,f2):
    frac1 = put_in_frac_form(f1) # fraccion 1
    frac2 = put_in_frac_form(f2) # fraccion 2
    
    ##### Obtener numeradores y denominadores #####
    numf1 = getnum(frac1)
    denf1 = getden(frac1)
    numf2 = getnum(frac2)
    denf2 = getden(frac2)

    ##### Calculo fraccion suma #####
    numsuma = numf1*denf2 + numf2*denf1
    densuma = denf1*denf2
    mcd = gcd(abs(numsuma), abs(densuma))
    numsuma = int(numsuma/mcd)
    densuma = int(densuma/mcd)

    ##### Formateo del output #####
    if densuma == 0: # division por cero
        raise ValueError("Division por cero:", frac1, frac2)
    elif densuma < 0: # denominador negativo
        numsuma = -1*numsuma
        densuma = -1*densuma
    
    if numsuma > 0:         # fraccion no nula positiva
        if densuma == 1:    # numero natural
            return str(abs(numsuma))
        else:               # numero natural
            return ['/', str(abs(numsuma)), str(densuma)]

    elif numsuma == 0: # cero
        return '0'

    else: # fraccion no nula negativa
        if densuma == 1:
            return ['-', '0', str(abs(numsuma))]
        else:
            return ['/', ['-', '0', str(abs(numsuma))], str(densuma)]


#####################################################################
# Producto de dos fracciones
#####################################################################
def fracprod(f1,f2):
    frac1 = put_in_frac_form(f1) # fraccion 1
    frac2 = put_in_frac_form(f2) # fraccion 2
    
    ##### Obtener numeradores y denominadores #####
    numf1 = getnum(frac1)
    denf1 = getden(frac1)
    numf2 = getnum(frac2)
    denf2 = getden(frac2)

    ##### Calculo fraccion producto #####
    numprod = numf1*numf2
    denprod = denf1*denf2
    mcd = gcd(abs(numprod), abs(denprod))
    numprod = int(numprod/mcd)
    denprod = int(denprod/mcd)

    ##### Formateo del output #####
    if denprod == 0: # division por cero
        raise ValueError("Division por cero:", frac1, frac2)
    elif denprod < 0: # denominador negativo
        numprod = -1*numprod
        denprod = -1*denprod
    if numprod > 0:         # fraccion no nula positiva
        if denprod == 1:    # numero natural
            return str(abs(numprod))
        else:               # numero natural
            return ['/', str(abs(numprod)), str(denprod)]

    elif numprod == 0: # cero
        return '0'

    else: # fraccion no nula negativa
        if denprod == 1:
            return ['-', '0', str(abs(numprod))]
        else:
            return ['/', ['-', '0', str(abs(numprod))], str(denprod)]


#####################################################################
# Potencia de una fraccion por un entero positivo, nulo o negativo
#####################################################################
def fracpot(f1,n):
    frac1 = put_in_frac_form(f1) # fraccion 1
    
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

    
    ##### Obtener numeradores y denominadores #####
    numf1 = getnum(frac1)
    denf1 = getden(frac1)

    ##### Si se pide 0^0 error #####
    if pot == 0 and numf1 == 0:
        raise ValueError('0^0:', frac1, pot)

    ##### Calculo fraccion potencia #####
    if pot >= 0:
        numpot = numf1**pot
        denpot = denf1**pot
    else:
        numpot = denf1**abs(pot)
        denpot = numf1**abs(pot)

    mcd = gcd(abs(numpot), abs(denpot))
    numpot = int(numpot/mcd)
    denpot = int(denpot/mcd)

    ##### Formateo del output #####
    if denpot == 0: # division por cero
        raise ValueError("Division por cero:", frac1, n)
    elif denpot < 0: # denominador negativo
        numpot = -1*numpot
        denpot = -1*denpot
    
    if numpot > 0:         # fraccion no nula positiva
        if denpot == 1:    # numero natural
            return str(abs(numpot))
        else:               # numero natural
            return ['/', str(abs(numpot)), str(denpot)]

    elif numpot == 0: # cero
        return '0'

    else: # fraccion no nula negativa
        if denpot == 1:
            return ['-', '0', str(abs(numpot))]
        else:
            return ['/', ['-', '0', str(abs(numpot))], str(denpot)]

#####################################################################
# Division de dos fracciones
#####################################################################
def fracdiv(f1,f2):
    return fracprod(f1,fracpot(f2,-1))

#####################################################################
# Resta de dos fracciones
#####################################################################
def fracdif(f1,f2):
    return fracsum(f1,fracprod(f2,convert('-1')))

#####################################################################
# gcd de dos polinomios
#####################################################################
def fracgcd(f1,f2):
    frac1 = put_in_frac_form(f1) # fraccion 1
    frac2 = put_in_frac_form(f2) # fraccion 2
    
    ##### Obtener numeradores y denominadores #####
    numf1 = getnum(frac1)
    denf1 = getden(frac1)
    numf2 = getnum(frac2)
    denf2 = getden(frac2)

    num = int(gcd(abs(numf1), abs(numf2)))
    den = int(abs(denf1*denf2)/gcd(abs(denf1), abs(denf2)))

    return fracdiv(str(num), str(den))



#####################################################################
############################## TESTING ##############################
#####################################################################

#f1 = ['/', '1', '4']
#f2 = ['1']
#n = convert('1/4')

#print(fracgcd(f1,f2))