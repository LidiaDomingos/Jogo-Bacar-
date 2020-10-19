# EP - Design de Software
# Equipe: Lídia Alves Chagas Domingos
# Data: 18/10/2020

'''
#O jogo com um baralho de 52 cartas e somente um jogador, sem regras avançadas!
import random
baralho = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
quantidade_de_fichas = 100
print('Olá, você começa o jogo com 100 fichas! Para sua primeira aposta, digite um valor entre 0 e 100!')
jogando = True
while jogando:
    
    if quantidade_de_fichas <= 0:
        print('Você não tem mais fichas para apostar!:C')
        print('Obrigada por jogar! Volte sempre! :D')
        break
       
    aposta = int(input('Qual a quantidade de fichas que você aposta?: '))
    
    if aposta == 0:
        print('Obrigada por jogar! Volte sempre! :D')
        break

    if quantidade_de_fichas > 0:
        pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')
        while pergunta_ganhador != 'j' and pergunta_ganhador != 'b' and pergunta_ganhador != 'e':
                print('Essa não é uma aposta válida! Por favor, digite j, b ou e para prosseguir o jogo! :)')
                pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')

        #carta um do jogador
        sorteado1 = random.randint(0,51)
        if baralho[sorteado1] == 'A':
            carta_jogador_1 = 1
        elif baralho[sorteado1] == 'J':
            carta_jogador_1 = 0
        elif baralho[sorteado1] == 'Q':
            carta_jogador_1 = 0
        elif baralho[sorteado1] == 'K':
            carta_jogador_1 = 0
        elif baralho[sorteado1] == 10:
            carta_jogador_1 = 0
        else: 
            carta_jogador_1 = baralho[sorteado1]
        #carta dois do jogador
        sorteado2 = random.randint(0,51)
        if baralho[sorteado2] == 'A':
            carta_jogador_2 = 1
        elif baralho[sorteado2] == 'J':
            carta_jogador_2 = 0
        elif baralho[sorteado2] == 'Q':
            carta_jogador_2 = 0
        elif baralho[sorteado2] == 'K':
            carta_jogador_2 = 0
        elif baralho[sorteado2] == 10:
            carta_jogador_2 = 0
        else:
            carta_jogador_2 = baralho[sorteado2]

        #soma das cartas 1 e 2 do jogador
        soma_jogador = carta_jogador_1 + carta_jogador_2

        #carta um do banco
        sorteado3 = random.randint(0,51)
        if baralho[sorteado3] == 'A':
            carta_banco_1 = 1
        elif baralho[sorteado3] == 'J':
            carta_banco_1 = 0
        elif baralho[sorteado3] == 'Q':
            carta_banco_1 = 0
        elif baralho[sorteado3] == 'K':
            carta_banco_1 = 0
        elif baralho[sorteado3] == 10:
            carta_banco_1 = 0
        else:
            carta_banco_1 = baralho[sorteado3]

        #carta dois do banco
        sorteado4 = random.randint(0,51)
        if baralho[sorteado4] == 'A':
            carta_banco_2 = 1
        elif baralho[sorteado4] == 'J':
            carta_banco_2 = 0
        elif baralho[sorteado4] == 'Q':
            carta_banco_2 = 0
        elif baralho[sorteado4] == 'K':
            carta_banco_2 = 0
        elif baralho[sorteado4] == 10:
            carta_banco_2 = 0
        else: 
            carta_banco_2 = baralho[sorteado4]

        #soma das cartas dos banco
        soma_banco = carta_banco_1 + carta_banco_2

        if soma_banco >= 10:
            soma_banco = soma_banco % 10    
        
        if soma_jogador >= 10:
            soma_jogador = soma_jogador % 10 

        print('A soma das cartas do jogador é {0} e do banco é {1}. Se a soma de uma for menor do que 5 e a outra menor que 8, o que tive menor soma recebe mais uma carta!'.format(soma_jogador, soma_banco))

        #condições

        if soma_jogador <= 5 and soma_banco < 8:
            sorteado5 = random.randint(0,51)
            carta_jogador_3 = baralho[sorteado5]
            if baralho[sorteado5] == 'A':
                carta_jogador_3 = 1
            elif baralho[sorteado5] == 'J':
                carta_jogador_3 = 0
            elif baralho[sorteado5] == 'Q':
                carta_jogador_3 = 0
            elif baralho[sorteado5] == 'K':
                carta_jogador_3 = 0
            elif baralho[sorteado5] == 10:
                carta_jogador_3 = 0
            soma_jogador = carta_jogador_1 + carta_jogador_2 + carta_jogador_3
        
        if soma_banco <= 5 and soma_jogador < 8:
            sorteado6 = random.randint(0,51)
            carta_banco_3 = baralho[sorteado6]
            if baralho[sorteado6] == 'A':
                carta_banco_3 = 1
            elif baralho[sorteado6] == 'J':
                carta_banco_3 = 0
            elif baralho[sorteado6] == 'Q':
                carta_banco_3 = 0
            elif baralho[sorteado6] == 'K':
                carta_banco_3 = 0
            elif baralho[sorteado6] == 10:
                carta_banco_3 = 0
            soma_banco = carta_banco_1 + carta_banco_2 + carta_banco_3

        if soma_banco >= 10:
            soma_banco = soma_banco % 10    
        
        if soma_jogador >= 10:
            soma_jogador = soma_jogador % 10  

        print('A soma das cartas do jogador deu {0}'.format(soma_jogador))
        print('A soma das cartas do banco deu {0}'.format(soma_banco))
        
        if soma_jogador > soma_banco:
            if pergunta_ganhador == 'j':
                quantidade_de_fichas += aposta
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            else:
                quantidade_de_fichas -= aposta
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
        if soma_jogador < soma_banco:
            if pergunta_ganhador == 'b':
                quantidade_de_fichas = quantidade_de_fichas + int(aposta*0.95)
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            else:
                quantidade_de_fichas -= aposta
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
        if soma_jogador == soma_banco:
            if pergunta_ganhador == 'e':
                quantidade_de_fichas += aposta*8
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            else:
                quantidade_de_fichas -= aposta
                print('Você tem {0} fichas!'.format(quantidade_de_fichas))
'''
#O jogo com 1, 6 ou 8 baralhos.
import random

quantidade_de_fichas = 100
print('Olá, você começa o jogo com 100 fichas! Para sua primeira aposta, digite um valor entre 0 e 100!')
pergunta_quantidade_baralho = int(input('Com quantos baralhos você deseja jogar?[1, 6 ou 8?]: '))
baralho = pergunta_quantidade_baralho*['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
comissão = 0 
jogando = True
while jogando:
    #com um baralho
    if pergunta_quantidade_baralho == 1:
        baralho = pergunta_quantidade_baralho*['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        if quantidade_de_fichas <= 0:
            print('Você não tem mais fichas para apostar!:C')
            print('Obrigada por jogar! Volte sempre! :D')
            break

        aposta = int(input('Qual a quantidade de fichas que você aposta?: '))
        while aposta > quantidade_de_fichas or aposta < 0:
            print('Este valor não é aceitável! Por favor, aposte de 0 até a quantidade de fichas que você possui!')
            aposta = int(input('Qual a quantidade de fichas que você aposta?: '))

        if aposta == 0:
            print('Volte sempre! :D')
            print('Obrigada por jogar! Volte sempre! :D')
            break
        if quantidade_de_fichas > 0:
            pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')
            while pergunta_ganhador != 'j' and pergunta_ganhador != 'b' and pergunta_ganhador != 'e':
                print('Essa não é uma aposta válida! Por favor, digite j, b ou e para prosseguir o jogo! :)')
                pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')

            #carta um do jogador
            sorteado1 = random.randint(0, 51)
            if baralho[sorteado1] == 'A':
                carta_jogador_1 = 1
            elif baralho[sorteado1] == 'J':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'Q':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'K':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 10:
                carta_jogador_1 = 0
            else: 
                carta_jogador_1 = baralho[sorteado1]
            #carta dois do jogador
            sorteado2 = random.randint(0,51)
            if baralho[sorteado2] == 'A':
                carta_jogador_2 = 1
            elif baralho[sorteado2] == 'J':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'Q':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'K':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 10:
                carta_jogador_2 = 0
            else:
                carta_jogador_2 = baralho[sorteado2]

            #soma das cartas 1 e 2 do jogador
            soma_jogador = carta_jogador_1 + carta_jogador_2

            #carta um do banco
            sorteado3 = random.randint(0,51)
            if baralho[sorteado3] == 'A':
                carta_banco_1 = 1
            elif baralho[sorteado3] == 'J':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'Q':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'K':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 10:
                carta_banco_1 = 0
            else:
                carta_banco_1 = baralho[sorteado3]

            #carta dois do banco
            sorteado4 = random.randint(0,51)
            if baralho[sorteado4] == 'A':
                carta_banco_2 = 1
            elif baralho[sorteado4] == 'J':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'Q':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'K':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 10:
                carta_banco_2 = 0
            else: 
                carta_banco_2 = baralho[sorteado4]

            #soma das cartas dos banco
            soma_banco = carta_banco_1 + carta_banco_2

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10 

            print('A soma das cartas do jogador é {0} e do banco é {1}. Se a soma de uma for menor do que 5 e a outra menor que 8, o que tive menor soma recebe mais uma carta!'.format(soma_jogador, soma_banco))   
            #condições
            if soma_jogador <= 5 and soma_banco < 8:
                sorteado5 = random.randint(0,51)
                carta_jogador_3 = baralho[sorteado5]
                if baralho[sorteado5] == 'A':
                    carta_jogador_3 = 1
                elif baralho[sorteado5] == 'J':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'Q':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'K':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 10:
                    carta_jogador_3 = 0
                soma_jogador = carta_jogador_1 + carta_jogador_2 + carta_jogador_3
            
            if soma_banco <= 5 and soma_jogador < 8:
                sorteado6 = random.randint(0,51)
                carta_banco_3 = baralho[sorteado6]
                if baralho[sorteado6] == 'A':
                    carta_banco_3 = 1
                elif baralho[sorteado6] == 'J':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'Q':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'K':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 10:
                    carta_banco_3 = 0
                soma_banco = carta_banco_1 + carta_banco_2 + carta_banco_3

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10  

            print('A soma das cartas do jogador deu {0}'.format(soma_jogador))
            print('A soma das cartas do banco deu {0}'.format(soma_banco))
            
            if soma_jogador > soma_banco:
                if pergunta_ganhador == 'j':
                    quantidade_de_fichas = quantidade_de_fichas + aposta - int(0.0129*aposta)
                    comissão += int(0.0129*aposta)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador < soma_banco:
                if pergunta_ganhador == 'b':
                    quantidade_de_fichas = quantidade_de_fichas + int(aposta*0.95) - int(0.0101*(int(aposta*0.95)))
                    comissão += int(0.0101*(int(aposta*0.95)))
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador == soma_banco:
                if pergunta_ganhador == 'e':
                    quantidade_de_fichas = quantidade_de_fichas + aposta*8 - int(0.1575*aposta*8)
                    comissão += int(0.1575*aposta*8)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
    
    #com 6 baralhos.
    if pergunta_quantidade_baralho == 6:
        baralho = pergunta_quantidade_baralho*['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        if quantidade_de_fichas <= 0:
            print('Você não tem mais fichas para apostar!:C')
            print('Obrigada por jogar! Volte sempre! :D')
            break

        aposta = int(input('Qual a quantidade de fichas que você aposta?: '))
        while aposta > quantidade_de_fichas or aposta < 0:
            print('Este valor não é aceitável! Por favor, aposte de 0 até a quantidade de fichas que você possui!')
            aposta = int(input('Qual a quantidade de fichas que você aposta?: '))
        
        if aposta == 0:
            print('Obrigada por jogar! Volte sempre! :D')
            break

        if quantidade_de_fichas > 0:
            pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')
            while pergunta_ganhador != 'j' and pergunta_ganhador != 'b' and pergunta_ganhador != 'e':
                print('Essa não é uma aposta válida! Por favor, digite j, b ou e para prosseguir o jogo! :)')
                pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')

            #carta um do jogador
            sorteado1 = random.randint(0, 311)
            if baralho[sorteado1] == 'A':
                carta_jogador_1 = 1
            elif baralho[sorteado1] == 'J':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'Q':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'K':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 10:
                carta_jogador_1 = 0
            else: 
                carta_jogador_1 = baralho[sorteado1]
            #carta dois do jogador
            sorteado2 = random.randint(0,311)
            if baralho[sorteado2] == 'A':
                carta_jogador_2 = 1
            elif baralho[sorteado2] == 'J':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'Q':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'K':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 10:
                carta_jogador_2 = 0
            else:
                carta_jogador_2 = baralho[sorteado2]

            #soma das cartas 1 e 2 do jogador
            soma_jogador = carta_jogador_1 + carta_jogador_2

            #carta um do banco
            sorteado3 = random.randint(0,311)
            if baralho[sorteado3] == 'A':
                carta_banco_1 = 1
            elif baralho[sorteado3] == 'J':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'Q':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'K':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 10:
                carta_banco_1 = 0
            else:
                carta_banco_1 = baralho[sorteado3]

            #carta dois do banco
            sorteado4 = random.randint(0,311)
            if baralho[sorteado4] == 'A':
                carta_banco_2 = 1
            elif baralho[sorteado4] == 'J':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'Q':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'K':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 10:
                carta_banco_2 = 0
            else: 
                carta_banco_2 = baralho[sorteado4]

            #soma das cartas dos banco
            soma_banco = carta_banco_1 + carta_banco_2

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10 
                
            print('A soma das cartas do jogador é {0} e do banco é {1}. Se a soma de uma for menor do que 5 e a outra menor que 8, o que tive menor soma recebe mais uma carta!'.format(soma_jogador, soma_banco))
            #condições
            if soma_jogador <= 5 and soma_banco < 8:
                sorteado5 = random.randint(0,311)
                carta_jogador_3 = baralho[sorteado5]
                if baralho[sorteado5] == 'A':
                    carta_jogador_3 = 1
                elif baralho[sorteado5] == 'J':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'Q':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'K':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 10:
                    carta_jogador_3 = 0
                soma_jogador = carta_jogador_1 + carta_jogador_2 + carta_jogador_3
            
            if soma_banco <= 5 and soma_jogador < 8:
                sorteado6 = random.randint(0,311)
                carta_banco_3 = baralho[sorteado6]
                if baralho[sorteado6] == 'A':
                    carta_banco_3 = 1
                elif baralho[sorteado6] == 'J':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'Q':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'K':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 10:
                    carta_banco_3 = 0
                soma_banco = carta_banco_1 + carta_banco_2 + carta_banco_3

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10  

            print('A soma das cartas do jogador deu {0}'.format(soma_jogador))
            print('A soma das cartas do banco deu {0}'.format(soma_banco))
            
            if soma_jogador > soma_banco:
                if pergunta_ganhador == 'j':
                    quantidade_de_fichas = quantidade_de_fichas + aposta - int(0.0124*aposta)
                    comissão += int(0.0124*aposta)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador < soma_banco:
                if pergunta_ganhador == 'b':
                    quantidade_de_fichas = quantidade_de_fichas + int(aposta*0.95) - int(0.0106*(int(aposta*0.95)))
                    comissão += int(0.0106*(int(aposta*0.95)))
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador == soma_banco:
                if pergunta_ganhador == 'e':
                    quantidade_de_fichas = quantidade_de_fichas + aposta*8 - int(0.1444*aposta*8)
                    comissão += int(0.1444*aposta*8)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
    
    #com 8 baralhos.
    if pergunta_quantidade_baralho == 8:
        baralho = pergunta_quantidade_baralho*['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        if quantidade_de_fichas <= 0:
            print('Você não tem mais fichas para apostar!:C')
            print('Obrigada por jogar! Volte sempre! :D')
            break

        aposta = int(input('Qual a quantidade de fichas que você aposta?: '))
        while aposta > quantidade_de_fichas or aposta < 0:
            print('Este valor não é aceitável! Por favor, aposte de 0 até a quantidade de fichas que você possui!')
            aposta = int(input('Qual a quantidade de fichas que você aposta?: '))

        if aposta == 0:
            print('Obrigada por jogar! Volte sempre! :D')
            break
        if quantidade_de_fichas > 0:
            pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')
            while pergunta_ganhador != 'j' and pergunta_ganhador != 'b' and pergunta_ganhador != 'e':
                print('Essa não é uma aposta válida! Por favor, digite j, b ou e para prosseguir o jogo! :)')
                pergunta_ganhador = input('Quem você acha que ganha?[j,b,e]: ')

            #carta um do jogador
            sorteado1 = random.randint(0, 415)
            if baralho[sorteado1] == 'A':
                carta_jogador_1 = 1
            elif baralho[sorteado1] == 'J':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'Q':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 'K':
                carta_jogador_1 = 0
            elif baralho[sorteado1] == 10:
                carta_jogador_1 = 0
            else: 
                carta_jogador_1 = baralho[sorteado1]
            #carta dois do jogador
            sorteado2 = random.randint(0,415)
            if baralho[sorteado2] == 'A':
                carta_jogador_2 = 1
            elif baralho[sorteado2] == 'J':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'Q':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 'K':
                carta_jogador_2 = 0
            elif baralho[sorteado2] == 10:
                carta_jogador_2 = 0
            else:
                carta_jogador_2 = baralho[sorteado2]

            #soma das cartas 1 e 2 do jogador
            soma_jogador = carta_jogador_1 + carta_jogador_2

            #carta um do banco
            sorteado3 = random.randint(0,415)
            if baralho[sorteado3] == 'A':
                carta_banco_1 = 1
            elif baralho[sorteado3] == 'J':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'Q':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 'K':
                carta_banco_1 = 0
            elif baralho[sorteado3] == 10:
                carta_banco_1 = 0
            else:
                carta_banco_1 = baralho[sorteado3]

            #carta dois do banco
            sorteado4 = random.randint(0,415)
            if baralho[sorteado4] == 'A':
                carta_banco_2 = 1
            elif baralho[sorteado4] == 'J':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'Q':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 'K':
                carta_banco_2 = 0
            elif baralho[sorteado4] == 10:
                carta_banco_2 = 0
            else: 
                carta_banco_2 = baralho[sorteado4]

            #soma das cartas dos banco
            soma_banco = carta_banco_1 + carta_banco_2

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10 
            print('A soma das cartas do jogador é {0} e do banco é {1}. Se a soma de uma for menor do que 5 e a outra menor que 8, o que tive menor soma recebe mais uma carta!'.format(soma_jogador, soma_banco))  
            #condições
            if soma_jogador <= 5 and soma_banco < 8:
                sorteado5 = random.randint(0,415)
                carta_jogador_3 = baralho[sorteado5]
                if baralho[sorteado5] == 'A':
                    carta_jogador_3 = 1
                elif baralho[sorteado5] == 'J':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'Q':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 'K':
                    carta_jogador_3 = 0
                elif baralho[sorteado5] == 10:
                    carta_jogador_3 = 0
                soma_jogador = carta_jogador_1 + carta_jogador_2 + carta_jogador_3
            
            if soma_banco <= 5 and soma_jogador < 8:
                sorteado6 = random.randint(0,415)
                carta_banco_3 = baralho[sorteado6]
                if baralho[sorteado6] == 'A':
                    carta_banco_3 = 1
                elif baralho[sorteado6] == 'J':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'Q':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 'K':
                    carta_banco_3 = 0
                elif baralho[sorteado6] == 10:
                    carta_banco_3 = 0
                soma_banco = carta_banco_1 + carta_banco_2 + carta_banco_3

            if soma_banco >= 10:
                soma_banco = soma_banco % 10    
            
            if soma_jogador >= 10:
                soma_jogador = soma_jogador % 10  

            print('A soma das cartas final do jogador deu {0}'.format(soma_jogador))
            print('A soma das cartas final do banco deu {0}'.format(soma_banco))
            
            if soma_jogador > soma_banco:
                if pergunta_ganhador == 'j':
                    quantidade_de_fichas = quantidade_de_fichas + aposta - int(0.0124*aposta)
                    comissão += int(0.0124*aposta)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador < soma_banco:
                if pergunta_ganhador == 'b':
                    quantidade_de_fichas = quantidade_de_fichas + int(aposta*0.95) - int(0.0106*(int(aposta*0.95)))
                    comissão += int(0.0106*(int(aposta*0.95)))
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
            if soma_jogador == soma_banco:
                if pergunta_ganhador == 'e':
                    quantidade_de_fichas = quantidade_de_fichas + aposta*8 - int(0.1436*aposta*8)
                    comissão += int(0.1436*aposta*8)
                    print('A comissão dada a casa é de {0} fichas até agora!'.format(comissão))
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))
                else:
                    quantidade_de_fichas -= aposta
                    print('Você tem {0} fichas!'.format(quantidade_de_fichas))

    if pergunta_quantidade_baralho != 1 and pergunta_quantidade_baralho != 6 and pergunta_quantidade_baralho != 8:
        print('Não é possível jogar com essa quantidade de baralhos! Por favor, digite 1, 6 ou 8!')
        pergunta_quantidade_baralho = int(input('Com quantos baralhos você deseja jogar?[1, 6 ou 8?]: '))

