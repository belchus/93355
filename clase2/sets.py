# CREAR UN SET (CONJUNTO)
# Un set guarda elementos ÚNICOS (sin repetidos) y SIN ORDEN fijo.
# Se escribe con llaves {} pero sin pares clave:valor (eso sería un diccionario).

etiquetas_post = {"Python", "Django", "Backend"}
print(etiquetas_post)         # El orden de salida puede variar en cada ejecución
print(type(etiquetas_post))   # -> <class 'set'>

# Set vacío: hay que usar set(), porque {} crea un diccionario vacío, no un set
datos = set()
print(type(datos))            # -> <class 'set'>


# AGREGAR ELEMENTOS CON add()
etiquetas_post.add("HTML")    # Agrega "HTML" al set
print(etiquetas_post)

# Si el elemento ya existe, NO se duplica y no da error
etiquetas_post.add("Python")  
print(etiquetas_post)
print(len(etiquetas_post))    # -> 4 


# discard() elimina el elemento si existe; si NO existe, no pasa nada (sin error)
etiquetas_post.discard("JAVA")   
print(etiquetas_post)

# remove() también elimina, pero si el elemento NO existe da KeyError. Por eso está comentado
#etiquetas_post.remove("Java")
#print(etiquetas_post)


# "in" devuelve True o False según si el elemento está en el set
print("Django" in etiquetas_post)   # -> True
print("Js" in etiquetas_post)       # -> False

# Los sets NO tienen índices (no tienen orden), por eso esto da TypeError:
#print(etiquetas_post[0])

# ELIMINAR DUPLICADOS DE UNA LISTA USANDO set()

etiquetas_lista = ["Python", "Java", "HTML", "Java"]   # "Java" está repetido

# set(lista) convierte la lista en set -> elimina los duplicados automáticamente
etiquetas_set = set(etiquetas_lista)

# list(set) vuelve a convertir el set en lista
etiquetas_inverso = list(etiquetas_set)

print("Original:", etiquetas_lista)      # ['Python', 'Java', 'HTML', 'Java']
print("Con Set:", etiquetas_set)         # {'Python', 'Java', 'HTML'} (orden variable)
print("Inverso:", etiquetas_inverso)     # ['Python', 'Java', 'HTML'] (orden variable)