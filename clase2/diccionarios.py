
# CREAR UN DICCIONARIO
# Un diccionario guarda datos en pares "clave": valor.
# Los valores pueden ser de cualquier tipo: texto, números, listas, otros diccionarios, etc.
autor = {
    "nombre": "Camila Arena",       # clave "nombre" -> valor de tipo str (texto)
    "usuario": "arenabelu",         # clave "usuario" -> valor de tipo str
    "posts": [                      # clave "posts" -> valor de tipo list (lista)
        "Mi primer post",
        "Mi segundo post",
        "Mi tercer post"
    ],
}

# Muestra el diccionario completo
print(autor)                # Muestra el diccionario completo
# Accede a un valor usando su clave 
print(autor["nombre"])      # -> "Camila Arena"
print(autor["usuario"])     # -> "arenabelu"
print(autor["posts"])       # -> la lista completa de posts

# Guardar un valor del diccionario en una variable
nombre_autor = autor["nombre"]
print(nombre_autor)        # -> "Camila Arena"

# f-string permite meter variables dentro de un texto con {}
print(f"{autor['nombre']} tiene {autor['posts']} posts")


# Reemplaza la lista de posts por el número 20.
autor["posts"] = 20
print(autor)               


# Si la clave no existe, se crea. Si ya existe, se sobrescribe.
# Agrega la clave "red_social"
autor["red_social"] = "@arenabelu" 
# Agrega la clave "es_admin" con un booleano 
autor["es_admin"] = True            
print(autor)                        


# pop() elimina la clave del diccionario y DEVUELVE su valor
red_social_eliminada = autor.pop("red_social")
print("Red social eliminada:", red_social_eliminada)   # -> "@arenabelu"
print(autor)                                           # "red_social" ya no está



# Con corchetes [] da error (KeyError) si la clave no existe. Por eso está comentada:
#print(autor["rating"])

# Con .get() NO da error: devuelve el valor por defecto que le indiques.
rating = autor.get("rating", "No existe")
print(rating)               # -> "No existe"


# autor["posts"] devuelve la lista, y [0] toma el primer elemento (los índices empiezan en 0)
print(autor["posts"][0])    # -> "Mi primer post"


#  DICCIONARIOS ANIDADOS (un diccionario dentro de otro)

post = {
    "titulo": "Diccionario en Python",   # str
    "fecha": "15-10-2026",               # str
    "autor": {                           # el valor de "autor" es OTRO diccionario
        "nombre": "Camila Arena",
        "usuario": "arenabelu",
        "posts": [
            "Mi primer post",
            "Mi segundo post",
            "Mi tercer post"
        ]
    }
}

print(post["titulo"])                 # -> "Diccionario en Python"
print(post["autor"]["nombre"])        # Primero entra a "autor", luego a "nombre" -> "Camila Arena"
print(post["autor"]["posts"][0])      # Entra a "autor", luego a "posts", luego al índice 0 -> "Mi primer post"