from polops import ispol, poldiff, poldiv, poldif, polcont, polprod
from euclidean import EED
from CONVERT import convert

def yun(pol):
    ##### Transformar a polinomios si hiciera falta #####
    if not ispol(pol):
        p = [pol]      # convierto a tipo polinomio
    else:
        p = pol.copy() # copio para no mutar el polinomio inicial
    #####################################################
    sqff = []
    con = polcont(p)
    if con != '0':
        p = poldiv(p,con)[0]
    cd = p[0]
    if isinstance(cd, list):
            if cd[0] == '-':
                p  = poldiv(p,[['-', '0', '1']])[0]
            elif cd[0] == '/' and isinstance(cd[1], list):
                p  = poldiv(p,[['-', '0', '1']])[0]

    [a1, a2, g] =  EED(p, poldiff(p))

    c = []
    [quot,rem] =  poldiv(p,g)
    c.append(quot)

    d = []
    [quot,rem] =  poldiv(poldiff(p),g)
    d.append(poldif(quot,poldiff(c[0])))
    i = 0

    while c[i] != ['1']:
        [a1, a2, g] =  EED(c[i], d[i])
        sqff.append(g)
        [quot,rem] =  poldiv(c[i], sqff[i])
        c.append(quot)
        [quot,rem] =  poldiv(d[i],sqff[i])
        d.append(poldif(quot,poldiff(c[i+1])))
        i = i+1
    
    if len(sqff) == 0:
        if isinstance(cd, list):
            if cd[0] == '-':
                p  = polprod(p,[['-', '0', '1']])
            elif cd[0] == '/' and isinstance(cd[1], list):
                p  = polprod(p,[['-', '0', '1']])
        return polprod(p,con)

    sqff[0] = polprod(sqff[0],con)
    if isinstance(cd, list):
            if cd[0] == '-':
                sqff[0]  = polprod(sqff[0],[['-', '0', '1']])
            elif cd[0] == '/' and isinstance(cd[1], list):
                sqff[0]  = polprod(sqff[0],[['-', '0', '1']])
    return sqff

#####################################################################
############################## TESTING ##############################
#####################################################################

#p = ['732736', '0', '549552', '0', '137388', '0', '11449']
#p = ['1']
#print(yun(p))
print(yun(convert(['-1', '3', '9', '-27'])))
