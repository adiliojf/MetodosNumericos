import PySimpleGUI as sg   

#esse eo valor padrao na inicializacao da interface
default_value_matrix = '''\
1 2 4;
2 5 6;
2 10 3,
2;3;4
                       '''




# interface principal
def main():
    sg.theme('DarkBlue12')
    frame = [
        [
            sg.Multiline(default_text=default_value_matrix,key='matrix',size=(20,10))
        ]
    ]
    coluna1 = [
        [
            sg.Combo(
                ['Fatoração LU','Fatoração LDP','Gauss'],
                default_value='Fatoração LU',
                key='tipo',size=(23,8)),
        ],
        [
            sg.Frame('Insira a matrix',layout=frame), 
        ],
        [
            sg.Ok(),
            sg.Button('Sair',mouseover_colors='red')
        ]
    ]

    parte1 = [[ sg.Multiline(
                    '',
                    horizontal_scroll=True,
                    disabled=True,
                    key='result',
                    size=(25,14),
                    expand_x=True,
                    expand_y=True) ]]
  

    coluna2 = [
        [
            sg.Frame('Resultado',layout=parte1)
        ]
        
    ]

    layout = [
        [
            sg.Column(layout=coluna1,element_justification='c'),
            sg.Column(layout=coluna2)
        ]
    ]


    return sg.Window('Trabalho Final',icon=r'C:\Users\mateu\OneDrive\Materias Ufc\Metodos Numericos\trabalho_final\matrix.ico',layout=layout,element_justification='L',font=('calibri',13))


