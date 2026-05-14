"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sums_by_letter = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.split('\t')
            letter_major = columns[0]
            elements = columns[4].strip().split(',')
            sum_row_column5 = 0
            for item in elements:
                # 'aaa:5' -> valor es 5
                value = int(item.split(':')[1])
                sum_row_column5 += value
            if letter_major in sums_by_letter:
                sums_by_letter[letter_major] += sum_row_column5
            else:
                sums_by_letter[letter_major] = sum_row_column5
    return dict(sorted(sums_by_letter.items()))