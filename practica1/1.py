"""Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse
  de la conversión de datos
- Identificar los tipos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los trabadores
localizándolos por la posición en la lista."""

nombre_usuario = input("ingrese su nombre")
edad_usuario = int(input("ingrese su edad"))

print("su nombre es {} y su edad {}".format(nombre_usuario, edad_usuario))
print("el tipo 'nombre_usuario' y 'edad_usuario' es: {}".format((type(nombre_usuario), type(edad_usuario))))

nombre_trab1= input("ingrese su nombre")
edad_trab1 = int(input("ingrese su edad"))
nombre_trab2= input("ingrese su nombre")
edad_trab2 = int(input("ingrese su edad"))

lista1 = [nombre_trab1, edad_trab1, nombre_trab2, edad_trab2]
print("lista de trabajadores {}".format(lista1))

suma_edades = lista1[1] + lista1[3]
print("la suma de las edades de ambos trabajadores es de: {}".format(suma_edades))