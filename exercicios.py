''' escreva uma função que receba uma lista de numeros inteiros e retorna a soma de todos os elementos pares contidos nela'''


def soma_pares(lista_de_numeros):
    result = 0
    for numero in lista_de_numeros:
        if numero %2 == 0:
            result += numero #resultado = resultado + numero
    return result


lista = [1,4,6,8,3,7,9,15]

print(f'O resultado da soma dos elementos dos pares é: {soma_pares(lista)}')