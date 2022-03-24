from tkinter import *
from tkinter import messagebox
import math
import matplotlib.pyplot as plt

def basico():
    while(True):
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")
        print("5) Salir")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        opcion = int(input("Ingresa una opción : "))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        if opcion== 1 :
            print("Suma de  dos números")
            print("-----------------------------------")
            n1=int(input("Introduce un número : "))
            n2= int(input("Introduce un número : "))
            suma=n1+n2
            print("La suma es :",suma)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion ==2:
            print("Resta de números")
            print("-----------------------------------")
            n1=int(input("Introduce un número: "))
            n2= int(input("Introduce un número: "))
            resta=n1-n2
            print("La resta es ",resta)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion ==3:
            print("Multiplicación de números")
            print("-----------------------------------")
            n1=int(input("Introduce un número: "))
            n2= int(input("Introduce un número: "))
            multiplicacion=n1*n2
            print("La multiplicación es ",multiplicacion)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion==4:
            print("División de números")
            print("-----------------------------------")
            n1=int(input("Introduce un número: "))
            n2= int(input("Introduce un número: "))
            division=n1/n2
            print("La división es",division)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion==5:
            print("Puedes seleccionar otra operación en el menú   😊")
            break



def numeroscomplejos():
    while(True):
        print("Números complejos/imaginarios")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("1-Suma")
        print("2-Resta")
        print("3-Multiplicación")
        print("4-Calculo de angulo y radio")
        print("5- Salir")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        opcion = int(input("Ingrese una opción : "))

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


        if opcion == 1 :
            print("Suma de números complejos:")


            variablea=int(input("Introduce el valor de a:"))
            variableb=int(input("Introduce el valor de b:"))
            print(complex(variablea,variableb))
            variablec=int(input("introduce el valor de c:"))
            variabled=int(input("introduce el valor de d:"))
            print(complex(variablec,variabled))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Resultado de suma:")
            x = complex(variablea,variablec) + complex(variableb,variabled)
            print("La suma es ",x)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion == 2 :
            print("Resta de números complejos:")
            variablea=int(input("Introduce el valor de a:"))
            variableb=int(input("Introduce el valor de b:"))
            variable1 =(complex(variablea,variableb))
            print(complex(variablea,variableb))
            variablec=int(input("introduce el valor de c:"))
            variabled=int(input("introduce el valor de d:"))
            variable2=(complex(variablec,variabled))
            print(complex(variablec,variabled))
            print("Calculando...")
            print("Resultado de resta:")
            x = (variable1-variable2)
            print(x)

        if opcion == 3 :
            print("Multiplicación de números imaginarios")
            variablea=int(input("Introduce el valor de a:"))
            variableb=int(input("Introduce el valor de b:"))
            print(complex(variablea,variableb))
            variablec=int(input("Introduce el valor de c:"))
            variabled=int(input("Introduce el valor de d:"))
            print(complex(variablec,variabled))
            print("Calculando")
            print("...")
            print("Resultado de la multiplicación:")
            x =(variablea*variablec)
            x1=(variableb*variabled)
            y =(variablea*variabled)
            y1=(variableb*variablec)

            print ((x-x1)+(y+y1),'j')

        if opcion == 4 :
            print("Calculo de angulo y radio de números imaginarios")
            variablea =int(input("Introduce el valor de a:"))
            variableb =int(input("INtroduce el valor de b:"))
            print(complex(variablea,variableb))
            r = variablea**2
            r1= variableb**2
            r2 = r + r1
            radio = r2**0.5
            print("El radio es:",radio)

            import math
            angúlo=math.atan(variableb/variablea)
            angúlo1 =math.degrees(angúlo)
            print("El angúlo es :",angúlo1,"grados")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")




        if opcion ==5:
            print("Puedes escojer otra opción en el menú  😊")
            break


def ecuacionesm():
        print("Ecuacion de primer grado del tipo ax+b=0")

        a = float(input('Introduce el valor de a:'))
        b = float(input('Introduce el valor de b:'))

        if a!=0:
            x = -b/a
            print('X es igual a:',x)

            if a == 0:
                if b!= 0:
                    print ('La ecuacion no tiene solucion:')
            if b == 0:
                print('La ecuacion tiene infinitas soluciones')


def sistemas():
    def cambio_base(decimal, base):
        conversion = ''
        while decimal // base != 0:
            conversion = str(decimal % base) + conversion
            decimal = decimal // base
        return str(decimal) + conversion

    numero = int(input('Introduce el número a cambiar de base: '))
    base = int(input('Introduce la base: '))
    print(cambio_base(numero, base))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

def segundogrado():
    print("Ecuaciones cuadraticas")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Formula(b²+-√ b²-4ac/2a)")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    a = int(input("Ingrese el valor de a: "))
    if a==0:
    	print("El valor de 'a' no puede ser cero ")
    	print("...")
    	a=int(input("Reingrese el valor de a"))
    b=int(input("Ingrese el valor de b: "))
    c=int(input("Ingrese el valor de c: "))
    x1=-b
    x2=(b**2)
    x3=(x2-4*a*c)
    x4=x3**(0.5)
    x5=(2*a)
    x= x1+x4/x5
    y= x1-x4/x5
    print("Las raíces son:",(x,y))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

def ecuacioncircunferencia():
    import math
    import matplotlib.pyplot as plt

    print("Ecuación de la circunferencia")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Opciones")
    print("-------------------")
    print("1)Ecuación con centro y radio")
    print("2)Ecuación con centro y tangente ")
    print(".")
    print(".")
    print(".")
    opcion=int(input("Selecciona una opción:"))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
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
    	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    	menu()
    	opc=int(input("Selecciona una opcion:"))
    if opcion==2:
    	print("Ecuación con centro y tangente")
    	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    	print("P=")
    	print("-------------")
    	x =int(input("Introduce el valor de x:"))
    	y =int(input("Introduce el valor de y:"))
    	puntos=(x,y)
    	p = (x,y)
    	print(p)
    	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
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
    	circle=plt.Circle((x,y),radio ,color='b')
    	plt.gcf() .gca().add_artist(circle)
    	plt.show()
    	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

def recta():
    import matplotlib.pyplot as plt
    print("Ecuación de la recta (y = mx+b)")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
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

    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")



ventana=Tk()
ventana.geometry("200x200+0+0")
ventana.title("Temas de matemáticas IS")
ventana.config(bg="black")
ventana.config(cursor="pirate")
imagenL=PhotoImage(file="descargar.gif")
lblIMage=Label(ventana,image=imagenL).place(x=0,y=0)

imageng=PhotoImage(file="gauss.gif")
lblIMage=Label(ventana,image=imageng).place(x=0,y=250)

mi_Label = Label(ventana, text="Carl Friedrich Gauss") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 18))
mi_Label.place(x=0, y=200)


imagenm=PhotoImage(file="newton2.gif")
lblIMage=Label(ventana,image=imagenm).place(x=300,y=250)

mi_Label2 = Label(ventana, text="Isaac Newton") #Creación del Label
mi_Label2.pack()
mi_Label2.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label2.config(font=('Arial', 18))
mi_Label2.place(x=350, y=200)


imagene=PhotoImage(file="euler.gif")
lblIMage=Label(ventana,image=imagene).place(x=585,y=250)

mi_Label3 = Label(ventana, text="Número e") #Creación del Label
mi_Label3.pack()
mi_Label3.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label3.config(font=('Arial', 18))
mi_Label3.place(x=650, y=200)



imagenp=PhotoImage(file="numeropi.gif")
lblIMag=Label(ventana,image=imagenp).place(x=850,y=250)

mi_Label4 = Label(ventana, text="Número pi") #Creación del Label
mi_Label4.pack()
mi_Label4.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label4.config(font=('Arial', 18))
mi_Label4.place(x=900, y=200)



imagenma=PhotoImage(file="numerosmayas.png")
lblIMag=Label(ventana,image=imagenma).place(x=1150,y=250)

mi_label5 = Label(ventana,text="Números mayas")
mi_label5.pack()
mi_label5.config(bg="black",fg="white")
mi_label5.config(font=('Arial', 18))
mi_label5.place(x=1150,y=200)

mi_Label4 = Label(ventana, text="Daniel Alejandro Morales Castillo",bg="White") #Creación del Label
mi_Label4.pack()
mi_Label4.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label4.config(font=('Arial', 18))
mi_Label4.place(x=1000, y=0)

def saliraplicacion():
    valor=messagebox.askquestion("Salir","¿Seguro que quieres salir?")

    if valor =="yes":
        ventana.destroy()




barraMenu=Menu(ventana)
#creamos los menús
mnuArchivo=Menu(barraMenu)
#crear los comandos de los menús

barraMenu.add_command(label="Básico",command=basico) #falta funcion de básico

submenu = Menu(ventana, tearoff=True)
submenu.add_command(label="Ecuaciones",command=ecuacionesm)
submenu.add_command(label="Ecuaciones de segundo grado",command=segundogrado)
submenu.config(bg="cyan")
barraMenu.add_cascade(label="Ecuaciones",menu=submenu)

barraMenu.add_command(label="Ecuaciones-circunferencia",command=ecuacioncircunferencia)
barraMenu.add_command(label="Ecuaciones-Recta",command=recta)


barraMenu.add_command(label="Números complejos",command=numeroscomplejos)
mnuArchivo.config(bg="cyan") #falta funcion de derivadas
#agregar los menus a la barra menuSuma
#indicamos la barra de menus estará en la ventana
ventana.config(menu=barraMenu)

submenu = Menu(ventana)
submenu.config(bg="cyan")
barraMenu.add_command(label="Sistemas de números",command=sistemas)


barraMenu.add_command(label="Salir",command=saliraplicacion)
barraMenu.config(bg="white")

ventana.mainloop()
