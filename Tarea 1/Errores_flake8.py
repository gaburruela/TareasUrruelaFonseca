
# Este comentario es un error al no dejar espacio despues del #
flag = True
# Este if no debe comparar el tipo de variable mediante un operador
if type(flag) is bool:
    # Este print contiene una linea demasiado larga
    print("Hello world, this is an overly large \
           message that will be detected by flake 8")
