import numpy as np 

assert np.seterr(divide='ignore',invalid='ignore')

def solucao( Ab ):
    size = np.size(Ab,0)
    valores_x = []

    for i in range(size - 1, -1, -1):
        valores_x.insert(0, Ab[i][size] / Ab[i][i])
        
        for k in range(i - 1, -1, -1):
            try:
                Ab[k][size] -= Ab[k][i] * valores_x[0]
            
            except OverflowError:
                Ab[k][size] -= 0
    
    return valores_x



def triangular_form( Ab , casa_decimal):
    size = np.size(Ab ,0)
    col  = np.size( Ab , 1 ) - 2

    for i in range( size-1 , -1 , -1 ):   
        for j in range(0,size-(size-i) ):   
            var_mk   = Ab[j,col]/Ab[i,col]  
            Ab[j,:] -= var_mk * Ab[i,:]

        col-= 1
    return np.around( Ab , decimals=casa_decimal)




def gauss( A , b , casa_decimal , complete =False ):
    Ab   = np.concatenate((A , b), axis=1 , dtype=np.float64 )
    size = np.size( Ab , 0 )

    for i in range(size):
        for j in range(i+1 , size):
            var_mk   =  Ab[j,i]/Ab[i,i]
            Ab[j,:] -=  var_mk * Ab[i,:]
        
    
    Ab = np.around( Ab , decimals=casa_decimal)
    
    if (complete):
        Ab = triangular_form(Ab, casa_decimal)
        xk = solucao(Ab)

    else: xk = solucao(Ab)

    return Ab , xk
            



