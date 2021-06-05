######################################################################
# Transforma un vector de coeficientes en texto plano a un vector 
# adecuado para poder realizar operaciones
######################################################################

from SQRPN import SQRPN
from SYA import SYA
from TOKENIZE import tokenize

def convert(vector):
    if isinstance(vector,list):
        for i in range (len(vector)):
            vector[i] = SQRPN(SYA(tokenize(vector[i])))

    else:
        vector = SQRPN(SYA(tokenize(vector)))

    return vector