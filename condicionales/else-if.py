ingreso_mensual = 100000
gasto_mensual = 1200
if ingreso_mensual > 10000:
    #if anidado (primero se tiene que ejecutar el if de arriba y despues se ejecuta este)
    if gasto_mensual - ingreso_mensual > 500:
        print('Estas gastando mucho')
    else:
        print('estas gastando poco')
    
elif ingreso_mensual > 1000:
    print('estas bien  en latinoamerica')
    
elif ingreso_mensual > 500:
    print('estas bien en colombia')
    
else:
    print('Eres pobre')