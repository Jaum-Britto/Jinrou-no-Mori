#desbloqueia as imagens de max na galeria.

label Rota_Max:
    show porao_max_noite
    show screen hud
    show M01 at center
    $ persistent.unlocked_sprites.add("M01")
    "Acordo, confuso, preso a uma cadeira. Cordas apertam meu corpo, impossibilitando qualquer movimento."
    "Max está ali, me observando em silêncio."
    show M3 at center
    $ persistent.unlocked_sprites.add("M3")
    max "…"
    "Ele parece mais surpreso do que eu."

    if max_pontos < 30:
        jump max_baixa_afinidade
    elif max_pontos == 30:
        jump max_media_afinidade
    else:
        jump max_alta_afinidade

label max_baixa_afinidade:
    menu:
        "O que fazer?"
        "Se apresentar (+10 max pontos)":
            $ max_pontos(+10)
            show M2 at center
            $ persistent.unlocked_sprites.add("M2")
            "Ele está agindo de maneira bem razoável… pra um sequestrador…"
            "Provavelmente é melhor só ir na dele por enquanto."
            mc "O meu é [povname]."
            show M3 at center
            max "Sim, exatamente…"
            show M2 at center
            "Ele sorri parecendo aliviado com alguma coisa."
            max "(letra pequena) isso foi mais fácil do que pensei…"
            jump max_baixa_continua
        "Não dizer nada (-10 sanidade)":
            $ alterar_sanidade(-10)
            show M4 at center
            $ persistent.unlocked_sprites.add("M4")
            "Ele realmente espera que dizer isso vai simplesmente resetar tudo o que aconteceu?"
            "O que ele acha que vai conseguir com isso?"
            "Não acho que seja seguro dar qualquer informação pra-"
            max "Tudo bem, eu já sei o seu nome…"
            max "O resto resolvemos depois..."
            jump max_baixa_continua

label max_baixa_continua:
    show M5 at center
    $ persistent.unlocked_sprites.add("M5")
    "Antes que eu pudesse reagir, ele se vira e sai da sala."
    "Ouço o som de várias trancas sendo fechadas atrás da porta…"
    "Ele não deve voltar tão cedo…"
    "É um bom momento para analisar a situação."
    "No momento, não posso me mexer. Preciso me livrar dessas cordas antes."
    "Ele não parece ameaçador, na verdade, parece bastante razoável…"
    "Talvez eu consiga convencê-lo a me soltar…"
    show Timeskip
    $ renpy.pause(2.0)
    hide Timeskip
    "Já faz algumas horas que estou aqui..."
    "O que há com aquele cara?"
    "Novamente ouço o som das trancas atrás da porta."
    "E ele aparece."
    show M6 at center
    $ persistent.unlocked_sprites.add("M6")
    "Max não parece muito interessado em conversar dessa vez."
    "Ele pega algo atrás da cortina e come. Parecia um remédio."
    "Ele apenas passa por mim sem dizer uma palavra e se senta à mesa..."
    "Abrindo a gaveta da mesa, tem vários pedaços de madeira."
    "Ele pega um e começa a arranhá-lo. Parece uma pequena escultura no formato de uma pessoa..."
    "Ah... acho que ele percebeu que eu estou olhando."
    show M7 at center
    $ persistent.unlocked_sprites.add("M7")
    max "Hã... isso é..."
    max "Bem... você sabe..."
    mc "O Apollo...?"
    max "Ah... eu não sei o nome..."
    "Max fica um pouco tenso, como se eu tivesse descoberto um segredo."
    mc "Ele trabalha na loja de conveniência..."
    max "Sim."
    show M2 at center
    max "Max: o rosto dele é um pouco estranho você não acha?"
    max "Digo... os olhos coloridos e aquelas coisinhas na bochecha...eee..."
    "Que papo é esse?"
    max "Eu não sabia que humanos poderiam ter aparências tão diferentes como a dele."
    max "É curioso..."
    "‘Humanos’? Ele fala como se não fosse um..."
    "Apesar de que, as orelhas e a cauda realmente não são nem um pouco humanas."
    mc "Você quer dizer... maquiagem?"
    "Ele parece bem confuso."
    mc "‘Humanos’ realmente não tem essa aparência naturalmente. Ele usa maquiagem pra isso."
    max "Ah... mas... então os olhos dele não são de cores diferentes?"
    mc "Oh isso é real... mas o resto não. A sombra roxa e os pontinhos na bochecha, não."
    max "Ah... certo."
    "Ele arranha um pouco mais a escultura. Dessa vez eu posso ver que ele está usando as unhas para fazer isso."
    "Ok. Esse cara realmente não é humano."

    menu:
        "Perguntar se é humano (-5 sanidade)":
            $ alterar_sanidade(-5)
            show M8 at center
            $ persistent.unlocked_sprites.add("M8")
            mc "Hã... Max."
            "Ele não se vira, apenas move os olhos para minha direção, sem parar de esculpir."
            mc "Você não é humano certo?"
            mc "Quer dizer, você falou do Apollo como se –"
            max "Você gosta mesmo de repetir o nome dele, não?"
            "Por um segundo, achei que ele continuaria, mas..."
            "Ele balança a cabeça como se não quisesse ter dito isso."
            max "Não sou..."
            $ alterar_sanidade(-5)
            jump max_baixa_humano
        "Perguntar o que Max é (-10 sanidade)":
            $ alterar_sanidade(-10)
            show M9 at center
            $ persistent.unlocked_sprites.add("M9")
            mc "Hã... Max."
            "Ele não se vira, apenas move os olhos para minha direção, sem parar de esculpir."
            mc "Você não é humano certo? O que... você é...?"
            max "Não pense muito sobre isso."
            jump max_baixa_humano

label max_baixa_humano:
    menu:
        "Você parece humano pra mim... (+10 max pontos)":
            $ max_pontos(+10)
            show M2 at center
            mc "Bem... você parece bem humano pra mim..."
            "Talvez eu consiga ganhar a confiança dele assim..."
            "Max pensa por um momento."
            "Acho que ele não esperava por essa resposta."
            max "Mas não sou."
            max "Não se confunda."
            show M4 at center
            "Ele solta uma risada baixa, mas é estranha, sem calor. Coloca a escultura na gaveta com um movimento rápido, como se fosse esconder algo mais do que apenas o objeto. Suas mãos tremem um pouco ao fechar a gaveta."
            jump max_baixa_continua2
        "Não dizer nada":
            show M5 at center
            "Ok... isso era óbvio, mas essa resposta só deixa a situação mais estranha."
            jump max_baixa_continua2

label max_baixa_continua2:
    # Diálogo sobre humanos, curiosidade, solidão, etc.
    "..."
    # Pule para a parte do ritual e morte, pois afinidade é baixa
    jump max_final_1

label max_final_1:
    show caverna
    show M010 at center
    $ persistent.unlocked_sprites.add("M010")
    "Parece mais uma caverna..."
    "É úmido, escuro..."
    "Eu estou amarrado de novo. Mas as cordas estão muito mais apertadas."
    "Meus pulsos estão posicionados acima da altura da cabeça, os braços estão esticados..."
    "Meu corpo está exausto, mas a dor é o que mais me domina."
    "E há algo mais no ar… algo que se move, que respira junto comigo."
    "Eu o vejo então, movendo-se na penumbra. Max."
    "Ele está diferente. Seus olhos brilham com uma intensidade estranha, e seus movimentos são rápidos, nervosos."
    "Ele para na escuridão e pega algo que eu não consigo identificar à primeira vista. Um peso na sua mão. Algo… grande."
    "A pele de um lobo, ainda fresca, com os pelos espessos e os olhos quase vívidos, como se o animal ainda vivesse."
    "Eu vejo os olhos do lobo, mortos, mas de algum modo, eles ainda estão me observando."
    "Max não me olha. Ele se aproxima e começa a se mover de forma frenética."
    "Ele rasga a pele do lobo com as unhas de dentes... Destroçando como se não fosse nada."
    "Ele começa com os meus braços. O corte é rápido, preciso. Suas garras deslizam através da minha carne, rasgando minha pele com uma dor que me faz gritar."
    "Mas ele não para. Max não se importa com o som que sai de minha garganta. Ele continua a trabalhar, a pele do lobo já pronta, esperando."
    max "Você vai entender..."
    "A voz dele não soa como de costume. Está baixa, rouca, mais como um rosnado."
    "Ele pega o pedaço de pele de lobo e a coloca sobre a carne exposta do meu braço, pressionando com força, como se fosse necessário selar a ferida dessa maneira."
    "A sensação é estranha, a carne fria contra a minha pele quente. Eu sinto a pele do animal grudando em mim, em uma fusão grotesca, e a dor nas minhas feridas é insuportável."
    mc "M-max-!"
    "Não há mais nada que eu consiga dizer. Gritos desesperados são a única coisa que escapa da minha garganta."
    "Ele vai mais longe. No meu peito, ele faz um corte profundo, um corte em forma de V, e o sangue escorre, quente e espesso."
    "Ele pega mais pele do lobo e começa a cobrir a ferida, quase com uma obsessão, pressionando com força enquanto o sangue começa a escorrer mais rápido."
    "A caverna parece estar viva. Cada som ecoa de forma pesada, como se as paredes respirassem junto comigo."
    "Quando ele coloca a pele do lobo sobre as minhas pernas, a sensação é insuportável, a dor mais intensa do que qualquer coisa que eu já tenha sentido."
    "Eu tento gritar, mas não posso. O corte no peito me faz perder a força. O sangue já está se misturando com a pele fria, e cada respiração se torna mais difícil."
    "Max parece ficar mais obcecado, seus olhos queimando com um desejo que é ao mesmo tempo insano e controlado."
    max "Vamos nos entender agora..."
    "Eu sinto a pele do lobo aderindo à minha própria, como se estivesse se fundindo comigo, selando meu destino em cada pedaço de carne que ele coloca sobre mim."
    "Ele termina, mas não se afasta. Ele fica ali, observando o que fez, o olhar satisfeito, como se estivesse esperando alguma reação minha."
    "O lobo agora está dentro de mim."
    max "Agora, você entende o que é ser um... monstro."
    jump expression show_ending("images/Max/max_jumpscaare_home.png", "audio/transforming_screaming_werewolf.ogg")

label max_media_afinidade:
    # Igual ao início da baixa afinidade, mas com chance de sobrevivência e mais diálogo
    menu:
        "O que fazer?"
        "Se apresentar (+10 max pontos)":
            $ max_pontos(+10)
            mc "O meu é [povname]."
            "A… uh… a calda dele se mexe com animação e um pouco de surpresa."
            max "Sim, exatamente…"
            "Ele sorri parecendo aliviado com alguma coisa."
            max "(letra pequena) isso foi mais fácil do que pensei…"
            jump max_media_continua
        "Não dizer nada (-10 sanidade)":
            $ alterar_sanidade(-10)
            "Ele realmente espera que dizer isso vai simplesmente resetar tudo o que aconteceu?"
            max "Tudo bem, eu já sei o seu nome…"
            max "O resto resolvemos depois..."
            jump max_media_continua

label max_media_continua:
    # Diálogo sobre solidão, curiosidade, etc.
    "Antes que eu pudesse reagir, ele se vira e sai da sala."
    "Ouço o som de várias trancas sendo fechadas atrás da porta…"
    "Ele não deve voltar tão cedo…"
    "É um bom momento para analisar a situação."
    # ... (igual ao trecho anterior)
    jump max_media_exploracao

label max_media_exploracao:
    # Exploração do quarto, barra de cereal, etc.
    # (Você pode expandir aqui conforme o roteiro)
    "Max retorna rapidamente, a porta range novamente ao ser aberta."
    "Ele entra, com um pacote nas mãos. Algo simples, mas eficaz: uma barra de cereais."
    max "Vi você comendo uma dessas na loja..."
    "Ele me entrega a barra, o olhar atento."
    mc "Ah... uma barra de cereais..."
    max "Algum problema?"
    mc "Isso não é exatamente... hã como posso dizer?... comida?"
    max "... isso não é comida?"
    mc "Não é isso... é só que eu imaginei uma refeição."
    max "Humanos complicam muito as coisas..."
    menu:
        "Comer barra de cereais":
            $ alterar_sanidade(15)
            $ max_pontos(+10)
            "Como a barra de cereais. Ela some do inventário."
            jump max_media_explora_quarto
        "Não comer":
            $ max_pontos(-20)
            "Decido não comer. A barra some do inventário."
            jump max_media_explora_quarto

label max_media_explora_quarto:
    # Exploração do quarto (janela, armário, porta, mesa, caixas, cortina, insetos, voltar à cadeira)
    # Você pode criar menus para cada opção, como no roteiro
    "Agora é um bom momento para explorar a sala e ver se encontro uma saída."
    # Exemplo de menu de exploração (adicione mais opções conforme desejar)
    menu:
        "Explorar a janela no teto":
            "Uma janela que dá para o lado de fora, tem duas trancas do outro lado e parece bem pesada. Além disso, precisaria de uma escada..."
            jump max_media_explora_quarto
        "Explorar o armário":
            "Abro o armário e... Ugh... isso são ossos...? Não apenas de animais... e-eu não quero ver isso..."
            jump max_media_explora_quarto
        "Voltar à cadeira":
            "Bem... acho que é isso... Não há muito mais que eu possa fazer agora."
            jump max_media_ritual

label max_media_ritual:
    # Ritual e transformação
    "O ar está denso, pesado demais para respirar com facilidade, como se o próprio ambiente estivesse me esmagando."
    "E então, uma sensação estranha começa a me envolver. Plantas…"
    "Eu levanto os olhos e vejo o que parece ser uma visão de floresta invadindo o espaço ao redor de minha visão."
    "Ramagens, folhas, trepadeiras. Elas começam a se estender lentamente, como se crescessem a partir do chão, do teto, como se a própria floresta estivesse se infiltrando no porão, entrando no lugar onde estou."
    "Quando eu fiquei com tanto sono?"
    show Timeskip
    $ renpy.pause(2.0)
    hide Timeskip
    "Eu acordo com um sobressalto, o coração batendo forte no peito."
    "As plantas desapareceram, mas a sensação de opressão permanece."
    "Quando meus olhos se ajustam, vejo Max à minha frente. Ele está coberto de sangue."
    "O rosto, a roupa, tudo manchado de um vermelho escuro, quase negro."
    "Não há sinais de agressão direta, mas o sangue parece novo, quente."
    "Ele respira rápido, de forma irregular, como se tivesse acabado de passar por algo..."
    "A expressão dele é estranha. Nervosa, tensa, mas ao mesmo tempo, ele sorri."
    max "Eu… acho que podemos conversar agora."
    max "Eu não entendo você..."
    max "E eu sei que você não entende, mas talvez... se você começasse a me entender, eu poderia... hã... conversar melhor com você."
    "E então, ele traz um pedaço de carne crua em sua mão."
    max "Comida humana. Não tem gosto pra mim. Eu tentei..."
    max "Agora, você devia tentar."
    menu:
        "Morder":
            $ alterar_sanidade(-20)
            "O gosto é ferroso, quente, errado. A textura densa, repulsiva. Meu estômago se revira, meu corpo rejeita, mas engulo mesmo assim."
            "Max observa. O sorriso dele desaparece. Seus ombros relaxam ligeiramente, e ele respira fundo, como se algo tivesse se encaixado."
            jump max_final_2
        "Virar o rosto":
            "Minha garganta está seca. Meu corpo inteiro grita para não fazer isso, mas eu forço um movimento. Um único gesto de recusa."
            "As samambaias ondulam na minha visão periférica, como se reagissem ao meu desafio."
            "O ar se torna mais denso."
            "Max não fala nada a princípio. Mas ele também não se afasta."
            "O silêncio cresce entre nós, sufocante, insuportável."
            "Eu o ouço respirar, lenta e controladamente."
            "Então, ele se move. Rápido."
            "Uma mão forte agarra meu queixo, forçando minha cabeça para frente."
            max "Desculpa, mas... só funciona se você comer..."
            "A carne crua pressiona contra meus lábios. O cheiro de sangue fresco inunda meu nariz."
            "Eu tento virar o rosto de novo, mas o aperto dele é firme."
            "Eu luto, mas é inútil. A carne é empurrada para dentro. Meu corpo se contorce em repulsa, mas minha própria respiração vacila."
            "Meu peito aperta. Meu estômago revira. Não quero. Mas engulo."
            "O gosto metálico do sangue se espalha pela minha boca, denso, enjoativo."
            "Max solta meu rosto devagar, observando cada movimento meu."
            max "Você não entende... ainda."
            "As samambaias tremulam ao nosso redor, um sussurro invisível rastejando pelo ar."
            "E eu percebo que algo mudou. Dentro de mim."
            "As samambaias se contraem. Tudo escurece."
            jump max_final_2

label max_final_2:
    # Final ritual, transformação, etc.
    show caverna
    show M010 at center
    $ persistent.unlocked_sprites.add("M010")
    "Parece mais uma caverna..."
    "É úmido, escuro..."
    "Eu estou amarrado de novo. Mas as cordas estão muito mais apertadas."
    "Meus pulsos estão posicionados acima da altura da cabeça, os braços estão esticados..."
    "Meu corpo está exausto, mas a dor é o que mais me domina."
    "E há algo mais no ar… algo que se move, que respira junto comigo."
    "Eu o vejo então, movendo-se na penumbra. Max."
    "Ele está diferente. Seus olhos brilham com uma intensidade estranha, e seus movimentos são rápidos, nervosos."
    "Ele para na escuridão e pega algo que eu não consigo identificar à primeira vista. Um peso na sua mão. Algo… grande."
    "A pele de um lobo, ainda fresca, com os pelos espessos e os olhos quase vívidos, como se o animal ainda vivesse."
    "Eu vejo os olhos do lobo, mortos, mas de algum modo, eles ainda estão me observando."
    "Max não me olha. Ele se aproxima e começa a se mover de forma frenética."
    "Ele rasga a pele do lobo com as unhas de dentes... Destroçando como se não fosse nada."
    "Ele começa com os meus braços. O corte é rápido, preciso. Suas garras deslizam através da minha carne, rasgando minha pele com uma dor que me faz gritar."
    "Mas ele não para. Max não se importa com o som que sai de minha garganta. Ele continua a trabalhar, a pele do lobo já pronta, esperando."
    max "Você vai entender..."
    "A voz dele não soa como de costume. Está baixa, rouca, mais como um rosnado."
    "Ele pega o pedaço de pele de lobo e a coloca sobre a carne exposta do meu braço, pressionando com força, como se fosse necessário selar a ferida dessa maneira."
    "A sensação é estranha, a carne fria contra a minha pele quente. Eu sinto a pele do animal grudando em mim, em uma fusão grotesca, e a dor nas minhas feridas é insuportável."
    mc "M-max-!"
    "Não há mais nada que eu consiga dizer. Gritos desesperados são a única coisa que escapa da minha garganta."
    "Ele vai mais longe. No meu peito, ele faz um corte profundo, um corte em forma de V, e o sangue escorre, quente e espesso."
    "Ele pega mais pele do lobo e começa a cobrir a ferida, quase com uma obsessão, pressionando com força enquanto o sangue começa a escorrer mais rápido."
    "A caverna parece estar viva. Cada som ecoa de forma pesada, como se as paredes respirassem junto comigo."
    "Quando ele coloca a pele do lobo sobre as minhas pernas, a sensação é insuportável, a dor mais intensa do que qualquer coisa que eu já tenha sentido."
    "Eu tento gritar, mas não posso. O corte no peito me faz perder a força. O sangue já está escorrendo, e cada respiração se torna mais difícil."
    "Max parece ficar mais obcecado, seus olhos queimando com um desejo que é ao mesmo tempo insano e controlado."
    "Mas há um pouco de frustração... Como se algo estivesse fora do lugar."
    max "Quase lá..."
    "Eu sinto a pele do lobo sendo pressionada contra meu corpo, o sangue sendo a única coisa nos separando, selando meu destino em cada pedaço de carne que ele coloca sobre mim."
    "Ele termina, mas não se afasta. Ele fica ali, observando o que fez, o olhar confuso, como se estivesse esperando alguma reação minha."
    "Minha pressão cai lentamente..."
    max "E-espera..."
    max "O que... o que eu-?"
    jump expression show_ending("images/Max/wolf_skin.png", "audio/melancolic_howl.ogg")
    $ persistent.CGS_6 = True
    jump endgame

label max_alta_afinidade:
    # Aqui você pode expandir para finais alternativos, sobrevivência, ou transformação completa
    # Por enquanto, encaminhe para o mesmo final até expandir o roteiro
    jump max_final_2

# Fim da Rota Max
