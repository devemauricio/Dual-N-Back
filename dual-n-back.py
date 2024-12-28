import tkinter as tk
import random
from collections import deque

class Square: # Cada quadrado da matriz
    def __init__(self, canvas, x1, y1, x2, y2, row, col, color="white"):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.row = row
        self.col = col
        self.color = color
        self.square_id = None

    def draw_square(self):
        self.square_id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline="")

    def paint(self, color="white"):
        if self.square_id:
            self.color = color
            self.canvas.itemconfig(self.square_id, fill=color)

    def get_color(self): # Retorna a cor atual do quadrado
        return self.color


class Game:
    def __init__(self, level=1):
        self.level = level
        self.points = 0 # Contagem com base em acertos e erros
        
        self.can_compute_position = False # Funcionalidade: impedir que seja a pontuação seja contabilizada mais de uma vez por período
        self.can_compute_color = False

        self.root = tk.Tk()
        self.root.title("N-Back")
        self.root.bind("p", self.compute_position) # O usuário deve apertar a tecla "a" quando houver repetição de posição
        self.root.bind("c", self.compute_color) # O usuário deve apertar a tecla "c" quando houver repetição de cor
        
    def play_game(self):
        self.create_grid()
        self.label = tk.Label(self.root, text=f"Nível: {self.level}  Score: {self.score}%", font=("Arial", 16))
        self.label.pack()
        self.pick_random_square()
        self.root.mainloop()

    def compute_position(self, event):
        if self.can_compute_position:
            if self.check_positions():
                self.points += 1
            else:
                self.points -= 1
            self.can_compute_position = False
            self.update_score()

    def compute_color(self, event):
        if self.can_compute_color:
            if self.check_colors():
                self.points += 1
            else:
                self.points -= 1
            self.can_compute_color = False
            self.update_score()

    def update_score(self):
        self.label.config(text=f"Nível: {self.level}  Score: {self.score}%") 
class Grid(Game):  # Herdando de Game
    def __init__(self, level=1, lines=3, cols=3, square_size=150):
        super().__init__(level)  # Inicializa o Game
        self.lines = lines
        self.cols = cols
        self.square_size = square_size
        self.canvas = tk.Canvas(self.root, width=self.lines * square_size, height=self.cols * square_size)
        self.root.geometry(f"{self.lines * self.square_size}x{self.cols * self.square_size + 30}")
        self.root.resizable(False, False)
        self.canvas.pack()
        self.grid = []
        self.positions_queue = deque() # Fila contendo as N últimas casas (ou quadrados) jogadas
        self.counter = 0
        self.max_moves = 10 # Número de repetições por nível
        self.score = 100
        self.set_colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
        self.lasts_colors = deque() # Fila contendo as N últimas cores

        

    def create_grid(self):
        for line in range(self.lines):
            squares_in_line = []
            for col in range(self.cols):
                x1 = line * self.square_size
                y1 = col * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                square = Square(self.canvas, x1, y1, x2, y2, line, col)
                square.draw_square()
                squares_in_line.append(square)
            self.grid.append(squares_in_line)

    def check_positions(self):
        if len(self.positions_queue) == self.level + 1 and self.positions_queue[0] == self.positions_queue[-1]:
            return True
        return False

    def update_positions(self, row, col):
        if len(self.positions_queue) > self.level:
            self.positions_queue.popleft()
        self.positions_queue.append(self.grid[row][col])

    def check_end_level(self):
        if self.counter == self.max_moves: # Se o número máximo de jogadas por nível for atingido
            
            if self.score < 75:
                if self.level == 1:
                    pass
                else:
                    self.level -= 1
                
            elif self.score < 90:
                self.level *= 1
                
            else:
                self.level += 1
                self.max_moves += 3 # Para permitir uma maior jogabilidade, a cada nível o número de repetições aumenta
            
            self.points = 0
            self.counter = 0
            self.score = 100
            self.positions_queue.clear()
            self.lasts_colors.clear()
            self.update_score()
            self.root.after(3000)        

    def correct_level(self):

        if self.score >= 100:
            self.score = 100 # Impede que o score ultrapasse o valor máximo de 100

    def check_and_penalize(self):
        
        if self.check_positions():
            self.points -= 1
                
        if self.check_colors():
            self.points -= 1
            
    def pick_random_square(self):
        
        #if len(self.positions_queue) > self.level:
        self.can_compute_position = True
        self.can_compute_color = True
            
        self.score = (self.max_moves + self.points) * 100 // self.max_moves

        self.correct_level()
        self.check_end_level()
  
        row = random.randint(0, self.lines - 1)
        col = random.randint(0, self.cols - 1)

        selected_color = self.pick_random_color()
        self.grid[row][col].paint(selected_color)
        self.update_positions(row, col)
        self.update_colors(row, col)
        
        # Verificação para a penalização
        
        if len(self.lasts_colors) == self.level + 1:
            self.check_and_penalize()

        self.root.after(2000, lambda: [self.grid[row][col].paint(), setattr(self, "can_compute_position", False), setattr(self, "can_compute_color", False)])
        self.counter += 1
        self.root.after(2500, self.pick_random_square)
        self.update_score()
        #print(self.lasts_colors)

    def check_colors(self):
        #print("checando se a cor atual foi igual à N última")
        if len(self.lasts_colors) == self.level + 1 and self.lasts_colors[0] == self.lasts_colors[-1]:
            #print(f"Cores iguais!")
            return True
        return False

    def update_colors(self, row, col):
        if len(self.lasts_colors) > self.level:
            self.lasts_colors.popleft()
        self.lasts_colors.append(self.grid[row][col].get_color())

    def pick_random_color(self):
        return self.set_colors[random.randint(0, len(self.set_colors) - 1)]

           
jogo = Grid()
jogo.play_game()
