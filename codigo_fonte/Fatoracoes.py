import numpy as np

assert np.seterr(divide='ignore',invalid='ignore')


import numpy as np
#Função que calcula as substuições retroativas


def fatoracao_LU(A:list,b:list) -> list:
    #tamanho da matriz A
    n = len(A)
    L = np.identity(len(A),dtype = float)
    for linha in range(0,n-1):
        for coluna in range(linha+1,n):
            m = -A[coluna][linha]/A[linha][linha]
            for j in range(linha+1,n):
                A[coluna][j]=m*A[linha][j]+A[coluna][j]
            L[coluna][linha] = -m
            A[coluna][linha]=0
    #Cálculo do Ly = b
    y =  sucessiva(L,b)
    #Cálculo do Ux = y
    U = A
    x = retroativa(U,y)
    return U,L,x
A =[[3,-2,1],[1,-3,4],[9,4,-5]]
b=[8,6,11]
U,L,x = fatoracao_LU(A,b)


def fatoracao_LDP(A, b):
    #tamanho da matriz A
    n = len(A)
    L = np.identity(len(A),dtype = float)
    D = np.identity(len(A), dtype = float)
    P =  np.identity(len(A), dtype = float)
    R = np.identity(len(A), dtype = float)

    for linha in range(0,n-1):
        for coluna in range(linha+1,n):
            m = -A[coluna][linha]/A[linha][linha]
            for j in range(linha+1,n):
                A[coluna][j]=m*A[linha][j]+A[coluna][j]
            L[coluna][linha] = -m
            A[coluna][linha]=0
    #Obtenção das Matrizes P e D a partir da matriz A(U) escalonada
    #Nessa parte também é obtida uma matriz R que é o resultado da multiplicação da matriz D pela a diagonal de P
    for i in range(0,n):
        for j in range(0,n):
            P[i][j] = A[i][j]
            P[i][i] = 1
            R[i][j] = A[i][j]
            if (i==j):
              D[i][j] = A[i][j]
              R[i][j] = P[i][j] * D[i][j]
    
    #Cálculo do Ly = b
    y =  sucessiva(L,b)
    #Cálculo do Rx = y
    x = retroativa(R,y)
    return L,D,P,x



#Função que calcula as substituições retroativas
def retroativa(A,b):
    #tamanho da matriz A
    n = len(A)
    #Inicialização do vetor de retorno
    x = n*[0]

    for i in range(n-1,-1,-1):
        s=0
        for j in range(i+1,n):
            s = s+A[i][j]*x[j]
        x[i]=(b[i]-s)/A[i][i]
    return x


#Função que calcula as substituições sucessivas
def sucessiva(A,b):
    #tamanho da matriz A
    n = len(A)
    #Inicialização do vetor de retorno
    x = n*[0]

    for linha in range(0,n):
        s=0
        for coluna in range(0,n):
            s = s+A[linha][coluna]*x[coluna]
        x[linha]=(b[linha]-s)/A[linha][linha]
    return x