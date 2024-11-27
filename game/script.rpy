# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

#Introduce the game in the script area.

# The game starts here.

label start:
#Teste com Hud para inventario
 show screen hud

 scene scene_black

 #script de escolha de nome:

 $ povname = renpy.input("Escolha o seu Nome:", length = 6)
 $ povname = povname.strip()

 if not povname:
    $ povname =  "Sam"

 #o script acaba aqui....

 #isso para a música
 stop music

 play music "audio/119402__kyster__nice-forrest-ambience.ogg"volume 50

 #isso mostra a cena
 scene Casa_5
 with dissolve
 
 mc "Mais um dia de trabalho terminou. Finalmente, um pouco de descanso..."
 mc "Pelo menos até o próximo projeto..."

 #isso esconde a cena e sprites
 hide Casa_5

 #pode ser usado também para mostrar cenas e sprites
 show scene_black

 "Entro em contato com o cliente para mostrar o projeto finalizado..."
 "5 páginas de um site para um abrigo de animais."
 "Tudo projetado com muito cuidado por mim..."
 "......"
 "Olho para a janela enquanto espero pela resposta do cliente..."
 "O tempo realmente voa, quero dizer, já era tarde esta manhã quando sentei aqui para trabalhar..."
 "Eu nem percebi que pulei o almoço."
 "*Ronca*"
 mc "...."
 mc "Bem, agora percebi..."
 "Meu estômago ronca..."
 "De repente, sinto como se não comesse há dias..."
 "Não pensei que estaria com tanta fome, mas também, né?"
 "Tomei um café da manhã simples e pulei o almoço..."
 "Talvez eu pudesse fazer um lanche na loja de conveniência. Tem um bom por aqui, embora eu costume ir lá fazer compras, sei que tem uns petiscos bem gostosos."
 "Talvez eu pudesse fazer as duas coisas dessa vez..."
 "Dois coelhos, numa cajadada só!!!"

 show Casa_10
 with dissolve

 "Saio de casa e caminho pela vizinhança, em direção à loja..."
 "Não há muito para ver por aqui, exceto o sorriso amigável dos poucos vizinhos que tenho..."
 "O número de pessoas que se mudaram daqui foi a razão pela qual eu posso me dar ao luxo de viver aqui, então eu deveria estar grato por isso..."

 hide Casa_10
 with dissolve

 stop music
 
 #isso toca a musica
 play music "audio/657265__ho52nest__wellcome-supermarket-background-music.ogg"volume 50

 show Loja_2
 with dissolve

 "Chego à loja bem rápido, o tempo sempre voa quando estou perdido em pensamentos, talvez isso se aplique também às distâncias..."
 "A loja está quase completamente deserta. Sou só eu, o caixa da frente e o do café..."
 "*Ronca*"
 "..."
 "É melhor eu pegar esse lanche de uma vez..."
 "Ando em direção à pequena área do café nos fundos da loja, anotando mentalmente todas as coisas que preciso reabastecer quando terminar de comer..."

 hide Loja_2
 with dissolve

 show Loja_1
 with dissolve
 
 "Assim que chego ao balcão, sou recebido com um sorriso familiar."

 show AP4
 with dissolve

 #povname é a definição da variável de escolha de nome
 ap "[povname]! Faz muito tempo que não te vejo, né?"

 hide AP4
 with dissolve

 show AP13
 with dissolve

 "É o Apollo..."
 "Um velho amigo. Ele costumava ser meu colega de classe no ensino médio..."
 "Ele sempre esteve ao meu lado desde que nos conhecemos. De alguma forma, nunca nos distanciamos realmente. Na verdade, eu nunca teria ouvido falar deste lugar se não fosse por ele..."

 hide AP13
 with dissolve

 show AP3
 with dissolve

 mc "Apollo! Ótimo ver você! Eu não sabia que você estaria aqui."
 ap "uh...por que não? Eu trabalho aqui..."
 "Ele ri como se isso fosse óbvio..."
 mc "Sim, bem, agora eu sei disso."

 hide AP3
 with dissolve

 show AP7
 with dissolve

 "Eu dou uma risada e ele sorri para mim confuso."

 hide AP7
 with dissolve

 show AP3
 with dissolve

 ap "Só agora? Eu te disse isso quando você se mudou para cá."
 mc "hein...?"
 "Isto é estranho..."
 "Ele me contou?"
 "Eu olho para ele..."
 "O olhar confiante e presunçoso se transforma em incerteza..."
 ap "Quer dizer..." 
 ap "Eu queria te contar..." 
 ap "Eu acho..."
 "Tenho certeza que ele pretendia..."
 "Eu rio..."
 "*RONCA*"

 hide AP3
 with dissolve

 show AP11
 with dissolve

 "Sou só eu ou meu estômago, está ficando cada vez mais barulhento?"

 hide AP11
 with dissolve

 show AP7
 with dissolve

 "Apollo me encara por um momento antes de soltar uma risada suave..."

 hide AP7
 with dissolve

 show AP2
 with dissolve

 ap "bem, eu trabalho aqui." 
 ap "Então, como posso ajudá-la, senhora?"

 hide AP2
 with dissolve

 show AP6
 with dissolve

 "Seus lábios formam um sorriso irônico quando ele diz a última palavra."

 #Teste para adicionar item
 label after_meeting_apollo:
   $ add_item(PropTeste)
   mc "Agora tenho um cachorro-quente no meu inventário."

 #stop music

 #Primeira escolha.

 menu:
   "Você é tão idiota":
      jump dumb
   "O atendimento aqui é incrível, bom senhor":
      jump drama
#Teste de deletar item
label some_other_part_of_the_game:
    $ remove_item(PropTeste)  # Remove o cachorro-quente
    mc "Eu comi o cachorro-quente."


label continuing:

 show Loja_1
 show AP6
 with dissolve

 ap "Enfim, o que será hoje?"

 hide AP6
 with dissolve

 show AP8
 with dissolve

 mc "Definitivamente, algo grande..."

 hide AP8
 with dissolve

 show AP9
 with dissolve

 mc "Estou com muita fome!!!" 
 mc "Alguma recomendação?"

 hide AP9
 with dissolve

 show AP10
 with dissolve

 ap "Bem...vamos ver."
 "Ele faz uma pausa por um momento e olha em volta."

 hide AP10
 with dissolve

 show AP6
 with dissolve

 ap "Os cachorros-quentes estão frescos...tipo, o pacote foi entregue hoje..."
 ap "Vai demorar um pouco para esquentar no forno..."
 mc "Você não pode simplesmente colocar no micro-ondas?"
 ap "Se você quiser cachorro-quente porém cru por dentro..."

 hide AP6
 with dissolve

 show AP7
 with dissolve

 "Ele sorri enquanto coloca um cachorro-quente no forno e o liga..."

 hide AP7
 with dissolve

 show AP8
 with dissolve

 mc "Ah..não."

 hide AP8
 with dissolve

 show AP1
 with dissolve

 ap "Olha, por que você não dá uma volta na loja? Provavelmente estará pronto quando você terminar de fazer compras."
 "Suspiro e olho em volta..." 
 "Por mais que eu queira procrastinar, preciso fazer as compras."
 mc "Não acho que haja outra coisa para fazer..."

 hide AP1
 with dissolve

 show AP7
 with dissolve

 ap "Não.Haha..."

 hide AP7
 with dissolve

 show AP12
 with dissolve

 #stop music

 "Antes que eu possa me virar, vejo a expressão brincalhona de Apollo se transformar em uma expressão preocupada..."
 
 hide AP12
 with dissolve

 show AP13
 with dissolve
 
 "Sigo seu olhar e vejo outra pessoa na loja..."
 "Quando ele chegou aqui? Não vi e nem ouvi mais ninguém aqui..."
 ap "Esse cara..."
 "Apollo murmurou mais alguma coisa, mas não consegui ouvir."
 mc "Você o conhece?"
 "Apollo me encarou por um momento, antes de responder..." 
 "Ele não parecia muito contente com a presença desse cara."
 ap "Não."
 "Estranho..."
 "Muito, mas muito estranho mesmo..."

 hide AP13
 with dissolve

 show AP10
 with dissolve

 "Eu me viro para sair, sentindo essa tensão estranha crescer..."

 hide AP10
 with dissolve

 show AP12
 with dissolve

 "De repente, Apolo me puxa pelo ombro, me fazendo encará-lo."
 ap "Só...só...tome cuidado, ok?"
 "Nosso clima lúdico desapareceu completamente agora..."

 hide AP12
 with dissolve

 show Loja_2
 with dissolve

 show M3
 with dissolve

 "Olho para o cara em questão, depois volto para Apollo e aceno com a cabeça..."

 hide Loja_2
 with dissolve

 show Loja_1
 with dissolve

 hide M3
 with dissolve

 "Não vi nenhum problema com esse homem, inicialmente."
 "Claro que ele não é alguém com quem eu estaria implorando para conversar, mas agora estou bastante curioso..."
 "Eles têm algum drama mal resolvido ou algo assim?"
 "De qualquer forma, preciso fazer algumas coisas aqui, não tenho tempo a perder..."
 "Se for importante, provavelmente descobrirei..."

 show Loja_2
 with dissolve

 #jump TimeSkip

 #Nesse local ficará a parte do script que tem relação ao timeskip...
 #label TimeSkip:

 #image Timeskip = Movie(play="timeskip.webp")

 jump continuing2

label continuing2:

 "*Suspira*"

 "Finalmente terminei as compras..."
 "Não demorou muito, no entanto eu gostaria de saber se o cachorro-quente está pronto."
 "Pago todas as minhas coisas e me viro para verificar Apollo..."

 #Segunda escolha:

 menu:
   "Corredor da esquerda(Artigos de jardinagem)":
      jump Left
   "Corredor da direita(Fast food)":
      jump continuing3
 
label continuing3:

 hide Loja_2

 show Loja_1

 "Limpo minha cabeça pensando no delicioso cachorro-quente me esperando nos fundos da loja."
 "Caminhando pelos corredores, rapidamente chego ao balcão novamente e vejo Apollo tirando cuidadosamente meu cachorro-quente do forno assim que me vê."

 show AP4
 with dissolve

 ap "Terminou?"

 hide AP4
 with dissolve

 show AP1
 with dissolve

 mc "Não até eu pegar meu cachorro-quente hehehe..."
 "Ele me dá o lanche e ri. Eu imediatamente dou uma mordida."

 hide AP1
 with dissolve

 show AP5
 with dissolve

 ap "É horrível, não é?"

 hide AP5
 with dissolve

 show AP13
 with dissolve

 "Apollo levanta uma sobrancelha na expectativa de um insulto..."

 hide AP13
 with dissolve

 show AP10
 with dissolve

 mc "Não é tão ruim..."
 mc "Nada de especial..."
 "Mastigo mais um pouco do lanche de sabor “ok”"

 hide AP10
 with dissolve

 show AP5
 with dissolve

 hide AP5
 with dissolve

 show AP2
 with dissolve

 ap "É o maior lanche que tenho aqui. Mas provavelmente você ficaria melhor com macarrão instantâneo"
 "Continuo comendo como se fosse o último pedaço de comida do planeta. É mais saboroso quando você está com fome, eu acho..."
 mc "Mas eu não compraria apenas macarrão… eu ainda passaria todo esse tempo fazendo compras e ainda teria que cozinhar em casa."

 hide AP2
 with dissolve

 show AP10
 with dissolve

 ap "Verdade..."
 "Nós ficamos em silêncio por alguns segundos..."
 "Eu pensei que teríamos mais coisas pra conversar depois de tanto tempo separados, mas acho que nenhum de nós consegue pensar em um assunto..."
 "Eu discretamente o examino dos pés a cabeça."
 "Pensando bem, o Apollo não parece ter mudado nada desde o ensino médio, seu rosto, seu senso de humor, tudo parece igual..."
 "Meus olhos ficam fixados no broche preso ao seu avental."

 hide AP10
 with dissolve

 show AP5
 with dissolve

 mc "Então, ainda gosta de palhaços?"
 "Eu olho para o broche de palhaço em seu avental."

 hide AP5
 with dissolve

 show AP2
 with dissolve

 ap "O que você quer dizer com “ainda”? Tipo, foi uma fase ou algo assim?"

 hide AP2
 with dissolve

 show AP13
 with dissolve

 mc "Quero dizer, você era bastante obcecado por eles durante o ensino médio."
 mc "Jardim de infância, ensino fundamental, ensino médio..."
 ap "..."

 hide AP13
 with dissolve

 show AP9
 with dissolve

 ap "Você está me fazendo parecer um esquisitão..."
 mc "Faculdade, seu primeiro emprego..."
 ap "Ok, ok, ok...já entendi."
 ap "Quer dizer... qual é, você abandonaria esse carinha?"
 "Ele aponta para o broche com uma cara suplicante."
 ap "Como eu poderia deixar esse carinha para trás?"
 "Ele faz uma cara de súplica apontando para a cara do palhaço."

 hide AP9
 with dissolve

 show AP8
 with dissolve

 "É um broche meio aleatório, especialmente se levar em conta o resto da roupa toda, mas eu o vejo desde que tinha 5 anos."
 "Seria difícil jogar fora a esse ponto."

 hide AP8
 with dissolve

 show AP6
 with dissolve

 "Eu dou uma risadinha."
 mc "Sim, acho que também não conseguiria jogar no lixo."
 "Conversamos um pouco sobre assuntos aleatórios, enquanto Apollo fica olhando para aquele homem estranho de antes."
 "O cara não parece ser um cliente comum..."
 "Ele está usando muitas camadas para uma noite de outono, além disso está gastando muito tempo escolhendo seus produtos, seu carrinho de compras ainda está bem vazio..."
 "Ele olhou para nós por cima do ombro, mas não pareceu se incomodar com os olhares constantes de Apollo."
 "Estou começando a pensar que isso é uma “interação” comum entre esses dois."
 
 #terceira escolha
 menu:
   "Perguntar qual é o problema":
      jump problem
   "Deixar para lá":
      jump lookback

 label lookback: #+10% com o Apollo

 "Ugh... eu realmente não preciso perguntar... Ele me diria se quisesse..."

 jump continuing4

 label continuing4:

 "Novamente, não estou desesperado para fazer amizade com aquele homem."
 "Não vai doer manter distância..."
 "Você sabe, só para ter certeza."
 "Um alarme repentino soa embaixo do balcão, interrompendo nosso silêncio."
 "Apollo olha para seu telefone e sua preocupação parece desaparecer..."

 show AP11
 with dissolve

 ap "Ah! Hora de te expulsar!"
 mc "Hein?"
 ap "Chama-se hora de fechar, senhora."
 "Seu sorriso irônico me pega desprevenido. E essa coisa de “senhora” de novo? Sério?"
 mc "Acho que o atendimento acaba na hora de fechar também..."

 hide AP11
 with dissolve

 show AP7
 with dissolve

 ap "Claro. Sou pago para ser legal até as 21h. Depois disso posso ser um merda..."
 "Nós dois rimos e eu arrumo minhas coisas e me preparo para sair."
 "Nós não nos falamos muito na faculdade, eu imaginava que ele se tornaria uma pessoa diferente..."
 "Mas ele parece ser exatamente o mesmo daqueles dias..."

 stop music

 play music "audio/ambience-wind-blowing-through-trees-01-186986.mp3"volume 50

 hide AP7
 with dissolve

 #Contexto: entrada externa da loja de conveniência (frente da loja - noite)

 show Casa_12

 "Cara, está escuro... Não percebi que passamos tanto tempo conversando. "
 "Não tinha planejado ficar fora até agora. "
 "Odeio voltar para casa depois de escurecer..."
 "Bom, eu não diria que odeio..."
 "É inconveniente, claro, não consigo enxergar muito bem, mesmo com as luzes da rua, sim..."
 "Mas, a noite ainda é linda."
 "Está frio, a brisa noturna sopra as folhas das árvores escuras, tornando toda a estética misteriosa..."

 #Contexto: casa do MC (pequeno estúdio - noite)

 stop music

 show Casa_4

 "Antes que eu perceba, estou em casa."
 "Entro na minha casa, lavo as mãos e começo a organizar meu armazenamento."

 #timeskip

 "Não havia muitas coisas para organizar, mas demorei um pouco mesmo assim."

 play music "audio/chuva-1-119168.mp3"volume 50

 "Começou a chover lá fora."
 "Estou cansado... "
 "É melhor dormir agora, amanhã terei um dia agitado... "
 "Provavelmente..."
 "Tomo um banho e caio na cama, adormecendo logo depois, o som da chuva me guia para um sono profundo."

 stop music
 hide Casa_4
 hide Casa_12
 hide Loja_1
 hide Loja_2
 hide Casa_10
 hide Casa_5
 hide scene_black
 hide AP9

 #timeskip

 
 #Teste de final de jogo...
 jump day_2

 #Label de créditos - final de jogo
label endgame:

 play music "audio/soundtrack/floresta.ogg"volume 5

 window hide dissolve

 show scene_credits

 $ renpy.pause(10.0)

return
