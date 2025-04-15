# Tela do inventário
init python:
    def ajustar_tamanho_inventario():
        largura_tela = renpy.config.screen_width
        altura_tela = renpy.config.screen_height
        # Tamanho fixo do inventário (ex: 50% da largura e 60% da altura da tela)
        largura_inventario = max(400, largura_tela * 0.5)  # Mínimo de 400 px de largura
        altura_inventario = max(300, altura_tela * 0.6)    # Mínimo de 300 px de altura
        return largura_inventario, altura_inventario

screen inventory_screen:
    # Chama a função de ajuste do inventário
    $ largura_inventario, altura_inventario = ajustar_tamanho_inventario()

    # Define o frame do inventário com tamanho mínimo fixo
    frame:
        style "inventory_frame"
        align (0.5, 0.5)
        xmaximum largura_inventario
        ymaximum altura_inventario
        xminimum largura_inventario
        yminimum altura_inventario

        vbox:
            align (0.5, 0.05)
            spacing 20
            text "Inventário" style "inventory_title" size 40 xalign 0.5

            # Mostra os itens no inventário
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15

                # Checa se o inventário está vazio e exibe uma mensagem
                if inventory:
                    for item in inventory:
                        # Cria um item-botão para funcionar a descrição
                        textbutton f"{item.name} (x{item.quantity})" action Function(show_item_description, item) xalign 0.5
                else:
                    text "Nenhum item no inventário" xalign 0.5 yalign 0.5

            # Exibe a descrição do item atual, se houver
            if current_item_description:
                text f"{current_item_description}" xalign 0.5

            # Botão para fechar o inventário
            textbutton "Fechar" action [Function(reset_item_description), Return()] align (1.0, 1.0) margin (10, 10, 10, 10)

# Função para abrir o inventário
label open_inventory:
    # Mostra a tela do inventário
    call screen inventory_screen
    return

# Exemplo de uso do inventário
label start_inventario:
    # Abre o inventário
    call open_inventory from _call_open_inventory
    return
