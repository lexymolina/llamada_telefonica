minutos = int(input("digite la duracion de la llamada: "))

if minutos ==3:
    costo_llamada = 300

else:
    costo_llamada = 300 + 50*(minutos - 3)

print("el costo de la llamada es: " + costo_llamada)        
