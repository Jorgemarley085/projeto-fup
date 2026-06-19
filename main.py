from Funcoes.funcoes import *
opcao = -1
transactions = loadTransactions()
#aqui estou carregando o que ja estava no arquivo para lista de transaçoes

while opcao!=0:
    print('''
----------------MENU----------------
          1- Adcionar
          2- Buscar
          3- Listar
          4- Atualizar
          5- Remover
          6- Total em Despesas
          7- Total em Receitas
          8- Saldo
          9 -Salvar Transações

          0- SAIR
-----------------------------------          

''')
    
    try:
        opcao=int(input("escolha uma opçao: "))
        if opcao==1:
            addTransaction(transactions)
        elif opcao==2:
            print("Buscar") 
            entrada = int(input("insira o ID "))
            find = findTransaction(entrada,transactions)
            if find:
                print("esse id esta no sistema") 
            else:
                print("esse id nao esta no sistema")    
        elif opcao==3:
            print(showTransactions(transactions))
        elif opcao==4:
            print('atualizar')
            entrada = int(input("insira ID da transaçao que deseja atualizar "))
            upgradeTransactions(entrada,transactions)

        elif opcao==5:
            entrada = int(input("insira o id da transação que deseja remover: "))
            removeTransaction(entrada,transactions)
        elif opcao==6:
    
            despesa = total_expense(transactions)   
            print("o total em despesa é {}".format(despesa)) 
        elif opcao==7:
            receita = total_income(transactions)
            print("o total em receita é :{}".format(receita))

        elif opcao==8:
            print("saldo total é ")
            balance = total_income(transactions)-total_expense(transactions)
            print(round(balance))
            if balance<0:
                print('voce esta negativado')
            else:
                print("voce esta positivo")    
        elif opcao==9:
            saveTransactions(transactions)
    # nao era mais necessario pedir para usuario carregar a lista e sim ja esta carregada ao iniciar o programa
    #  elif opcao==7:
        # loadTransactions()
    except ValueError:
        print("insira um NUMERO no intervalo de 1 a 6 e para sair 0")    
