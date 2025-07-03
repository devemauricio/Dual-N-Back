# 🧠 N-Back Visual Game com Cores e Posições (Tkinter)

Este projeto implementa uma variação do jogo **N-Back**, utilizando **interface gráfica com Tkinter**. O jogador deve identificar repetições de **posição** e/ou **cor** em uma grade, memorizando elementos apresentados há *N* rodadas.

---

## 🎮 Como Jogar

- A cada rodada, um quadrado aleatório da grade é colorido.
- Você deve pressionar:
  - **`p`** se a **posição** do quadrado atual for igual à de N rodadas atrás.
  - **`c`** se a **cor** do quadrado atual for igual à de N rodadas atrás.
- O nível (N) aumenta ou diminui conforme o desempenho.

---

## ⌨️ Controles

| Tecla | Ação |
|------|------|
| `p`  | Detectar repetição de **posição** |
| `c`  | Detectar repetição de **cor**     |

---

## 📈 Sistema de Pontuação

- Acerto → +1 ponto  
- Erro → −1 ponto  
- Score = `(max_moves + pontos) * 100 // max_moves`  
- O score varia de 0 a 100 e determina a progressão de nível:

| Score (%)        | Ação            |
|------------------|-----------------|
| < 75             | Nível diminui   |
| 75 ≤ Score < 90  | Nível mantém    |
| ≥ 90             | Nível aumenta e `max_moves += 3` |

---

## 🧩 Arquitetura do Código

### `Square` (classe)

Representa um quadrado individual da grade.

| Método           | Função                                   |
|------------------|------------------------------------------|
| `draw_square()`  | Desenha o quadrado no canvas             |
| `paint(color)`   | Altera a cor do quadrado                 |
| `get_color()`    | Retorna a cor atual                      |

---

### `Game` (classe base)

Lida com interface gráfica, score e eventos de teclado.

| Método                  | Função                                                  |
|-------------------------|---------------------------------------------------------|
| `play_game()`           | Inicia a interface do jogo                              |
| `compute_position()`    | Verifica acerto de posição                              |
| `compute_color()`       | Verifica acerto de cor                                  |
| `update_score()`        | Atualiza o texto da pontuação e nível                   |

---

### `Grid` (classe derivada de `Game`)

Implementa a lógica principal do jogo e manipula o tabuleiro.

| Método                     | Função                                                        |
|----------------------------|---------------------------------------------------------------|
| `create_grid()`            | Cria a grade de quadrados                                     |
| `pick_random_square()`     | Gera jogada, atualiza estado e repinta                       |
| `check_positions()`        | Verifica repetição de posição                                 |
| `check_colors()`           | Verifica repetição de cor                                     |
| `update_positions()`       | Atualiza fila de posições                                     |
| `update_colors()`          | Atualiza fila de cores                                        |
| `check_and_penalize()`     | Penaliza por repetições não reconhecidas                     |
| `check_end_level()`        | Finaliza nível e ajusta dificuldade conforme score            |
| `correct_level()`          | Garante que score não ultrapasse 100                          |
| `pick_random_color()`      | Seleciona uma cor aleatória da paleta                         |

---

## 🧠 Conceito de N-Back

O **N-Back** é um exercício cognitivo usado para treinar a memória de trabalho. Neste projeto, o usuário é desafiado a se lembrar da posição e cor de estímulos visuais após um número *N* de passos.

---

## ▶️ Execução

Para executar o jogo:

```bash
python nome_do_arquivo.py
