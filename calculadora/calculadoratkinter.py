from tkinter import *
from math import *



ventana=Tk()
ventana.title("CALCULADORA - AMCDanyMX")
ventana.geometry("250x600")
ventana.configure(background="black")
color_boton=("white")

#imagen1=PhotoImage(file="amcdanymx.png")
#lblIMage=Label(ventana,image=imagen1).place(x=600,y=0)


mi_Label = Label(ventana, text="Daniel Alejandro Morales Castillo") #Creación del Label
mi_Label.pack()
mi_Label.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label.config(font=('Arial', 18))
mi_Label.place(x=600, y=200)
mi_Label2 = Label(ventana, text="2° 'A'") #Creación del Label
mi_Label2.pack()
mi_Label2.config(bg="black",fg="white") #Cambiar color de fondo
mi_Label2.config(font=('Arial', 18))
mi_Label2.place(x=600, y=240)


def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) #ESTA PARTE SIRVE PARA VISUALIZAR LA OPERACION EN LA PANTALLA


def clear():
    global operador
    operador=("")
    input_text.set("0")

def operacion():
    global operador
    try:
        opera=str(eval(operador))#SIRVE PARA REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
    except:
        clear()
        opera=("MATH ERROR")
    input_text.set(opera)#MUESTRA EL RESULTADO


ancho_boton=14
alto_boton=3
input_text=StringVar()
operador=""
clear() #MUESTRA "0" AL INICIAR LA CALCULADORA
Boton1=Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=17,y=180)
Boton2=Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=107,y=180)
Boton3=Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=197,y=180)
Boton4=Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=287,y=180)
Boton5=Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=17,y=240)
Boton6=Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=107,y=240)
Boton7=Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=197,y=240)
Boton8=Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=287,y=240)
Boton9=Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=17,y=300)
Boton0=Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=300)
BotonC=Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=300)
BotonComa=Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
BotonResta=Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
BotonMulti=Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
BotonDiv=Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
Botonln=Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log")).place(x=17,y=420)
BotonParen1=Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
BotonParen2=Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
BotonResto=Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=480)
BotonSqrt=Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt")).place(x=287,y=480)
BotonC=Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
BotonExp=Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
BotonResul=Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=operacion).place(x=287,y=420)


Salida=Entry(ventana,font=('arial',20,'bold'),width=25,textvariable=input_text,bd=20,insertwidth=4,bg="cyan",justify="right").place(x=10,y=60)


ventana.mainloop()
