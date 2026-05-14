"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    count_keys = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            column = line.split('\t')
            elements = column[4].strip().split(',')

            for item in elements:
                key = item.split(':')[0]

                if key in count_keys:
                    count_keys[key] += 1
                else:
                    count_keys[key] = 1 
    return dict(sorted(count_keys.items()))