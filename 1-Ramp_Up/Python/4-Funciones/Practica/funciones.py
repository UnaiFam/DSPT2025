
def dias_semana(num):
    """
     Devuelve el dia de la semana a partir de un numero """
    match num:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miercoles"
        case 4:
            return "Jueves"
        case 5:
            return"Viernes"
        case 6:
            return "Sabado"
        case 7:
            return "Domingo"
        case _:
            return "Otro"
         


def contructor_piramidal(filas):
    #primero genero una lista con todos los numeros que voy a necesitar
    lista_=list(range(filas,0,-1))
    #luego itero la lista
    for i in lista_:
        #cada vez que iterara  pasa al siguiente numero
        for i in  range(i,0,-1):
            #imprime y lo imprime todo seguido
            print(i, end=" ")
        # esto es para pasar de linea
        print(" ")  

         
def contructor_piramidal(filas):
    #primero genero una lista con todos los numeros que voy a necesitar
    lista_=list(range(filas,0,-1))
    #luego itero la lista
    for i in lista_:
        #cada vez que iterara  pasa al siguiente numero
        for i in  range(i,0,-1):
            #imprime y lo imprime todo seguido
            print(i, end=" ")
        # esto es para pasar de linea
        print(" ")


def comparador(arg1, arg2):
    if arg1==arg2:
        return "iguales"
    if arg1>arg2:
        return "1-o mayor que el 2-o"
    if arg1<arg2:
        return "1-o menor que el 2-o"         
                         

def contador_letras(texto, letra):
    return texto.count(letra)         

         


def contador_fulletras(texto):
    #primero genero un diccionario que tendra la letra y las veces que se repite
    contador={}
    #luego itero cada letra en el texto
    for letra in texto:
        #si la letra existe en el dicc. le suma 1
        if letra in contador:
            contador[letra]+=1
        # no existe lo añade al diccionario empezando por 1
        if letra not in contador:
            contador[letra]=1

        #elimino caracteres que no son letras
    contador.pop(",")
    contador.pop(".")
    contador.pop(" ")
    return contador

def editor_lista(lista, comando, elemento=None):
    match comando:
        case "add":
            lista.append(elemento)

        case "remove":
            lista.remove(elemento)
            
    return lista
         


def palabras(*arg):
    palabros=arg
    return " ".join(palabros)         

         
def fibonacci(n):
    if n<=1:
        return n

         

def area_cuadrado(base, altura):
    return base*altura

def area_triangulo(base, altura):
    return base*altura/2

def area_circulo(radio):
    import math
    return math.pi*radio**2
         
