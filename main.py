from turtle import Screen # imporra la libreri turtle 
from snake import Snake#llama al archivo snake y le importa la clase snake 
from food import Food# llama al archico food y le im porta la clase food
from scoreboard import Scoreboard# llama al archico scoreboard y le im porta la clase scoreboard
import time #este permite contar el tiempo de ejecucion y controlar su flujo 

#Craeacion de las ventanas
screen = Screen()#importa la ventana
screen.setup(width=600, height=600)# Este controla las dimensiones 
screen.bgcolor("black")# este le da color 
screen.title("My Snake Game")# este le asigna el nombre
screen.tracer(0) # Reconoce la animacion de la libreria turtle 

snake = Snake()# importa la clase snake 
food = Food()#Importa la clase food
scoreboard = Scoreboard() #importa la clase scoreboard

screen.listen()# da el numero de conexiones no aceptadas en el sistema antes de rechazar nuevas conexiones
screen.onkey(snake.up, "Up")#vincula la liberacionm d el alketra superior
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                
screen.exitonclick()













