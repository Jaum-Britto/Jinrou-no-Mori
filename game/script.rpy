# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

#Introduce the game in the script area.

# The game starts here.

label start:

 scene scene_black

 #script de escolha de nome:

 $ povname = renpy.input("Escolha o seu Nome:", length = 6)
 $ povname = povname.strip()

 if not povname:
    $ povname =  "Sam"

 #o script acaba aqui....

 stop music

 play music "audio/119402__kyster__nice-forrest-ambience.ogg"volume 150

 scene scene_1
 with dissolve
 

 mc "Mais um dia de trabalho terminou. Finalmente, um pouco de descanso..."
 mc "Pelo menos até o próximo projeto..."

 hide scene_1

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

 show scene_2
 with dissolve

 "Saio de casa e caminho pela vizinhança, em direção à loja..."
 "Não há muito para ver por aqui, exceto o sorriso amigável dos poucos vizinhos que tenho..."
 "O número de pessoas que se mudaram daqui foi a razão pela qual eu posso me dar ao luxo de viver aqui, então eu deveria estar grato por isso..."

 hide scene_2
 with dissolve

 stop music

 play music "audio/657265__ho52nest__wellcome-supermarket-background-music.ogg"volume 50

 show scene_5
 with dissolve

 "Chego à loja bem rápido, o tempo sempre voa quando estou perdido em pensamentos, talvez isso se aplique também às distâncias..."
 "A loja está quase completamente deserta. Sou só eu, o caixa da frente e o do café..."
 "*Ronca*"
 "..."
 "É melhor eu pegar esse lanche de uma vez..."
 "Ando em direção à pequena área do café nos fundos da loja, anotando mentalmente todas as coisas que preciso reabastecer quando terminar de comer..."

 hide scene_5
 with dissolve

 show scene_4
 with dissolve

 show scene_3
 with dissolve
 
 "Assim que chego ao balcão, sou recebido com um sorriso familiar."

 show AP1
 with dissolve

 ap "[povname]! Faz muito tempo que não te vejo, né?"
 "É o Apollo..."
 "Um velho amigo. Ele costumava ser meu colega de classe no ensino médio..."
 "Ele sempre esteve ao meu lado desde que nos conhecemos. De alguma forma, nunca nos distanciamos realmente. Na verdade, eu nunca teria ouvido falar deste lugar se não fosse por ele..."
 mc "Apollo! Ótimo ver você! Eu não sabia que você estaria aqui."
 ap "uh...por que não? Eu trabalho aqui..."
 "Ele ri como se isso fosse óbvio..."
 mc "Sim, bem, agora eu sei disso."
 "Eu dou uma risada e ele sorri para mim confuso."
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
 "Sou só eu ou meu estômago, está ficando cada vez mais barulhento?"
 "Apollo me encara por um momento antes de soltar uma risada suave..."
 ap "bem, eu trabalho aqui." 
 ap "Então, como posso ajudá-la, senhora?"
 "Seus lábios formam um sorriso irônico quando ele diz a última palavra."

 stop music

 #Primeira escolha.

 menu:
   "Você é tão idiota":
      jump dumb
   "O atendimento aqui é incrível, bom senhor":
      jump drama

label continuing:

 show scene_4
 show scene_3
 show AP1
 with dissolve

 ap "Enfim, o que será hoje?"
 mc "Definitivamente, algo grande..."
 mc "Estou com muita fome!!!" 
 mc "Alguma recomendação?"
 ap "Bem...vamos ver."
 "Ele faz uma pausa por um momento e olha em volta."
 ap "Os cachorros-quentes estão frescos...tipo, o pacote foi entregue hoje..."
 ap "Vai demorar um pouco para esquentar no forno..."
 mc "Você não pode simplesmente colocar no micro-ondas?"
 ap "Se você quiser cachorro-quente porém cru por dentro..."
 "Ele sorri enquanto coloca um cachorro-quente no forno e o liga..."
 mc "Ah..não."
 ap "Olha, por que você não dá uma volta na loja? Provavelmente estará pronto quando você terminar de fazer compras."
 "Suspiro e olho em volta..." 
 "Por mais que eu queira procrastinar, preciso fazer as compras."
 mc "Não acho que haja outra coisa para fazer..."
 ap "Não.Haha..."

 stop music

 "Antes que eu possa me virar, vejo a expressão brincalhona de Apollo se transformar em uma expressão preocupada..."
 
 hide AP1
 with dissolve

 show AP3
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
 "Eu me viro para sair, sentindo essa tensão estranha crescer..."
 "De repente, Apolo me puxa pelo ombro, me fazendo encará-lo."
 ap "Só...só...tome cuidado, ok?"
 "Nosso clima lúdico desapareceu completamente agora..."
 "Olho para o cara em questão, depois volto para Apollo e aceno com a cabeça..."
 "Não vi nenhum problema com esse homem, inicialmente."
 "Claro que ele não é alguém com quem eu estaria implorando para conversar, mas agora estou bastante curioso..."
 "Eles têm algum drama mal resolvido ou algo assim?"
 "De qualquer forma, preciso fazer algumas coisas aqui, não há tempo a perder..."
 "Se for importante, provavelmente descobrirei..."

 hide AP3
 with dissolve

 show scene_5
 with dissolve

 #Nesse local ficará a parte do script que tem relação ao timeskip...
 #label TimeSkip:
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

 "Limpo minha cabeça pensando no delicioso cachorro-quente me esperando nos fundos da loja."
 "Caminhando pelos corredores, rapidamente chego ao balcão novamente e vejo Apollo tirando cuidadosamente meu cachorro-quente do forno assim que me vê."
 ap "Terminou?"
 mc "Não até eu pegar meu cachorro-quente hehehe..."
 "Ele me dá o lanche e ri. Eu imediatamente dou uma mordida."
 ap "É horrível, não é?"
 "Apollo levanta uma sobrancelha na expectativa de um insulto..."
 mc "Não é  tão ruim..."
 mc "Nada de especial..."
 "Mastigo mais um pouco do lanche de sabor “ok”"
 ap "É o maior lanche que tenho aqui. Mas provavelmente você ficaria melhor com macarrão instantâneo"
 "Continuo comendo como se fosse o último pedaço de comida do planeta. É mais saboroso quando você está com fome, eu acho..."
 mc "Mas eu não compraria apenas macarrão… eu ainda passaria todo esse tempo fazendo compras e ainda teria que cozinhar em casa."
 ap "Verdade..."
 "Nós ficamos em silêncio por alguns segundos..."
 "Eu pensei que teríamos mais coisas pra conversar depois de tanto tempo separados, mas acho que nenhum de nós consegue pensar em um assunto..."
 "Eu discretamente o examino dos pés a cabeça."
 "Pensando bem, o Apollo não parece ter mudado nada desde o ensino médio, seu rosto, seu senso de humor, tudo parece igual..."
 "Meus olhos ficam fixados no broxe preso ao avental."
 mc "Então, ainda gosta de palhaços?"
 "Eu olho para o broche de palhaço em seu avental."
 

 #Teste de final de jogo...
 jump endgame

label endgame:

 window hide dissolve

 pause 1.0

 show scene_credits

 $ renpy.pause(4.0)

return
