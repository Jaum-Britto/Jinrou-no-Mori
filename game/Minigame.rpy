default card_amount = 12
default card_rows = 3
default cards = []
default selected_cards = []
default hidden_cards = 0
default match_found = False
default max_attempts = 2
default attempts_remaining = max_attempts
default preview_time = 5
default preview_time_remaining = preview_time
default memory_score = 0
default preview_mode = True
default waiting_to_check = False
default persistent.show_memory_rules = True
default persistent.memory_highscore = 0

init python:
    if persistent.memory_highscore is None:
        persistent.memory_highscore = 0

    def randomize_cards():
        import random
        global cards, hidden_cards, selected_cards, preview_mode, preview_time_remaining
        imagens = [
            "card-1", "card-2", "card-3", "card-4", "card-5", "card-6"
        ]
        cartas = imagens * 2
        random.shuffle(cartas)
        cards = [[c, "deselected", "visible"] for c in cartas]
        hidden_cards = 0
        selected_cards = []
        preview_mode = True
        preview_time_remaining = preview_time

    def hide_all_cards():
        for card in cards:
            card[1] = "deselected"

    def update_preview_timer():
        global preview_time_remaining, preview_mode
        if preview_time_remaining > 0:
            preview_time_remaining -= 1
            renpy.restart_interaction()
        else:
            preview_mode = False
            hide_all_cards()
            renpy.restart_interaction()

    def select_card(card_index):
        global selected_cards, waiting_to_check
        if cards[card_index][1] == "deselected" and cards[card_index][2] == "visible":
            cards[card_index][1] = "selected"
            selected_cards.append(card_index)
            if len(selected_cards) == 2:
                waiting_to_check = True
                renpy.restart_interaction()

    def reset_memory_game():
        global memory_score, attempts_remaining, preview_mode
        memory_score = 0
        attempts_remaining = max_attempts
        preview_mode = True
        randomize_cards()

    def continue_memory_game():
        global attempts_remaining, preview_mode, preview_time
        attempts_remaining = max_attempts
        preview_time = max(2, preview_time - 0.5)
        preview_mode = True
        randomize_cards()

    def check_game_end():
        if hidden_cards == card_amount:
            return "win"
        elif attempts_remaining <= 0:
            return "lose"
        return None

    def update_highscore():
        if memory_score > persistent.memory_highscore:
            persistent.memory_highscore = memory_score

    def process_selected_cards():
        global selected_cards, attempts_remaining, memory_score, hidden_cards, waiting_to_check, preview_time
        c1, c2 = selected_cards
        if cards[c1][0] == cards[c2][0]:
            cards[c1][2] = "hidden"
            cards[c2][2] = "hidden"
            memory_score += 10
            hidden_cards += 2
        else:
            attempts_remaining -= 1
        cards[c1][1] = "deselected"
        cards[c2][1] = "deselected"
        selected_cards = []
        waiting_to_check = False
        # Se venceu, diminui o preview_time
        if check_game_end() == "win":
            preview_time = max(2, preview_time - 0.5)
        renpy.restart_interaction()

# Tela de confirmação genérica
screen memory_confirm(text, yes_action, no_action):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 20
            text text size 32 xalign 0.5
            hbox:
                spacing 40
                textbutton "Não" action no_action xpos 155
                textbutton "Sim" action yes_action xpos 155                

# Tela do minigame
screen memory_mini_game():
    add "images/Minigames/Jogo_da_memoria/mini_game_BK.png"

    vbox:
        align (0.5, 0.05)
        spacing 10
        text "Jogo da Memória" size 50 xalign 0.5
        hbox:
            spacing 40
            text "Pontos: [memory_score]" size 30
            text "Recorde: [persistent.memory_highscore]" size 30
            text "Vidas: [attempts_remaining]" size 30
            if preview_mode:
                text "Preview: [preview_time_remaining]s" size 30

    # Botão Sair com confirmação
    textbutton "Sair" action Show("memory_confirm", 
        text="Deseja realmente sair do minigame?", 
        yes_action=[Hide("memory_confirm"), Hide("memory_mini_game"), Show("gallery_minigames")], 
        no_action=Hide("memory_confirm")) xalign 0.97 yalign 0.03

    # Botão Reiniciar com confirmação
    textbutton "Reiniciar" action Show("memory_confirm", 
        text="Deseja reiniciar a rodada?", 
        yes_action=[Hide("memory_confirm"), Function(reset_memory_game)], 
        no_action=Hide("memory_confirm")) xalign 0.87 yalign 0.03

    # Botão para mostrar as regras
    textbutton "Regras" action Show("memory_rules_popup") xalign 0.72 yalign 0.03

    frame:
        background None
        xalign 0.5
        yalign 0.7
        xsize 900
        ysize 500

        grid int(card_amount / card_rows) card_rows:
            align (0.5, 0.5)
            spacing 40
            for i, card in enumerate(cards):
                if preview_mode:
                    image "images/Minigames/Jogo_da_memoria/%s.png" % card[0] xysize (90, 120)
                elif card[1] == "deselected" and card[2] == "visible":
                    imagebutton:
                        idle Transform("images/Minigames/Jogo_da_memoria/card-back.png", xysize=(90, 120))
                        sensitive (len(selected_cards) != 2 and not waiting_to_check)
                        action Function(select_card, card_index=i)
                elif card[1] == "selected" and card[2] == "visible":
                    image "images/Minigames/Jogo_da_memoria/%s.png" % card[0] xysize (90, 120)
                else:
                    null

    if preview_mode:
        timer 1.0 action Function(update_preview_timer) repeat True

    if waiting_to_check:
        timer 0.5 action Function(process_selected_cards)

    if check_game_end() == "win":
        use memory_win_screen
    elif check_game_end() == "lose":
        use memory_lose_screen

# Tela de vitória
screen memory_win_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 20
            text "Parabéns! Você venceu!" size 40 xalign 0.5
            text "Pontuação: [memory_score]" size 30 xalign 0.5
            text "Recorde: [persistent.memory_highscore]" size 30 xalign 0.5
            textbutton "Continuar" action [Function(update_highscore), Function(continue_memory_game), Hide("memory_win_screen")] xalign 0.5
            textbutton "Voltar à Galeria" action [Function(update_highscore), Hide("memory_win_screen"), Hide("memory_mini_game"), Show("gallery_minigames")] xalign 0.5

# Tela de derrota
screen memory_lose_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 20
            text "Fim de Jogo!" size 40 xalign 0.5
            text "Pontuação: [memory_score]" size 30 xalign 0.5
            text "Recorde: [persistent.memory_highscore]" size 30 xalign 0.5
            textbutton "Tentar Novamente" action [Function(update_highscore), Function(reset_memory_game), Hide("memory_lose_screen")] xalign 0.5
            textbutton "Voltar à Galeria" action [Function(update_highscore), Hide("memory_lose_screen"), Hide("memory_mini_game"), Show("gallery_minigames")] xalign 0.5

# Label para iniciar o minigame
label mini_game:
    $ reset_memory_game()
    if persistent.show_memory_rules:
        call screen memory_rules_popup
    show screen memory_mini_game
    $ renpy.pause(9999, hard=True)
    jump gallery_minigames
