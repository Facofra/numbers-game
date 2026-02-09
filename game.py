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

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_divisores(n):
    # Incluye n
    divisores = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisores.add(i)
            divisores.add(n // i)
        i += 1
    return sorted(list(divisores))

def get_Misma_raiz_digital(k,n):
    # Números cuya raíz digital (suma repetida hasta un dígito) sea igual a la del número secreto.
    # Ejemplo: 16→1+6=7, 25→2+5=7, 97→9+7=16→1+6=7  (todos tienen raíz digital 7)
    
    def raiz_digital(num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num
    
    raiz_secreto = raiz_digital(n)
    misma_raiz = []
    
    for i in range(1, k + 1):
        if raiz_digital(i) == raiz_secreto:
            misma_raiz.append(i)
    
    return misma_raiz

def get_Perfecto(k):
    # nunca voy a usar k tan grande
    return [i for i in [6, 28, 496, 8128,33550336] if i <= k]
    
def get_Cubo_perfecto(k):

    Cubo_perfecto = []
    for i in range(1,k):
        if i**3 > k:
            return Cubo_perfecto
        Cubo_perfecto.append(i**3)
        
def get_Altamente_compuesto(k):

    max_divisores=0
    Altamente_compuestos=[]
    for i in range(1,k+1):
        cantidad_divisores =  len(get_divisores(i))
        if cantidad_divisores > max_divisores:
            Altamente_compuestos.append(i)
            max_divisores = cantidad_divisores

    return Altamente_compuestos

def get_Pronico(k):
    
    pronico = []
    for i in range(1,k+1):
        next = i+1
        muliplication = i*next
        if muliplication > k:
            return pronico
        pronico.append(i * next)

def get_Fibonacci(k):
    fibonacci = [1,2]
    for i in range(1,k+1):
        suma = fibonacci[i] + fibonacci[i-1]
        if suma > k:
            return fibonacci
        fibonacci.append(suma)

def get_Cuadrado_perfecto(k):
    Cuadrado_perfecto = []
    for i in range(1,k):
        if i**2 > k:
            return Cuadrado_perfecto
        Cuadrado_perfecto.append(i**2)

def get_Multiplo_de_9(k):
    multiplos = []

    i = 1
    while i*9 <= k:
        multiplos.append(i*9)
        i+=1

    return multiplos

def get_Multiplo_de_8(k):
    multiplos = []

    i = 1
    while i*8 <= k:
        multiplos.append(i*8)
        i+=1

    return multiplos

def get_Triangular(k):
    triangular = [1]
    for i in range(2,k):
        suma = i + triangular[i-2]
        if suma > k:
            return triangular
        triangular.append(suma)

def get_Multiplo_de_7(k):
    multiplos = []

    i = 1
    while i*7 <= k:
        multiplos.append(i*7)
        i+=1

    return multiplos

def get_Multiplo_de_6(k):
    multiplos = []

    i = 1
    while i*6 <= k:
        multiplos.append(i*6)
        i+=1

    return multiplos

def get_Palindrome(k):

    palindromes = []
    for num in range(1, k + 1):
        str_num = str(num)
        # Verificar si es palíndromo comparando con su reverso
        if str_num == str_num[::-1]:
            palindromes.append(num)
    return palindromes

def get_Numero_feliz(k):
    # Un número que eventualmente llega a 1 cuando se reemplaza repetidamente por la suma de los cuadrados de sus dígitos.
    # Ejemplo: 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1
    
    def es_numero_feliz(num):
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = sum(int(digit) ** 2 for digit in str(num))
        return num == 1

    numeros_felices = []
    for i in range(1, k + 1):
        if es_numero_feliz(i):
            numeros_felices.append(i)

    return numeros_felices

def get_Multiplo_de_5(k):
    multiplos = []

    i = 1
    while i*5 <= k:
        multiplos.append(i*5)
        i+=1

    return multiplos

def get_Abundante(k):
    # Un número menor que la suma de todos sus divisores propios.
    # Ejemplo: 18 → divisores propios: 1,2,3,6,9 → suma: 21 > 18
    abundantes = []
    for i in range(1,k+1):
        suma = sum(get_divisores(i)) - i
        if i < suma:
            abundantes.append(i)
    return abundantes    

def get_Harshad(k):
    # Un número divisible por la suma de sus dígitos.
    # Ejemplo: 84 → suma de dígitos: 8+4=12 → 84÷12 = 7 (exacto)
    harshad = []
    for i in range(1, k + 1):
        suma_digitos = sum(int(digit) for digit in str(i))
        if i % suma_digitos == 0:
            harshad.append(i)
    return harshad

def get_Primo(k):
    primos = []
    for i in range(2, k + 1):
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

def get_Multiplo_de_4(k):
    multiplos = []

    i = 1
    while i*4 <= k:
        multiplos.append(i*4)
        i+=1

    return multiplos

def get_Multiplo_de_3(k):
    multiplos = []

    i = 1
    while i*3 <= k:
        multiplos.append(i*3)
        i+=1

    return multiplos

def get_Numero_regular(k):
    # Un número cuyos únicos factores primos son 2, 3 y 5.
    # Ejemplo: 48 → 48 = 2⁴×3¹ (solo factores 2 y 3)
    regulares = []
    for i in range(1, k + 1):
        num = i
        # Dividir por 2, 3 y 5 mientras sea posible
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        # Si queda 1, significa que solo tenía factores 2, 3 y 5
        if num == 1:
            regulares.append(i)
    return regulares

def get_Semi_primo(k,primos):
    # Un número que es el producto de exactamente dos números primos (no necesariamente distintos).
    # Ejemplo: 35 → 5×7 = 35 (producto de dos primos)
    semi_primos = []
    
    for i in range(1, k + 1):
        # Contar factores primos (con repetición)
        factor_count = 0
        num = i
        
        for primo in primos:
            if primo * primo > num:
                break
            while num % primo == 0:
                factor_count += 1
                num //= primo
        
        # Si queda un número > 1, es un factor primo
        if num > 1:
            factor_count += 1
        
        # Si tiene exactamente 2 factores primos, es semi-primo
        if factor_count == 2:
            semi_primos.append(i)
    
    return semi_primos

def get_Suma_de_digitos_prima(k):
    # Números cuya suma de dígitos es primo.
    # Ejemplo: 29 → 2+9=11 (primo), 38 → 3+8=11 (primo)
    Suma_de_digitos_prima = []
    for i in range(1,k+1):
        suma_digitos = sum(int(digit) for digit in str(i))
        if es_primo(suma_digitos):
            Suma_de_digitos_prima.append(i)

    return Suma_de_digitos_prima

def get_Dígitos_ascendentes(k):
    # Los dígitos van en orden creciente.
    # Ejemplo: 12, 18, 27, 34
    digitos_ascendentes = []
    for i in range(1,k+1):
        num_str = str(i)
        if [n for n in num_str] == sorted(num_str) and len(set(num_str)) == len(num_str):
            digitos_ascendentes.append(i)
    return digitos_ascendentes

def get_Par(k):
    multiplos = []

    i = 1
    while i*2 <= k:
        multiplos.append(i*2)
        i+=1

    return multiplos

def get_Impar(k,pares):
    return [i for i in range(1,k+1) if i not in pares]

def get_Compuesto(k,primos):
    return [i for i in range(2,k+1) if i not in primos]

def get_Deficiente(k):
    deficientes = []
    for i in range(1,k+1):
        suma = sum(get_divisores(i)) - i
        if i > suma:
            deficientes.append(i)
    return deficientes    

def get_Natural(k):
    return [i for i in range(1,k+1)]


k = 100



secreto = random.randint(1,k)

# categories = {
#     'Divisor': get_divisores(secreto),
#     'Misma raiz digital': get_Misma_raiz_digital(k,secreto),
#     # 'Categoria secreta': get_Categoria secreta(k),
#     'Perfecto': get_Perfecto(k),
#     'Cubo perfecto': get_Cubo_perfecto(k),
#     'Altamente compuesto': get_Altamente_compuesto(k),
#     'Prónico': get_Pronico(k),
#     'Fibonacci': get_Fibonacci(k),
#     'Cuadrado perfecto': get_Cuadrado_perfecto(k),
#     'Multiplo de 9': get_Multiplo_de_9(k),
#     'Multiplo de 8': get_Multiplo_de_8(k),
#     'Triangular': get_Triangular(k),
#     'Multiplo de 7': get_Multiplo_de_7(k),
#     'Multiplo de 6': get_Multiplo_de_6(k),
#     'Palindrome': get_Palindrome(k),
#     'Numero feliz': get_Numero_feliz(k),
#     'Multiplo de 5': get_Multiplo_de_5(k),
#     'Abundante': get_Abundante(k),
#     'Harshad': get_Harshad(k),
#     'Primo': get_Primo(k),
#     'Multiplo de 4': get_Multiplo_de_4(k),
#     'Multiplo de 3': get_Multiplo_de_3(k),
#     'Numero regular': get_Numero_regular(k),
#     # 'Semi primo': get_Semi_primo(k),
#     'Suma de digitos prima': get_Suma_de_digitos_prima(k),
#     'Dígitos ascendentes': get_Dígitos_ascendentes(k),
#     'Par': get_Par(k),
#     # 'Impar': get_Impar(k),
#     # 'Compuesto': get_Compuesto(k),
#     'Deficiente': get_Deficiente(k),
#     'Natural': get_Natural(k)
# }


jugando = False
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




    
