# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        # retorna uma função com parametros a, b
        # function(a, b)
        return f(a, b)
    return pair
    # retorna pair, que recebe uma função e passa a mesma
    # para os parametros a e b
    # pair(function(a,b))


def car(pair):
    # recebe a função pair(function(a, b))
    def getFirst(first, second):
        # essa função recebe os dois parametros a e b
        # e retorna apenas o primeiro.
        return first
    return pair(getFirst)
    # passa a função getFirst para pair
    # pair(getFirst(a, b))

def cdr(pair):
    # mesma logica de cima
    def getSecond(first, second):
        # mesma logica de cima
        # porem retorna apenas o segundo parametro.
        return second
    return pair(getSecond)
    # mesma logica de cima


if __name__ == '__main__':
    a = cons(3, 4)
    print(car(a))
    print(cdr(a))
