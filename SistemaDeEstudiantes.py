
NOTA_MINIMA = 0
NOTA_MAXIMA = 100
NOTA_APROBACION = 51
CANTIDAD_NOTAS = 3

estudiantes = []

print("SISTEMA DE REGISTRO DE CALIFICACIONES")

while continuar:
 
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre == "":
            print("ERROR: El nombre no puede estar vacío.")
 
    notas = []
    for i in range(1, CANTIDAD_NOTAS + 1):
        mensaje = f"Ingrese la calificación {i}: "
        valida = False