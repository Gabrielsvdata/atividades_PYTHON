def frequencia(palavras):
    lista = palavras.split(' ')
    dicionario = {}
    for palavra in lista:
        if palavra not in dicionario.keys(): 
            dicionario[palavra] = lista.count(palavra)  
    return dicionario


sobrenomes = 'Gabriel, Silvano, Vieira, Luciene, Silvano, Alexandre, Vieira'


print(f'Dicionário: {frequencia(sobrenomes)}')
