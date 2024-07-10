import csv
import random

def asignarCreditos(alumnos):
    #Funcion asigna creditosaleatorios entre 50 y 200 a cada alumno
    #Devuelve un diccionario con los créditos asignados
    creditos_alumnos = {}
    #iterar sobre cada alumno en la lista alumnos
    for alumno in alumnos:
        #generar un número entero aleatorio entre 50 y 200 para cada alumno
        credito = random.randint(50,200)
        #asignar el crédito generado al alumno que corresponde en el diccionario
        creditos_alumnos[alumno] = credito
    print('\nCreditos asignados correctamente.\n')
    print(creditos_alumnos)

    return creditos_alumnos

def clasificarCreditos(creditos_alumnos):
    menor_100 = {}
    entre_100_150 = {}
    mayor_150 = {}

    for alumno, credito in creditos_alumnos.items():
        if credito < 100:
            menor_100[alumno] = credito
        elif credito <= 150:
            entre_100_150[alumno] = credito
        else:
            mayor_150[alumno] = credito
    
    #mostrar resultados de la clasificacion
    print('\nCreditos menores a 100 TOTAL', len(menor_100))
    print('-------------------------------')
    for alumno, credito in menor_100.items():
        print(alumno, ': $', credito)
    print()

    print('\nCreditos entre 100 y 150 TOTAL', len(entre_100_150))
    print('-------------------------------')
    for alumno, credito in entre_100_150.items():
        print(alumno, ': $', credito)
    print()

    print('\nCreditos mayores a 150 TOTAL', len(mayor_150))
    print('-------------------------------')
    for alumno, credito in mayor_150.items():
        print(alumno, ': $', credito)
    print()

def calcularEstadisticas(creditos_alumnos):
    #calcular maximos, minimos, promedios
    creditos = list(creditos_alumnos.values()) #va a crear una lista sólo con los valores de los créditos
    if not creditos:
        print('No se han asignado créditos aún.')
        return None, None, None

    max_credito = max(creditos) #debería aparecer sólo el máximo
    min_credito = min(creditos) #devería aparecer sólo el mínimo
    promedio_credito = sum(creditos) / len(creditos)

    return max_credito, min_credito, promedio_credito

def generarReporte(creditos_alumnos):
    #generar un reporte en formato csv con los creditos de los alumnos
    with open('reportes_creditos.csv', 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter=',')
        
        #escribir encabezados
        escritor.writerow(['Nombre alumno', 'Credito'])

        #escribir cada línea de dato
        for alumno, credito in creditos_alumnos.items():
            escritor.writerow([alumno, credito])
    print('\nReporte generado correctamente en reportes_creditos.csv\n')