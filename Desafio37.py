# Converte um número inteiro em binário, octal ou hexadecimal, conforme solicitação do usuário.
n = int(input('Digite um número inteiro: '))
print('Escolha uma opção abaixo para converter:\n'
      '\033[31m[1]\033[m converter em BINÁRIO.\n'
      '\033[31m[2]\033[m converter em OCTAL.\n'
      '\033[31m[3]\033[m converter em HEXADECIMAL.')
tipo = int(input('Digite a usa oção: '))
cor = {'1': '\033[35m', '2': '\033[m'}
if tipo == 1:
    print('O número {0}{2}{1} em base binária é {0}{3}{1}'.format(cor['1'], cor['2'], n, bin(n)[2:]))
elif tipo == 2:
    print('O número {0}{2}{1} em base octal é {0}{3}{1}'.format(cor['1'], cor['2'], n, oct(n)[2:]))
elif tipo == 3:
    print('O número {0}{2}{1} em base hexadecimal é {0}{3}{1}'.format(cor['1'], cor['2'], n, hex(n)[2:]))
else:
    print('\033[31mDigite uma opção válida.\033[m')
