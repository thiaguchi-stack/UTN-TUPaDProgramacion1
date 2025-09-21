#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”edad = input ("Ingrese su edad:")
edad = int(input("Ingrese su edad:"))
if edad > 18:
    print ("Es mayor de edad")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un número par:"))
if numero % 2==0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
edad = int(input("Ingrese su edad:"))
if edad < 0:
    print ("Ingrese una edad valida")
elif edad >= 0 and edad < 12:
    print ("Niño/a")
elif edad >= 12 and edad < 18:
    print ("Adolecente")
elif edad >= 18 and edad < 30:
    print ("Adulto/a joven")
else:
    print ("Adulto/a")
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres:")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean
print ("Se buscará el sesgo de una lista de números aleatorios")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print ("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print ("No hay sesgo")
else:
    print ("No se puede determinar el sesgo")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase_oracion = str(input("Ingrese una frase o palabra:")).strip()
if frase_oracion[-1] in "aeiouAEIOU":
    print(f"{frase_oracion}!")
else:
    print (frase_oracion)
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee
nombre = str(input("Ingrese un nombre:"))
opcion = int(input("Elige un número 1, 2 o 3:"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla
magnitud = float(input("Ingrese la magnitud del terremoto:"))
if magnitud < 3:
    print ("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
elif magnitud >= 7:
    print ("Extremo")
#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano
ubi = str(input("Ingrese en qué hemisferio se encuentra (N/S):")).upper()
mes = str(input("Ingrese el mes del año:")).title()
dia = int(input("Ingrese el día del mes (1-31):"))
if ubi == "N":
    if (mes == "Diciembre" and dia >= 21) or (mes == "Enero") or (mes == "Febrero") or (mes == "Marzo" and dia < 21):
        print ("Invierno")
    elif (mes == "Marzo" and dia >= 21) or (mes == "Abril") or (mes == "Mayo") or (mes == "Junio" and dia < 21):
        print ("Primavera")
    elif (mes == "Junio" and dia >= 21) or (mes == "Julio") or (mes == "Agosto") or (mes == "Septiembre" and dia < 23):
        print ("Verano")
    elif (mes == "Septiembre" and dia >= 23) or (mes == "Octubre") or (mes == "Noviembre") or (mes == "Diciembre" and dia < 21):
        print ("Otoño")
elif ubi == "S":
    if (mes == "Diciembre" and dia >= 21) or (mes == "Enero") or (mes == "Febrero") or (mes == "Marzo" and dia < 21):
        print ("Verano")
    elif (mes == "Marzo" and dia >= 21) or (mes == "Abril") or (mes == "Mayo") or (mes == "Junio" and dia < 21):
        print ("Otoño")
    elif (mes == "Junio" and dia >= 21) or (mes == "Julio") or (mes == "Agosto") or (mes == "Septiembre" and dia < 23):
        print ("Invierno")
    elif (mes == "Septiembre" and dia >= 23) or (mes == "Octubre") or (mes == "Noviembre") or (mes == "Diciembre" and dia < 21):
        print ("Primavera")