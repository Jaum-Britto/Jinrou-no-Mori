default card_amount = 12
default card_rows = 3
default cards = []
default selected_cards = []
default hidden_cards = 0
default match_found = False
default max_attempts = 2  # Número máximo de tentativas
default attempts_remaining = max_attempts  # Tentativas restantes
default preview_time_remaining = 5  # Tempo inicial do preview em segundos


init python:
    def randomize_cards():
        global cards
        cards = []
        for i in range(int(card_amount / 2)):
            rand_card_num = renpy.random.randint(1, 8)
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
        renpy.random.shuffle(cards)
    
    def hide_all_cards():
        global preview_mode
        for card in cards:
            card[1] = "deselected"  # Retorna ao estado inicial
        preview_mode = False  # Desativa o modo de preview

    def update_preview_timer():
        global preview_time_remaining
        if preview_time_remaining > 0:
            preview_time_remaining -= 1    

    def select_card(card_index):
        global selected_cards
        global match_found

        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
            match_found = True

    def deselect_card():
        global selected_cards
        global attempts_remaining

        if len(selected_cards) == 2:
            if cards[selected_cards[0]][0] != cards[selected_cards[1]][0]:
                attempts_remaining -= 1  # Reduz tentativas se não houver correspondência
            for card in selected_cards:
                cards[card][1] = "deselected"
        selected_cards = []

    def hide_matches():
        global selected_cards
        global match_found
        global hidden_cards

        cards[selected_cards[0]][2] = "hidden"
        cards[selected_cards[1]][2] = "hidden"
        hidden_cards += 2
        deselect_card()
        match_found = False

    def reset_memory_game():
        global match_found
        global hidden_cards
        global attempts_remaining

        match_found = False
        hidden_cards = 0
        attempts_remaining = max_attempts
        randomize_cards()
        renpy.restart_interaction()

    def check_game_state():
        if hidden_cards == card_amount:
            return "victory"
        elif attempts_remaining <= 0:
            return "defeat"
        return "ongoing"

transform card_fadein:
    alpha 0.0
    easein 0.5 alpha 1.0

screen defeat_screen:
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20, 20, 20)
        background "#0008"
        vbox:
            spacing 20
            text "Você perdeu!" size 30 color "#FFF" xalign 0.5
            hbox:
                spacing 20
                textbutton "Reiniciar" action [Function(reset_memory_game), Hide("defeat_screen"), Show("memory_mini_game")]
                textbutton "Sair" action Return()

screen memory_mini_game:
    image "mini_game_BK.png"
    grid int(card_amount / card_rows) card_rows:
        align (0.5, 0.5)
        spacing 10

        for i, card in enumerate(cards):    
            if preview_mode:
                image "%s.png" % card[0]  # Exibe todas as cartas no modo preview
            elif card[1] == "deselected" and card[2] == "visible":
                imagebutton idle "card-back.png" sensitive (len(selected_cards) != 2) action Function(select_card, card_index=i) at card_fadein 
            elif card[1] == "selected" and card[2] == "visible":
                image "%s.png" % card[0] at card_fadein
            else:
                null

    # Exibir o tempo restante ou tentativas dependendo do estado
    if preview_mode:
        text "Tempo para começar: [preview_time_remaining]s" size 40 color "#FFF" align (0.5, 0.05)  # Tamanho e cor ajustados
        timer 1.0 action Function(update_preview_timer) repeat True
    else:
        text "Tentativas restantes: [attempts_remaining]" size 40 color "#FFF" align (0.5, 0.05)  # Tamanho e cor ajustados

    # Timer para esconder as cartas após o período de preview
    if preview_mode and preview_time_remaining == 0:
        timer 0.1 action Function(hide_all_cards) repeat False

    if match_found:
        timer 1.0 action Function(hide_matches) repeat True
    elif len(selected_cards) == 2:
        timer 1.0 action Function(deselect_card) repeat True
    elif check_game_state() == "defeat":
        timer 0.5 action Show("defeat_screen") repeat False
    elif hidden_cards == card_amount:
        timer 0.5 action Function(reset_memory_game) repeat False

label mini_game:
    $ randomize_cards()
    $ preview_mode = True
    $ preview_time_remaining = 5  # Reinicia o tempo do preview
    $ attempts_remaining = max_attempts
    call screen memory_mini_game
    return
