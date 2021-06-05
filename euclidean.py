from CONVERT import convert
from polops import ispol, poldiv, poldif, polprod, polsum, polcont, poldiff
from fracops import fracgcd

#################################################################
# EED: Extended Euclidean Division
# Devuelve a1, a2, y g tales que dados dos polinomios p, q, 
# a1*p + a2*q = g, siendo g = mcd(p,q)
#################################################################
def EED(pol1,pol2):
    ##### Transformar a polinomios si hiciera falta #####
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()
    #####################################################
    c1 = polcont(p1) # contenido
    c2 = polcont(p2)
    c = fracgcd(c1,c2)
    if c1 != '0':
        p1 = poldiv(p1,c1)[0]
    if c2 != '0':
        p2 = poldiv(p2,c2)[0]

    a1 = ['1']
    a2 = ['0']
    b1 = ['0']
    b2 = ['1']

    while p2 != ['0']:
        [q,r] = poldiv(p1,p2)
        p1 = p2
        p2 = r
        r1 = poldif(a1, polprod(q,b1))
        r2 = poldif(a2, polprod(q,b2))
        a1 = b1
        a2 = b2
        b1 = r1
        b2 = r2


    if len(p1) != 1:
        if c1 != '0':
            A1 = poldiv(polprod(poldiv(a1,polcont(p1))[0],c),c1)[0]
        else:
            A1 = polprod(poldiv(a1,polcont(p1))[0],c)
        
        if c2 != '0':
            A2 = poldiv(polprod(poldiv(a2,polcont(p1))[0],c),c2)[0]
        else:
            A2 = polprod(poldiv(a2,polcont(p1))[0],c)

        G = polprod(poldiv(p1,polcont(p1))[0],c)
        cd = G[0]

        if isinstance(cd, list):
            if cd[0] == '-':
                A1 = poldiv(A1,[['-', '0', '1']])[0]
                A2 = poldiv(A2,[['-', '0', '1']])[0]
                G  = poldiv(G,[['-', '0', '1']])[0]
            elif cd[0] == '/' and isinstance(cd[1], list):
                A1 = poldiv(A1,[['-', '0', '1']])[0]
                A2 = poldiv(A2,[['-', '0', '1']])[0]
                G  = poldiv(G,[['-', '0', '1']])[0]
        return [A1, A2, G]
    else:
        
        if polcont(p1) != '0':
            if c1 != '0':
                A1 = poldiv(polprod(poldiv(a1,polcont(p1))[0],c),c1)[0]
            else:
                A1 = polprod(poldiv(a1,polcont(p1))[0],c)
        
            if c2 != '0':
                A2 = poldiv(polprod(poldiv(a2,polcont(p1))[0],c),c2)[0]
            else:
                A2 = polprod(poldiv(a2,polcont(p1))[0],c)

            G = polprod(poldiv(p1,polcont(p1))[0],c)
            cd = G[0]
            if isinstance(cd, list):
                if cd[0] == '-':
                    A1 = poldiv(A1,[['-', '0', '1']])[0]
                    A2 = poldiv(A2,[['-', '0', '1']])[0]
                    G  = poldiv(G,[['-', '0', '1']])[0]
                elif cd[0] == '/' and isinstance(cd[1], list):
                    A1 = poldiv(A1,[['-', '0', '1']])[0]
                    A2 = poldiv(A2,[['-', '0', '1']])[0]
                    G  = poldiv(G,[['-', '0', '1']])[0]
            return [A1, A2, G]
        else:
            if c1 != '0':
                A1 = poldiv(polprod(a1,c),c1)[0]
            else:
                A1 = polprod(a1,c)
        
            if c2 != '0':
                A2 = poldiv(polprod(a2,c),c2)[0]
            else:
                A2 = polprod(a2,c)
            
            G = polprod(poldiv(p1,polcont(p1))[0],c)
            cd = G[0]
            if isinstance(cd, list):
                if cd[0] == '-':
                    A1 = poldiv(A1,[['-', '0', '1']])[0]
                    A2 = poldiv(A2,[['-', '0', '1']])[0]
                    G  = poldiv(G,[['-', '0', '1']])[0]
                elif cd[0] == '/' and isinstance(cd[1], list):
                    A1 = poldiv(A1,[['-', '0', '1']])[0]
                    A2 = poldiv(A2,[['-', '0', '1']])[0]
                    G  = poldiv(G,[['-', '0', '1']])[0]
            
            return [A1, A2, G]
#################################################################
# EEDio: Extended Euclidean Diophantine
# Devuelve a1 y a2 tales que dados tres polinomios p, q, t
# a1*p + a2*q = t
#################################################################
def EEDio(pol1,pol2, pol3):
    ##### Transformar a polinomios si hiciera falta #####
    if not ispol(pol1):
        p1 = [pol1]      # convierto a tipo polinomio
    else:
        p1 = pol1.copy() # copio para no mutar el polinomio inicial

    if not ispol(pol2):
        p2 = [pol2]
    else:
        p2 = pol2.copy()

    if not ispol(pol3):
        p3 = [pol3]
    else:
        p3 = pol3.copy()
    #####################################################
    
    [a1, a2, g] = EED(p1,p2)

    [q, r] = poldiv(p3, g)

    if r != ['0']:
        raise ValueError("El polinomio t no esta en el ideal generado por p y q")

    a1 = polprod(q,a1)
    a2 = polprod(q,a2)

    if a1 != ['0'] and len(a1) >= len(p2):
        [q, r] = poldiv(a1,p2)
        a1 = r
        a2 = polsum(a2, polprod(q,p1))
    
    return [a1, a2]

#####################################################################
############################## TESTING ##############################
#####################################################################

p1 = convert(['1', '3'])
p2 = convert(['1', '-3'])
p3 = convert(['-17', '0', '83'])
#p1 = ['16', '4', ['/', '1', '4']]
s = EEDio(p1,p2,p3)[0]
t = EEDio(p1,p2,p3)[1]
print(polsum(polprod(s,p1), polprod(t,p2)))
print(EEDio(p1,p2,p3))
#print(polprod(p2,EEDio(p1,p2,p3)[1] ))
