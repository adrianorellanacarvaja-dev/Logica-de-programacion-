import random
import string

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_num, usar_simbolos):
    caracteres = ""

    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_num:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecciona al menos un tipo de carácter")

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def pedir_numero():
    while True:
        entrada = input("Ingrese la longitud: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Ingresa solo números")

def main():
    while True:
        try:
            longitud = pedir_numero()

            mayus = input("¿Mayúsculas? (si/no): ").lower() == "si"
            minus = input("¿Minúsculas? (si/no): ").lower() == "si"
            numeros = input("¿Números? (si/no): ").lower() == "si"
            simbolos = input("¿Símbolos? (si/no): ").lower() == "si"

            pwd = generar_contraseña(longitud, mayus, minus, numeros, simbolos)
            print("Contraseña:", pwd)

        except ValueError as e:
            print("Error:", e)

        repetir = input("¿Otra contraseña? (s/n): ").lower()
        if repetir != "s":
            break

if __name__ == "__main__":
    main()