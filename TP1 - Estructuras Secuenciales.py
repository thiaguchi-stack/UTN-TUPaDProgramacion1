# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("#1)")
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("\n#2)")
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia 
# imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("\n#3)")
nombre2 = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, indique su edad: ")
residencia = input("Por favor indique su lugar de residencia: ")
print(f"Soy {nombre2}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("\n#4)")
circulo = int(input("Indique el radio del círculo: "))
area = 3.1416* (circulo**2)
perimetro = 2*3.1416*circulo
print(f"El área del circulo es {area}, y su perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("\n#5)")
segundos=int(input("Ingrese la cantidad de segundos que desee pasar a horas: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas!")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("\n#6)")
num = int(input("Ingrese el número del que desea conocer su tabla: "))
i=0
while i<=10:
    mult = num*i
    print(f"{num} x {i} = {mult}")
    i=i+1

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y 
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("\n#7)")

num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

print(f"El resultado de sumar estos dos números es: {num1} + {num2} = " + str(num1+num2))
print(f"El resultado de dividir estos dos números es: {num1} / {num2} = " + str(num1/num2))
print(f"El resultado de multiplicar estos dos números es: {num1} * {num2} = " + str(num1*num2))
print(f"El resultado de restar estos dos números es: {num1} - {num2} = " + str(num1-num2))


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = (Peso en kg) / (altura en m)**2
print("\n#8)")
altura = float(input("Indique su altura en metros: "))
peso = int(input("Indique su peso corporal en kg: "))
IMC = (peso)/(altura**2)
print(f"Su índice de masa corporal es: {IMC}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius 
# imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: Fº = (9/5) * Cº + 32
print("\n#9)")
temp=int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit= (9/5) * temp + 32
print(f"{temp} grados Celsius son: {fahrenheit}Fº")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
print("\n#10)")
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))
promedio = (num_1+num_2+num_3)/3
print(f"El promedio de los números ingresados es: {promedio}")


