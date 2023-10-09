from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
#ukoliko zelimo da prekinemo/iskljucimo animaciju, a to je kretanje objekta
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #update screen i pokazemo sta je se desilo nedavno u pozadini
    screen.update()
    ball.ball_move()

    #Detect collusion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collusion with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect ball go out of the R paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect ball go out of the L paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()