from CONVERT import convert
from yun import yun
from polops import ispol, poldiv, polpot, polprod, poldiff, polsum, poldif
from euclidean import EEDio

def hr(pol1, pol2):
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
    
    sqff = yun(p2)
    g = []

    for i in range (1, len(sqff)):
        if len(sqff[i]) >1:
            V = sqff[i]
            [quot, rem] = poldiv(p2,polpot(V,i+1))
            U = quot

            for j in range(i, 0, -1):
                ter1 = polprod(U, poldiff(V))
                ter2 = V
                ter31 = polprod(p1, ['-', '0', '1'])
                [quot, rem] = poldiv(ter31, str(j))
                [B, C] = EEDio(ter1, ter2, quot)
                
                [quot, rem] = poldiv(B, polpot(V,j))
                g.append(quot)
                g.append(['q', rem, V,'^', str(j)])

                t1 = polprod(C, str(j))
                t1 = polprod(t1, ['-','0','1'])

                t2 = polprod(U,poldiff(B))
                p1 = poldif(t1,t2)
            
            p2 = polprod(U,V)
    return [g, p1, p2]

#p1 = convert(['17', '0', '-83'])
#p2 = convert(['-1','3','9', '-27'])

#print(hr(p1,p2))