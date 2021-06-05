from CONVERT import convert
from polops import ispol
from FieldExtension import FEpolpdiv, FEpoldiv, FEpolpot, FEpolprod
from fracops import fracpot
def subresultant(pol1,pol2):
    #################################################################
    # Convertir a tipo polinomio con coeficientes polinomicos
    # si hiciera falta

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
    #################################################################
    resto = []
    resto.append(p1)
    resto.append(p2)

    r     = []
    r.append(p1[0]) # el primer elemento es irrelevante

    i = 1

    gamma = []
    gamma.append(0) # el primero es irrelevante
    gamma.append([['-', '0', '1']])

    delta = []
    delta.append(0) # el primero es irrelevante
    delta.append(len(p1)-len(p2))

    beta = []
    beta.append(0) # el primero es irrelevante
    beta.append([fracpot(['-','0','1'],delta[i]+1)])
   
    while resto[i] != [['0']]:
        restoprov = resto[i]
        r.append([restoprov[0]])
        [Q, R] = FEpolpdiv(resto[i-1], resto[i])
        [quot, rem] = FEpoldiv(R, beta[i])
        resto.append(quot)

        
        i = i+1
        if resto[i] == [['0']]:
            break
        ter1 = FEpolprod(r[i-1], [['-','0','1']])
        ter1 = FEpolpot(ter1, delta[i-1])
        ter2 = FEpolpot(gamma[i-1], 1-delta[i-1])
        gamma.append(FEpolprod(ter1,ter2))
        delta.append(len(resto[i-1])-len(resto[i]))

        ter1 = FEpolprod(r[i-1], [['-','0','1']])
        ter2 = FEpolpot(gamma[i], delta[i])
        beta.append(FEpolprod(ter1,ter2))


    k = i-1

    if len(resto[k])-1>0:
        return [['0'], resto]
    if len(resto[k-1])-1 == 1:
        return [resto[k], resto]

    s = 1
    c = [['1']]

    for l in range(k-1):
        j = l+1
        if (len(resto[j-1])-1)%2 == 1 and (len(resto[j])-1)%2 == 1:
            s = -s
        [quot, rem] = FEpoldiv(beta[j], FEpolpot(r[j],1+delta[j]))
        ter1 = quot
        ter1 = FEpolpot(ter1, len(resto[j])-1)
        ter2 = FEpolpot(r[j], len(r[j-1])-len(r[j+1]))
        ter3 = FEpolprod(ter1, ter2)
        c = FEpolprod(c, ter3)

    res = FEpolpot(resto[k], len(resto[k-1])-1)
    res = FEpolprod(c, res)
    s = convert(str(s))
    return [FEpolprod(s,res),resto]


#####################################################################
############################## TESTING ##############################
#####################################################################

#a1 = convert(['3', '0'])
#a2 = convert(['-1', '0', '0', '-4'])
#a3 = convert(['1', '0', '0', '0'])
#p1 = [a1, '0', a2]
#p2 = ['1', a3, ['-','0','9']]
#t  = ['1', '0', '1']
#print(subresultant(p1,p2)[0][0])

#a1 = convert(['2', '-17'])
#a2 = convert(['118/3'])
#a3 = convert(['-9'])
#p2 = [a1, a2]
#p1 = ['1', '0', ['-', '0', '5'], '0', '5', '0', '4']
#p2  = [[['-', '0', '6'], '0'], ['1'], ['20', '0'], [['-', '0', '3']], [['-', '0', '10'], '0'], ['6']]
#p1 = [[['-','0','2'], '0'],['1']]
#p2 = [['1'], ['0'], ['1']]
#print(subresultant(p2,p1)[1][3])
