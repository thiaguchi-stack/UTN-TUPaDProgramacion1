#1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = list(precios_frutas.keys())
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
agenda_telefonica = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ").capitalize()
    numero = input("Ingrese el número telefónico del contacto: ")
    if numero.isdigit():
        numero = int(numero)
    else:
        print("Número inválido. Intente nuevamente.")
        continue
    agenda_telefonica[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ").capitalize()
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta} en la agenda.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese una frase: ").title()
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
notas = {}
for i in range(3):
    nombre_alumn = input("Ingrese el nombre del alumno: ").capitalize()
    notas_alumno = ()
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}º: "))
        notas_alumno += (nota,)
    notas[nombre_alumn] = notas_alumno
print(notas)

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
aprobados_parcial_1 = {1, 2, 3, 4, 5}
aprobados_parcial_2 = {2, 3, 6, 7, 8}
aprobados_ambos = aprobados_parcial_1.intersection(aprobados_parcial_2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobados_al_menos_uno = aprobados_parcial_1.union(aprobados_parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock_productos = {}
while True:
    print("1. Consultar stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Opción inválida. Intente nuevamente.")
        continue
    
    match opcion:
        case 1:
            if not stock_productos:
                print("El stock está vacío.")
                continue
            producto = input("Ingrese el nombre del producto a consultar: ").capitalize()
            if producto not in stock_productos:
                print(f"El producto {producto} no existe en el stock.")
            else:
                print(f"El stock de {producto} es {stock_productos[producto]} unidades.")
        case 2:
            producto = input("Ingrese el nombre del producto a agregar unidades: ").capitalize()
            if producto not in stock_productos:
                print(f"El producto {producto} no existe en el stock.")
            else:
                unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
                stock_productos[producto] += unidades
                print(f"Se han agregado {unidades} unidades a {producto}. Nuevo stock: {stock_productos[producto]} unidades.")
        case 3:
            producto = input("Ingrese el nombre del nuevo producto: ").capitalize()
            if producto in stock_productos:
                print(f"El producto ya existe en el stock.")
            else:
                unidades = int(input("Ingrese la cantidad de unidades del nuevo producto: "))
                stock_productos[producto] = unidades
                print(f"Se ha agregado el producto {producto} con {unidades} unidades al stock.")
        case 4:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")
            continue

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda = {
    ("Lunes", "9:00"): "Reunión",
    ("Martes", "14:00"): "Cita médica",
    ("Miércoles", "11:00"): "Clase de yoga",
    ("Jueves", "19:00"): "Cena con amigos"
}
dia = input("Ingrese el día del evento a consultar: ").capitalize()
hora = input("Ingrese la hora del evento que quieres consultar: ")
clave = (dia, hora)
if clave in agenda:
    print(f"El evento programado para el {dia} a las {hora} es: {agenda[clave]}")
else:
    print(f"No hay eventos programados para el {dia} a las {hora}.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima"
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)