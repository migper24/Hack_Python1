"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
 result = [1, 3, 5, 7, 9]
 lista_resultante = result[1:-1]
 return lista_resultante
print(fn_hack_8())