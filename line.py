import math
def line():
    a = float(input("Ingrese coeficiente A: "))
    b = float(input("Ingrese Coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1:"))
    x2 = float(input("Ingrese el coeficiente X2:"))
    print(f'El coeficiente A de su ecuacion es:{a}')
    print(f'El coeficiente B de su ecuacion es:{b}')
    print(f'El coeficiente X1 de su ecuacion es:{x1}')
    print(f'El coeficiente X2 de su ecuacion es:{x2}')
    y = (f'{a}X + {b}')
    P1 = float((f'{a*x1+b}'))
    P2 = float((f'{a*x2+b}'))
    print(f'\nPara la siguiente ecuacion:\n\t Y = {y}')
    print(f'\nDados los siguientes puntos:\n\t P1 ({x1}, {P1})\n\t P2 ({x2}, {P2})')
    a= P1 - P2
    b= x1 - x2
    c= math.sqrt(a**2 + b**2)
    

    print(f'\nLa distancia entre ellos es:{c}')
line()
