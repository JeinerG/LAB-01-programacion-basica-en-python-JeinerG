"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    values = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
                      
            column = line.split('\t')
           
            elements = column[4].strip().split(',')

            for item in elements:
               
                key, value_str = item.split(':')
                value = int(value_str)

                if key in values:
                    max_p, min_p = values[key]
                    if value > max_p:
                        max_p = value
                    if value < min_p:
                        min_p = value
                    values[key] = (max_p, min_p)
                else:
                    values[key] = (value, value)

    
    result = [(key, v[1], v[0]) for key, v in sorted(values.items())]
    return result