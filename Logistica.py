# produtos é atribuido um dicionário vázio.
produtos = {}


# função criada para o menu e suas devidas opções.
def menu():
    # variável que foi atribuida o valor 1.
    contador = 1
    # criado um loop para as opções do menu.
    while True:
        # mostra na tela as opções do menu.
        print('Digite a opção que deseja:\n'
              '1 - Cadastrar Peças\n'
              '2 - Consultar Peças\n'
              '3 - Remover Peças\n'
              '4 - Sair')
        # criado um loop dentro do primeiro loop para receber e validar o dado.
        while True:
            # pede ao usuário a opção desejada e verifica se é um número inteiro.
            try:
                answer = int(input())
                # se passar na validação, continua o código.
                break
            # caso de erro de tipo ou valor, mostra que a opção não existe e volta para pedir os dados.
            except(TypeError, ValueError):
                print('Opção inexistente!\n'
                      'Favor digitar uma das opções do menu.')

        # se a resposta for 1, executa a função cadastrarPeca e adiciona 1 no contador.
        if answer == 1:
            cadastrarPeca(contador)
            contador += 1
        # se a resposta for 2, executa a função consultarPeca.
        elif answer == 2:
            consultarPeca()
        # se a reposta for 3, executa a função removerPeca.
        elif answer == 3:
            removerPeca()
        # se a resposta for 4, fecha o programa.
        elif answer == 4:
            break
        # caso não seja nenhuma das opções do menu, mostra que a opção não existe e pede para tentar novamente.
        else:
            print('Opção inexistente!\n'
                  'Favor digitar uma das opções do menu.')


# função criada para cadastrar a peça dentro do dicionário.
def cadastrarPeca(codigo):
    # mostra na tela a opção que foi escolhida e o código que foi atribuido devido ao contador.
    print('Você escolheu a opção cadastrar peça!')
    print('Código atribuido a peça: {}'.format(codigo))
    # pede ao usuário o nome, fabricante e valor da peça.
    nome = input('Qual o nome da peça?')
    fabricante = input('Qual o fabricante?')
    valor = float(input('Qual o valor da peça?'))
    # cria uma chave ao dicionário, atribuindo os devidos valores a outro dicionário.
    produtos[codigo] = {
            'Nome': nome,
            'Fabricante': fabricante,
            'Valor': valor,
        }


# função criada para consultar as peças dentro do dicionário.
def consultarPeca():
    # mostra na tela a opção escolhida.
    print('Você escolheu a opção consultar peça!')
    # criado um loop para as opções dentro do consultar peças.
    while True:
        # mostra na tela as opções.
        print('1 - Consultar todas as peças\n'
              '2 - Consultar peças por código\n'
              '3 - Consultar peças por fabricante\n'
              '4 - Retornar')
        # criado um loop dentro do primeiro loop para receber e validar o dado.
        while True:
            try:
                answer_consulta = int(input(''))
                # se passar na validação, continua o código.
                break
            # caso de erro de tipo ou valor, mostra que a opção não existe e volta para pedir os dados.
            except(ValueError, TypeError):
                print('Opção inexistente!\n'
                      'Favor digitar uma das opções do menu.')
        # se a resposta for 1, mostra todas as peças e o código atribuido nelas.
        if answer_consulta == 1:
            # layout criado para mostrar na tela.
            print('_' * 50)
            print(f'Peças Cadastradas'.center(50))
            # mostra os itens dentro do dicionário produtos.
            for k, v in produtos.items():
                print('Código:', k)
                # mostra na tela as chaves e valores que estão no dicionário.
                for c, j in v.items():
                    print(c, ':', str(j).center(0))
                print('-' * 50)
        # se a resposta for 2, pede ao usuário o código da peça que deseja mostrar na tela.
        elif answer_consulta == 2:
            # solicita ao usuário o código da peça para consultar e verifica se é um inteiro.
            try:
                cod_produto = int(input('Qual o código da peça?'))
                # procura dentro do dicionário o código digitado.
                produto = produtos.get(cod_produto)
                # se for um código existente, estará mostrando tanto o código da peça quanto suas informações.
                if produto:
                    print('-' * 25)
                    for k, v in produto.items():
                        print(k, ':', v)
                    print('-' * 25)
                    break
                # se não for um código existente, avisa o usuário e pede para tentar outro código.
                else:
                    print('Código inexistente!\n'
                          'Favor tentar um código válido.')
            # caso o que for digitado não seja um númerico, avisa o usuário.
            except(ValueError, TypeError):
                print('Código não existente!\n'
                      'Favor tentar novamente.')
        # se a reposta for 3, pede ao usuário o nome do fabricante cadastrado para mostrar na tela.
        elif answer_consulta == 3:
            # variável solicitando ao usuário o fabricante.
            fabricante_produto = input('Qual o fabricante?')
            # direciona as chaves e valores que está dentro do dicionário "produtos".
            for k, v in produtos.items():
                # condição para encontrar o fabricante dentro do dicionário.
                if v.get('Fabricante') == fabricante_produto:
                    # mostra o código da peça.
                    print('-' * 25)
                    print('Código:', k)
                    # dentro do dicionário "produtos", procura as chaves e valores referente ao mesmo.
                    for c, j in v.items():
                        print(c, ':', j)
                    print('-' * 25)
                # se o fabricante não for encontrado, avisa o usuário.
                else:
                    print('Fabricante não encontrado!')
        # se a resposta for 4, encerra o programa.
        elif answer_consulta == 4:
            break


# função criada para remover a peça do dicionário, usando seu código como referência.
def removerPeca():
    # mostra na tela a opção escolhida.
    print('Você escolheu a opção de remover peça!')
    # criado um loop para válidar as informações.
    while True:
        # valida se o código é digitado é um inteiro.
        try:
            # solicita ao usuário o código que deseja remover.
            remover = int(input('Qual código de peça deseja remover?'))
            # caso o código digitado pelo usuário não estiver dentro do dicionário, avisa na tela.
            if remover not in produtos:
                print('Código inexistente!')
            # se o código for existente, deleta o que foi desejado.
            else:
                del produtos[remover]
                print('Peça removida!')
                break
        # caso o código digitado pelo usuário não seja um inteiro, avisa que não existe e pede para tentar novamente.
        except(ValueError, TypeError):
            # mostra na tela que o código é inexistente.
            print('Codigo inexistente!\n'
                  'Favor tentar novamente.')


# mostra na tela a mensagem de bem vindo e minha identificação.
print('Bem vindo ao controle de peças da Bicicletaria do Lucas Gabriel de Moura Santos (RU:3927427)')
# executa a função menu().
menu()
# encerra o programa com a minha identificação
print('Programa encerrando...')
