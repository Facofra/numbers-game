import random

categorias = {
    'perfecto'            : [6,28],
    'cubo_perfecto'       : [1,8,27,64],
    'divisor'             : [],
    'altamente_compuesto' : [1,2,4,6,12,24,36,48,60],
    'pronic_number'       : [2,6,12,20,30,42,56,72,90],
    'fibonacci'           : [1,2,3,5,8,13,21,34,55,89],
    'cuadrado_perfecto'   : [1,4,9,16,25,36,49,64,81,100] ,
    'multiplo_9'          : [9,18,27,36,45,54,63,72,81,90,99],
    'multiplo_8'          : [8,16,24,32,40,48,56,64,72,80,88,96],
    'triangular'          : [1,3,6,10,15,21,28,36,45,55,66,78,91],
    'multiplo_7'          : [7,14,21,28,35,42,49,56,63,70,77,84,91,98],
    'multiplo_6'          : [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96],
    'palindrome'          : [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99],
    'numero_feliz'        : [10,13,19,23,28,31,32,44,49,68,70,79,82,86,91,94,97,100],
    'multiplo_5'          : [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    'abundante'           : [12,18,20,24,30,36,40,42,48,54,56,60,66,70,72,78,80,84,88,90,96,100],
    'harshad'             : [10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100],
    'primo'               : [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97],
    'multiplo_4'          : [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100],
    'multiplo_3'          : [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99],
    'numero_regular'      : [1,2,3,4,5,6,8,9,10,12,15,16,18,20,24,25,27,30,32,36,40,45,48,50,54,60,64,72,75,80,81,90,96,100],
    'semi_primo'          : [4,6,9,10,14,15,21,22,25,26,33,34,35,38,39,46,49,51,55,57,58,62,65,69,74,77,82,85,86,87,91,93,94,95],
    'par'                 : [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100],
    'impar'               : [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99],
    'compuesto'           : [4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,57,58,60,62,63,64,65,66,68,69,70,72,74,75,76,77,78,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100],
    'deficiente'          : [1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,21,22,23,25,26,27,29,31,32,33,34,35,37,38,39,41,43,44,45,46,47,49,50,51,52,53,55,57,58,59,61,62,63,64,65,67,68,69,71,73,74,75,76,77,79,81,82,83,85,86,87,89,91,92,93,94,95,97,98,99],
    'natural'             : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
}
# mismo cuadrante 12 arriba 12 abajo. o lo que de


def print_matrix(matriz,secreto):
    print()
    TRUE_CHAR = "✔"
    FALSE_CHAR = "·"

    # reemplazar numero secreto por x
    matriz = {llave if llave != secreto else 'x'
        :matriz[llave] for llave in matriz
    }

    numeros = list(matriz.keys())
    categorias = list(next(iter(matriz.values())).keys())

    # Anchos de columna
    num_width = max(len(str(n)) for n in numeros) + 2
    cat_width = max(len(c) for c in categorias) + 2

    # Header
    header = "Categoria".ljust(cat_width)
    for n in numeros:
        header += str(n).ljust(num_width)

    print(header)
    print("-" * len(header))

    # Filas
    for cat in categorias:
        row = cat.ljust(cat_width)
        for n in numeros:
            row += (TRUE_CHAR if matriz[n][cat] else FALSE_CHAR).ljust(num_width)
        print(row)

    print()



secreto = random.randint(1,100)
categorias['divisor'] = [n for n in range(1,101) if secreto % n == 0]


jugando = True
matriz_adjacencia = {
    secreto : {}
}

print('==================')
print('Guess the number x')
print('==================')
print()

while jugando:
    guess = int(input('guess: '))
    
    if guess == secreto:
        jugando = False
        print('WIN!!!!')
        continue

    if guess in matriz_adjacencia:
        print('Ya jugado')
        continue

    for categoria,miembros in categorias.items():
        if secreto in miembros and guess in miembros :
            
            matriz_adjacencia[guess] = {**matriz_adjacencia[secreto],categoria: True}

            # Actualizar categoria para cada numero ya en la matriz
            for numero in matriz_adjacencia:
                valor = True if numero in miembros else False
                matriz_adjacencia[numero] = {**matriz_adjacencia[numero],categoria: valor}

            # Actualizar valores para el guess recien ingresado
            for categoria_en_matriz in matriz_adjacencia[secreto]:
                matriz_adjacencia[guess][categoria_en_matriz] = True if guess in categorias[categoria_en_matriz] else False
                

            # ordenar matriz segun orden ya establecido en categorias
            matriz_adjacencia = {
                numero : {cat: matriz_adjacencia[numero][cat] for cat in categorias if cat in matriz_adjacencia[numero]}
                for numero in matriz_adjacencia
            }


            print_matrix(matriz_adjacencia,secreto)

            break




    
