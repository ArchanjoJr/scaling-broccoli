import math as mat

def distribuicao_nominal(n,k,p,q):
    """
    N= numero total de provas
    K= numero de vezes que se quer a ocorrencia
    P= probabilidade de sucesso da ocorrencia
    Q= probabilidade de fracasso da ocorrencia
    """
    a = mat.factorial(n)/(mat.factorial(k)*mat.factorial(n-k))
    b = (p**k) * (q**(n-k))
    result = a*b
    print('P(X='+str(k)+')='+str(result))


def rol(s):
    '''
    Recebe uma string com todos os valores do rol como uma string,
    Separa por espaço e retorna como uma lista de inteiros ou float.
    Exemplo:
    rol("20 12 11 12 33 14 10")//retorna [10,11,12,12,14,20,33]
    rol('0.3 2,3 1,1 3 4.1 0') //retorna [0.0,0.3,1.1,2.3,3,4.1]

    :param s:String
    :return: []
    '''
    r = s.split(' ')
    result= []
    for x in r:
        result.append(float(x))
    result.sort()
    return result

def numero_classes(lista):

    '''
    :param lista:[]
    :return: int
    '''

    i = 1+ (3.3 * mat.log(len(lista), 10))
    return int(i+1)

def amplitude_cla(lista):
    """

    :param lista:[]
    :return: int
    """
    at = lista[len(lista)-1]-lista[0]
    h = at/(numero_classes(lista))
    return int(h+1)

def probabilidade(a,s):
    """
    A = OCORRENCIA DO EVENTO
    S = TOTALIDADE DO EVENTO
    :param a:int, float
    :param s: int,float
    :return: int,float
    """
    return float(a/s)

def probabilidadeE(pa,pb):
    """

    :param aA:int or float
    :param sA:int or float
    :param aB:int or float
    :param sB:int or float
    :return:int or float
    """
    return float(pa*pb)

def probabilidadeU(pa,pb):
    return float((pa+pb)-probabilidadeE(pa,pb))

def probabilidadeC(pa,pb):
    return float(probabilidadeE(pa,pb)/pb)