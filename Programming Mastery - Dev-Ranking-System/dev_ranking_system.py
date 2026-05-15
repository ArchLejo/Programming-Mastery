#Seudónimo/Handle: ArchLejo.
#Rol/Role: Software Development Student.
#Fecha/Date: 09/05/2026 (D/M/Y).
#Proyecto/Project: Programming Mastery - Dev-Ranking-System.
#Descripcion/Description: Implementación de lógica modular para el cálculo de reputación y categorización de rangos (Sistema de Ranking de Desarrolladores).

def ObtenciondeDatos ():
    nombre = input("Ingrese el Nombre o Seudónimo del desarrollador: ") #Esto pedira el nombre del desarrollador y se guardara en la variable nombre.
    print()
    while True: #Este bucle while se encargara de que proyectos se pueda convertir a entero.
        proyectos = (input("Ingrese el número de proyectos que hizo el desarrollador: ")) #Esto pedira el numero de proyectos del desarrollador y se almacenara en proyectos.
        print()
        try:
            i = int(proyectos) #En este espacio i tomara el valor de proyectos como entero.
            proyectos = i #En este espacio proyectos tomara el valor de i ya convertido en entero.
            break #Una vez pase la validacion se rompe el bucle.
        except ValueError: #Si proyectos no puede ser convertido en entero por alguna anomalia dara error y se reinicia el bucle.
            print("Error, solo se permiten valores númericos.")
            print()
    return nombre, proyectos

def LogicadeEjecucion(proyectos):
    calificaciones = [] #Creamos la lista adentro pues el hacerlo fuera del def resultara en errores por la modulacion.
    if proyectos >= 1: #Esta condicional sirve para en caso de que proyecto sea mayor o igual a 1 el codigo entre en el bucle.
        #Creamos un bucle que recorrera el numero de veces acorde al numero que sea asignado en proyectos.
        for i in range(proyectos):
            while True:
                try:
                    datos = float(input(f"{i+1}. ingrese la nota en un rango de 1.0 a 5.0: ")) #En este espacio se solicitaran los espacios como float.
                    print()
                    if 1.0 <= datos <=5.0: #Si los datos estan en el rango entonces el codigo simplemente almacenara el dato.
                        calificaciones.append(datos) #Esto almacenara los datos en la lista calificaciones siempre y cuando esten en el rango acordado.
                        break #Si la nota es valida entonces el bucle se rompe.
                    else:
                        print("Los datos deben estar en un rango de 1.0 a 5.0")
                        print()
                except ValueError: #En caso de ingresar texto.
                    print("Entrada no numerica.")
                    print()
                
    else:
        #Si proyecto es menor a 1 entonces el programa asigna 0 en proyectos y calificaciones.
        proyectos = 0
        calificaciones = [0.0]
    return calificaciones

def CalculoFinal (calificaciones, proyectos):
    prepromedio = sum(calificaciones) #Este prepromedio se calcula con la suma de la lista calificaciones.
    promedio = prepromedio / proyectos #El promedio se calcula con prepromedio dividido por proyectos.
    nota_final = promedio * proyectos #La nota final es un calculo de promedio * proyectos para posterior al resultado asignar un rango al desarrollador.
    return promedio, nota_final

def CalculoRango (nota_final):
    #Aca dependiendo del resultado de nota final se le asignara un rango u otro al desarrollador.
    if nota_final < 10.0:
        rango = "Novato del Código"
    elif nota_final >=10.0 and nota_final < 40.0:
        rango = "Desarrollador Teso"
    else:
        rango = "Arquitecto Senior"
    return rango

#Flujo Principal.

#Ejecucion y obtencion para guardar en variables globales.
nombrefinal, totalproyectos = ObtenciondeDatos()
listanotas = LogicadeEjecucion(totalproyectos)
promediofinal, reputacion = CalculoFinal(listanotas, totalproyectos)
rangofinal = CalculoRango(reputacion)

#Aca simplemente se imprimen los resultados finales.
#EL PRINT FINAL
print("========================================")
print(f"Nombre: {nombrefinal}")
print(f"Número de Proyectos: {totalproyectos}")
print(f"Promedio de Notas: {promediofinal}")
print(f"Rango: {rangofinal}")
print("========================================")
