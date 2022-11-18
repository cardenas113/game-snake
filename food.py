from turtle import Turtle #importa la libreria turtle 
import random #importa random para la aparicion de la comida de forma aleatoria 

class Food(Turtle):

    def __init__(self): 
        super().__init__()
        self.shape("circle")# Define la forma del objeto 
        self.penup()#para que no deje los rastros de la linea  del objeto
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #
        self.color("blue") # Le da color al objeto
        self.speed("fastest")#le da velocidad de reaparecer la comida
        self.refresh()# Hace que la comida vuelva a aparcer 
    def refresh(self):
        random_x = random.randint(-280, 280)#sirve para ubicar el objeto dentro de la ventana de forma aleatoria en el eje x.
        random_y = random.randint(-280, 280)#sirve para ubicar el objeto dentro de la ventana de forma aleatoria en el eje y.
        self.goto(random_x, random_y)# le da una direccion al objeto