# Python
Ejercicios Python:

Entrenamiento semana 2:
#Estado de aprobación
calificacion = int(input("Ingresa una calificación entre 0 y 100: "))

if calificacion > 0 and calificacion <= 100:
    if calificacion >= 60:
        print("El estudiante ha APROBADO.")
    else:
        print("El estudiante ha REPROBADO.")
else:
    print("Calificación inválida. Debe estar entre 0 y 100.")

#Promedio de calificaciones
ListaC = input("Ingresa una lista de calificaciones que esten separadas por comas: ")

# Convertimos la cadena a lista 
calificaciones = []
numero = ""
for caracter in ListaC:
    if caracter != ',':
        numero = numero + caracter
    else:
        calificaciones.append(int(numero))
        numero = ""
if numero != '':
    calificaciones.append(int(numero))

# Calcular del promedio
suma = 0
for nota in calificaciones:
    suma = suma + nota
promedio = suma / len(calificaciones)
print(f"El promedio es: {promedio}")

#Contar cuántas calificaciones son mayores 
valor = int(input("Ingresa un valor para comparar: "))
indice = 0
contMayor = 0
while indice < len(calificaciones):
    if calificaciones[indice] > valor:
        contMayor += 1
    indice += 1
print(f"Cantidad de calificaciones mayores a {valor} : {contMayor}")

#Verificar y contar calificaciones específicas
Notespecifica = int(input("Ingresa una calificación para buscar en la lista: "))
contador = 0
encontrado = False
for nota in calificaciones:
    if nota == Notespecifica:
        contador += 1
        encontrado = True
        continue  
if encontrado:
    print(f"La calificación {Notespecifica} está en la lista y aparece {contador} vez(veces)")
else:
    print(f"La calificación {Notespecifica} no está en la lista")

