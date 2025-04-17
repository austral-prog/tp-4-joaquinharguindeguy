def leap_year():
	a= float(input("ingrese un año:"))
	a= int(a)
	if (a % 4 ==0 and a % 100 != 0) or (a % 400 == 0):
		print(f'El año {a} es bisiesto')
	else:
		print(f'El año {a} no es bisiesto')
