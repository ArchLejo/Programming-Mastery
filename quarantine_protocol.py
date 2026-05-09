#Seudónimo/Handle: ArchLejo.
#Rol/Role: Software Development Student.
#Fecha/Date: 09/05/2026 (D/M/Y).
#Proyecto/Project: Programming Mastery - Quarantine-Protocol.
#Descripcion/Description: Implementación de la lógica de detección de riesgos secuenciales (Protocolo de Cuarentena).


Temperaturas = [ 36.2, 37.5, 38.4, 39.1, 38.9, 36.8, 40.2, 39.5, 37.2, 38.1 ]

ResultadoLista = ("")

Contador = 0

Consecutivos = 0

Limite = 38.0

#La función Principal es buscar en Temperaturas 3 datos mayores a 38.0 consecutivos, de lo contrario todo sera correcto.
for n in Temperaturas:
    if n >= Limite:
        Contador += 1 #Si n es mayor a Limite en la lista temperatura Contador se le suma 1.
        if Contador == 3:
            Consecutivos += 1 #Si contador es mayor o igual a 3 entonces consecutivos se le suma 1.
            break #Opcion para romper el bucle for y que deje de buscar.
    else:
        Contador = 0 # Si n es menor al limite en la lista temperatura, contador se reinicia en 0.

if Consecutivos != 0: #Si Consecutivos es distinto de 0 entonces se imprime en pantalla el siguiente texto.
    print("Alerta: Se ha detectado un pico en la lista de Temperaturas.")

else: #En caso contrario (Consecutivos == 0) entonces se imprime en pantalla el siguiente texto.
    print("Resultados completamente normales, No se detectaron picos en la lista de temperaturas.")

