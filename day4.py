# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def lowestPositiveNotInArray(array, tam):
    maior = max(array)

    # checa se o menor que não está no array está dentro do
    # intervalo entre 1 e o maior número
    for i in range(1, maior):
        if i > 0 and i not in array:
            print(i)
            return i
    # se não estiver, quer dizer que o menor possível será igual
    # ao maior + 1
    print(maior+1)
    return maior+1


if __name__ == '__main__':
    print('PRIMEIRO CASO')
    array = [3, 4, -1, 1]
    lowestPositiveNotInArray(array, len(array))
    print('SEGUNDO CASO')
    array = [1, 2, 0]
    lowestPositiveNotInArray(array, len(array))
    print('TERCEIRO CASO')
    array = [0, -1, -3]
    lowestPositiveNotInArray(array, len(array))
    print('QUARTO CASO')
    array = [0, 1, 2, 3, 4]
    lowestPositiveNotInArray(array, len(array))
    print('QUINTO CASO')
    array = [0, 6, 10, -2]
    lowestPositiveNotInArray(array, len(array))
