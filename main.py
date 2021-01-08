from urllib import request

def getValorDolar ():
    html_da_pagina = request.urlopen('https://dolarhoje.com/')

    find = '<input type="text" id="nacional" '

    lista = (html_da_pagina.read().decode('utf-8')).split(find)

    parte2 = (lista[1]).split()

    value_html = parte2[0]

    valor_real = (value_html.split('"'))[1]

    float_real = float(valor_real.replace(',', '.'))

    return float_real

res = float(input('Quantos dólares você quer converter??\nEx: U$S 2.32\n>: U$S '))
umDolarEmReal = getValorDolar()
valorReal = res * umDolarEmReal

print('\n\nU$S', res, ' em reais é igual a: R$ ', valorReal, '\n\n')
