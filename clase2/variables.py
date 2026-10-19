
# VARIABLES Y TIPOS DE DATOS BÁSICOS
# Una variable es un nombre que guarda un valor. Python detecta el tipo automáticamente.
titulo_post = "Mi primer post"   # str (string): texto, siempre entre comillas
autor = "Camila"                 # str
visitas = 150                    # int (integer): número entero, sin decimales
rating = 4.5                     # float: número con decimales (se usa punto, no coma)
destacado = True                 # bool (booleano): solo puede ser True o False (con mayúscula inicial)


# print() acepta varios argumentos separados por coma y los muestra con un espacio entre ellos
print("Titulo del post:", titulo_post)       # -> Titulo del post: Mi primer post
print("Cantidad de visitas:", visitas)       # -> Cantidad de visitas: 150


#  CONSULTAR EL TIPO CON type()

print(type(titulo_post))    # -> <class 'str'>
print(type(visitas))        # -> <class 'int'>
print(type(rating))         # -> <class 'float'>
print(type(destacado))      # -> <class 'bool'>


# Con f"..." se pueden insertar variables dentro del texto usando {}
print(f"El post {titulo_post} fue escrito por {autor}")

# ============================================================
# CONVENCIONES PARA NOMBRAR VARIABLES
# ============================================================
# Buenas prácticas (snake_case: minúsculas separadas por guion bajo):
#   cantidad_likes
#   es_admin
#   nombre_autor
#
# Nombres INCORRECTOS o a evitar:
#   titulo post     -> tiene un espacio (error de sintaxis)
#   NombreAutor     -> es CamelCase/PascalCase; en Python se reserva para nombres de clases
#   1visitas        -> no puede empezar con un número (error de sintaxis)
#   a, x            -> son válidos, pero poco descriptivos