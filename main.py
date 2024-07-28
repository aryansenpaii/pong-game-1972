
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Aryan's Pong Game-1972")

#turn off the animations
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle= Paddle((-350,0))

main_ball=Ball()
score_board= Scoreboard()



screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

#a while loop to keep updating the frames
game_is_on= True

while game_is_on:
    time.sleep(main_ball.move_speed)
    screen.update()
    main_ball.move()

    #this part will detect collision
    if(main_ball.ycor() >280 or main_ball.ycor()<-280):
        main_ball.bounce_y()

    #this part detects collision with the paddle
    if(main_ball.distance(r_paddle)<70 and main_ball.xcor()>320 or main_ball.distance(l_paddle)<70 and main_ball.xcor()<-320):
        main_ball.bounce_x()

    #detect collsion with the right wall
    if(main_ball.xcor()>350 ):
        main_ball.reset_position()
        score_board.update_left()
        time.sleep(0.5)

    #detect collision with the left wall
    if(main_ball.xcor()<-350):
        main_ball.reset_position()
        score_board.update_right()
        time.sleep(0.5)




screen.exitonclick()
