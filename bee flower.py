import pgzrun
import random

WIDTH=600
HEIGHT=600
TITLE="cacth the flower"

bee=Actor("bee")
flower=Actor("flower")

bee.pos=(300,300)
flower.pos=(436,285)

def draw():
    screen.blit("grassfild",(0,0))
    bee.draw()
    flower.draw()
def update():
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        flower.pos=random.randint(0,600),random.randint(0,600)


pgzrun.go()