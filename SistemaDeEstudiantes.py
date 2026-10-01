nombres = []
notas_estudiantes = []
promedios = []
estados = []

opcion = 0
while opcion != 4:
    print("""
SISTEMA DE REGISTRO DE CALIFICACIONES

1.Registrar estudiante
2.Mostrar resultados
3.Buscar estudiante
4.Salir del Sistema

""")
    texto_opcion = input("Elija una opcion:  ").strip()

    if texto_opcion.isdecimal():
        opcion = int(texto_opcion)
    else:
        opcion = 0

    match opcion:

        case 1:
            nombre = ""
            while nombre == "":
                nombre = input("Ingrese el nombre del estudiante:  ").strip()
                if nombre == "":
                    print("ERROR: El nombre no puede estar vacio.")

            notas = []
            for i in range(1, 3 + 1):
                mensaje = f"Ingrese la calificacion {i}:  "
                valida = False
    
                while not valida:
                    texto = input(mensaje).strip()
    
                    if texto.isdecimal():
                        nota = int(texto)
                        if nota <= 100:
                            notas.append(nota)
                            valida = True
                        else:
                            print("ERROR: La calificacion debe estar entre 0 y 100.")
                            mensaje = "Ingrese nuevamente la calificacion:  "
                    elif texto.startswith("-") and texto[1:].isdecimal():
                        print("ERROR: La calificacion no puede ser negativa. Debe estar entre 0 y 100.")
                        mensaje = "Ingrese nuevamente la calificacion:  "
                    else:
                        print("ERROR: Debe ingresar un numero entero (no texto ni vacio).")
                        mensaje = "Ingrese nuevamente la calificacion:  "
    
                promedio = sum(notas) / len(notas)
    
                if promedio >= 51:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
    
                nombres.append(nombre)
                notas_estudiantes.append(notas)
                promedios.append(promedio)
                estados.append(estado)
    
                print("\n--- RESULTADO ---")
                print(f"Estudiante: {nombre}")
                for i in range(len(notas)):
                    print(f"Nota {i+1}: {notas[i]}")
                print(f"Promedio: {promedio:.2f}")
                print(f"Estado: {estado}")
                print("-----------------")        