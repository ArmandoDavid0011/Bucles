#Blucle While Intro
import math
numero=int(input("Digite un valor positivo: "))

while numero<0:
    print("No sea pendejo, tiene que ser numero positivo: ")
    numero=int(input("Digite un valor posito: "))
print(f"El resultado de la Raiz cuadrada es: {math.sqrt(numero):.2f}")
