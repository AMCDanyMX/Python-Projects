def menu():
	print("::::::::::::::::::::::::::::::::")
	print("Ingeniería de Software UAZ - Matemáticas para ingeniería")
	print("::::::::::::::::::::::::::::::::")
	print("Temas de matemáticas")
	print("................................")
	print("1-¿Qué número es mayor?.")
	print("2-Fracciones .")
	print("3-Ecuacion géneral de la recta.")
	print("4-Ecuaciones de primer grado.")
	print("5-Ecuación de la circunferencia.")
	print("6-Números complejos/imaginarios.")
	print("7-Ecuaciones cuadráticas.")
	print("8-Salir ")	
	print("---------------------------------")
	print(".................................")

def menuimaginarios():
	print("Numeros complejos/imaginarios")
	print("----------------")
	print("1)Suma")
	print("2)Resta")
	print("3)Multiplicación")
	print("4)Cálculo de ángulo y radio")
	print("::::::::::::::::::::")

menu()
opc=int(input("Selecciona una opción:"))
print("-------------")
while(opc>0 and opc<8):
	if (opc == 1 ):
		print("Suma de dos números")
		print("Dame dos numeros...")
		n1 = int(input("Número 1:"))
		n2 = int(input("Número 2:"))
		if(n1>n2):
			print("El número 1 es mayor")
		if(n2>n1):
 			print("El número 2 es mayor")
		elif(n2==n1):	
			print("Los números son iguales")
		print("::::::::::::::::::::")
		print("::::::::::::::::::::")
		menu()
		opc=int(input("Selecciona una opcion:"))

	if (opc == 2):
		print("Fracciones")
		from fractions import Fraction
		print("operaciones basicas")  #Todas las operaciones 
		n1 = Fraction(input("Digite un numero fraccionario, ejemplo(4/5) : "))	
		print(n1)
		n2 = Fraction(input("Digite un número fraccionario, ejemplo(3/4) :"))
		print(n1)
		print("Resultado suma:" + str(n1+n2))
		print("Resultado resta:" + str(n1-n2))
		print("Resultado multiplicacion:" + str(n1*n2))
		print("Resultado division:" + str(n1/n2))
		print("::::::::::::::::::::::")
		print("----------------------")
		menu()
		opc=int(input("Selecciona una opcion:"))

	if(opc == 3):
		import matplotlib.pyplot as plt
		print("Ecuación de la recta (y = mx+b)")
		print(".................")
		print("------------------")
		b = int(input("Define el valor del intercepto:"))
		def pendiente(a1,b1,a2,b2):
			m = (b2-b1)/(a2-a1)
			print('La pendiente de la recta es %5.2f' %m)
		x1 = float(input('Punto x1:')) #a1
		y1 = float(input('Punto y1:')) #b1
		x2 = float(input('Punto x2:')) #a2
		y2 = float(input('Punto y2:')) #b2
 
		pendiente(x1,y1,x2,y2)

		x = [1,2,3,4,5,6,7,8,9,10]
		y = [3,6,9,12,15,18,21,24,27,30]
		print("Se mostrara la recta en breve...")

		plt.scatter(x,y)
		plt.show()

		print("::::::::::::::::::::::::::")
		print("::::::::::::::::::::::::::")
		menu()
		opc=int(input("Selecciona una opcion:"))

	if(opc == 4):
		print("Ecuación de primer grado con una incognita (ax+b=0)")
		print("::::::::::::::::::::::::::::::::::")
		a = float(input('Introduce el valor de a:')) 
		b = float(input('Introduce el valor de b:'))
		if a != 0:
			x = -b/a
			print('X es igual:',x)
		if a == 0:
			if b!=0:
				print("La ecuación no tiene solucion ")
		if b == 0:
			print("La ecuación tiene infinitas soluciones")
		print("::::::::::::::::::::::::::::::::")
		menu()
		opc=int(input("Selecciona una opción:"))

	if(opc == 5):
		print("Ecuación de la circunferencia")
		print("::::::::::::::::::::")
		print("Opciones")
		print("-------------------")
		print("1)Ecuación con centro y radio")
		print("2)Ecuación con centro y tangente ")
		print(".")
		print(".")
		print(".")
		opcion=int(input("Selecciona una opción:"))
		print("-------------")
		if opcion == 1 :
			print ("Ecuación con centro y radio")
			p1= int(input("Introduce valor de p1:"))
			p2=int(input("introduce el valor de p2:"))
			r=int(input("introduce el valor del radio:"))
			numerodos=2
			#(x-h)²+(y-k)²=r² -Ecuacion general de la circunferencia
			h=(int(numerodos)*int(p1))#EL soble del segundo(h)-Binomio al cuadrado
			k=(int(numerodos)*int(p2))#El doble del segundo(k)-Binomio al cuadrado
			h1=(int(p1)*int(p1))
			k1=(int(p2)*int(p2))
			hk=(int(h1)+int(k1))
			hkr=(int(hk)-int(r))
			print("La ecuación de la circunferencia es...")
			print("x² + y² -",h,"x +",k,"y +",hkr,"= 0")
			print("::::::::::::::::::::::::::::::.")
			menu()
			opc=int(input("Selecciona una opcion:"))
		if opcion==2:
			print("Ecuación con centro y tangente")
			print("::::::::::::::::::::::::")
			print("P=")
			print("-------------")
			x =int(input("Introduce el valor de x:"))
			y =int(input("Introduce el valor de y:"))
			puntos=(x,y)
			p = (x,y)
			print(p)
			print("------------")
			print("C=")
			h =int(input("Introduce el valor de h:"))
			k =int(input("Introduce el valor de k:"))
			puntos = (h,k)
			c = (h,k)
			print(c)
			print("Calculando el radio...")
			print("...")
			print("...")
			print("...")
			import math 
			r1=(int(x)-int(h))
			r2=(int(y)-int(k))
			r3=(r1**r2)
			r4=(r2**2)
			r5=(r4+r4)
			radio=(r5**0.5)
			print("Elradio es:",radio)
			print("::::::::::::::::")
			print("Graficando...")
			print(".............")
			import matplotlib.pyplot as plt
			circle=plt.Circle((x,y),radio ,color='b')
			plt.gcf() .gca().add_artist(circle)
			plt.show()
			print("::::::::::::::::::::")
			menu()
			opc=int(input("Selecciona una opción:"))

	if (opc==6):
		menuimaginarios()
		opcion=int(input("Ingrese una opción:"))
		if opcion==1:
			print("Suma de números imaginarios/complejos")
			print("----------------------------")
			variable1=int(input("Introduce el valor de a:"))
			variable2=int(input("Introduce el valor de b:"))
			variablea=(complex(variable1,variable2))
			print(complex(variable1,variable2))
			variable3=int(input("Introduce el valor de c:"))
			variable4=int(input("Introduce el valor de d:"))
			variableb=(complex(variable3,variable4))
			print(complex(variable3,variable4))
			print("Calculando...")
			print(".")
			print(".")
			print("Resultado de la suma:")
			x = complex(variablea+variableb)
			print(x)
			menu()
			opc=int(input("Selecciona una opción:"))
		if opcion==2:
			print("Resta de números imaginarios/complejos:")
			print("----------------------")
			variable1=int(input("Introduce el valor de a:"))
			variable2=int(input("Introduce el valor de b:"))
			variablea=(complex(variable1,variable2))
			print(complex(variable1,variable2))
			variable3=int(input("Introduce el valor de c:"))
			variable4=int(input("Introduce el valor de d:"))
			variableb=(complex(variable3,variable4))
			print(complex(variable3,variable4))
			print("Calculando...")
			print(".")
			print(".")
			x=complex(variablea-variableb)
			print(x)
			print("------------------")
			menu()
			opc=int(input("Selecciona una opción:"))

		if opcion==3:
			print("Multiplicación de números imaginarios/complejos")
			print("-----------------")
			variable1=int(input("Introduce el valor de a:"))
			variable2=int(input("Introduce el valor de b:"))
			print(complex(variable1,variable2))
			variable3=int(input("Introduce el valor de c:"))
			variable4=int(input("Introduce el valor de d:"))
			print(complex(variable3,variable4))
			print("----------------------------")
			print("Calculando...")
			print("...")
			print("Resultado de la multiplicación:")
			x =(variable1*variable3)
			x1=(variable2*variable4)
			y=(variable1*variable4)
			y1=(variable2*variable3)

			print((x-x1)+(y+y1),'j')
			print("-----------------")
			print("::::::::::::::::::::")

			menu()
			opc=int(input("Selecciona una opción:"))
		if opcion ==4:
			print("Calculo de angúlo y radio")
			variablea=int(input("Introduce el valor de a:"))
			variableb=int(input("Introduce el valor de b:"))
			print(complex(variablea,variableb))
			r = variablea**2
			r1=variableb**2
			r2=r + r1
			radio=r2**0.5
			print("El radio es:",radio)
			import math 
			angúlo=math.atan(variableb/variablea)
			angúlo1=math.degrees(angúlo)
			print("El angúlo es :", angúlo1,"grados")
			print("-----------------------")
			print("-----------------------")
			print(":::::::::::::::::::::::")
			menu()
			opc=int(input("Selecciona una opción:"))

	if (opc ==7):
		print("Ecuaciones cuadraticas")
		print("::::::::::::::::::::::")
		print("Formula(b²+-√ b²-4ac/2a)")
		print(":::::::::::::::::::::::")
		import math
		a = int(input("Ingrese el valor de a: "))
		if a==0:
			print("El valor de 'a' no puede ser cero ")
			print("...")
			a=int(input("Reingrese el valor de a"))
		b=int(input("Ingrese el valor de b: "))
		c=int(input("Ingrese el valor de c: "))
		x1=-b
		x2= b**2
		x3=((x2)-(4*a*c))
		x4=x3**(0.5)
		x5=(2*a)
		x= (x1+(x4/x5))
		y= (x1-(x4/x5))
		print("Las raíces son:",(x,y))
		print("::::::::::::::::::::::::::::::::")
		menu()
		opc=int(input("Selecciona una opción:"))
			








			







		


		