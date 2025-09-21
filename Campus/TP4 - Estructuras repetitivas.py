#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 10 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(11):
    print(i)
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = input ("Ingrese un número entero:")
print("El número tiene", len(numero), "dígitos")
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
dnum1 = 0
dnum2 = 0
suma = 0
for i in range(num1):
    dnum1 += i
for i in range(num2):
    dnum2 += i
suma = dnum1 + dnum2
print("La suma de los digitos entre el número", num1, "y", num2, "es:", suma)
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int(input("Ingrese un número entero (0 para finalizar): "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
print("La suma total es:", suma)
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
random_num= random.randint(0, 9)
intento = int(input("Intenta adivinar el número entre 0 y 9: "))
cont_intentos = 0
while intento != random_num:
    cont_intentos += 1
    intento = int(input("¡Incorrecto! Intenta de nuevo: "))
print(f"¡Has adivinado el número! Solo te tomó {cont_intentos} intentos")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
num = int(input("Ingrese un número (entero positivo): "))
suma = 0
for i in range(num + 1):
    suma += i
print("La suma de los números entre 0 y", num, "es:", suma)
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
for i in range(10):
    num = int(input(f"Ingrese un número entero: "))
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
    if num >= 0:
        cont_pos += 1
    else:
        cont_neg += 1

print(f"Cantidad de números pares: {cont_par}")
print(f"Cantidad de números impares: {cont_impar}")
print(f"Cantidad de números positivos: {cont_pos}")
print(f"Cantidad de números negativos: {cont_neg}")
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)
suma = 0
for i in range(10):
    num = int(input(f"Ingrese un número entero:"))
    suma += num
media = suma / 10
print("La media de los números ingresados es:", media)
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = input("Ingrese un número entero: ")
for i in range(len(num)-1, -1, -1):
    print(num[i], end="")
print()