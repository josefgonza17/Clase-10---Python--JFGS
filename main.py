# Proyecto: Fundamentos de Python - Clase 10
# Estudiante: José F González Salgado
# Fecha de Inicio: [2025/03/26]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import media

from analisis_datos import *

lista_compras = generar_lista_compras()
print(lista_compras)
precios = [precios for _, precios in lista_compras]
print(precios)
print("La media aritmetica de la compra es: ", media(precios))
print("La mediana de la compra es:", mediana(precios))

