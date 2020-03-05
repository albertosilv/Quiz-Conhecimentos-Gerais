from tkinter import *#importa a biblioteca tkinter
from random import randint
import os.path
contador=0#Contadora para indice do ftempo da função sair
contador1=0#Contadora para o indice do fquestao da função sair
quest=[]#Lista que recebe a ordem as questões
t=0#Variavel que recebera a numeração refere ao começar, instrução ou recordes do jogo
m=0#Variavel contadora das questões
sec=0#Variavel dos segundos
numero=0
vetor=[0]*10
n=0#Variavel que recebe o \n que sera removido da lista num
ftempo=[]#vetor para receber o tempo em que o usuario respondeu N questoes
fquestao=[]#vetor que recebe a quantidade de questões
#Variavel que contrubuira para organização do ftempo e fquestao
a=0
b=0
c=0
d=0
#Zeramento da lista quest e atribuição de numeros entre 1 e 50 não repetidos
#a lista quest
def arquivos ():
     #Leitura do arquivo recordes.txt
     arquivo=open('recordes.txt','r+')
     #Atribuição dos dados do recordes.txt para a lista num
     num=arquivo.readlines()         
     n='\n'
     #Retirada das strings \n da lista num
     for x in range(0,10):
      for i in range(0,len(n)):
        num[x]=num[x].replace(n[i],'')
     #Atribuido os valores da lista num para uma lista de inteiros chamada vetor
     for x in range(0,10):
      t=int(num[x])
      vetor[x]=t
     for x in range(0,10):
        if x%2==0:
            ftempo.append(vetor[x])
        else:
            fquestao.append(vetor[x])
#Atribuiçao dos valores aleatorios não repetidos para a lista quest
def numeracao():
    quest.clear()
    while len(quest)<50:
          numero=randint(1,50)
          if numero not in quest:
                quest.append(numero)
#Criação do arquivo recordes.txt ou abertura dele
def cria_arquivo():
 if os.path.exists('recordes.txt'):#Teste para saber se o arquivo existe
    #Abertura do arquivo no modo leitura para saber a quantidade strings nele
    arquivo=open('recordes.txt','r')
    num=arquivo.readlines()
    arquivo.close()
    #Caso ele tenha menos de 10 strings será atribuido strings com valor 0
    #até chegar em 10
    if len(num)<10:
         arquivo=open('recordes.txt','a')
         mn=10-len(num)
         for x in range(0,mn):
             arquivo.write('0')
             arquivo.write("\n")
         arquivo.close()
         arquivo=open('recordes.txt','r')
         num.clear()
         num=arquivo.readlines
         arquivo.close()                  
    arquivos()
 else:
    #Se caso recordes.txt não existe, será criado e colocando 10 strings com valor 0
    arqui=open('recordes.txt','w')
    for x in range(0,10):
        arqui.write(str(0))
        arqui.write("\n")
    arqui.close()
    arquivos()


class jogo_adivinhacao(object):
 def  __init__(self, janela):


     
     #Criação das frames
     
     self.frame1=Frame(janela,bg='#00ffff')
     self.frame2=Frame(janela,bg='#00ffff')
     self.frame3=Frame(janela,bg='#00ffff')
     self.frame4=Frame(janela,bg='#00ffff')
     self.frame6=Frame(janela,bg='#00ffff')
     self.frame5=Frame(janela,bg='#00ffff')
     
     
     #Empacotamento das frames
     
     self.frame1.pack()
     self.frame2.pack()
     self.frame3.pack()
     self.frame4.pack(side= RIGHT)
     self.frame5.pack(side= LEFT)
     self.frame6.pack()
     
     #widgets da tela inicial

     self.foto=Label(self.frame1,text='GUESS ',font=('verdana','60'),bg='#00ffff')
     self.enu2=Label(self.frame1,text='STUDYING',font=('verdana','65'),bg='#00ffff') 
     self.novo_jog=Button(self.frame2, width=20, text='COMEÇAR',bg="magenta",font=20,padx=5,command=self.novo_jogo)
     self.reco=Button(self.frame2,width=20, text='RECORDE',bg="magenta",font=20,padx=5,command=self.record)
     self.instr=Button(self.frame3,width=20, text='INSTRUÇÃO',bg="magenta",padx=5,font=20,command=self.instru)
     self.sai=Button(self.frame3,width=20, text='SAIR',bg='magenta',padx=5,font=20,command=self.sair)

     #widgets da tela do jogo
     self.numquest=Label(self.frame1,font=('verdana','20'),bg='#00ffff')
     self.questao=Label(self.frame1,font=25,bg='#00ffff')
     self.questaocont=Label(self.frame1,font=25,bg='#00ffff')
     self.dica1=Button(self.frame2,text='Dica 1',width=20,bg='magenta',font=20,command=self.dicas1)
     self.dica2=Button(self.frame2,text='Dica 2',width=20,bg='magenta',font=20,command=self.dicas2)
     self.dica3=Button(self.frame2,text='Dica 3',width=20,bg='magenta',font=20,command=self.dicas3)
     self.d1=Label(self.frame3,font=25,bg='#00ffff')
     self.leitura_dados=Entry(self.frame3,font=('verdana','15'))
     self.receber=Button(self.frame5,text='CONFIRMAR',width=20,bg='magenta',font=20,command=self.resposta)
     self.tim = Label(self.frame5,font=('verdana','20'),bg='#00ffff')

     #widgets para voltar

     self.voltar=Button(self.frame4,width=10, text='Voltar',bg='magenta',font=20,command=self.remover_voltar)
     
     #widgets para espaço
     self.d11=Label(self.frame1,bg='#00ffff')
     self.d21=Label(self.frame2,bg='#00ffff')
     self.d22=Label(self.frame3,bg='#00ffff')
     self.d2=Label(self.frame3,bg='#00ffff')

     #Widgets para mostrar a pontuação que fez ao sair do jogo e voltar pra menu inicial

     self.enunciado=Label(self.frame1,text='Fim de jogo',font=('verdana','20'),bg='#00ffff')
     self.enunciado2=Label(self.frame1,text='  Tempo   |   Quantidade de questões',font=('verdana','20'),bg='#00ffff')    
     self.finquest=Label(self.frame1,text='',font=('verdana','12'),bg='#00ffff')
     self.fintempo=Label(self.frame1,text='',font=('verdana','12'),bg='#00ffff')
     self.volta=Button(self.frame2,text='VOLTAR PARA MENU INICIAL',bg='magenta',font=('verdana','12'),command=self.volt)

     #widgets das instruções
     
     self.instru1=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru2=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru3=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru4=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru5=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru6=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru7=Label(self.frame1,font=('verdana','12'),bg='#00ffff')
     self.instru8=Label(self.frame1,font=('verdana','12'),bg='#00ffff')

     #Widgets dos recordes
     
     self.recorde1=Label(self.frame1,text='1',font=('verdana','12'),bg='#00ffff')
     self.recorde11=Label(self.frame1,text='1',font=('verdana','12'),bg='#00ffff')
     self.recorde2=Label(self.frame1,text='2',font=('verdana','12'),bg='#00ffff')
     self.recorde21=Label(self.frame1,text='2',font=('verdana','12'),bg='#00ffff')
     self.recorde3=Label(self.frame1,text='3',font=('verdana','12'),bg='#00ffff')
     
     cria_arquivo()
     #Chamada pra mostrar os botões da tela principal

     self.tela_principal()
     
 #Empacotamento dos botões da tela principal    
 def tela_principal(self):

    self.foto.pack(side=TOP)
    self.enu2.pack()
    self.d21.pack()
    self.novo_jog.pack()
    self.reco.pack()
    self.instr.pack()
    self.sai.pack()
     
 #Empacotamento do botão de voltar
 def botao_voltar(self):
    self.voltar.pack(side= RIGHT)
    
   
 #Remove as widgets da tela principal
 #da o valor 1 a variavel t para que ao clicar em voltar futuramente
 #as widgets da função jogo seja removidas
 #E zera o m para que as questões começe tudo de novo e não de um questão N
 def novo_jogo(self):
      global sec
      sec=0
      self.remover_principal()
      self.tim = Label(self.frame5,font=('verdana','20'),bg='#00ffff') 
      global m
      m=0
      global t
      t=1
      numeracao()
      self.jogo()
      
 def jogo(self):# Tela do jogo, ela ira empacotar as widgets, chamar as funçoes
     #do tempo,etc
      global seco
      global n
      if m==0:
       paramet=1000
       self.tick()
      self.numquest['text']='QUESTÃO '+str(m+1)
      self.numquest.pack()
      self.d11.pack()
      self.questoes()
      self.questao.pack()
      self.questaocont.pack()
      self.d2.pack()
      self.d1['text']=''
      self.d21.pack(side= TOP)
      self.dica1.pack(side = LEFT)
      self.dica2.pack(side = LEFT)
      self.dica3.pack(side = LEFT)
      self.d1.pack(side = TOP)
      self.d22.pack(side= TOP)
      self.leitura_dados.pack()
      if m==0:
        self.tim.pack()
      self.receber.pack(side=LEFT)         
      self.botao_voltar()
      g=1
    

 def questoes(self):#Funçao questoes era atribuir ao text do questao o enunciado
     #da questão e assim mostrar na interface
       
        if quest[m]==1:
            self.questao['text']='Como são chamadas as substâncias que atuam como'
            self.questaocont['text']='coenzimas?'
        elif quest[m]==2:
            self.questao['text']='Como são chamadas as proteínas de estruturas terciárias '
            self.questaocont['text']='e que atuam como catalisadoras?'
        elif quest[m]==3:
            self.questao['text']='A que ser se refere a seguinte definição:'
            self.questaocont['text']=' “preparada a partir de antígenos mortos ou enfraquecidos”'
        elif quest[m]==4:
            self.questao['text']='A que ser se refere a seguinte definição: '
            self.questaocont['text']='“preparado a partir de anticorpos que neutralizam os antigenos”'
        elif quest[m]==5:
            self.questao['text']='Como são chamadas as macromoléculas formadas pela'
            self.questaocont['text']='união de vários aminoácidos ou monopeptídeos?'
        elif quest[m]==6:
            self.questao['text']='É o conjunto de reações químicas que ocorrem' 
            self.questaocont['text']='em um organismo.'
        elif quest[m]==7:
            self.questao['text']='É um composto químico inorgânico abundante'
            self.questaocont['text']='na composição dos seres vivos.'
        elif quest[m]==8:
            self.questao['text']='Os sais minerais são encontrados de duas maneiras nos seres vivos.'
            self.questaocont['text']='Quais são?'
        elif quest[m]==9:
            self.questao['text']='“Glucídios”, “açucares” e “Hidratos de carbono”' 
            self.questaocont['text']=' são sinônimos de que composto?'
        elif quest[m]==10:
            self.questao['text']='Substância de natureza química variada com grande '
            self.questaocont['text']='peso molecular'
        elif quest[m]==11:
            self.questao['text']='Como se chama a parte que é comum a dois conjuntos '
            self.questaocont['text']='numéricos?'
        elif quest[m]==12:
            self.questao['text']='Como se chama a junção de dois conjuntos numéricos?'
            self.questaocont['text']=''
        elif quest[m]==13:
            self.questao['text']='Como se chama o conjunto representado por “Z” ?'
            self.questaocont['text']=''
        elif quest[m]==14:
            self.questao['text']='Como se chama o conjunto representado por “Q” ?'
            self.questaocont['text']=''
        elif quest[m]==15:
            self.questao['text']=')Qual o nome da função dada pela lei f(x)=ax+b?'
            self.questaocont['text']=''
        elif quest[m]==16:
            self.questao['text']='Qual função tem como gráfico uma parábola?'
            self.questaocont['text']=''
        elif quest[m]==17:
            self.questao['text']='“ A função f de R em R que associa cada número ao seu módulo”.'
            self.questaocont['text']=' De que função é essa definição?'
        elif quest[m]==18:
            self.questao['text']='Qual a função dada pela dei f(x):a^x?'
            self.questaocont['text']=''
        elif quest[m]==19:
            self.questao['text']='Que função é dada pela lei f(x)=log a x ?'
            self.questaocont['text']=''
        elif quest[m]==20:
            self.questao['text']='Como se chama o plano usado para representar os pontos das '
            self.questaocont['text']='funções graficamente?'
        elif quest[m]==21:
            self.questao['text']='Ocorre quando interagimos com outras pessoas.'
            self.questaocont['text']=''
        elif quest[m]==22:
            self.questao['text']='O Português apresenta duas variações linguísticas. '
            self.questaocont['text']='Quais são?'
        elif quest[m]==23:
            self.questao['text']='“Os textos não fazem, necessariamente, parte da realidade” . '
            self.questaocont['text']='A que traço de um texto literário esse trecho se refere?'
        elif quest[m]==24:
            self.questao['text']='Os textos literários são divididos em 2 grupos. '
            self.questaocont['text']='Quais são?'
        elif quest[m]==25:
            self.questao['text']='Na literatura, como se denomina o gênero que era criado para encenação?'
            self.questaocont['text']=''
        elif quest[m]==26:
            self.questao['text']='"É caracterizada como sendo uma subversão do que já foi dito anteriormente”. '
            self.questaocont['text']='Esse trecho é a definição de que elemento da língua portuguesa?'
        elif quest[m]==27:
            self.questao['text']=' “ É a reafirmação de algo que já foi dito”. '
            self.questaocont['text']='Esse trecho é a definição de que elemento da língua portuguesa?'
        elif quest[m]==28:
            self.questao['text']='“Recursos de nosso idioma para tornar as mensagens mais expressivas e significativas”'
            self.questaocont['text']=' A que elemento da língua portuguesa esse trecho se refere?'
        elif quest[m]==29:
            self.questao['text']='“Consiste em atribuir ações próprias de seres humanos a algo inanimado”. '
            self.questaocont['text']='A que figura de linguagem o trecho se refere?'
        elif quest[m]==30:
            self.questao['text']='“Opostos que ocorrem simultaneamente”. '
            self.questaocont['text']='A que figura de linguagem o trecho se refere?'
        elif quest[m]==31:
            self.questao['text']='União dos elementos fisicos e culturas da paisagem'
            self.questaocont['text']=''
        elif quest[m]==32:
            self.questao['text']='Ciência que trata da origem, história, vida e estrutura da Terra '
            self.questaocont['text']=' em relação às rochas, incluindo as forças que operam para modificá-las.'
        elif quest[m]==33:
            self.questao['text']='Camada mais superficial da terra'
            self.questaocont['text']=''
        elif quest[m]==34:
            self.questao['text']='Camada mais profunda da terra'
            self.questaocont['text']=''
        elif quest[m]==35:
            self.questao['text']='Qual o nome dos blocos que integram a parte sólida da litosfera'
            self.questaocont['text']=''
        elif quest[m]==36:
            self.questao['text']='As planícies designam as superfícies planas de baixas altitudes (até 100 metros),'
            self.questaocont['text']='formados por:'
        elif quest[m]==37:
            self.questao['text']='Em qual era apareceu os seres humanos?'
            self.questaocont['text']=''
        elif quest[m]==38:
            self.questao['text']='Em qual era apareceu os dinossauros?'
            self.questaocont['text']=''
        elif quest[m]==39:
            self.questao['text']='Qual ciencia estuda os relevos e seus agentes  produtores '
            self.questaocont['text']='e modeladores?'
        elif quest[m]==40:
            self.questao['text']='O conjunto de ações naturais, fisicas, quimícas e biológicas que '
            self.questaocont['text']='causam desagregação e decomposição das rochas é chamado de?'
        elif quest[m]==41:
            self.questao['text']='Quais os dois periodos da pré-historia?'
            self.questaocont['text']=''
        elif quest[m]==42:
            self.questao['text']='Qual foi a primeira escrita criada pelo homem?'
            self.questaocont['text']=''
        elif quest[m]==43:
            self.questao['text']='Em qual civilicação foi criada a pólis?'
            self.questaocont['text']=''
        elif quest[m]==44:
            self.questao['text']='Qual civilização antiga teve 3 formas de governo?'
            self.questaocont['text']=''
        elif quest[m]==45:
            self.questao['text']='Qual o profeta do islamismo??'
            self.questaocont['text']=''
        elif quest[m]==46:
            self.questao['text']='Qual civilização foi fundada entre o rio Tigre e Eufrates?'
            self.questaocont['text']=''
        elif quest[m]==47:
            self.questao['text']='Qual civilização antiga situava na região do Irã?'
            self.questaocont['text']=''
        elif quest[m]==48:
            self.questao['text']='Qual foi o primeiro povo monoteista ?'
            self.questaocont['text']=''
        elif quest[m]==49:
            self.questao['text']='Qual era o nome da civilização dos povos navegadores?'
            self.questaocont['text']=''
        elif quest[m]==50:
            self.questao['text']='Qual foi a civilização que dominou a Grecia?'
            self.questaocont['text']=''
    
    
 def dicas1(self):
     #Função dica1 que irá  colocar no label da d1, o texto
     #da dica 1 da questão e com isto irá mostrar a dica
        if quest[m]==1:
            self.d1['text']='Podem ser lipossolúveis: K,E,D,A'
        elif quest[m]==2:
            self.d1['text']='teoria da “chave-fechadura”'
        elif quest[m]==3:
            self.d1['text']='Tem caráter preventivo'
        elif quest[m]==4:
            self.d1['text']='Tem caráter combativo'
        elif quest[m]==5:
            self.d1['text']='ligação peptídica'
        elif quest[m]==6:
            self.d1['text']='É uma característica do ser vivo'
        elif quest[m]==7:
            self.d1['text']='Tem alto poder de reação'
        elif quest[m]==8:
            self.d1['text']='Formação de estruturas como dentes e carapaças'
        elif quest[m]==9:
            self.d1['text']='Esse composto pode ter função estrutural e/ou energética.'
        elif quest[m]==10:
            self.d1['text']='Hidrófobas'
        elif quest[m]==11:
            self.d1['text']='Nesse caso, pode-se ler “A inter B”'
        elif quest[m]==12:
            self.d1['text']='Nesse caso, pode-se ler “A união B”'
        elif quest[m]==13:
            self.d1['text']='Nesse conjunto está contido os números naturais'
        elif quest[m]==14:
            self.d1['text']='Descrito como conjunto dos quocientes de 2 números inteiros'
        elif quest[m]==15:
            self.d1['text']='Seu gráfico é uma linha reta oblíqua.'
        elif quest[m]==16:
            self.d1['text']='Ela é dada pela lei ax²+bx+c'
        elif quest[m]==17:
            self.d1['text']='Para desenhar seu gráfico a transformamos em 2 sentenças'
        elif quest[m]==18:
            self.d1['text']='As curvas de seu gráfico é chamada de curva exponencial'
        elif quest[m]==19:
            self.d1['text']='Seu gráfico localiza-se a direita do eixo y (No 1º e  4º quadrante  )'
        elif quest[m]==20:
            self.d1['text']='É dividido em quatro partes, chamadas de quadrantes'
        elif quest[m]==21:
            self.d1['text']='Para isso utilizamos a linguagem.'
        elif quest[m]==22:
            self.d1['text']='Essa variação surgiu a partir das situações de uso da língua'
        elif quest[m]==23:
            self.d1['text']='Esse traço faz referência ao fato do texto poder assumir caráter fantástico'
        elif quest[m]==24:
            self.d1['text']='Um dos grupos tem a característica de apresentar um texto  escrito em parágrafos. '
        elif quest[m]==25:
            self.d1['text']='Nesse gênero eram apresentadas, principalmente, tragédias e comédias.'
        elif quest[m]==26:
            self.d1['text']='Esse elemento é usado com finalidade satírica ou jocosa.'
        elif quest[m]==27:
            self.d1['text']='Mesmo usando palavras diferentes, não há mudança na semantica .'
        elif quest[m]==28:
            self.d1['text']='Nesse elemento as palavras são empregadas em sentido figurado.'
        elif quest[m]==29:
            self.d1['text']='Essa atribuição pode ser de sentimento.'
        elif quest[m]==30:
            self.d1['text']='Pode ser confundido com a antítese.'
        elif quest[m]==31:
            self.d1['text']='É concreto(materializado) e abstrato(imaterial)'
        elif quest[m]==32:
            self.d1['text']='Mineral'
        elif quest[m]==33:
            self.d1['text']='Também chamada de litosfera'
        elif quest[m]==34:
            self.d1['text']='É composta por ferro e nível'
        elif quest[m]==35:
            self.d1['text']='Limites convergentes,divergentes e conservatiso'
        elif quest[m]==36:
            self.d1['text']='São classificadas em: costeira, fluvial  e lacustre '
        elif quest[m]==37:
            self.d1['text']='Possui o periodo quartenario e terciario '
        elif quest[m]==38:
            self.d1['text']='Possui o periodo cretáceo,o Jurássico e o Triássico'
        elif quest[m]==39:
            self.d1['text']='Planalto,planíce,depressão e motanha'
        elif quest[m]==40:
            self.d1['text']='As ações fisicas são o termoclastica,crioclastia e abrasão'
        elif quest[m]==41:
            self.d1['text']='Surgimento do fogo'
        elif quest[m]==42:
            self.d1['text']='Criada no antigo Egito'
        elif quest[m]==43:
            self.d1['text']='Originária dos aques,jônios,eólios e dórios'
        elif quest[m]==44:
            self.d1['text']='Patrícios,clientes,plebeus e escravos'
        elif quest[m]==45:
            self.d1['text']='Ultimo e pricipal profeta'
        elif quest[m]==46:
            self.d1['text']='Primeiro Império Babilônico'
        elif quest[m]==47:
            self.d1['text']='Aquemênidas'
        elif quest[m]==48:
            self.d1['text']='Judaismo'
        elif quest[m]==49:
            self.d1['text']='Eram politeístas'
        elif quest[m]==50:
            self.d1['text']='Falanges'

 #Atribuição da dica 2 da questão N para o label d1
 def dicas2(self):
     
        if quest[m]==1:
            self.d1['text']='Atuam estimulando a atividade das enzimas'
        elif quest[m]==2:
            self.d1['text']='reversível(Competitiva) ou irreversível (não-competitiva)'
        elif quest[m]==3:
            self.d1['text']='É uma imunização artificial'
        elif quest[m]==4:
            self.d1['text']='É uma imunização artificial'
        elif quest[m]==5:
           self.d1['text']='Sua estrutura pode ser primária, secundária, terciária ou quaternária'
        elif quest[m]==6:
            self.d1['text']='Classificado em anabolismo e catabolismo'
        elif quest[m]==7:
            self.d1['text']='Alto poder de dissolução.'
        elif quest[m]==8:
            self.d1['text']=' Podem ser encontrados na forma de íons'
        elif quest[m]==9:
            self.d1['text']='monossacarídeos e oligossacarídeos.'
        elif quest[m]==10:
            self.d1['text']='Óleos,gorduras,graxas,etc'
        elif quest[m]==11:
            self.d1['text']='A simbologia dessa situação é um U de cabeça pra baixo “∩”'
        elif quest[m]==12:
            self.d1['text']='A simbologia dessa situação é um “U”'
        elif quest[m]==13:
            self.d1['text']='Contém também os números negativos.'
        elif quest[m]==14:
            self.d1['text']='Contém também os números negativos.'
        elif quest[m]==15:
            self.d1['text']='Se a=0 a função passa a ser constante'
        elif quest[m]==16:
            self.d1['text']='Pode apresentar 2 raízes'
        elif quest[m]==17:
            self.d1['text']=' O gráfico dessa função tem formato de “V”'
        elif quest[m]==18:
            self.d1['text']='Para resolvê-la devemos ter em mente o conceito de potenciação'
        elif quest[m]==19:
            self.d1['text']='Essa função associa cada número real positivo ao seu logaritmo na base a'
        elif quest[m]==20:
            self.d1['text']=' É composto por um eixo horizontal e um vertical'
        elif quest[m]==21:
            self.d1['text']='Podemos utilizar palavras'
        elif quest[m]==22:
            self.d1['text']='Em uma dessas variações deve ser observado se o uso é adequado ou não.'
        elif quest[m]==23:
            self.d1['text']=' É possível também que o texto seja verossími'
        elif quest[m]==24:
            self.d1['text']='Num deles se encaixa a poesia'
        elif quest[m]==25:
            self.d1['text']='Teve origem na Grécia.'
        elif quest[m]==26:
            self.d1['text']='Sendo engraçada de crítica, promove divertimento e também reflexão'
        elif quest[m]==27:
            self.d1['text']='Vem entre aspas (“”)'
        elif quest[m]==28:
            self.d1['text']='Nesse elemento estão inseridas ,por exemplo , a comparação e a metonímia.'
        elif quest[m]==29:
            self.d1['text']='Um exemplo dessa figura de linguagem é “ A natureza está brava”'
        elif quest[m]==30:
            self.d1['text']='Um exemplo é “Essa menina parece que dorme acordada”'
        elif quest[m]==31:
            self.d1['text']='Possui elementos naturias, culturas e invisíveis'
        elif quest[m]==32:
            self.d1['text']='Rochas'
        elif quest[m]==33:
            self.d1['text']='Possui 80kg continetal e 10 oceanica'
        elif quest[m]==34:
            self.d1['text']='é divida em externo e interno'
        elif quest[m]==35:
            self.d1['text']='Possui 12 blocos principais'
        elif quest[m]==36:
            self.d1['text']='Possui pouca variação de altitude'
        elif quest[m]==37:
            self.d1['text']='Ocorreu a 11 mil anos'
        elif quest[m]==38:
            self.d1['text']='Desenvolvimento dos gimnospermas'
        elif quest[m]==39:
            self.d1['text']='Os agents endógenos são o tecntonismo,vulcanismo e os abalos sísmicos'
        elif quest[m]==40:
            self.d1['text']='Também chamado de meteorização'
        elif quest[m]==41:
            self.d1['text']='Criação dos instrumentos de pedra e artefatos com lascas'
        elif quest[m]==42:
            self.d1['text']='Deu origem a forma chamada de hierática'
        elif quest[m]==43:
            self.d1['text']='Periodo Homérico'
        elif quest[m]==44:
            self.d1['text']='Júlio Cesar'
        elif quest[m]==45:
            self.d1['text']='Hégira'
        elif quest[m]==46:
            self.d1['text']='Código de Hamurabi'
        elif quest[m]==47:
            self.d1['text']='A administração se baseou nas satrapias'
        elif quest[m]==48:
            self.d1['text']='Tempo de Moisés'
        elif quest[m]==49:
            self.d1['text']='Deus Baal'
        elif quest[m]==50:
            self.d1['text']='Filipe II'

 #Atribuição da dica 3 da questão N para o label d1
 def dicas3(self):
        if quest[m]==1:
            self.d1['text']='Podem ser hidrossolúveis :C e complexo B'
        elif quest[m]==2:
            self.d1['text']='Cada uma apresenta sua temperatura ideal (ponto ótimo)'
        elif quest[m]==3:
            self.d1['text']='Estimulam a produção de anticorpos'
        elif quest[m]==4:
            self.d1['text']=' Fornece os anticorpos'
        elif quest[m]==5:
            self.d1['text']=' processo de desnaturação e renaturação'
        elif quest[m]==6:
            self.d1['text']='Ex: Fotossíntese, respiração celular, digestão'
        elif quest[m]==7:
            self.d1['text']='Tem alto poder de reação'
        elif quest[m]==8:
            self.d1['text']='Alguns dos principais íons são Cloro (Cl-) e Iodo (I-)'
        elif quest[m]==9:
            self.d1['text']='Maltose,Sacarose e Lactose'
        elif quest[m]==10:
            self.d1['text']='Reguladora e Estrutural'
        elif quest[m]==11:
            self.d1['text']='Sua representação por compreensão é “x|x Є A e x Є  B”'
        elif quest[m]==12:
            self.d1['text']='Sua representação por compreensão é “x|x Є A ou x Є  B'
        elif quest[m]==13:
            self.d1['text']='É infinito em suas extremidades'
        elif quest[m]==14:
            self.d1['text']='Nesse conjunto está contido os números naturais'
        elif quest[m]==15:
            self.d1['text']='B é chamado de coeficiente linear da função, e é o ponto onde a reta corta o eixo y.'
        elif quest[m]==16:
            self.d1['text']='Também chamada de função polinomial de 2º grau'
        elif quest[m]==17:
            self.d1['text']='Para resolvê-la devemos ter em mente o conceito de módulo'
        elif quest[m]==18:
            self.d1['text']='Seu gráfico não toca no eixo x'
        elif quest[m]==19:
            self.d1['text']='Essa função f é dada de R*+ em R.'
        elif quest[m]==20:
            self.d1['text']='Os eixos são chamados de eixos das abscissas e das ordenadas'
        elif quest[m]==21:
            self.d1['text']='Podemos usar gestos'
        elif quest[m]==22:
            self.d1['text']='Na outra variação deve ser observado se o uso está certo ou errado'
        elif quest[m]==23:
            self.d1['text']='Vem da característica do texto de não ser real, ou seja, ser ficção '
        elif quest[m]==24:
            self.d1['text']='Aqueles que são formados por versos estão em um dos grupos'
        elif quest[m]==25:
            self.d1['text']='Predomina o discurso em segunda pessoa (tu, vós)'
        elif quest[m]==26:
            self.d1['text']='Um exemplo de seu uso é a “mudança” em músicas para propaganda eleitoral.'
        elif quest[m]==27:
            self.d1['text']='Deve ser mencionado quem foi o “criador’” da citação.'
        elif quest[m]==28:
            self.d1['text']='Usada para produzir efeitos de interpretação'
        elif quest[m]==29:
            self.d1['text']='Designa o ato de “tornar iguala uma pessoa”'
        elif quest[m]==30:
            self.d1['text']='São encontrados, por exemplo, em músicas.'
        elif quest[m]==31:
            self.d1['text']='Montanhas,casas, odores das poluições'
        elif quest[m]==32:
            self.d1['text']='Estrutura da terra'
        elif quest[m]==33:
            self.d1['text']='É composta por  silicatos de alumínio e magnésio'
        elif quest[m]==34:
            self.d1['text']='O externo é liquido e interno é solido'
        elif quest[m]==35:
            self.d1['text']='Podem causar terremotos'
        elif quest[m]==36:
            self.d1['text']='É uma area plana que recebe sedimentos de outras áreas'
        elif quest[m]==37:
            self.d1['text']='É a mesma era que apareceu as plamas como as de hoje em dia'
        elif quest[m]==38:
            self.d1['text']='Grande atividade vulcanica'
        elif quest[m]==39:
            self.d1['text']='O tectonismo é dividido em orogênese e epirogênese'
        elif quest[m]==40:
            self.d1['text']='A união dela com o transporte do material da origem a erosão'
        elif quest[m]==41:
            self.d1['text']='Um das eras era chamada de Idade da Pedra solida'
        elif quest[m]==42:
            self.d1['text']='Reservada para uso em inscrições religiosos em monumentos e templos'
        elif quest[m]==43:
            self.d1['text']='Atenas e Espartas'
        elif quest[m]==44:
            self.d1['text']='Cristianismo'
        elif quest[m]==45:
            self.d1['text']='Morreu em 632'
        elif quest[m]==46:
            self.d1['text']='Primeiros zigurantes'
        elif quest[m]==47:
            self.d1['text']='Dárico'
        elif quest[m]==48:
            self.d1['text']='Expressão Justiça salomônica'
        elif quest[m]==49:
            self.d1['text']='A escrita deles deu origem a escrita grega e latina'
        elif quest[m]==50:
            self.d1['text']='Caráter heterogêneo da população do reino'
 #Comparação da resposta e chamada da proxima questão, sendo se caso chegar na questão 50
##será chamada a função fim_jogo
 def resposta(self):
        res = self.leitura_dados.get()
        if quest[m]==1:
            if res.upper()=='VITAMINAS':
              if m<49:
                self.remover_jogo()
                self.jogo()
              else:
                self.fim_jogo()
        elif quest[m]==2:
            if res.upper()=='ENZIMAS':
                if m<49:
                 self.remover_jogo()
                 self.jogo()
                else:
                 self.fim_jogo()
        elif quest[m]==3:
            if res.upper()=='VACINA':
                if m<49:
                  self.remover_jogo()
                  self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==4:
            if res.upper()=='SORO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==5:
            if res.upper()=='PROTEÍNAS' or res.upper()=='PROTEINAS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==6:
            if res.upper()=='METABOLISMO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==7:
            if res.upper()=='ÁGUA' or 'AGUA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==8:
            if res.upper()=='IMOBILIZADOS E LIVRES' or res.upper()=='LIVRES E IMOBILIZADOS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==9:
            if res.upper()=='CARBOIDRATOS' or res.upper()=='CARBOIDRATO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==10:
            if res.upper()=='LIPÍDIOS' or res.upper()=='LIPIDIOS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==11:
            if res.upper()=='INTERSEÇÃO' or res.upper()=='INTERSECÇÃO:':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==12:
            if res.upper()=='UNIÃO' or res.upper()=='UNIAO':
                if m<50:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==13:
            if res.upper()=='INTEIROS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==14:
            if res.upper()=='RACIONAIS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==15:
            if res.upper()=='FUNÇÃO AFIM':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==16:
            if res.upper()=='FUNÇÃO QUADRATICA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==17:
            if res.upper()=='FUNÇÃO MODULAR':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==18:
            if res.upper()=='FUNÇÃO EXPONENCIAL':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==19:
            if res.upper()=='FUNÇÃO LOGARÍTMICA' or res.upper()=='FUNÇAO LOGARITMICA' or res.upper()=='FUNÇÃO LOGARITMICA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==20:
            if res.upper()=='PLANO CARTESIANO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==21:
            if res.upper()=='COMUNICAÇÃO' or res.upper()=='COMUNICAÇAO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==22:
            if res.upper()=='FORMAL E INFORMAL' or res.upper()=='INFORMAL E FORMAL':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==23:
            if res.upper()=='FICCIONALIDADE':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==24:
            if res.upper()=='VERSOS E PROSA' or res.upper()=='PROSA E VERSOS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==25:
            if res.upper()=='DRAMÁTICO' or res.upper()=='DRAMATICO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==26:
            if res.upper()=='PARÓDIA' or res.upper()=='PARODIA':
               if m<49:
                   self.remover_jogo()
                   self.jogo()
               else:
                  self.fim_jogo()
        elif quest[m]==27:
            if res.upper()=='PARÁFRASE' or res.upper()=='PARAFRASE':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==28:
            if res.upper()=='FIGURAS DE LINGUAGEM':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==29:
            if res.upper()=='PERSONIFICAÇÃO' or res.upper()=='PERSONIFICAÇAO' or res.upper()=='PROSOPOPEIA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==30:
            if res.upper()=='PARADOXO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==31:
            if res.upper()=='ESPAÇO GEOGRAFICO' or res.upper()=='ESPAÇO GEOGRÁFICO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==32:
            if res.upper()=='GEOLOGIA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==33:
            if res.upper()=='CROSTA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==34:
            if res.upper()=='NÚCLEO' or res.upper()=='NUCLEO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==35:
            if res.upper()=='PLACAS TECTÓNICAS' or res.upper()=='PLACAS TECTONICAS' :
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==36:
            if res.upper()=='ROCHAS SEDIMENTARES':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==37:
            if res.upper()=='CENOZOICO' or res.upper()=='CENOZOICA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==38:
            if res.upper()=='MESOZOICO' or res.upper()=='MESOZOICA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==39:
            if res.upper()=='GEOMORFOLOGIA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==40:
            if res.upper()=='INTEMPERISMO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==41:
            if res.upper()=='PALEOLÍTICO E NEOLÍTICO' or res.upper()=='PALEOLITICO E NEOLÍTICO' or res.upper()=='PALEOLÍTICO E NEOLITICO' or res.upper()=='PALEOLITICO E NEOLITICO':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==42:
            if res.upper()=='HIEROGLIFICA' or res.upper()=='HIEROGLÍFICA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==43:
            if res.upper()=='GRECIA ANTIGA' or res.upper()=='GRÉCIA ANTIGA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==44:
            if res.upper()=='ROMA ANTIGA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==45:
            if res.upper()=='MAÓME' or res.upper()=='MAOME':
               if m<49:
                   self.remover_jogo()
                   self.jogo()
               else:
                  self.fim_jogo()
        elif quest[m]==46:
            if res.upper()=='MESOPOTÂMIA' or res.upper()=='MESOPOTAMIA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==47:
            if res.upper()=='PERSAS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==48:
            if res.upper()=='HEBREUS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==49:
            if res.upper()=='FENÍCIOS' or res.upper()=='FENICIOS':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()
        elif quest[m]==50:
            if res.upper()=='MACEDÔNIA' or res.upper()=='MACEDONIA':
                if m<49:
                   self.remover_jogo()
                   self.jogo()
                else:
                  self.fim_jogo()

 #Cronometro do tempo 
 def tick(self):
       global sec
       if sec<300:                       
         sec = sec + 1
         self.tim['text'] = str(sec)+'/300'
         self.tim.after(1000,self.tick)#after chama a função tick a cada 1 segundo 
       else:
        self.fim_jogo()
 #Remove as widgets do jogo, atribui o tempo e questão as outras variaveis
 #e mostra na tela a pontuação feita
 def fim_jogo(self):
         global sec
         global finalquestao
         global finaltempo
         global m
         finalquestao=m
         finaltempo=sec
         self.tim.destroy()
         self.salvar_recordes()
         self.remover_jogo()
         self.jogo_sair()
 #Mostra o tempo e a quantidade de questões o que jogador fez ao sair
 def jogo_sair(self):

     self.finquest['text']=str(finalquestao)
     self.fintempo['text']='        '+str(finaltempo)
     self.enunciado.pack()
     self.enunciado2.pack()
     self.fintempo.pack(side=LEFT)
     self.finquest.pack()

     self.volta.pack()
 #Remover as widgets da função jogo_sair e chamar a função tela_principal
 def volt(self):

     self.enunciado.pack_forget()
     self.enunciado2.pack_forget()
     self.fintempo.pack_forget()
     self.finquest.pack_forget()
     self.volta.pack_forget()
     self.tela_principal()
     

 #empacotamento das instruções   
 def instru(self):

    global t
    t=3     
    self.remover_principal()
    self.texto_instru()
    self.instru1.pack()
    self.instru2.pack()
    self.instru3.pack()
    self.instru4.pack()
    self.instru5.pack()
    self.instru6.pack()
    self.instru7.pack()
    self.instru8.pack()    
    self.botao_voltar()

 #Texto das instruções   
 def texto_instru(self):

    self.instru1['text']='1 - O jogo possui 50 questões aleátorios de português, matemática,'
    self.instru2['text']='biologia, historia e geografia.'
    self.instru3['text']='2 - Cada questão possui 3 dicas'
    self.instru4['text']='3 - O tempo para acertar as 50 questões é de 300 segundos'
    self.instru5['text']='Quanto mais você acerta, mais o tempo acelera'
    self.instru6['text']='4 - O jogo não possui continue, logo se caso você sair do jogo tera'
    self.instru7['text']='que começar novamente, sendo que as questões serão possivelmente outras.'
    self.instru8['text']='5 - Os recordes só são salvos se o jogador sair usando o botão sair'

 #Função que empacota as widgets da tela de recordes
 def record(self):
    
    global t
    self.remover_principal()
    t=2
    self.texto_record()
    self.enunciado2.pack()
    self.recorde1.pack()
    self.recorde11.pack()
    self.recorde2.pack()
    self.recorde21.pack()
    self.recorde3.pack()
    self.botao_voltar()
 #Colocando os recordes a suas label   
 def texto_record(self):

     self.recorde1['text']=str(ftempo[0])+'       '*6+str(fquestao[0])+'   '*5
     self.recorde11['text']=str(ftempo[1])+'       '*6+str(fquestao[1])+'   '*5
     self.recorde2['text']=str(ftempo[2])+'       '*6+str(fquestao[2])+'   '*5
     self.recorde21['text']=str(ftempo[3])+'       '*6+str(fquestao[3])+'   '*5
     self.recorde3['text']=str(ftempo[4])+'       '*6+str(fquestao[4])+'   '*5
 #teste para ver se a quantidade de questão do usuario foi maior que as 5 do recordes
 #Caso seja será reorganizado os recordes decrescentemente      
 def salvar_recordes(self):

     global finalquestao
     global finaltempo
     if fquestao[0]<finalquestao:
         a=ftempo[0]
         b=fquestao[0]
         ftempo[0]=finaltempo
         fquestao[0]=finalquestao
         c=ftempo[1]
         d=fquestao[1]
         ftempo[1]=a
         fquestao[1]=b
         a=ftempo[2]
         b=fquestao[2]
         ftempo[2]=c
         fquestao[2]=d
         c=ftempo[3]
         d=fquestao[3]
         ftempo[3]=a
         fquestao[3]=b
         ftempo[4]=c
         fquestao[4]=d
     elif fquestao[1]<finalquestao:
         c=ftempo[1]
         d=fquestao[1]
         ftempo[1]=finaltempo
         fquestao[1]=finalquestao
         a=ftempo[2]
         b=fquestao[2]
         ftempo[2]=c
         fquestao[2]=d
         c=ftempo[3]
         d=fquestao[3]
         ftempo[3]=a
         fquestao[3]=b
         ftempo[4]=c
         fquestao[4]=d
     elif fquestao[2]<finalquestao:
         a=ftempo[2]
         b=fquestao[2]
         ftempo[2]=finaltempo
         fquestao[2]=finalquestao
         c=ftempo[3]
         d=fquestao[3]
         ftempo[3]=a
         fquestao[3]=b
         ftempo[4]=c
         fquestao[4]=d
     elif fquestao[3]<finalquestao:
         c=ftempo[3]
         d=fquestao[3]
         ftempo[3]=finaltempo
         fquestao[3]=finalquestao
         ftempo[4]=c
         fquestao[4]=d
     elif fquestao[4]<finalquestao:
         ftempo[4]=finaltempo
         fquestao[4]=finalquestao
 #Fecha o jogo e salva os recordes no recordes.txt  
 def sair(self):
     global contador
     global contador1
     arquivo=open('recordes.txt','w')
     for x in range(0,10):
      #Estrutura para organizar o tempo a questão, 
      #sendo primeiro tempo, depois questão,e assim em diante
      if x%2==0:
        arquivo.write(str(ftempo[contador]))
        arquivo.write("\n")
        contador=contador+1
      else:
        arquivo.write(str(fquestao[contador1]))
        arquivo.write("\n")
        contador1=contador1+1
     arquivo.close()
     janela.destroy()

 #Remover as widgtes da tela principal    
 def remover_principal(self):

    self.novo_jog.pack_forget()
    self.enu2.pack_forget()
    self.d21.pack_forget()
    self.instr.pack_forget()
    self.sai.pack_forget()
    self.reco.pack_forget()
    self.foto.pack_forget()


 def remover_voltar(self):#Voltar para a tela principal
   if t==1:
      self.fim_jogo()
   elif t==2:
      self.remover_recordes()
      self.voltar.pack_forget()
      self.tela_principal()
   elif t==3:
      self.remover_instrucao()
      self.voltar.pack_forget()
      self.tela_principal()
      

 #remover as widgets da tela do jogo
 def remover_jogo(self):

     global m
     self.numquest.pack_forget()
     self.d11.pack_forget()
     self.dica1.pack_forget()
     self.dica2.pack_forget()
     self.dica3.pack_forget()
     self.questao.pack_forget()
     self.questaocont.pack_forget()
     self.d1.pack_forget()
     self.leitura_dados.pack_forget()
     self.receber.pack_forget()
     self.receber.pack_forget()
     self.voltar.pack_forget()
     self.leitura_dados.delete(0,END)
     self.d2.pack_forget()
     self.d21.pack_forget()
     self.d22.pack_forget()
     m=1+m
 #Remove as widgets tela de recordes
 def remover_recordes(self):
    self.enunciado2.pack_forget()
    self.recorde1.pack_forget()
    self.recorde11.pack_forget()
    self.recorde2.pack_forget()
    self.recorde21.pack_forget()
    self.recorde3.pack_forget()

 #remover as widgets das intruções
 def remover_instrucao(self):

    self.instru1.pack_forget()
    self.instru2.pack_forget()
    self.instru3.pack_forget()
    self.instru4.pack_forget()
    self.instru5.pack_forget()
    self.instru6.pack_forget()
    self.instru7.pack_forget()
    self.instru8.pack_forget()
 
 
   
     
#DEFINIÇÃO DA JANELA DO JOGO
janela=Tk()
janela.title("Guess Studying")#nome da janela
janela["bg"]="#00ffff"#cor de plano de fundo
janela.geometry("700x600+200+100")#resolução
jogo_adivinhacao(janela)
janela.mainloop()
