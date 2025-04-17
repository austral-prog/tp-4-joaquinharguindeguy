import math
def line():
    a = float(input("Ingrese coeficiente A: "))
    b = float(input("Ingrese coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1:"))
    x2 = float(input("Ingrese el coeficiente X2:"))
    print(f'El coeficiente A de su ecuacion de la recta es: {a}')
    print(f'El coeficiente B de su ecuacion de la recta es: {b}')
    print(f'El coeficiente X1 de su ecuacion de la recta es: {x1}')
    print(f'El coeficiente X2 de su ecuacion de la recta es: {x2}')
    P1 = a*x1+b
    P2 = a*x2+b
    print(f'\nPara la siguiente ecuacion:\n\t Y = {a}X + {b}')
    print(f'\nDados los siguientes puntos:\n\t P1 ({x1}, {P1})\n\t P2 ({x2}, {P2})')
    C1= P1 - P2
    C2= x1 - x2
    c= math.sqrt(C1**2 + C2**2)
    

    print(f'\nLa distancia entre ellos es: {c}')
