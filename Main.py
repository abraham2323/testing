
import datetime
from itertools import cycle

ListaPersona=[]
VectorPersona=[]
Vector=[]


#validar que el rut sea valido en norma chilena
def valida_rut(validar):
    rut = validar
    rut = rut.upper()
    rut = rut.replace("-","")
    rut = rut.replace(".","")
    aux = rut[:-1]
    dv = rut[-1:]
     
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
     
    if str(res) == dv:
        return True
    elif dv=="K" and res==10:
        return True
    else:
        return False

#convertir la fecha de nacimiento en edad
def edad(naci):
    hoy = datetime.date.today()
    if hoy < naci:
        print('error en la fecha de nacimiento')
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)
        return(edad-1)

#esta formula le da la interpretacion segun el peso altura

def IMC(formula):
    estado = ""
    if formula < 20:
        estado = "Bajo Peso"
    elif formula >= 20 and formula <= 24.9:
        estado = "Normal" 
    elif formula > 25 and formula <= 29.9:
        estado = "Obecidad Leve"
    elif formula > 40:
        estado = "Obesidad Severa"
    else:
        print("hubo un error al calculart el IMC")
    return estado


#usamos para ver si el vector se encuentra vacío o lleno
def Buscar(Codigo):
    Posicion=len(ListaPersona)
    return Posicion
 
#Buscamos el nombre del producto a consultar
def BuscarRut(Codigo):
    Posicion=len(ListaPersona)
    if Posicion==0:
        Nombre=''
    else:
        for VectorProducto in ListaPersona:
            if VectorProducto[0]==Codigo:
                Nombre=VectorProducto[0]
            else:
                Nombre=''
    return Nombre

#Mostramos los datos del producto buscado
def CalcularPeso(Codigo):
    VPERSONA=[]
    for VPERSONA in ListaPersona:
        if VPERSONA[0]==Codigo:
            dia_pes = int(input("ingrese dia Pesage :"))
            mes_pes = int(input("ingrese mes Pesage :"))
            ano_pes = int(input("ingrese año Pesage :"))
            Fecha_pes = str(dia_pes)+"/"+str(mes_pes)+"/"+str(ano_pes)
            peso = float(input("ingrese el peso en Kg :"))
            altura = float(input("ingrese la altura del Paciente en M :"))
            formula = peso/(altura*altura)
            IMC_pac = IMC(formula)
            VPERSONA[6] = True
            VectorPersona.append(Fecha_pes)
            VectorPersona.append(peso)
            VectorPersona.append(altura)
            VectorPersona.append(formula)
            VectorPersona.append(IMC_pac)
            
            print("Rut: ",VPERSONA[0])
            print("Nombre: ",VPERSONA[1])
            print("fecha de nacimiento: ",VPERSONA[2])
            print("edad: ",VPERSONA[3])
            print("Sexo: ",VPERSONA[4])
            print("Fisico: ",VPERSONA[5])
            print("IMC: ",VPERSONA[10])
            print("Interpretacion: ",VPERSONA[11])
        else:
            print("no se encontro a la persona buscada")



#Mostramos los datos del producto buscado
def BuscarPaciente(Codigo):
    VPERSONA=[]
    for VPERSONA in ListaPersona:
        if VPERSONA[0]==Codigo:
            if VPERSONA[6] == True:
                print("Rut: ",VPERSONA[0])
                print("Nombre: ",VPERSONA[1])
                print("fecha de nacimiento: ",VPERSONA[2])
                print("edad: ",VPERSONA[3])
                print("Sexo: ",VPERSONA[4])
                print("Fisico: ",VPERSONA[5])
                print("fecha pesage: ",VPERSONA[7])
                print("peso: ",VPERSONA[8])
                print("Altura: ",VPERSONA[9])
                print("IMC: ",VPERSONA[10])
                print("Interoretacion: ",VPERSONA[11])
            else:
                print("Rut: ",VPERSONA[0])
                print("Nombre: ",VPERSONA[1])
                print("fecha de nacimiento: ",VPERSONA[2])
                print("edad: ",VPERSONA[3])
                print("Sexo: ",VPERSONA[4])
                print("Fisico: ",VPERSONA[5])
        else:
            print("no se encontro a la persona buscada")

 
 
#Realizamos el Ingreso de Producto
def Ingreso():
    print('')
    print('****** INGRESO PERSONA ******')
    dia_nac = int(input("ingrese dia de nacimiento :"))
    mes_nac = int(input("ingrese mes de nacimiento :"))
    ano_nac = int(input("ingrese año de nacimiento :"))
    Fecha_nac = str(dia_nac)+"/"+str(mes_nac)+"/"+str(ano_nac)
    age = (edad(datetime.date(ano_nac, mes_nac, dia_nac)))
    if age > 15 and age < 70:
        Rut=input("Ingrese el RUT del Paciente: ")
        if valida_rut(Rut):
            if BuscarRut(Rut)=='':
                Nombre=input("Ingrese el nombre del Paciente: ")
                print("Mujer = M   Hombre = H")
                sexo=input("Ingrese el sexo del Paciente: ")
                print("Deportista = D Persona Normal = N ")
                Fisico=input("Ingrese el estado del paciente: ")
                calculado = False
                VectorPersona.append(Rut)
                VectorPersona.append(Nombre)
                VectorPersona.append(Fecha_nac)
                VectorPersona.append(age)
                VectorPersona.append(sexo.upper())
                VectorPersona.append(Fisico.upper())
                VectorPersona.append(calculado)
                ListaPersona.append(VectorPersona)
            else:
                print("\n *El rut ya existe*")
        else:
            print("\n *El rut ingresado no es valido*")
    else:
        print("\n *La edad no es valida para el calculo*")


# Menú Principal
while True:
    print(' ')
    print('****** Menú Principal ******')
    print('0. SALIR')
    print('1. INGRESAR PERSONA')
    print('2. CALCULAR PESO')
    print('3. BUSQUEDA PERSONA')
    opcion=input('Digitar una Opción: ')
    if opcion=='0':
        break
    elif opcion=='1':
        Ingreso()
    elif opcion=='2':
        print('')
        print('****** CALCULAR PESO ******')
        Rut=input("Ingrese el rut de la persona: ")
        try:
            CalcularPeso(Rut)
        except:
            print("\n *no se encontro a la persona Buscada*")

    elif opcion=='3':
        print('')
        print('****** BUSQUEDA DE PERSONA ******')
        Rut=input("Ingrese el rut de la persona: ")
        try:
            BuscarPaciente(Rut)
        except:
            print("\n *no se encontro a la persona Buscada*")
    else:
        print('*Opción no válida*')