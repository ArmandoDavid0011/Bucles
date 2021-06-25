#Blucle While Intro
import math
numero=int(input("Digite un valor positivo: "))

while numero<0:
    print("Tiene que ser numero positivo: ")
    numero=int(input("Digite un valor positivo: "))
print(f"El resultado de la Raiz cuadrada es: {math.sqrt(numero):.2f}")
