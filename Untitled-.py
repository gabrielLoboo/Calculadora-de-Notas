nota1 = float (input ('Primeira Nota: '))
nota2 = float (input ('Segunda Nota: '))
nota3 = float (input ('Terceita Nota: '))

total = (nota1 + nota2 + nota3) / 3

print('Sua media foi:',total)

if total >= 9:
    conceito = 'A'
elif total >= 8 and total <= 8.9:
    conceito = 'B'
elif total >= 7 and total <= 7.9:
    conceito = 'C'
elif total >= 6 and total <= 6.9:
    conceito = 'D'
else:
    conceito = 'E'

match conceito:
    case 'A':
        print('O seu conceito foi', conceito)
    case 'B':
        print('O seu conceito foi', conceito)
    case 'C':
        print('O seu conceito foi', conceito)
    case 'D':
        print('O seu conceito foi', conceito)
    case 'E':
        print('O seu conceito foi', conceito)
    case _:
        print('Nenhuma media listada')
