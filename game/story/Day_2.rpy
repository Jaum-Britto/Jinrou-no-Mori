# Continuação do Dia 1 e implementação do Dia 2 - 3:00 am
#Criando a Sanidade
default sanidade = 100

label day_2:
    # Transição do fim do dia 1 para o início do dia 2
    play music "audio/soundtrack/floresta.ogg"volume 5
    show scene_black
    "Depois de um longo dia, você finalmente chega em casa."
    "Você toma um banho, organiza suas coisas e, com o som da chuva lá fora, adormece rapidamente."

    # Hora do despertar durante a noite
    "*CLANK*"
    "Você acorda com um barulho alto. Seu coração dispara."
    "O que foi isso? Veio de dentro da casa?"

    # Investigação inicial - a gaveta e a janela aberta
    "Você olha em volta e percebe que sua gaveta está meio aberta."
    mc "Eu tinha certeza de que fechei a gaveta..."
    "Há uma trilha de roupas que vai até a janela, que também está aberta. O vento balança as cortinas."
    "Ugh... algumas roupas estão cobertas de lama... e sangue?"

    # Escolha: Investigar mais ou trancar-se no quarto
    menu:
        "Chegar mais perto.":
            jump investigate_noise
        "Voltar para o quarto e trancar a porta.":
            jump go_back_to_bed

label investigate_noise:
    "Você decide investigar de onde veio o barulho."
    "Enquanto você desce até a cozinha, o ambiente está escuro e assustadoramente silencioso."

    show Casa_7
    
    "Você nota algo estranho no chão perto da geladeira. Não parece comida..."
    
    # Escolha: Investigar o objeto estranho
    menu:
        "Chegar mais perto.":
            show Casa_9
            "Você se aproxima e vê... um coelho morto. Suas entranhas estão expostas."
            mc "Isso... isso são tripas?"
            "A visão é horrível. Você se afasta, enjoado, tentando processar o que acabou de ver."
            hide Casa_9
            hide Casa_7
            $ sanidade -= 30  # Reduz a sanidade
            jump day_2_continue
        "Voltar para o quarto e trancar a porta.":
            hide Casa_7
            jump go_back_to_bed

label go_back_to_bed:
    show Casa_4
    "Você decide que é melhor voltar para o quarto. Tranca a porta e tenta se acalmar."
    mc "O que quer que seja, não está mais aqui... certo?"
    "Você respira fundo e tenta voltar a dormir, mas não consegue parar de pensar no que aconteceu."
    hide Casa_4
    $ sanidade += 10  # Recupera um pouco de sanidade
    jump day_2_continue

label day_2_continue:
    # Dia seguinte - 9:00 AM
    stop music
    play music "audio/119402__kyster__nice-forrest-ambience.ogg"volume 50
    show scene_black
    "Você finalmente acorda, o sol já brilha através da janela."
    mc "Foi tudo um pesadelo...?"
    "Você respira fundo, se levanta, e decide ir verificar a cozinha."

    # Escolha: Checar a cozinha ou evitar
    menu:
        "Checar a cozinha.":
            jump check_kitchen
        "Evitar a cozinha.":
            jump avoid_kitchen

label check_kitchen:
    show Casa_6
    show Casa_8
    "Quando você entra na cozinha, o cheiro de sangue e carne toma conta do ambiente."
    "O coelho ainda está lá, e agora, sob a luz do dia, a cena é ainda mais perturbadora."
    mc "Isso... isso realmente são as entranhas de um coelho."
    "Você tenta limpar a cozinha, usando uma sacola plástica para se livrar da carcaça."
    hide Casa_8
    "Apesar de tudo, se sente um pouco melhor depois de terminar."
    hide Casa_6
    $ sanidade -= 15  # Perde sanidade pela visão
    $ sanidade += 5  # Recupera um pouco ao limpar
    jump visit_apollo

label avoid_kitchen:
    "Você não tem coragem de voltar para a cozinha agora."
    "O pensamento de ver aquele coelho morto novamente é demais para você."
    "Você decide sair para tomar um ar."
    $ sanidade -= 10  # Perde sanidade por evitar a situação
    jump visit_apollo

label visit_apollo:
    # Visita de Apollo após o incidente
    show Casa_11
    "Você está prestes a sair de casa quando ouve alguém se aproximando da porta."
    show AP4
    ap "Ah... eu estava prestes a bater..."
    hide AP4
    show AP8
    mc "Apollo? O que você está fazendo aqui tão cedo?"
    hide AP8
    show AP6
    ap "Eu... ouvi alguns barulhos estranhos ontem à noite. Queria ver se estava tudo bem."
    hide AP6

    # Escolha: Contar sobre o coelho ou não
    menu:
        "Contar sobre o coelho.":
            jump tell_about_rabbit
        "Não contar.":
            jump dont_tell_about_rabbit

label tell_about_rabbit:
    mc "Na verdade, não... eu encontrei algo muito estranho ontem à noite."
    mc "Havia... um coelho morto na minha cozinha."
    show AP5
    ap "O quê? Um coelho morto?"
    mc "Sim, não sei como ele foi parar lá."
    hide AP5
    show AP9
    ap "Isso é estranho... você tem certeza de que era um coelho?"
    hide AP9
    show AP8
    mc "Sim, eu praticamente o raspei do chão."
    hide AP8
    show AP9
    ap "Algo muito estranho está acontecendo..."
    hide AP9
    jump apollo_concern

label dont_tell_about_rabbit:
    mc "Ah, só ouvi alguns barulhos estranhos, nada demais."
    show AP8
    "Apollo parece desconfiado, mas não insiste no assunto."
    hide AP8
    show AP9
    ap "Hum... certo. Mas se algo estranho acontecer de novo, me avise, ok?"
    hide AP9
    jump apollo_concern

label apollo_concern:
    show AP3
    ap "Olha, eu realmente acho que você deveria passar a noite na minha casa hoje."
    mc "Hã...? O que você quer dizer?"
    ap "Não sei... só tenho um mau pressentimento sobre isso tudo. Não me parece natural."
    hide AP3
    menu:
        "Aceitar o convite.":
            mc "Talvez você tenha razão. Pode ser uma boa ideia."
            jump go_to_apollo_house
        "Recusar.":
            mc "Eu agradeço, Apollo, mas acho que posso lidar com isso."
            jump stay_home

label go_to_apollo_house:
    "Você decide ir para a casa de Apollo, tentando se sentir mais seguro."
    hide Casa_11
    stop music
    jump endgame
    # Continuação...

label stay_home:
    "Você decide ficar em casa, mesmo com a preocupação crescente."
    hide Casa_11
    stop music
    jump endgame
    # Continuação...

# Continuação do jogo...