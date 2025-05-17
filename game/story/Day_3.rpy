label day_3:
    show text "{size=100}Dia 3{/size}" at truecenter with dissolve
    pause 2
    hide text with fade

    play music "audio/119402__kyster__nice-forrest-ambience.ogg" volume 50
    show screen hud

    "Ficamos em silêncio enquanto penso sobre tudo."
    "Apollo realmente parece saber mais do que eu, mas também não contei todos os detalhes..."
    "Não queria preocupá-lo. Não preciso de babá."
    "Provavelmente só esqueci a porta aberta e algum cachorro entrou... ou..."
    "Ugh, não sei, mas simplesmente ir pra casa dele soa um tanto extremo demais."
    "Acabamos de nos reencontrar depois de pelo menos 2 anos..."
    "Apesar de ter ficado com medo ontem, sinto que nada aconteceu."
    "Digo, ainda estou aqui. Não me machuquei nem nada do tipo."

    mc "Não se preocupe tanto. Até porque nada aconteceu."
    ap "E você quer esperar acontecer?"
    mc "É bom saber que posso contar com você, mas isso parece um pouco exagerado…"
    ap "…"
    "Ele pensa por alguns segundos. Sua expressão de preocupação relaxa."
    ap "Você não gosta de pedir ajuda, né? Não mudou nada..." # letra pequena
    "Apesar desse sorriso de derrota, ele não parece completamente convencido."
    ap "Eu vou dar uma olhada aqui hoje à noite também, okay?"
    mc "Uh… certo, faz sentido."
    "Ele se vira e sai sem dizer mais nada."
    "Eu realmente não esperava esse tipo de preocupação dele. Ele nunca foi do tipo de se envolver muito."
    "Parece que ele mudou um pouco então."
    "…"
    "Onde eu estava? Ah sim, minha caminhada pra esparecer."
    "Essa conversa me deixou um mais leve, na verdade. É bom saber que posso contar com alguém por aqui."
 
    show Timeskip
    $ renpy.pause(2.0)
    hide Timeskip
    
    "Eu ando por alguns minutos, sem um destino predefinido."
    "Ando, e ando…"
    "É um pouco reconfortante andar por essa rua."
    "As árvores do início da floresta são grandes e bonitas. O cheiro de grama é uma das melhores coisas que meu nariz já viu."
    "…"
    "Cada vez que desvio o olhar para as árvores, elas parecem mais chamativas."
    "É estranho, mas a impressão que tenho é de que a floresta está me atraindo de alguma forma."
    "Bem, há uma trilha mais à frente."
    "Não é um destino turístico, nem nada. Acho que nunca vi alguém entrar aí, na verdade."
    "Provavelmente porque não tem nada de interessante."
    "E todos na região já devem ter visto o mesmo monte de mato, então não voltariam pra ver de novo…"
    "Bem… eu não vi, então…"
    "Eu entro na trilha."
    "Ando por menos de 10 minutos até perceber que ela simplesmente acaba no meio do nada."
    "Andei rápido demais? Não, estava andando bem devagar… aproveitando a paisagem e tal."
    "Huh… estranho."
    "Estou prestes a me virar e ir embora, quando uma árvore me chama a atenção."
    "Não há nada de especial nela. Apenas parece ser o caminho certo…"
    "…"
    "Acho que contanto que eu me lembre dela, tudo bem entrar."
    "Essa floresta não é tão grande certo? É um bosque, não? Algo assim?"
    "Tenho certeza que se andar o suficiente, provavelmente vou chegar a uma rua do outro lado…"
    "Eu passo pela árvore."

    menu:
        "O que fazer com a árvore?"
        "Marcar árvore.":
            $ alterar_sanidade(-10)
            $ max_pontos += 2  # Pequena afinidade por cautela
            $ marcou_arvore = True
            "Quero ter certeza de onde estou e de onde vim, é melhor marcar a árvore de alguma forma."
            "Pego minha chave de casa e faço um risco na casca da árvore, fazendo uma seta apontando a direção da rua."
            "Isso provavelmente é suficiente."
        "Eu vou me lembrar.":
            $ alterar_sanidade(10)
            $ max_pontos -= 1  # Menos afinidade por confiar só em si
            $ marcou_arvore = False
            "Essa árvore parece bem marcante pra mim, e como eu disse, esse bosque não é tão grande, não tem um risco real de me perder aqui."

    # Floresta profunda
    scene floresta_profunda
    "Ando pelo que parece ter sido poucos minutos e o cenário parece ter mudado por completo."
    "As árvores ficam mais altas e é difícil ver o céu…"
    "Por que está tão escuro? Não está de manhã?"
    "Não andei tanto, certo?"
    "Provavelmente deveria voltar."
    "Quando olho pra trás, não consigo reconhecer nenhuma das árvores…"
    "A floresta parece tão profunda, não importa a direção que eu olhe."
    "Não consigo ver a trilha…"
    "…"
    "O que eu faço agora?"

    menu:
        "Para onde ir?"
        "Direita.":
            jump floresta_direita
        "Esquerda.":
            jump floresta_esquerda
        "Seguir em frente.":
            jump floresta_frente
        "Voltar.":
            jump floresta_voltar
        "Gritar.":
            jump floresta_gritar

label floresta_direita:
    "Me viro para a direita e sigo reto."
    jump floresta_loop

label floresta_esquerda:
    "Me viro para a esquerda e sigo reto."
    jump floresta_loop

label floresta_frente:
    "Não tenho muitas opções… devo acabar na cidade apenas seguindo em frente. Certo? Não é tão grande… não é tão grande…"
    "Sigo em frente."
    jump floresta_loop

label floresta_voltar:
    "Eu devo voltar de qualquer forma. Se eu der meia volta, é apenas lógico que eu volte para a trilha em algum momento."
    "Dou meia volta e sigo pela direção de onde vim."
    jump floresta_loop

label floresta_gritar:
    mc "TEM ALGUÉM AÍ?"
    "…"
    "Não tem resposta. Parece que o som nem mesmo saiu dessa área…"
    "A cidade está logo ali… ninguém ouviu?"
    "Talvez eu esteja próxima da rua o suficiente para pensarem que isso é uma piada ou algo assim…?"
    jump day_3_flor_loop

label floresta_loop:
    "Eu não acho que fiz muito progresso…"
    "Andei bastante dessa vez, já deveria ter chegado em algum lugar, visto alguém…"
    "Ah… aquela é a árvore que marquei?"
    "Essa sensação de… quase nostalgia… sinto que já vi essa árvore antes."
    "Ela era assim mesmo?"
    "Eu me aproximo da árvore em questão e ela é exatamente a árvore que vi antes."
    "Ela estava aqui? Aqui mesmo?"
    "Parece que estou cada vez me afundando mais nessa floresta, como essa árvore está aqui?"
    "A marca que fiz… é exatamente igual."
    "Mas, eu não sei… a sensação é diferente. Não é igual…"
    "…"
    "..."
    "Um vulto e barulho de galho."
    "O que foi isso?"
    "Isso já está ficando perturbador."
    "Onde eu estou?"
    "Instintivamente me afasto das árvores atrás de mim."
    "A esse ponto é melhor apenas continuar me movendo."
    "…"
    "Por que inventei de entrar nesse lugar?"
    scene floresta_profunda2
    "Esse som, esse cheiro… esse silêncio…"
    # Aqui pode entrar um gif de alucinação, se desejar
    "É muito parecido com o que vi no meu quarto ontem…"
    "É calmo, mas… parece artificial."
    "Esse lugar todo, de repente, fica irreconhecível."
    "Onde eu entrei?"
    "..."
    "Essas duas pedras…"
    # Aqui pode entrar uma CG das pedras
    "…"
    "Esquisitas pra cacete."
    # Fade para preto
    scene scene_black
    "..."
    "..."
    # Timeskip para o porão do Max
    
    show Timeskip
    $ renpy.pause(2.0)
    hide Timeskip
    
    scene porao_max
    "Hã? O que?"
    "Olho ao meu redor e não estou mais na floresta."
    "Isso parece uma casa, mas definitivamente não é a minha."
    "..."
    "Eu tento me mover e percebo que estou preso a uma cadeira."
    "O que? O que isso significa?"
    "Parece uma corda bem longa, colando meu pescoço, pulsos, cintura e calcanhares a uma cadeira de madeira… tem muitos nós…"
    "Eu realmente não consigo sair!"
    "..."
    "A pessoa fazendo esse som… ela me prendeu aqui?"
    "Isso não pode estar acontecendo! Quer dizer, por que eu!?"
    "Quem faria isso? Quem faria isso comigo?"
    "..."
    "Já está aqui…"
    "..."
    "Ouço o som de tranca e porta abrindo."
    max "…"
    max "Ah!"
    max "V-você já acordou…"
    "Ele parece mais surpreso do que eu."

    menu:
        "O que fazer?"
        "Gritar.":
            $ alterar_sanidade(5)
            $ max_pontos -= 20  # Gritar assusta Max, reduz afinidade
            mc "AAAAAAAAAAAAAAAAAAAAAAAAAAH!"
            "Antes que eu pudesse pensar em algo pra dizer, um grito estridente escapa da minha garganta."
            "Ele se afasta e imediatamente cobre as orelhas com as mãos…"
            max "Tudo bem, eu esperava por isso…"
            $ alterar_sanidade(-10)
            jump interrogatorio_max
        "\"O que está acontecendo?\"":
            $ max_pontos -= 10  # Confrontar reduz afinidade
            mc "Quem é você? O-o que você quer? O que está acontecendo!?"
            "Ele parece ter ficado bem desorientado com as perguntas."
            max "…não pense muito nisso."
            max "Você deve ficar okay, eu acho…"
            jump interrogatorio_max
        "\"Me desamarre!\"":
            $ max_pontos -= 5  # Exigir reduz afinidade
            $ alterar_sanidade(-10)
            mc "Me desamarre agora!"
            max "…"
            max "Não."
            jump interrogatorio_max
        "Não dizer nada.":
            $ max_pontos += 10  # Calma aumenta afinidade
            $ alterar_sanidade(-10)
            "Eu fico em silêncio por um momento, quase paralisado."
            "Nós ficamos só nos encarando por longos segundos…"
            jump interrogatorio_max

label interrogatorio_max:
    "Ele respira fundo como se estivesse tentando organizar os pensamentos."
    max "Você parece ter muitas perguntas…"
    "Ele faz uma pausa."
    max "O meu nome é Max…"

    menu:
        "Se apresentar?"
        "Se apresentar.":
            $ max_pontos += 10  # Sinceridade aumenta afinidade
            mc "O meu é [povname]."
            "A calda dele se mexe com animação e um pouco de surpresa."
            max "Sim, exatamente…"
            "Ele sorri parecendo aliviado com alguma coisa."
            max "Bem, agora que já nos conhecemos o resto será bem mais fácil…"
            jump proximo_evento
        "Não dizer nada.":
            $ alterar_sanidade(-10)
            $ max_pontos -= 5  # Frieza reduz afinidade
            "Ele realmente espera que dizer isso vai simplesmente resetar tudo o que aconteceu?"
            "O que ele acha que vai conseguir com isso?"
            "Não acho que seja seguro dar qualquer informação pra-"
            max "Tudo bem, eu já sei o seu nome…"
            jump proximo_evento

label proximo_evento:
    if max_pontos < 30:
        jump max_baixa_afinidade
    elif max_pontos == 30:
        jump max_media_afinidade
    else:
        jump max_alta_afinidade

# Fim do Day 3. Continue daqui para os próximos eventos.