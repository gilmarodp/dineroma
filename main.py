from urllib import request

def getValorDolar ():
    html_da_pagina = request.urlopen('https://dolarhoje.com/') 

    find = '<input type="text" id="nacional" ' #diz onde vai quebrar pra transformar em lista
    
    lista = (html_da_pagina.read().decode('utf-8')).split(find) #quebrar

    parte2 = (lista[1]).split() #separar por espaço já q n tá escrito nada

    value_html = parte2[0] #parte que interessa da lista

    valor_real = (value_html.split('"'))[1] #separar o valor a partir das aspas e pegar o índice 1

    float_real = float(valor_real.replace(',', '.')) #trocar a "," pro "." e converter pro float

    return float_real #retorna o float_real

res = float(input('Quantos dólares você quer converter? Ex: U$S 2.32\n>: U$S '))
umDolarEmReal = getValorDolar()
valorReal = res * umDolarEmReal

print('\n\nU$S', res, ' em reais é igual a: R$ ', valorReal, '\n\n') 


def getValorEuro ():
    html_da_pag_euro = request.urlopen('https://www.dolarhoje.net.br/euro-hoje/')

    findEur = '<input type="text" id="moeda" '

    listaEur = (html_da_pag_euro.read().decode('utf-8')).split(findEur) 

    parte3 = (listaEur[1]).split()

    value_htmlEur = parte3[0]

    valor_realEur = (value_htmlEur.split('"'))[1]

    float_realEur = float(valor_realEur.replace(',', '.'))
   
    return float_realEur

resEur = float(input('Quantos euros você quer converter? Ex: € 20\n>: € '))

umEuroEmReais = getValorEuro()

valorRealEur = resEur * umEuroEmReais

print('\n\n€', res, 'em reais é igual a: R$', valorRealEur, '\n\n')