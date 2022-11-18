from turtle import Turtle # Importa la libreria turtle 
ALIGNMENT = "center" # Centra la barra de puntajes 
FONT = ("Courier", 24, "normal") # Le da una fuente a la barra de resultado

class Scoreboard(Turtle):# Le da una clase a la barra de puntajes.

    def __init__(self): #Se comienza la funcion 
        super().__init__() #Se empieza con la funcion super 
        self.score = 0 # Este le asigna un puntaje
        self.color("white") # Le da color al puntaje 
        self.penup() #Se evita que se creen lineas 
        self.goto(0, 270) # Se loe asigna un puntaje 
        self.hideturtle() # Oculta el contenido de la barra solo dejando el texto
        self.update_scoreboard() # para actualizar la barra 

    def update_scoreboard(self): #Este le asigna color y forma  a la fuente 
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):# Se actuliza la informacion  en la barra actuliza el puntaje y enseña el game over
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)

    def increase_score(self):#incrementa el puntaje conforme avanza el juego
        self.score += 1
        self.clear()
        self.update_scoreboard()

