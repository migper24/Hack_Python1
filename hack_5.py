"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
 result = 'fooziman'
 reemplazos = {  'o': '0', 'i': '1',  'a': '@'  }
  
 for char, replacement in reemplazos.items():
    result = result.replace(char, replacement)       
 return result

print(fn_hack_5())





                
