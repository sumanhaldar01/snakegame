from turtle import*
import turtle
from random import randrange
from freegames import square,vector
wn=turtle.Screen()
wn.bgcolor("black") 

apple=vector(0,0)
s=[vector(10,0)]
aim=vector(0,-10)

def directionchange(x,y):
    aim.x=x
    aim.y=y
def bound(head):
    return-380<head.x<370 and-322<head.y<312
def move():
    head=s[-1].copy()    
    head.move(aim)
    if not bound(head)or head in s:
        square(head.x,head.y,10,'yellow')
        update()
        print("GAME OVER!!!!")
        return

    s.append(head)
   
    if head==apple:
        print('s:',len(s))    
        apple.x=randrange(-20,20)*10
        apple.y=randrange(-20,20)*10
    else:
        s.pop(0)
    clear()

    for body in s:
        square(body.x,body.y,10,'red')
   
    square(apple.x,apple.y,10,'green')
    update()
    ontimer(move,100)
hideturtle()
tracer(False)                
listen()
onkey(lambda:directionchange(10,0),'Right')
onkey(lambda:directionchange(-10,0),'Left')
onkey(lambda:directionchange(0,10),'Up')
onkey(lambda:directionchange(0,-10),'Down')
move()
done()
