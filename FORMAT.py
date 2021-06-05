from infix import infix
from CONVERT import convert
from simplify import simplify

def formatpol(pol, var='X'):
    output = ''
    for i in range(len(pol)):
        if (len(pol)-1-i == 0):
            output = output+infix(pol[i])
        else:
            output = output+infix(pol[i])+'*'+var+'^'+str(len(pol)-1-i)+' + '
    return output


def formatquot(num,den):
    l = max(len(num), len(den))
    difnum = l-len(num)
    difden =l-len(den)
    raya = '-'*l
    print(' '*int(difnum/2)+num)
    print(raya)
    print(' '*int(difden/2)+den)



def formathermite(quot):
    den = formatpol(quot[2].copy())
    den = '('+den+')^'+quot[4]
    num =formatpol(quot[1])
    formatquot(num, den)


def printint(num,den):
    l = max(len(num), len(den))
    difnum = l-len(num)
    difden =l-len(den)
    raya = '-'*l
    print('    /¯')
    print('   |')
    print('   | ', ' '*int(difnum/2)+num)
    print('   | ',raya, ' = Parte Racional Polinomial + Parte Polinomial Hermite + Parte logaritmica')
    print('   | ', ' '*int(difden/2)+den)
    print('   |')
    print(' _/')
def formatlogpart(logpart):
    for element in logpart:
        print('.-----')
        print('\\')
        print(' \\  ')
        print('  . '+ "  t*log(", formatpol2var(element[1]),")")
        print(" /")
        print("/")
        print('.-----')
        print('  t  \n')
        print("Con t tal que: ", formatpol(element[0], 't'), ' = 0\n\n')


def formatpol2var(pol):
    p = pol.copy()
    polinomio = ''
    n = len(p)-1
    for coef in p:
        if n == len(p)-1:
            polinomio = polinomio+'('+formatpol(coef, 't')+')*X^'+str(n)
        else:
            polinomio = polinomio+'+('+formatpol(coef, 't')+')*X^'+str(n)
        n = n-1
    return polinomio

#print(formatpol2var([['1', '3'], ['1']]))