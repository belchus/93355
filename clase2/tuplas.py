
# CREAR TUPLAS
# Una tupla es como una lista, pero INMUTABLE: una vez creada no se puede modificar.
# Se escribe con paréntesis () y mantiene el orden (tiene índices).
# A diferencia de los sets, SÍ permite elementos repetidos.
categorias = ("Python", "Django", "HTML", "Python")   # "Python" repetido: es válido
coordenadas = (120, 20)                               # Ejemplo típico: datos fijos como (x, y)
tipo_usuarios = ("Admin", "Editor", "Escritor")       # Valores que no deberían cambiar


#  MOSTRAR Y ACCEDER A ELEMENTOS
print(categorias)             # -> ('Python', 'Django', 'HTML', 'Python')
print(type(categorias))       # -> <class 'tuple'>
print(categorias[0])          # Primer elemento -> "Python"
print(categorias[-1])         # Último elemento (índice negativo) -> "Python"


# No se pueden modificar elementos (daría TypeError):
#categorias[0] = "Backend"

# Tampoco tienen append(), pop(), remove(), etc. (daría AttributeError):
#categorias.append("Backend")


# FUNCIONES Y MÉTODOS ÚTILES

print(len(categorias))              # Cantidad de elementos -> 4
print("Django" in categorias)       # ¿Está "Django"? -> True
print("Camila" in categorias)       # ¿Está "Camila"? -> False

# count() cuenta cuántas veces aparece un elemento
print(categorias.count("Python"))   # -> 2

# index() devuelve la posición de la primera coincidencia
# (si no existe, da ValueError)
print(categorias.index("Django"))   # -> 1