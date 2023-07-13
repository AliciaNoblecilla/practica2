"""
Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
edad =  input("ingrese su edad")
dni =  input("ingrese su dni")

mi_dicc = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'dni': dni}
print(mi_dicc)
"""pra obetener solo los valores"""
valores = list(mi_dicc.values())

print(valores)
mi_dicc["profesion"] = "economista"
print("mi diccionario actualizado es: {}".format(mi_dicc))

del mi_dicc["dni"]

print("los datos actualizados de mi diccionario son: {}".format(mi_dicc))
