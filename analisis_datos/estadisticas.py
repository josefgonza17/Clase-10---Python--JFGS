# estadisticas.py
def media(datos):
    media_aritmetica = sum(datos) / len(datos)
    return media_aritmetica
    
def mediana(datos):
    #mediana
    #paso 1: ordenar los valores ascedente
    #cantidad de elementos
    precios_asc = sorted(datos)
    n = len(precios_asc)
    print(precios_asc)
    mitad = n // 2 
    print(mitad)
    if n % 2 == 0:
        mediana = (precios_asc[mitad -1] + precios_asc [mitad])/2
    else:
        mediana = precios_asc[mitad]
    return mediana