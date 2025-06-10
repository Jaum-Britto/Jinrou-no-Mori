# 🐺 Jinrou no Mori

**Jogo Visual Novel interativo desenvolvido com Ren’Py**

## 🎯 Descrição do Projeto

`Jinrou no Mori` é um TCC acadêmico que apresenta uma **visual novel leve (light novel)**, desenvolvida em Ren’Py e voltada para narrativas imersivas com escolhas do jogador. A história mistura **mistério, romance e fantasia**, ambientada em uma pequena cidade próxima a uma floresta misteriosa.

O gameplay consiste basicamente em avançar pela narrativa (clique para continuar), inserir o nome do protagonista, escolher entre opções que impactam o enredo, alimentar stats como sanidade e gerenciar um inventário simples. A interface inclui telas como *inventário*, *minigame de memória* e *galeria de finais*, além de um menu de *configurações*.

## 🎮 Funcionalidades Principais

- Inserção do nome do protagonista  
- Avanço de diálogo por clique  
- Sistema de escolhas com ramificações de rotas  
- Inventário simples (coleta de itens, visualização)  
- Minigame: “Jogo da Memória”  
- Galeria com finais, personagens e minigames desbloqueáveis  
- Configurações: som, velocidade de texto, idioma (pt/en)  
- Sistema de saves e carregamentos nativo do Ren’Py  
- Arquivos de tradução organizados na pasta `tl/`

## 🛠 Tecnologias

- **Ren’Py** — motor gráfico para visual novel (Python)  
- **Python** — scripts e lógica do jogo  
- **VS Code** — editor de código  
- **GitHub** — controle de versões  
- **Itch.io / Steam** — plataformas de distribuição  
- **Krita** — criação de arte e sprites

## 🧩 Estrutura do Repositório

```
Jinrou-no-Mori/
├── game/                    # Códigos fonte do Ren'Py
├── tl/                      # Arquivos de tradução (pt-br)
├── assets/                  # Imagens, sprites e cenários
├── gallery/                 # Recursos de galeria desbloqueável
├── minigame/                # Scripts e assets do jogo da memória
├── saves/                   # Pasta de saves (Ren'Py padrão)
├── README.md                # Este documento
└── LICENSE                  # Licença do projeto
```

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Jaum-Britto/Jinrou-no-Mori.git
   cd Jinrou-no-Mori
   ```
2. Instale o **Ren’Py** (versão 7.x ou superior).
3. No launcher do Ren’Py, abra a pasta do jogo e clique em **“Launch Project”**.
4. Aproveite a experiência narrativa.

## 📈 Pontos de Função (Análise APF)

O sistema foi avaliado por **Pontos de Função (APF)** com total estimado de **43 PF**, demonstrando baixa complexidade funcional compatível com uma visual novel:

| Tipo | Funcionalidade                       | Qtde | Complexidade | Pontos/item | Total |
|------|--------------------------------------|------|--------------|-------------|-------|
| ALI  | Saves e inventário                   | 2    | Baixa        | 7           | 14    |
| EE   | Nome do protagonista e escolhas      | 4    | Baixa        | 3           | 12    |
| SE   | Minigame e inventário                | 2    | Baixa/Média  | 4–5         | 9     |
| CE   | Consulta do inventário               | 1    | Baixa        | 3           | 3     |
| AIE  | Arquivos de tradução (pasta `tl/`)   | 1    | Baixa        | 5           | 5     |
| **Total** |                                  |      |              |             | **43** |

## 📝 Licença

# 📜 Ren'Py
- Licença: MIT License

- Link oficial: https://www.renpy.org/doc/html/license.html

## Resumo:

- Você pode usar, modificar e distribuir Ren'Py livremente, até mesmo em projetos comerciais, desde que mantenha a licença e o aviso de copyright.

# 📜 Visual Studio Code
- Licença do binário oficial (Microsoft): Licença Proprietária (não-livre)

- Licença do código-fonte (repositório open source): MIT License

## Resumo:

- O código-fonte é livre (MIT), mas o VS Code baixado do site oficial da Microsoft inclui partes proprietárias (como o branding), então não pode ser redistribuído.
Para projetos livres, recomenda-se usar VSCodium — que é o VS Code sem as partes fechadas.




## 🚀 Próximos Passos

- Adicionar recursos visuais ao minigame  
- Expandir rotas alternativas e finais  
- Traduzir para mais idiomas  
- Lançamento oficial no Steam e Itch.io
