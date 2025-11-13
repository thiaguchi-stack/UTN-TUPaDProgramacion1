# Trabajo Práctico: Recursividad
# Cada punto está separado con comentarios para fácil lectura

# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 2) Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 3) Potencia recursiva (base^exponente)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# 4) Decimal a binario (recursivo)
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


# 5) Verificar palíndromo (sin usar slicing inverso)
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


# 6) Suma de dígitos sin convertir a string
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


# 7) Contar bloques de una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


# 8) Contar ocurrencias de un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)


# FIN DEL ARCHIVO
