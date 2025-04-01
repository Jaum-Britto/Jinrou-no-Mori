default ap_points = 0


label apollo_route:
    # Introdução da cena
    "Ficamos em silêncio enquanto eu penso sobre."
    "Ele realmente parece saber mais do que eu."
    "Mas ao mesmo tempo, eu também não contei a ele todos os detalhes..."
    "Eu não queria preocupá-lo."

    mc "Tudo bem mesmo eu ir?"
    show AP2
    ap "Claro, não quero que corra perigo."
    show scene_black
    ap "Fique o tempo que quize-"
    mc "Olha, não foi nada de mais, ok? É só uma noite..."

    "Eu não queria soar desse jeito..."
    "É que às vezes parece que ele sempre consegue o que quer."
    "Mesmo que o que ele quer geralmente seja ajudar..."

    mc "É estranho pensar nisso, ok?"
    ap "..."
    hide AP2
    ap "Se você realmente quer fingir que nada aconteceu, não precisamos falar sobre isso."
    ap "Finja que é uma festa do pijama, ou algo do tipo..."

    "Acho que posso fazer isso."
    "Apesar de que esse assunto não morreu completamente."
    "Digo, ele vai querer conversar sobre isso novamente alguma hora..."

    mc "Certo."
    ap "Então, vamos?"
    ap "Arrume suas coisas."

    # Transição para a casa do ap
    show bg_ap_room
    show AP13
    with dissolve
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
    show AP7
    ap "Decorei especialmente pra você..."

    # Transição para o momento do choque
    show scene_black
    with dissolve
    "Antes que pudesse me virar, sinto algo puxar meu cabelo."
    "A última coisa que vejo é a quina da porta."

    # Personagem acorda
    "Abro os olhos lentamente..."
    mc "Ugh... minha cabeça está me matando."
    show AP10
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
    $ ap_points += 5
    jump next_scene

label prank_question:
    ap "...?"
    show AP14
    ap "Ppfff – HAHAHAHAHAHAHAHAHAHA!"
    $ ap_points += 10
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
    $ ap_points -= 10
    show AP11
    ap "Se eu quisesse que você ficasse em silêncio, já teria te matado, não acha?"
    jump next_scene

label next_scene:
    # Escolha do jogador
    menu:
        "Ficar em silêncio.":
            $ ap_points -= 20
            jump silent_end
        "Isso dói...":
            $ ap_points += 5
            jump pain_reaction
        "Eu faço qualquer coisa.":
            $ ap_points += 10
            jump beg_for_mercy

label silent_end:
    "Não existe nada para ser dito."
    "Eu apenas o encaro, sem conseguir acreditar em tudo o que está acontecendo..."
    ap "Não me ignore!"
    "Sinto algo pressionar contra meu pescoço... Acho que são suas mãos..."
    jump bad_end_1

label pain_reaction:
    mc "Ack... isso dói!"
    ap "Mesmo?"
    "Ele se anima instantaneamente."
    show AP7
    ap "Você fica uma gracinha quando está prestes a chorar..."
    ap "Esse era meu objetivo no início."
    ap "Mas sua expressão é boa também..."
    jump continue_scene

label beg_for_mercy:
    mc "Ack... E- Eu faço qualquer coisa!"
    "Seus dedos afrouxam um pouco, apesar de ele não soltar meu cabelo completamente."
    ap "Mesmo? Qualquer coisa?"
    mc "Q-qualquer coisa! Só... por favor, não me machuque..."
    ap "Pff- haha... qualquer coisa?"
    show AP6
    ap "O que mais você acha que eu quero fazer além de te machucar?"
    jump continue_scene

label continue_scene:
    "ap está sempre sorrindo. Isso é o normal dele..."
    "Mas isso..."
    "Esse sorriso... eu nunca vi."
    "É tão... genuíno."
    "Pela primeira vez, parece que ele não está sorrindo pra deixar os outros felizes, mas sim porque ele mesmo está satisfeito."
    "Muito satisfeito."
    return
