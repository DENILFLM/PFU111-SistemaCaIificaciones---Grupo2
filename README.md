# PFU111-SistemaCaIificaciones---Grupo2


## Descripción
Programa que permite registrar las calificaciones de estudiantes, calcular su
promedio y determinar si aprobaron o reprobaron, controlando entradas
inválidas para evitar errores durante la ejecución.

## Funcionalidades
- Registrar el nombre de un estudiante.
- Registrar tres calificaciones.
- Calcular el promedio.
- Determinar si el estudiante aprobó o reprobó.
- Mostrar los resultados.
- Registrar varios estudiantes en una misma ejecución.

## Validaciones
- El nombre no puede estar vacío.
- Las calificaciones deben ser numéricas.
- Las calificaciones deben estar entre 0 y 100; si no, se vuelve a solicitar el dato.

## Manejo de errores
- Texto ingresado donde se espera un número.
- Calificación negativa o mayor a 100.
- Nombre vacío.
- Otras entradas inesperadas.
En todos los casos el programa detecta el problema, informa al usuario,
solicita corrección y continúa funcionando.

## Pruebas realizadas
Prueba | Entrada | Resultado |

Datos válidos | Ana, 80, 75, 90 | Promedio correcto y estado mostrado |
Calificación negativa | -10 | Mensaje de error y se vuelve a pedir |
Mayor al máximo | 150 | Mensaje de error y se vuelve a pedir |
Nombre vacío | (vacío) | Mensaje de error y se vuelve a pedir |
Entrada inesperada | texto (ej. "abc") | Mensaje de error y se vuelve a pedir |

## Tecnologías utilizadas
- Python 
- Git
- GitHub
