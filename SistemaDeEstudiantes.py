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