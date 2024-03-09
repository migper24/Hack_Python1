"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    
    result = "fooziman"
    lista_original = list(result)
    lista_mayusculas = [resul1.upper() for resul1 in lista_original]
    lista_mayusculas[1] ='0'
    lista_mayusculas[2] ='0'
    lista_mayusculas[4] ='1'
    lista_mayusculas[6] ='@'
    return lista_mayusculas

print (fn_hack_10()) 