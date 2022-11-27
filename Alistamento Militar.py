from datetime import date


atual = date.today().year
nascimento = int(input('Em que anos Nasceu?'))
idade = atual - nascimento
print('Quem nasceu no ano de {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você deve se apresentar IMDEDIATAMENTE!')
elif idade < 18:
    saldo_anos = 18 - idade
    print('Você deverá se apresentar em {} anos'.format(saldo_anos))
    ano = atual + saldo_anos
    print('Seu alistamento será no ano de {}'.format(ano))
elif idade >18:
    saldo_anos = idade - 18
    print('Voce deveria ter se apresentado há {} anos.'.format(saldo_anos), end='')
    ano = atual - saldo_anos
    print('Seu alistamento foi em {}.'.format(ano))

