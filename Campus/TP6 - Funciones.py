#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return print (f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ").capitalize()
saludar_usuario(nombre_usuario)
#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ").capitalize()
apellido = input("Ingrese su apellido: ").capitalize()
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ").capitalize()
informacion_personal(nombre, apellido, edad, residencia)
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    area = 3.1416 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")
#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")
#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    if b == 0:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print(operaciones_basicas(a, b))
#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    indice_masa_corporal = peso / (altura ** 2)
    return indice_masa_corporal

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su índice de masa corporal (IMC) es: {calcular_imc(peso, altura):.2f}")
#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en ºC"))
print(f"La temperatura en ºF es: {celsius_a_fahrenheit(celsius)}")
#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio de los tres números es: {calcular_promedio(a, b, c)}")