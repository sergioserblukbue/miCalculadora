import os
#------- por aca van las funciones-----
def sumar():
    numero1 = int(input('ingrese el primer numero'))
    numero2 = int(input('ingrese el segundo numero'))
    return(numero1 + numero2)
def resta():
    n1=int(input("ingrese un número :")) 
    n2=int(input("ingrese otro numero: "))
    return (n1-n2)
def multiplicar():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    return(numero1 * numero2)
def dividir():    
    x=input("ingrese un numero")
    y=input("Ingrese un numero")
    res=int(x)/int(y)
    return res
# ------funcion para el menu----
def menu():
    os.system("cls")
    print(" + para Sumar ")
    print(" - para Restar ")
    print(" * para Multiplicar ")
    print(" / para Dividir ")
    print("s para salir ")

# funcion principal -------

def main():
    menu()
    op=input("ingrese una opción")
    while op !="s":
        if op=="+":
            print("El resultado de la suma es: ", sumar() ) 
        elif op=="-":
            print("el resultado de la resta es: " ,resta())
        elif op=="*":
            print("El resultado de la multiplicación es: ", multiplicar())
        elif op=="/":
            print("el resultado de la división es: " , dividir())
        else:
            print("opción no válida")
        input("Presione una tecla para continuar ...")
        menu()
        op=input("ingrese una opción")




# aca empieza el programa ----------
main()