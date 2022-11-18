from turtle import Turtle #importa la libreria turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, #Guarada las direcciones dentro de una variable 
0)]
MOVE_DISTANCE = 20 # Le da moviento al objeto
UP = 90 # Este hace que el objeto (serpiente) se mueva hacia arriba 
DOWN = 270 #  Este hace que el objeto (serpiente) se mueva hacia abajo
LEFT = 180 # Este hace que el objeto (serpiente) se mueva hacia la izquierda 
RIGHT = 0 #  Este hace que el objeto (serpiente) se mueva hacia la derecha

class Snake:

    def __init__(self):  
        self.segments = [] # guarda cada segmento
        self.create_snake()# crea el objeto "snake"
        self.head = self.segments[0] #Guarda los 2 anteriores datos dentro del objeto

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) #Le da la posicion inicial al objeto

    def add_segment(self, position):
        new_segment = Turtle("square") #Le asigna defincion a la figura del objeto
        new_segment.color("green") # Le da color al objeto 
        new_segment.penup() #elimina el objeto
        new_segment.goto(position) #Define la posicion del objeto 
        self.segments.append(new_segment) # Agrega todo lo anterio al objeto

    def extend(self): # Crea una extencion a la serpiente 
        self.add_segment(self.segments[-1].position()) #Le da un segmento a la cola de la serpiente 

    def move(self): # Le da el movimineto 
        for seg_num in range(len(self.segments)- 1, 0, -1): #La cantidad del segmento que hay

            new_x = self.segments[seg_num -1].xcor() #Da nuevos segmentos en los ejes x,y
            new_y = self.segments[seg_num -1].ycor() #Da nuevos segmentos en los ejes x,y
            self.segments[seg_num].goto(new_x,new_y) #Da da movimiento  en los ejes x,y
        self.head.forward(MOVE_DISTANCE) #Mueve la cabeza junto a los segmentos

    def up(self): # Este hace que se mueva hacia arriba 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):# Este hace que se mueva hacia abajo
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):# Este hace que se mueva hacia izquierda 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):# Este hace que se mueva hacia derecha

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)