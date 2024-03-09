"""
text: "fooziman" output => "foozimaN"
"""
def fn_hack_4():
 # Palabra original
 palabra = 'fooziman'

# Extraemos todas las letras excepto la última
 letras_excepto_ultima = palabra[:-1]

# Convertimos la última letra a mayúscula
 ultima_letra_mayuscula = palabra[-1].upper()

# Combinamos las letras excepto la última con la última letra modificada
 palabra_modificada = letras_excepto_ultima + ultima_letra_mayuscula

 return palabra_modificada
print(fn_hack_4())