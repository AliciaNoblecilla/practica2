"""conversion de datos"""

var_1 = "20"   # string
var_2 = 6789    # int
var_3 = 89.67   # float
var_4 = "alicia"

" para juntar dos string 'letras' "
suma_string = var_1 + " " + var_4
print("suma de string: {}".format(suma_string))

"""de string: str a int: int"""

conversiondevar_1 = int(var_1)
suma_int = conversiondevar_1 + var_2

print("suma de int: {}".format(suma_int))

"para ver que tipo de dato es mi variables usamos el type"

print("mi variable 'var_1' es de tipo: {} y mi variable 'var_2' es de tipo: {}".format(type(var_1),type(var_2)))

"""suma de dos variables: int + float = float"""

suma_2 = var_2 + var_3
print("la suma de 'var_2' y 'var_3' es: {}".format(suma_2))