from subsresultant import subresultant
from polops import poldiv, polprod, poldiv, poldiff
from euclidean import EED
from yun import yun
from FieldExtension import FEpoldiv, FEpolprod, FEpoldif

def intlogpart(p1,p2):
    [res, restos] = subresultant(p1,p2)
    restos = restos[0:-1]
    sqffRes = yun(res[0])
    subres = []
    for i in range(len(sqffRes)):
        for j in range(len(restos)):
            if len(restos[j]) == i+2:
                subres.append(restos[j])


    for i in range(len(sqffRes)):
        if len(sqffRes[i])>1:
            sqff = yun(subres[i][0])
            for j in range(len(sqff)):
                [a1, a2, gcd] = EED(sqff[j], sqffRes[i])
                ter = polprod(gcd,str(j+1))
                subres[i] = FEpoldiv(subres[i], ter)[0]
                subres[i] = FEpolprod(subres[i], [['1']], sqffRes[i])


    logpart = []

    for i in range(len(sqffRes)):
        if len(sqffRes[i])>1:
            logpart.append([sqffRes[i], subres[i]])

    return logpart

#p1 = ['1']
#p2  = ['1', '0']
#pol2 = FEpolprod([['1', '0']], poldiff(p2))

#pol2 = FEpoldif(p1, pol2)
#print(intlogpart(p2,pol2))