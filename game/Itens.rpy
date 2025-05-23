# Definições relacionadas a itens
init python:

    # Lista para armazenar os itens do inventário
    inventory = []

    # Classe de item com nome, descrição, quantidade e imagem
    class Item:
        def __init__(self, name, description, image, quantity=1, consumable=True, effect=None):
            self.name = name
            self.description = description
            # image deve ser o nome da imagem registrada em scenes.rpy
            self.image = image
            self.quantity = quantity
            self.consumable = consumable  # Novo atributo
            self.effect = effect          # Função de efeito opcional
            
        def __str__(self):
            return f"{self.name} (x{self.quantity})"

    # Função para adicionar itens ao inventário
    def add_item(item):
        if item not in inventory:
            inventory.append(item)
            renpy.notify(f"Adicionado: {item.name}")

    # Função para remover itens do inventário
    def remove_item(item):
        if item in inventory:
            inventory.remove(item)
            renpy.notify(f"Removido: {item.name}")

    # Variável global para armazenar o item atual
    current_item_description = ""

    # Função que define a descrição do item atual
    def show_item_description(item):
        global current_item_description
        current_item_description = f"{item.description}"
    # Função para resetar a descrição do item
    def reset_item_description():
        global current_item_description
        current_item_description = ""


# Itens do inventário
default item_enroladinho = Item(
    name="Enroladinho",
    description="Um enroladinho de salsicha, parece apetitoso.",
    image="images/inventario/hotdog.png",
    consumable=True,
    effect=lambda: alterar_sanidade(10)  
)

default item_folha = Item(
    name="Arvore esculpida",
    description="Uma folha seca, talvez tenha algum uso especial.",
    image="images/inventario/treesculpture.png",
    consumable=False
)

default item_capsulas = Item(
    name="Comprimidos",
    description="Duas cápsulas de cor vermelha e azul. Para que servem?",
    image="images/inventario/pills.png",
    consumable=True,
    effect=lambda: alterar_sanidade(50)

)

default item_identidade = Item(
    name="Carteira de Identidade",
    description="Um documento de identidade. Pode ser útil para provar quem você é.",
    image="images/inventario/maxid.png",
    consumable=False,
    effect=lambda: renpy.notify("Você olha a identidade. A foto parece familiar...")
)




