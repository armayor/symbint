from CONVERT import convert
from HermiteReduce import hr
from subsresultant import subresultant
from FieldExtension import FEpolsum, FEpolprod, FEpoldif 
from polops import poldiff, polint, poldiv
from FORMAT import formatpol, formatquot, formathermite, printint, formatlogpart, formatpol2var
from intlogpart import intlogpart

#num = convert(['1', '0', '-3', '0', '6'])
#den = convert(['1', '0', '-5', '0', '5', '0', '4'])

#num = convert(['6', '2', '-1', '1/2', '-2', '8'])
#den = convert(['1', '0', '-9', '2'])

#num = convert(['3/5', '0', '0'])
#den = convert(['1', '1'])

##################### Input #####################
num = ''
den = ''

while num != "exit" and den != "exit":
    print("\n \n --------------------------------------------------------------------------\n")
    print("SYMBINT v1 (programado por Miguel Armayor Martinez)\n")
    print("Para salir del programa introducir 'exit' (sin comillas).\n")
    print("El numerador y el denominador deben ser polinomios con coeficientes en Q. Deben introducirse")
    print("los coeficientes de estos separados por espacios. Ejemplo: ")
    print("Para el polinomio 1*X^3-3X^2+1/4X-2/5 se debe introducir 1 -3 1/4 (-2)/5\n")
    print("El programa no funcionara si los polinomios son excesivamente largos o tienen una gran cantidad")
    print("de coeficientes fraccionarios, ya que en los calculos se obtienen numeros muy grandes que python")
    print("no puede gestionar como enteros.\n\n")
    num = input('Numerador: ')
    if num == "exit":
        break
    num = convert(num.split())
    den = input('Denominador: ')
    if den == "exit":
        break
    den = convert(den.split())
    print("\n\n")

    [quot, rem] = poldiv(num,den)
    A = rem
    D = den
    [g, p, q] = hr(A,D)

    pol2 = FEpolprod([['1', '0']], poldiff(q))

    pol2 = FEpoldif(p, pol2)



    ##################### OUTPUT #####################

    printint(formatpol(num), formatpol(den)) 


    print("\nParte racional Polinomial: \n")

    print(formatpol(polint(quot)))

    print("\nParte racional Hermite: \n")

    for element in g:
        if element[0] == 'q':
            formathermite(element)
        elif element != ['0']:
            print(element)

    #formatquot(formatpol(p), formatpol(q))
    #print(q)
    #print(pol2)
    #print("\nResultante: ", formatpol2var(subresultant(q, pol2)[0]))

    print("\nParte logaritmica:\n")

    logpart = intlogpart(q,pol2)
    formatlogpart(logpart)
    print("--------------------------------------------------------------------------\n")