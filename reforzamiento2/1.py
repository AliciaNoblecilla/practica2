"Crear una lista de 6 objetos y mostrar en pantalla (ítems de cursos que lleves o hayas"
import math

"llevado en la universidad)"

cursos = ["finanzas", "finanzas1", "contabilidad", "calculo", "estadistica", "estadistica para economistas"]

print(" Algunos cursos que lleve en la universidad son: {}".format(cursos))

"Agregar 4 Objetos nuevos a tu lista (append)"

cursos.append("matematica1")
cursos.append("matematica2")
cursos.append("matematica3")
cursos.append("matematica4")

print(" mi nueva lista de cursos son: {}".format(cursos))

"Quita 2 elementos de tu nueva lista ítems por valor, no por índice"

cursos.remove("matematica1")
cursos.remove("matematica2")
print(" mi nueva lista de cursos son: {}".format(cursos))

"Invierte y muestra en consola tu lista de cursos"

cursos.reverse()
print(" mi nueva lista de cursos en reversa son: {}".format(cursos))

"Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el resultado en"
"consola. (Pista: len(lista))"

print("la cantidad de mi lista es de {}".format(len(cursos)))

"Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)"
"dentro de la lista"

cursos.append("fisica")
cursos.append("fisica")
cursos.append("fisica")
cursos.append("fisica")

print("las veces que se repite el curso de 'fisica' son de: {}".format(cursos.count("fisica")))

"Borra el primer ítem de la lista usando debidamente su índice"

cursos.pop(0)
print(" mi nueva lista eliminando el primer elemento es: {}".format(cursos))

"Crea una nueva lista vacía y agregue 4 ítems (diferentes tipos de datos 3 floats, 3 ints y 3"
"strings) (append)"

list_1 = []
list_1.append(12.3)
list_1.append(34.5)
list_1.append(56.7)
list_1.append(20)
list_1.append(40)
list_1.append(60)
list_1.append("buenos dias")
list_1.append("buenas tardes")
list_1.append("buenas noches")

print("mi nueva lista es: {}".format(list_1))

"Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal"

suma_de_listas = cursos + list_1
print("la suma de mis dos listas unidas es: {}".format(suma_de_listas))

"crea una lista donde luego se puedan usar los metodos de orden los elementos tienen que estar desordenados"

list_num = [20, 30, 50, 12.4, 60, 10, 40.69]
list_num.sort()

print("mi lista 'list_num' ordenada es: {}".format(list_num))

"crear una lista entre floats y bools de 6 elementos donde imprimas el penultimo y ultimo valor por indice "

lista = [10.2, 98.3, 60.5, 70.34, False, True]

penul_lista = lista[4]
ulti_lista = lista[5]

print("el valor penultimo es: {} y el valor ultimo es: {}".format(penul_lista, ulti_lista))
print("los tipos de datos de mi lista es: {}".format(type(lista)))

"Elimina ahora todoslos elementos de la lista creada previamente y mostrar en consola"
"el estado de la lista"

lista.clear()
print("la nueva lista actualizada es: {}".format(lista))
print("hay : {} datos en mi lista nueva ".format(len(lista)))

"Elimina un elemento por dos índices existentes y ya no por el valor"

lista2 = [10.2, 98.3, 60.5, 70.34, False, True]
lista2.pop(2)
lista2.pop(3)

print("la nueva lista actualizada es: {}".format(lista2))

"15. Crear una lista con los 100 primeros enteros"

numeros_enteros = range(100)
range(0, 100)
print(list(numeros_enteros))
"16. Mostrar sólo los datos comprendidos entre la posición 10 y 35"
print(list(range(10, 35)))





