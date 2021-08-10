
'''
Enunciado: Escriba un programa para verificar si una matriz se puede dividir en una posición tal que 
la suma del lado izquierdo de la división sea igual a la suma del lado derecho.
'''

'''
Debes escribir una función llamada canBeSplitted que reciba un array de números y devuelva 1 si se puede dividir, -1 si no se pu
ede dividir y 0 si el array es vacío.
Ejemplo de entrada:
'''

import  argparse
from typing import List

def canBeSplitted(array:List[int]) -> int:
    canBeSplitted:int = 0
    result:int = sum(array)
    count:int = 0

    array_a:List[int] = []
    array_b:List[int] = []

    for i,num in enumerate(array,0):
        
        if sum(array_a) < result//2:
            array_a.append(num)
        elif sum(array_a) == result//2 and sum(array_b) < result//2:
            array_b.append(num)
        elif sum(array_a) > result//2 or sum(array_b) > result//2: 
            #Si a y b son mayores que la suma de la mitad de elementos, entonces no es divisible
            return -1


    if sum(array_a) == sum(array_b):
        # array_b puede ser menor, asi que compruebo si son iguales
        return 1
    else:
        return -1
    return 0


def main(args:List[int]) -> int:
    return canBeSplitted(args)


if __name__=='__main__':

    parser = argparse.ArgumentParser(
        description ='test test test!',
        usage='%(prog)s [options] --list 1 2 3 3 3',
        epilog='Enjoy the program! :)'
    )


    parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True, type=int)
    args = parser.parse_args()

    print(main(args.list))