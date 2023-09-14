import numpy as np 
import PySimpleGUI as sg


assert np.seterr(divide='ignore',invalid='ignore')
# essa e arquivo tem como objetico tranformar o valor digitado pelo usuario que 
# do tipo string e tranformar ela nua matrix

def transform_matrix( string ):
    try:
        parte1 = string.split(',')
        A = parte1[0]
        B = parte1[1]


        valores_a = []
        for i in A.split(';'):
            
            if ('\n' in i):i = i.replace('\n','')
            
            linha   = i.split(' ')
            numeros = []
            
            for e in linha: numeros.append(float(e))

            valores_a.append(numeros)

        if (np.linalg.det(np.array(valores_a)) == 0):
            sg.popup('Não possui matrix inversa , det(A) == 0')
            return 'None','None'


        valores_b = []        
        for i in B.split(';'):valores_b.append([float(i)])

        return [
            np.array(
                valores_a,dtype=np.float64
                    ),
            np.array(
                valores_b,dtype=np.float64
                    )]

    except Exception as e:
        sg.popup(str(e))
        return 'None','None'


def tostring(ab):
    string = ''
    for i in ab.tolist(): string += str(i)+'\n'

    return string


def tostring_x(xb):
    alert  = '0'
    string = ''; num = 0
    
    for i in xb:
        if (i>2): alert = "Foguete Explode"
        
        string += f'x{num}  ='+str(i)+'\n'
        num+=1

    if (alert == '0'): alert = 'Foguete não esplode'
    return alert,string