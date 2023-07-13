"""
REQUISITOS:
- Crear 3 variables: nombre, apellido, edad y sueldo
-imprimir el siguiente mensaje: 'hola 'nombre apellido' su sueldo actual es de: sueldo soles
- mostrar la suma(concatenancion) del sueldo y la edad en un mensaje

"""

nombre = "alicia"
apellido = "noblecilla"
edad = "20"
sueldo = 3000

print(" hola {} {} su sueldo actual es de {} soles".format(nombre, apellido, sueldo))

conversion_sueldo = str(sueldo)
suma_string = edad + " y " + conversion_sueldo

print("la concatenacion es {}".format(suma_string))