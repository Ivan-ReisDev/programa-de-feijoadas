valorTotalAcompanhamento = []  # Acumula o valor do acompanhamento para somar no na função final.
# ------------------------- FUNÇÕES --------------------------
# ---------------------- VOLUMEFEIJOADA ---------------------- 
def volumeFeijoada():
    while True:
        try:
            print('Menu volume Feijoada')
            volume = int(input('O volume da porção(em ml): '))
            int(volume)
            if volume > 5000 or volume < 300:  # Verifica se o usuário digitou um valor entre 300 e 5000 ml, caso contrário entra no except.
                print('Não aceitamos porções menores que 300 ml ou maiores que 5l. Tente novamente!')
            else:
                global volumePreco  # transforma variavel em global (funciona em todas as seções).
                volumePreco = volume * 0.08
                break
        except ValueError:
            print('Só pode números')
            continue
# ---------------------- OPÇÃOFEIJOADA -----------------------
def opcaoFeijoada():
    while True:
        print("Entre com as opçôes de feijoada: ")
        print("b - Básica (Feijão + paiol + costelinha)")
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        opcao = str(input('>> '))
        if opcao == 'b' or opcao == 'p' or opcao == 's':  # Verifica se a opção é válida, caso contrário cai no laço de repetição, voltando até que digite uma string válida.
            if opcao == 'b':
                global valorFeijoada
                valorFeijoada = 1
                break
            elif opcao == 'p':
                valorFeijoada = 1.25
                break
            elif opcao == 's':
                valorFeijoada = 1.50
                break
            else:
                print('Você não digitou uma opção válida')
                continue
# ------------------ ACOMPANHAMENTOFEIJOADA ------------------
def acompanhamentoFeijoada():
    while True:
        try:
            print('Deseja mais algum acompanhamento:')
            print('0- Não desejo mais acompanhamentos (encerrar pedido)')
            print('1- 200g de arroz')
            print('2- 150g de farofa especial')
            print('3- 100g de couve cozida')
            print('4- 1 laranja descascada')
            acompanhamento = int(input('>> '))
            int(acompanhamento)
            if acompanhamento == 1:
                valorTotalAcompanhamento.append(
                    5)  # Guarda os valores dentro em uma lista, para no final somar os valores do acompanhamento.
                continue
            elif acompanhamento == 2:
                valorTotalAcompanhamento.append(6)
                continue
            elif acompanhamento == 3:
                valorTotalAcompanhamento.append(7)
                continue
            elif acompanhamento == 4:
                valorTotalAcompanhamento.append(3)
                continue
            elif acompanhamento == 0:
                valorTotalAcmp = sum(valorTotalAcompanhamento)  # Soma os valores dentro da lista acompanhamento
                valorTotal = (
                                         volumePreco * valorFeijoada) + valorTotalAcmp  # calcula o de todos os valores e opções que o usuário respondeu.
                print('O valor a ser pago é R${}'.format(valorTotal))
                break
            else:
                print('Essa opção não existe. Tente novamente!')

        except ValueError:
            print('Digite um valor numérico entre 0 e 4.')
            continue

# --------------------------- MAIN ---------------------------


print('Bem-vindo ao programa de Feijoada do .')

volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()

