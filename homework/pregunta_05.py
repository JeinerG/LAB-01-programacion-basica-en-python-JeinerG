"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
value = {}

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as file:
        for line in file:
            
            column = line.split('\t')
            letter = column[0]
            num = int(column[1])

            if letter in value:
                
                max_actual, min_actual = value[letter]
                
                if num > max_actual:
                    max_actual = num
                if num < min_actual:
                    min_actual = num
                
                value[letter] = (max_actual, min_actual)
            else:
                
                value[letter] = (num, num)

   
    resultado = [(letter, v[0], v[1]) for letter, v in sorted(value.items())]
    return resultado