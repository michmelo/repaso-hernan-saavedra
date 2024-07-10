import funcionesAWS as fn

alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]

creditos_alumnos = {} #Diccionario de creditos

while True:
    print('---Menú Principal---\n')
    print('0. Inicializar creditos.')
    print('1. Asignar créditos aleatorios.')
    print('2. Clasificar créditos.')
    print('3. Calcular estadísticas.')
    print('4. Generar reporte en csv.')
    print('5. Salir.\n')

    op = int(input('Ingrese opción: '))

    if op == 0:
        creditos_alumnos = {alumno : 0 for alumno in alumnos} #se inicializa el diccionario en 0
        print('\nCreditos inicializados correctamente.\n')

    elif op == 1:
        if not creditos_alumnos:
            print('\nPrimero debe inicializar créditos.\n')
        else:
            creditos_alumnos = fn.asignarCreditos(alumnos)

    elif op == 2:
        if creditos_alumnos: #validar que existan créditos
            fn.clasificarCreditos(creditos_alumnos)
        else:
            print('\nPrimero debe asignar créditos.\n')

    elif op == 3:
        if creditos_alumnos:
            max_credito, min_credito, promedio_credito = fn.calcularEstadisticas(creditos_alumnos)
            if max_credito is not None:
                print('\nCredito máximo: ', max_credito)
                print('Credito mínimo: ', min_credito)
                print('Promedio de créditos: ', promedio_credito, '\n')
        else:
                print('\nPrimero debe asignar créditos\n')

    elif op == 4:
        if creditos_alumnos:
            fn.generarReporte(creditos_alumnos)
        else:
            print('\nPrimero debe asignar créditos.\n')

    elif op == 5:
        print('\nSaliendo...\n')
        break
    else:
        print('\nOpción no válida. Intente nuevamente.\n')