Documentação do Código - Jogo N-Back Visual com Cores e Posições
Este código implementa uma variação do jogo N-Back usando interface gráfica com Tkinter, onde o jogador deve detectar repetições de posição e/ou cor em uma grade de quadrados. O nível de dificuldade aumenta ou diminui conforme o desempenho do jogador.

1. Classe Square
Representa cada quadrado individual na grade (grid).

Atributos
canvas: Objeto Canvas onde o quadrado é desenhado.

x1, y1, x2, y2: Coordenadas do quadrado.

row, col: Posição (linha, coluna) do quadrado na grade.

color: Cor atual do quadrado.

square_id: ID da forma desenhada no canvas.

Métodos
draw_square(): Desenha o quadrado no canvas.

paint(color): Pinta o quadrado com uma cor específica.

get_color(): Retorna a cor atual do quadrado.

2. Classe Game
Classe base para o jogo. Define pontuação, interface gráfica e captura de teclas.

Atributos
level: Nível de dificuldade (N do N-Back).

points: Pontuação bruta (acertos - erros).

can_compute_position, can_compute_color: Flags que controlam se as ações de pontuação podem ser processadas.

root: Janela principal do Tkinter.

label: Label que exibe o score e nível.

Métodos
play_game(): Inicia a interface e o jogo.

compute_position(event): Verifica repetição de posição ao pressionar "p".

compute_color(event): Verifica repetição de cor ao pressionar "c".

update_score(): Atualiza o score mostrado no label.

3. Classe Grid (herda de Game)
Classe principal que implementa a lógica do jogo com a grade de quadrados.

Atributos
lines, cols: Número de linhas e colunas da grade.

square_size: Tamanho de cada quadrado.

canvas: Área onde os quadrados são desenhados.

grid: Matriz contendo os objetos Square.

positions_queue: Fila com as últimas posições selecionadas.

lasts_colors: Fila com as últimas cores usadas.

max_moves: Número de rodadas por nível.

score: Score percentual (de 0 a 100).

counter: Número de rodadas jogadas.

set_colors: Lista de cores possíveis.

Métodos
Criação e Desenho
create_grid(): Cria e desenha a grade de quadrados.

Verificação de Repetições
check_positions(): Verifica se a posição atual é igual à posição de N rodadas atrás.

check_colors(): Verifica se a cor atual é igual à cor de N rodadas atrás.

Atualização de Estado
update_positions(row, col): Atualiza a fila de posições.

update_colors(row, col): Atualiza a fila de cores.

pick_random_color(): Retorna uma cor aleatória da lista set_colors.

Pontuação e Nível
update_score(): Atualiza o label com o score.

correct_level(): Limita o score a 100.

check_and_penalize(): Penaliza o jogador por não detectar repetições.

check_end_level(): Avalia fim do nível e ajusta o nível conforme score:

Score < 75 → nível diminui (exceto se for 1);

75 ≤ score < 90 → mantém;

Score ≥ 90 → aumenta o nível e o número de rodadas.

Execução Principal do Jogo
pick_random_square():

Escolhe uma posição aleatória da grade.

Define uma cor aleatória.

Pinta o quadrado.

Atualiza filas de posição e cor.

Permite o usuário responder durante 2 segundos.

Penaliza se necessário.

Avança para a próxima jogada após 2.5 segundos.

4. Execução Final
python
Copiar
Editar
jogo = Grid()
jogo.play_game()
Cria uma instância da classe Grid e inicia o loop principal do jogo.

Resumo de Controles
Tecla "p" → Jogador indica que a posição do quadrado é igual à de N jogadas atrás.

Tecla "c" → Jogador indica que a cor do quadrado é igual à de N jogadas atrás.
