# Definições relacionadas a itens

default inventory = []  # Assim o Ren'Py salva e carrega junto com o save

init python:

    # Classe de item com nome, descrição, quantidade e imagem
    class Item:
        def __init__(self, name_pt, name_en, desc_pt, desc_en, image, quantity=1, consumable=True, effect=None):
            self.name_pt = name_pt
            self.name_en = name_en
            self.desc_pt = desc_pt
            self.desc_en = desc_en
            self.image = image
            self.quantity = quantity
            self.consumable = consumable  # Novo atributo
            self.effect = effect          # Função de efeito opcional

        @property
        def name(self):
            return self.name_en if _preferences.language == "english" else self.name_pt

        @property
        def description(self):
            return self.desc_en if _preferences.language == "english" else self.desc_pt

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
    name_pt="Enroladinho",
    name_en="Sausage Roll",
    desc_pt="Um enroladinho de salsicha, parece apetitoso.",
    desc_en="A sausage roll, looks tasty.",
    image="images/inventario/hotdog.png",
    consumable=True,
    effect=effect_enroladinho
)

default item_folha = Item(
    name_pt="Árvore esculpida",
    name_en="Carved Tree",
    desc_pt="Uma folha seca, talvez tenha algum uso especial.",
    desc_en="A dry leaf, maybe it has a special use.",
    image="images/inventario/treesculpture.png",
    consumable=False
)

default item_capsulas = Item(
    name_pt="Comprimidos",
    name_en="Pills",
    desc_pt="Duas cápsulas de cor vermelha e azul. Para que servem?",
    desc_en="Two capsules, one red and one blue. What are they for?",
    image="images/inventario/pills.png",
    consumable=True,
    effect=effect_capsulas
)

default item_identidade = Item(
    name_pt="Carteira de Identidade",
    name_en="ID Card",
    desc_pt="Um documento de identidade. Pode ser útil para provar quem você é.",
    desc_en="An identity document. It might be useful to prove who you are.",
    image="images/inventario/maxid.png",
    consumable=False,
    effect=effect_identidade
)

init python:

    def effect_enroladinho():
        alterar_sanidade(10)

    def effect_capsulas():
        alterar_sanidade(50)

    def effect_identidade():
        renpy.notify("Você olha a identidade. A foto parece familiar...")




