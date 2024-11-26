# Definições relacionadas a itens
init python:

    # Classe de item com nome, descrição, quantidade e imagem
    class Item:
        def __init__(self, name, description, quantity=1):
            self.name = name
            self.description = description
            self.quantity = quantity

        def __str__(self):
            return f"{self.name} (x{self.quantity})"

    # Lista para armazenar os itens do inventário
    inventory = []

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



# Exemplo de itens com nome, descrição, quantidade e imagem
default PropTeste = Item(
    name="Cachorro Quente", 
    description="Cachorro Quente (Pão com salcisha e vários complementos)", 
    quantity=1
)


