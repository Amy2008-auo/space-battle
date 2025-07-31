import pgzrun,pyautogui
WIDTH,HEIGHT=pyautogui.size()
TITLE="space battle"

ship=Actor("ship")
ship.pos=WIDTH/2,HEIGHT-100

def draw():
    screen.clear()
    ship.draw()

def update():
    if keyboard.left:
        ship.x-=10
    if keyboard.right:
        ship.x+=10
    if ship.x<0:
        ship.x=WIDTH
    if ship.x>WIDTH:
        ship.x=0
















pgzrun.go()
