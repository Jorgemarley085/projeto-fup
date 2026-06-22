import json

from datetime import datetime

agora = datetime.now()
#transformar datetime.now em string para salvar no arquivo json
convert = str(agora)

#aqui estou adicionando uma transação e como parametro estou passando a lista de transações
def addTransaction(transactions):
    #para usuario nao colocar id repetidos resolvi deixar id incrementado 
    # onde verifico se a lista esta vazia se vazia o id recebe  1 se nao tiver
    #ai pego o ultimo id atraves do ultimo indice [-1] e adiciono mais 1
    if not transactions:
        novo_id=1
        # description = input("insira a descrição: ")
        # value = float(input("insira o valor da transação:  "))
        # category = input("insira a categoria :  ")
        # date = int(input("insira a Data: "))
        # transaction= {'id':id,'description':description,'value':value,'category':category,'date':date}
        # transactions.append(transaction)
        #estava repetindo codigo
    else:
        ultimo_id = transactions[-1]['id']
        novo_id= ultimo_id+1
    try:     
        description = input("insira a descrição: ")
        while True:
            #laço para verificar o valor 
            value = float(input("insira o valor da transação:  "))
            if value<=0:
                print('insira um valor maior que zero')
            else:
                break   
             
        
        transaction_type=""

        while True:
            #aqui decidi deixar que usuario so selecione e nao digite o tipo da transação assim verificando se a entrada ou é 1 ou 2
            first_type = int(input("INSIRA SE É RECEITA DIGITE-> 1 SE DESPESA DIGITE ->2::    "))
            if first_type==1:
                transaction_type= "receita"
                break
    
                
            elif first_type==2:
                transaction_type="despesa"
                break
            #caso usuario insira outro valor o laço nao ira parar
            print("opção invalida digite 1 ou 2")


        caterogy = ""
        while True:
            #outro while True para verificar a entrada obrigando o usuario escolher somente as opções do menu
            print('''
                  
     -----------CATEGORIA ---------------
                  
                Alimentação (1)
                Transporte  (2)
                Moradia     (3)
                Lazer       (4)
                Saúde       (5)
                Educação    (6)
                Salário     (7)
                Investimento (8)
                Outros      (9)
    --------------------------------------------
    
            ''') 
            entrada = int(input("escolha uma opçao: "))
            if entrada <=0 or entrada>9:
                print("digite uma opção valida")  
            #aqui verifica caso if nao seja atingido cai no else    
            else:
                if entrada == 1:
                    caterogy="Alimentação"
                    break 
                if  entrada == 2:
                    caterogy="Transporte"
                    break 
                if entrada ==3:
                    caterogy="Moradia"
                    break 
                if entrada ==4:
                    caterogy="ALazer"
                    break 
                if entrada ==5:
                    caterogy="Saúde"
                    break 

                if entrada ==6:
                    caterogy="Educação"
                    break 
                if entrada ==7:
                    caterogy="Salário"
                    break 
                if entrada ==8:
                    caterogy="Investimento"
                    break 
                if entrada ==9:
                    caterogy="Outros"  
                    break       
                     
        #ja fora dos laços pegamos so os valores e colocamos no dicionario 
       # if transaction_type=="receita" or transaction_type=="despesa":
        transaction= {'id':novo_id,'description':description,'value':value,'type':transaction_type,'category':caterogy,'date':convert}
        transactions.append(transaction) 
       # else:
        #        print("tipo vazia!!")   ---> esse if e else resolvi tirar por serem redudantes   ja que se usuario nao inserir as opções para tipo
        #           o programa para e volta para menu incial solicitando que usuario digite a opção correta so entra no execept caso usuario  insira uma string se inserir inteiro o laço segura
    except ValueError:
        print("insira o valor  corretamente")      


#aqui calculo o total das despesas atraves do for acessando chave valor e somando "value" na variavel tot_despesa
def total_expense(transactions):
    tot_despesa=0
    for transaction in transactions: # aqui eu pego cada tipo despesa e adiciono o valor ao tot_despesa
        if transaction["type"] =="despesa":
            tot_despesa+=transaction['value']
         
    return tot_despesa        

def total_income(transactions):
    tot_receita=0
    for transaction in transactions:  # aqui eu pego cada categoria receita e adiciono o valor ao tot_receita
        if transaction["type"] =="receita":
            tot_receita+=transaction['value']
            
    return tot_receita  

#aqui procuro a transação pelo id 
def findTransaction(entrada,transactions):
    
    for i in range(len(transactions)):
        if entrada == transactions[i]['id']:# se a entrada for igual o valor do id
            
            return True
            # print("o id-> {} esta na lista de transações".format(entrada))
            # print("categoria:{}".format(transactions[i]['category']) )
            # print("descrição:{} ".format(transactions[i]['description']))
            # resultado = True
            # break
            
    return False
#aqui retorono todas as transaçoes inseridas para que usuario veja detalhes nos quais possa querer alterar
def showTransactions(transactions):
    for transaction in transactions:
        print("---"*20)
        print("id:{}".format(transaction['id']))
        print("description:{}".format(transaction['description']))
        print("value:{}".format(transaction['value']))
        print("type: {}".format(transaction['type']))
        print("category:{}".format(transaction['category']))
        print("date: {}".format(transaction['date']))
        print("---"*20)
#aqui removo a transação usando tambem a função de procurar id, se id achado, excluo o indice onde esta toda a transação
def removeTransaction(entrada,transactions):
    verication = findTransaction(entrada,transactions)
    if verication:
        for i in range(len(transactions)):
            if entrada ==transactions[i]['id']:
                transactions.remove(transactions[i])
                #transaction.remove(entrada)
                print("REMOÇÂO CONCLUIDA")
                break
    else:
        print("ID nao encontrado ")        
#aqui atualizo a transação pelo id lido e validado pela função findTransactions
#se validado pergunto o que usuario ira atualizar, utilizo a mesma logica  da função de adicionar transaçao, com uma diferença que atualizo somente um campo 
def upgradeTransactions(entrada,transactions):
    find  = findTransaction(entrada,transactions)
    if find:
        try:
            option = int(input("Deseja alterar valor digite ->(1) ou o tipo de transação digite->(2) ou alterar categoria digite ->(3) : "))
            for i in range(len(transactions)):
                if entrada ==transactions[i]['id']:
                    if option ==1:
                            transactions[i]['value'] = float(input("coloque o valor novo: "))
                            break
                    elif option==2:
                        #aqui aproveitei o codigo da função adicionar transação
                            transaction_type=""

                            while True:

                                    first_type = int(input("INSIRA SE É RECEITA DIGITE-> 1 SE DESPESA DIGITE ->2::    "))
                                    if first_type==1:
                                        transaction_type= "receita"
                                        transactions[i]['type'] = transaction_type
                                        print("atualização concluida!!")
                                        break
                            
                                        
                                    elif first_type==2:
                                        transaction_type="despesa"
                                        transactions[i]['type'] = transaction_type
                                        print("atualização concluida!!")
                                        
                                        break
                                    print("opção invalida digite 1 ou 2")
                    elif option==3:
                                caterogy = ""
                                while True:
                                    print('''
                                        
                            -----------CATEGORIA ---------------
                                        
                                        Alimentação (1)
                                        Transporte  (2)
                                        Moradia     (3)
                                        Lazer       (4)
                                        Saúde       (5)
                                        Educação    (6)
                                        Salário     (7)
                                        Investimento (8)
                                        Outros      (9)
                            --------------------------------------------
                            
                                    ''') 
                                    entrada2 = int(input("escolha uma opçao: "))
                                    if entrada2 <=0 or entrada2>9:
                                        print("digite uma opção valida")  
                                    else:
                                        if entrada2 == 1:
                                            caterogy="Alimentação"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif  entrada2 == 2:
                                            caterogy="Transporte"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==3:
                                            caterogy="Moradia"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==4:
                                            caterogy="Lazer"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==5:
                                            caterogy="Saúde"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 

                                        elif entrada2 ==6:
                                            caterogy="Educação"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==7:
                                            caterogy="Salário"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==8:
                                            caterogy="Investimento"
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 
                                        elif entrada2 ==9:
                                            caterogy="Outros"  
                                            transactions[i]['category'] = caterogy
                                            print("atualização concluida!!")
                                            break 

                                  
                                            
        except ValueError:
            print("insira  1 ou 2 ou 3")            
    else:
        print("nao encontrado")    

        
#aqui estou salvando as transações feitas pelo usuario 
def saveTransactions(transactions):
    print("salvando")
    send = open('transacoes.json', 'w',encoding='utf-8') 
    dados = json.dumps(transactions, indent=2)#transformo a lista com os dicionarios em json
    #indent usado para deixar o formato do json mais bonito
    send.write(dados)
    send.close()
    print(dados)

#aqui essa função esta carregando o arquivo transacoes.json,primiero tentando abrir o arquivo e fecha-lo e retornando o que foi lido e armazena na transactions
#se o arquivo estiver vazio ele retorna uma lista vazia

def loadTransactions():
    try:
        load = open('transacoes.json','r')
        read = json.load(load)
        load.close()
        
        return read
    except FileNotFoundError:
        return []

    # for transacoes in read:
    #     print("""A descrição: {}\n A categoria: {}
    #           """.format(transacoes["description"],transacoes["category"]))
   