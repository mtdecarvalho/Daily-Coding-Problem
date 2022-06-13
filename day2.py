# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def arrayDeProdutos(array, tam):
    if tam == 1:
        print(0)
        return

    i, temp = 1, 1

    # inicializando o array prod como 1
    prod = [1 for i in range(tam)]

    # neste loop, a variavel temp contem o produto dos elementos do
    # lado esquerdo do array com a exceção de array[i]
    for i in range(tam):
        prod[i] = temp
        temp *= array[i]

    # reseta a variável temporária para calcular o lado direito do array
    temp = 1

    # neste loop, a variavel temp contem o produto dos elementos do
    # lado direito do array com a exceção de array[i]
    for i in range(tam-1, -1, -1):
        prod[i] *= temp
        temp *= array[i]

    print(prod)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    tam = len(array)
    arrayDeProdutos(array, tam)

    array = [3, 2, 1]
    tam = len(array)
    arrayDeProdutos(array, tam)
