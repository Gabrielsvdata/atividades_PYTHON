
''' na lista de duplas, retonar o nome da pessoa e a idade de forma crescente'''

#LAMBDA () => ()
# SORTED() cria uma copia 
#SORT () modifica a lista original 
def ordenação_tuplas(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key= lambda tupla: tupla[1]) 
    return lista_ordenada

lista_tuplas = [('Silvano', 27), ('Joyce', 26), ('Sogro', 75), ('Pai', 52), ('Mãe', 46), ]

print(f'A lista de tuplas ordenada por idade: {ordenação_tuplas(lista_tuplas)}')

# LAMBDA () => ()
# SORTED() cria uma cópia
# SORT() modifica a lista original

