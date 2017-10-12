import math as mat

def distribuicao_nominal(n,k,p,q):
    """
    N= numero total de provas
    K= numero de vezes que se quer a ocorrencia
    P= probabilidade de sucesso da ocorrencia
    Q= probabilidade de fracasso da ocorrencia
    PERCENT= SE DESEJA O RESULTADO EM PORCENTAGEM(default=FALSE)
    """
    a=mat.factorial(n)/(mat.factorial(k)*mat.factorial(n-k))
    b=(p**k)*(q**(n-k))
    result=a*b
    print('P(X='+str(k)+')='+str(result))
