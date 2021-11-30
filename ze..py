# Jogo do Zé, o guarda de portaria mais eficiente do mundo. Sem crachá não entra...
#
# Ronaldo Barros von Paraski - Novembro de 2021

# Inicializando variáveis

# Fim da inicialização de variáveis

# Import de módulos necessárias
import os
# Fim de import de módulos

def limpa_tela():
    os.system('cls')

def boas_vindas():

    print("*********************************")
    print("Bem vindo ao jogo do Zé!         ")
    print("*********************************")

    input("Tecle enter para iniciar")

def chegando_portaria():
    print("")
    print("R está chegando ao trabalho e já no guichê inicial do guarda Z percebe que esqueceu o crachá...     ")
    print("W está ali, ao lado de Z, aguardando o pessoal da manutenção chegar para realizar obras no banheiro.")
    print("Como R é recorrente no esquecimento do crachá, ele pensa nas alternativas sobre como fará para      ")
    print("entrar sem o crachá, evitando ter seu dia de trabalho descontado mais uma vez.                      ")

def alternativas_portaria_principal():
    print("")
    print("Ajude R e dê a ele uma oportunidade de não ser descontado no dia de hoje...:")
    print("")
    print("1 - R disfarça tentando impedir a visão de Z quanto ao uso do crachá")
    print("2 - R Distrai Z contando uma piada e tenta passar enquanto ele ri sem que perceba a ausência do crachá")
    print("3 - W alerta Z que viu R fechando o casaco e que há algo estranho, pois não está frio")
    print("")
    escolha = input("Escolha uma das opções acima e decida o futuro próximo de R ? ")

    escolha_opt = int(escolha)

    if(escolha_opt < 1 or escolha_opt > 3):
        print("Você deve digitar um número entre 1 e 3 !")
        input("Tecle enter para encerrar o jogo.")
        os._exit(0)
    else:
        if(escolha_opt == 1 or escolha_opt == 3):
            print("")
            print("A ausência do seu crachá foi percebida. Você não trabalhará hoje !")
            print("")
            input("Tecle enter para voltar para casa.")
            limpa_tela()
            os._exit(0)
        else:
            if(escolha_opt == 2):
                limpa_tela()
                print("Muito bem, você conseguiu avançar e chegou ao bebedouro")
                print("Agora você está mais próximo de chegar ao CPD")
                input("Tecle enter para ir adiante !")
                limpa_tela()
                print("R passou por Z e conseguiu avançar até o bebedouro.")

def parada_no_bebedouro():
    print("Como de costume, diariamente antes de iniciar o trabalho, R para no bebedouro")
    print("que fica próximo à entrada do banheiro para beber água. ")
    print("Neste momento, Z sai repentinamente do banheiro.")
    print("")
    print("1 - R entra no banheiro ao lado do bebedouro visando dar uma chicane em Z")
    print("2 - W aparece e chama Z para ver problemas de vazamento no banheiro")
    print("3 - Z vem saindo do banheiro e observa atentamente R")
    print("")
    escolha = input("Escolha uma das opções acima e decida o futuro próximo de R ? ")

    escolha_opt = int(escolha)

    if(escolha_opt < 1 or escolha_opt > 3 and True):
        print("Você deve digitar um número entre 1 e 3 !")
    else:
        if(escolha_opt == 1 or escolha_opt == 3):
            print("")
            print("A ausência do seu crachá foi percebida. Você não trabalhará hoje !")
            print("")
            input("Tecle enter para voltar para casa.")
            os._exit(0)
        else:
            if(escolha_opt == 2):
                print("R passou por Z e agora dirige-se à etapa final, rumo ao CPD.")

def acessa_cpd():
    print("Finalmente, após beber água, R dirigi-se ao CPD para acessar")
    print(" a sala dos servidores e iniciar mais um dia de trabalho  ")
    print("")
    print("1 - R dirige-se à entrada do CPD")
    print("2 - R passa por W e inicia conversa sobre a obra no banheiro")
    print("3 - Z esqueceu sua necessaire no banheiro e volta pra pega-la")
    print("")
    escolha = input("Escolha uma das opções acima e decida o futuro próximo de R ? ")

    escolha_opt = int(escolha)

    if(escolha_opt < 1 or escolha_opt > 3 and True):
        print("Você deve digitar um número entre 1 e 3 !")
    else:
        if(escolha_opt == 1 or escolha_opt == 2):
            print("")
            print("A ausência do seu crachá foi percebida. Você não trabalhará hoje !")
            print("")
            input("Tecle enter para voltar para casa.")
            os._exit(0)
        else:
            if(escolha_opt == 3):
                print("R passou por Z e agora dirige-se à etapa final, rumo ao CPD.")

if(__name__ == "__main__"):
    limpa_tela()
    boas_vindas()
    limpa_tela()
    chegando_portaria()
    limpa_tela()
    alternativas_portaria_principal()
    limpa_tela()
    parada_no_bebedouro()
    limpa_tela()
    acessa_cpd()
