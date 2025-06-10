label Rota_Apollo:
    play music "audio/119402__kyster__nice-forrest-ambience.ogg"volume 50
    show Casa_11
    # Introdução da cena
    "Ficamos em silêncio enquanto eu penso sobre."
    "Ele realmente parece saber mais do que eu."
    "Mas ao mesmo tempo, eu também não contei a ele todos os detalhes..."
    "Eu não queria preocupá-lo."

    mc "Tudo bem mesmo eu ir?"
    show AP2
    $ persistent.unlocked_sprites.add("AP2")
    ap "Claro, não quero que corra perigo."
    show scene_black
    ap "Fique o tempo que quize-"
    mc "Olha, não foi nada de mais, ok? É só uma noite..."
    hide AP2
    show AP5
    $ persistent.unlocked_sprites.add("AP5")
    hide scene_black
    "Eu não queria soar desse jeito..."
    "É que às vezes parece que ele sempre consegue o que quer."
    "Mesmo que o que ele quer geralmente seja ajudar..."

    mc "É estranho pensar nisso, ok?"
    ap "..."
    hide AP5
    show AP8
    $ persistent.unlocked_sprites.add("AP8")
    ap "Se você realmente quer fingir que nada aconteceu, não precisamos falar sobre isso."
    ap "Finja que é uma festa do pijama, ou algo do tipo..."

    "Acho que posso fazer isso."
    "Apesar de que esse assunto não morreu completamente."
    "Digo, ele vai querer conversar sobre isso novamente alguma hora..."

    mc "Certo."
    hide AP8
    show AP6
    $ persistent.unlocked_sprites.add("AP6")
    ap "Então, vamos?"
    ap "Arrume suas coisas."
    hide AP6
    show scene_black
    with dissolve
    hide scene_black
    hide Casa_11
    # Transição para a casa do ap
    show Ap_bedroom_3
    show AP22
    $ persistent.unlocked_sprites.add("AP22")
    
    ap "Chegamos!"

    "Ele corre para a cozinha assim que entramos na casa."
    "Eu dou uma olhada rápida na sala."
    "É... bem a cara dele, de certa forma..."
    "Ele sempre teve um visual meio punk na faculdade, meio que ainda tem..."
    "Mas acho que não dá pra notar por causa do uniforme do trabalho agora..."

    ap "Pode colocar suas coisas no quarto no fim do corredor, eu pego algo pra beber..."
    "Passo pelo corredor e chego à porta."

    ap "Você gostou?"
    mc "O... o que?"
    show AP24
    $ persistent.unlocked_sprites.add("AP24")
    ap "Decorei especialmente pra você..."

    # Transição para o momento do choque
    show scene_black
    with dissolve
    "Antes que pudesse me virar, sinto algo puxar meu cabelo."
    "A última coisa que vejo é a quina da porta."
    hide scene_black
    # Personagem acorda
    "Abro os olhos lentamente..."
    mc "Ugh... minha cabeça está me matando."
    show AP19
    $ persistent.unlocked_sprites.add("AP19")
    ap "Ah... você acordou!"
    ap "Já estava pensando que tinha usado muita força..."
    ap "Mas você sempre foi resistente, não é?"

    mc "O que...?"
    mc "Ah... é mesmo... Eu... Eu estou na casa do ap..."
    mc "Eu... estou amarrado...?"

    ap "Ei? Você está ouvindo?"
    ap "Você tem que prestar atenção quando eu estou falando."

    # Escolha do jogador
    menu:
        "O que? Por quê?":
            jump why_captured
        "Isso é uma pegadinha?":
            jump prank_question
        "...":
            jump silence_response

label why_captured:
    ap "Não é óbvio?"
    ap "Diversão, excitação..."
    ap "Pra ter você..."
    ap "Porque eu posso."
    $ add_ap_points(+5)
    jump next_scene

label prank_question:
    ap "...?"
    show AP16
    $ persistent.unlocked_sprites.add("AP16")
    ap "Ppfff – HAHAHAHAHAHAHAHAHAHA!"
    $ add_ap_points(+10)
    "Ele começa a rir como se isso fosse a coisa mais engraçada do mundo."
    mc "E-eu estou falando sério!"
    "Tento me remexer, mas é impossível com as cordas..."
    mc "Isso não é engraçado..."
    ap "Haha... suas reações sempre me divertem..."
    ap "Você não cansa de ser idiota? Hahaha!"
    jump next_scene

label silence_response:
    mc "..."
    "Eu realmente não tenho reação pra isso..."
    "Isso não pode ser real..."
    "O que se diz em uma situação assim?"
    ap "Ei... está me vendo?"
    ap "Diga algo..."
    "Ele chacoalha a mão na minha frente, tentando chamar minha atenção."
    ap "Fala sério."
    $ add_ap_points(-10)
    show AP21
    $ persistent.unlocked_sprites.add("AP21")
    ap "Se eu quisesse que você ficasse em silêncio, já teria te matado, não acha?"
    jump next_scene

label next_scene:
    # Escolha do jogador
    menu:
        "Ficar em silêncio.":
            $ add_ap_points(-20)
            jump silent_end
        "Isso dói...":
            $ add_ap_points(+5)
            jump pain_reaction
        "Eu faço qualquer coisa.":
            $ add_ap_points(+10)
            jump beg_for_mercy

label silent_end:
    "Não existe nada para ser dito."
    "Eu apenas o encaro, sem conseguir acreditar em tudo o que está acontecendo..."
    show AP14
    $ persistent.unlocked_sprites.add("AP14")
    ap "Não me ignore!"
    "Sinto algo pressionar contra meu pescoço... Acho que são suas mãos..."
    hide AP14
    stop music
    jump bad_end_1

label pain_reaction:
    mc "Ack... isso dói!"
    ap "Mesmo?"
    "Ele se anima instantaneamente."
    show AP17
    $ persistent.unlocked_sprites.add("AP17")
    ap "Você fica uma gracinha quando está prestes a chorar..."
    ap "Esse era meu objetivo no início."
    ap "Mas sua expressão é boa também..."
    hide AP17
    stop music
    jump continue_scene

label continue_scene:
    "ap está sempre sorrindo. Isso é o normal dele..."
    "Mas isso..."
    "Esse sorriso... eu nunca vi."
    "É tão... genuíno."
    "Pela primeira vez, parece que ele não está sorrindo pra deixar os outros felizes, mas sim porque ele mesmo está satisfeito."
    "Muito satisfeito."
    stop music
    jump beg_for_mercy

label beg_for_mercy:
    mc "Ack... E- Eu faço qualquer coisa!"
    "Seus dedos afrouxam um pouco, apesar de ele não soltar meu cabelo completamente."
    ap "Mesmo? Qualquer coisa?"
    mc "Q-qualquer coisa! Só... por favor, não me machuque..."
    ap "Pff- haha... qualquer coisa?"
    show AP22
    ap "O que mais você acha que eu quero fazer além de te machucar?"
    hide AP22

    "Ele me encara, olhando no fundo dos meus olhos por alguns segundos."
    ap "Bem, pra começar que tal um joguinho básico?"
    "Ele se vira e anda até o outro lado da sala, mexendo nas caixas e algo que está em cima da mesa."
    ap "Afinal, você bateu a cabeça com tudo agora pouco haha..."
    ap "Vamos só nos concentrar em recuperar completamente os sentidos, ok?"
    "Isso na mão dele é..."
    ap "Eu vou fazer algumas perguntas... sobre seu dia, seu trabalho... coisas assim, você sabe."
    ap "E se você der a resposta errada..."
    "Antes que eu pudesse processar tudo o que ele estava falando, sinto algo ser atirado na minha direção com muita rapidez."
    # Aqui pode entrar uma CG de dardo na parede
    "Um... dardo!?"
    ap "Haha, digamos que é melhor responder corretamente."
    "Ele não está falando sério. Ele não pode estar..."

    ap "Primeira pergunta, hã... ah já sei, que dia é hoje?"
    "O-ok... acho que eu consigo fazer isso..."
    mc "Hoje é..."
    "..."
    "Na verdade..."
    "Agora que pare para pensar, eu não tenho certeza..."
    "Eu... Eu não me lembro... muito bem..."
    "Apollo se prepara para atirar o dardo."

    menu:
        "Quinta-feira.":
            $ add_ap_points(+5)
            $ alterar_sanidade(10)
            mc "Hã... quinta-feira?"
            "Acho que eu peguei ele de surpresa..."
            ap "Ah... sim..."
            ap "Não era o tipo de resposta que eu esperava, mas está certo..."
            "Ele repete ‘quinta-feira’ algumas vezes enquanto nega com a cabeça e rindo."
            "Ele... achou engraçado?"
            jump apollo_question_2
        "32 de dezembro.":
            $ add_ap_points(+10)
            $ alterar_sanidade(-10)
            mc "Um... 32 de dezembro..."
            ap "Pff- HAHAHAHAHAHAHAHAHA!!!"
            ap "Uau... eu devo ter batido sua cabeça muito forte mesmo..."
            "Espera... por que eu disse aquilo?"
            ap "Esperava que fosse mais resistente, é uma pena..."
            mc "N-não, espera-"
            "Antes que eu conseguisse dizer algo, Apollo atira o dardo."
            # -2 health (adicione lógica se desejar)
            "A dor do espinho se espalha pela minha perna."
            "Da primeira vez pareceu que ele estava mirando próximo ao meu rosto, mas dessa vez ele apenas atirou para frente."
            "Eu olho para a mancha de sangue se formando nas minhas roupas..."
            ap "Anime-se! Você fez o melhor que pode!"
            ap "Mesmo que tenha sido patético."
            "Ele dá um sorriso empático."
            "Como ele consegue ser tão bom ator?"
            jump apollo_question_2
        "5.":
            $ alterar_sanidade(-10)
            mc "D-dia 5...?"
            ap "Hã...? Não...?"
            ap "Isso não é nem perto da resposta certa."
            "Ele sorri como se estivesse tentando parecer empático."
            ap "Bem, regras são regras."
            "Ele atira o dardo diretamente no meu ombro."
            # -2 health (adicione lógica se desejar)
            "O espinho do dardo entrou quase que completamente no meu corpo..."
            "A dor se alastra imediatamente e sentir o sangue escorrendo torna tudo ainda pior."
            jump apollo_question_2

label apollo_question_2:
    "Apollo suspira enquanto me olha da cabeça aos pés..."
    ap "Certo... próxima pergunta."
    ap "Na verdade, agora quero testar um pouco de sinceridade haha..."
    "Engulo em seco."
    ap "O que acha de palhaços?"
    mc "O-o quê?"
    ap "Te perguntei isso uma vez há muito tempo, mas recentemente conversamos sobre isso de novo..."
    ap "Acho que sua resposta pode ter mudado, então estou curioso."
    mc "Ué, mas... se nem você sabe a resposta certa, não importa o que eu disser..."
    ap "Vou saber quando me responder."
    mc "M-mas..."
    "Ele se aproxima e toca meu queixo de leve."
    ap "Eu conheço você. Vou saber se estiver mentindo."
    "Isso vai ser difícil..."

    menu:
        "Detesto palhaços.":
            $ alterar_sanidade(-10)
            $ add_ap_points(-10)
            mc "E-eu odeio palhaços!"
            "Na mesma hora, um dardo é atirado na minha direção."
            "Mas não me atinge, ao invés disso, ele pousa na parede logo ao lado do meu pescoço."
            $ alterar_sanidade(-10)
            ap "O que foi?"
            ap "Eu não atirei em você... foi só um reflexo."
            ap "Não sou tão infantil assim."
            "Ele dá de ombros, mas parece que ele ficou meio magoado."
            "Geralmente, em momentos como esse, eu o provocaria um pouco..."
            "Nós sempre ríamos disso..."
            "Nós... Eu e o Apollo..."
            "Esse homem... não pode ser o Apollo..."
            $ alterar_sanidade(-10)
            jump apollo_next
        "Amo palhaços.":
            $ alterar_sanidade(-10)
            $ add_ap_points(+5)
            mc "Eu gosto de palhaços... adoro eles-"
            "Antes que eu pudesse terminar de falar, ele atira um dardo na minha coxa."
            "Por que tem que doer tanto?"
            "Tento pensar nisso como uma injeção ou algo do tipo... mas o espinho é muito pior."
            ap "O que foi? Realmente achou que eu ia cair nessa?"
            ap "Apesar que... eu fico um pouco feliz que você queira me agradar ~❤️"
            ap "Mas você já deveria saber que me agradar não te protege de nada ~❤️"
            "Ele se agacha na minha frente."
            ap "Se realmente quiser me deixar feliz, nós podemos esquecer esse jogo e ir logo pra parte que você implora pela sua vida..."
            "A sua mão dá um pequeno empurrão no dardo preso na minha coxa, fazendo o espinho se mexer na minha carne."
            ap "Como eu disse antes, eu quero sinceridade, ok?"
            jump apollo_next
        "Nunca pensei sobre.":
            $ alterar_sanidade(-10)
            $ add_ap_points(-10)
            mc "Ah... bem, eu... nunca pensei sobre isso..."
            ap "..."
            "Ele fica em silêncio por alguns longos segundos antes de atirar o dardo na minha coxa."
            ap "Você está brincando, certo?"
            "Ele chega mais perto e pressiona o dardo contra minha carne."
            ap "Você ouviu o que eu disse?"
            ap "Você literalmente já pensou sobre isso antes. Já tivemos essa conversa!"
            mc "Ack! E-eu... Aahh!"
            "Eu não consigo pensar direito com ele mexendo o espinho."
            "Apollo segura o último dardo próximo ao meu pescoço."
            ap "Estou tentando fazer algo divertido pra nós aqui."
            jump apollo_next

label apollo_next:
    "Apollo observa minha reação, sorrindo de um jeito estranho."
    ap "Vamos para a próxima pergunta, então."
    ap "Sobre aquela noite... você lembra quem invadiu sua casa?"
    "Meu coração dispara. Eu hesito."
    menu:
        "Não vi o rosto.":
            $ alterar_sanidade(-10)
            mc "Eu... não vi o rosto."
            ap "Hmm... que pena. Eu esperava que você lembrasse de algo útil."
            "Ele parece decepcionado, mas logo volta a sorrir."
            jump apollo_fingers
        "Acho que era alguém do trabalho.":
            $ alterar_sanidade(-15)
            mc "Acho que era alguém do trabalho..."
            ap "Sério? Interessante... mas não parece muito certo."
            "Ele gira um dardo nos dedos, pensativo."
            jump apollo_fingers
        "Prefiro não falar sobre isso.":
            $ alterar_sanidade(-20)
            mc "Prefiro não falar sobre isso."
            ap "Você nunca facilita, né?"
            "Ele lança um olhar frio, mas não insiste."
            jump apollo_fingers

label apollo_fingers:
    ap "Agora, quantos dedos eu estou mostrando?"
    "Ele levanta a mão, mas minha visão está turva."
    menu:
        "Cinco.":
            $ alterar_sanidade(-5)
            mc "Cinco..."
            ap "Errado!"
            "Ele atira um dardo, que acerta de raspão seu braço."
            # -2 health
            jump apollo_envelope
        "Três.":
            $ alterar_sanidade(-10)
            mc "Três..."
            ap "Quase, mas não."
            "Outro dardo, dessa vez mais perto da perna."
            # -2 health
            jump apollo_envelope
        "Nenhum.":
            $ alterar_sanidade(-5)
            mc "Nenhum..."
            ap "Hahaha, criativo, mas não."
            "Ele ri e joga o dardo na parede, perto da sua cabeça."
            jump apollo_envelope

label apollo_envelope:
    "De repente, Apollo para e olha para a porta."
    ap "Ah, parece que chegou algo para você."
    "Ele pega um envelope e joga em sua direção."
    "O envelope está manchado de algo escuro... sangue?"
    ap "Vai, abre. Pode ser importante."
    "Com dificuldade, abro o envelope."
    "Dentro, há uma carta com letras recortadas de revista: 'VOCÊ NÃO ESTÁ SEGURO. ELE ESTÁ AQUI.'"
    mc "O que... é isso?"
    ap "Acho que alguém está preocupado com você. Ou talvez só queira brincar."
    "Sinto um frio na espinha. Apollo observa cada reação minha, divertido."

    menu:
        "Pedir para ir embora.":
            $ alterar_sanidade(-10)
            mc "Apollo... por favor, posso ir embora?"
            ap "Agora? Depois de tudo isso? Não seja ingrato."
            "Ele se aproxima, ameaçador."
            jump apollo_final_choices
        "Ficar em silêncio.":
            $ alterar_sanidade(-10)
            mc "..."
            ap "Silêncio de novo? Você nunca aprende."
            "Ele suspira, mas não faz nada por enquanto."
            jump apollo_final_choices
        "Perguntar sobre o envelope.":
            $ alterar_sanidade(-5)
            mc "Você sabia desse envelope?"
            ap "Talvez. Talvez não. O que importa é: você está aqui comigo."
            "O sorriso dele é assustadoramente sincero."
            jump apollo_final_choices

label apollo_final_choices:
    "Apollo se aproxima, olhando fundo nos meus olhos."
    ap "Última pergunta: se você pudesse desejar qualquer coisa agora, o que seria?"
    menu:
        "Quero ir para casa.":
            $ alterar_sanidade(-20)
            $ add_ap_points(-10)
            mc "Eu só quero ir para casa..."
            ap "Casa? Hm... não sei se posso deixar você ir."
            jump apollo_final_1
        "Quero que tudo isso acabe.":
            $ alterar_sanidade(-25)
            $ add_ap_points(-10)
            mc "Quero que tudo isso acabe."
            ap "Acabar? Isso depende só de você."
            jump apollo_final_2
        "Quero que o perseguidor suma.":
            $ alterar_sanidade(-15)
            $ add_ap_points(+5)
            mc "Quero que o perseguidor suma."
            ap "Talvez eu possa ajudar com isso... ou talvez não."
            jump apollo_ending_3

label apollo_ending_3:
    # Final onde Apollo mostra a cabeça do Max
    show AP19
    $ persistent.unlocked_sprites.add("AP19")
    "Apollo ri, pega algo atrás de si e joga aos meus pés."
    "É... a cabeça do Max."
    ap "Agora você está seguro. Ninguém mais vai te incomodar."
    "O horror toma conta de mim enquanto Apollo sorri satisfeito."
    jump endgame

label apollo_final_1:
    show AP19
    $ persistent.unlocked_sprites.add("AP19")
    ap "Heh... desculpa, acho que bati sua cabeça muito forte antes."
    ap "Bom, o jogo não tem graça se você não consegue pensar, não é?"
    "Apollo respira fundo."
    ap "Bem, acho que acabamos por hoje..."
    "Ele se levanta e guarda os dardos restantes no lugar."
    mc "O- o que vai fazer?"
    ap "Você quer dizer agora?"
    ap "Nada."
    ap "Por que não descansa um pouco?"
    "Ele se aproxima, segurando meu queixo."
    "Em um movimento rápido, ele empurra minha cabeça para trás com toda força, batendo meu crânio contra o encosto da cadeira."
    play sound "audio/wood_break.ogg"
    ap "Parece que eu bati sua cabeça muito forte dessa vez."
    jump apollo_final_1_5

label apollo_final_1_5:
    show AP19
    $ persistent.unlocked_sprites.add("AP19")
    "Ugh... minha cabeça dói..."
    "Ah... eu... eu estava dormindo?"
    "Ouço passos."
    mc "Apollo...?"
    ap "Oiê! Bom dia!"
    "Ele parece segurar um envelope amassado."
    ap "Hã, nossa, você está horrível hoje..."
    mc "Minha cabeça dói..."
    ap "Ah... sim, isso."
    "Ele me olha de cima a baixo, como se estivesse me examinando."
    "Murmura algo sobre perda de sangue, mas não dá pra escutar com a minha cabeça latejando."
    ap "Heh... desculpa, acho que bati sua cabeça muito forte antes."
    ap "Bom, a surpresa não tem graça se você não consegue pensar, não é?"
    "Apollo respira fundo."
    ap "Bem, acho que acabamos por hoje..."
    mc "O- o que vai fazer?"
    ap "Você quer dizer agora?"
    ap "Nada."
    ap "Por que não descansa um pouco?"
    "Ele se aproxima, segurando meu queixo."
    "Em um movimento rápido, ele empurra minha cabeça para trás com toda força, batendo meu crânio contra o encosto da cadeira."
    play sound "audio/wood_break.ogg"
    ap "Parece que eu bati sua cabeça muito forte dessa vez."
    jump endgame

label apollo_final_2:
    show AP19
    $ persistent.unlocked_sprites.add("AP19")
    $ add_ap_points(+10)
    mc "Eu... eu quero ficar."
    "Provavelmente é a melhor opção."
    "Apollo é um psicopata."
    "Não importa como me sinto, é a verdade."
    "Não sei as intenções do invasor, mas sei que ele não vai me matar."
    "Tenho certeza disso... Não é?"
    "Apollo sorri."
    ap "É a melhor opção, realmente..."
    ap "Vamos nos divertir muito."
    jump endgame