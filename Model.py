import math as mat
from fractions import Fraction
def distr_binom(n,k,p,q):
    """
    N= numero total de provas
    K= numero de vezes que se quer a ocorrencia
    P= probabilidade de sucesso da ocorrencia
    Q= probabilidade de fracasso da ocorrencia
    :return float(or int)
    """
    a = mat.factorial(n)/(mat.factorial(k)*mat.factorial(n-k))
    b = (p**k) * (q**(n-k))
    result = a*b
    return result