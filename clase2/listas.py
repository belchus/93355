
# CREAR UNA LISTA
# Una lista guarda varios elementos ordenados entre corchetes [].
# Cada elemento tiene un índice que empieza en 0.
posts = ["Mi primer post", "Mi segundo post", "Mi tercer post"]
#            índice 0          índice 1          índice 2

# Lista vacía
posts_vacios = []

# Muestra la lista completa
print(posts)         
print(posts[0])      # Primer elemento -> "Mi primer post"
print(posts[1])      # Segundo elemento -> "Mi segundo post"
print(posts[-1])     # Índice negativo: cuenta desde el final. -1 es el último -> "Mi tercer post"

# Esta línea daría IndexError porque la lista solo tiene 3 elementos (índices 0, 1, 2).
#print(posts[10])


# Se asigna un nuevo valor usando el índice
posts[0] = "Bienvenidos a Python"   # Reemplaza "Mi primer post"
print(posts)         

# append() agrega el elemento AL FINAL de la lista
posts.append("Ultimo Post")
print(posts)         

# len() devuelve la cantidad de elementos de la lista
cantidad_posts = len(posts)
print(cantidad_posts)   # -> 4


# pop() sin argumentos elimina el ÚLTIMO elemento y lo devuelve
post_eliminado = posts.pop()
print("Eliminado:", post_eliminado)   # -> "Ultimo Post"
print(posts)                          


# pop(2) elimina el elemento que está en la posición 2 y lo devuelve
post_eliminado_indice = posts.pop(2)

# acá imprime post_eliminado (la variable anterior) y no post_eliminado_indice, por eso muestra "Ultimo Post" en lugar de "Mi tercer post".
print("Eliminado con indice:", post_eliminado)
print(posts)         

# index() devuelve la posición de la primera coincidencia.
# Si el elemento no existe, da ValueError.
indice = posts.index("Mi segundo post")
print(indice)        # -> 1