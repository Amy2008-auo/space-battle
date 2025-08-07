import pgzrun,pyautogui,random
WIDTH,HEIGHT=pyautogui.size()
TITLE="space battle"
enemies=[]
ship=Actor("ship")
ship.pos=WIDTH/2,HEIGHT-100

def draw():
    screen.clear()
    ship.draw()
    for i in enemies:
        i.draw()

def update():
    if keyboard.left:
        ship.x-=10
    if keyboard.right:
        ship.x+=10
    if ship.x<0:
       ship.x=WIDTH
    if ship.x>WIDTH:
        ship.x=0

    for i in enemies:
        i.y+=2
        i.x+=1
        if i.x<20:
            i.x+=1
        if i.x>WIDTH-20:
            i.x-=1

    

def create_enemies():
    global enemies
    enemie=Actor("alien")
    enemie.pos=random.randint(20,WIDTH-20),0
    enemies.append(enemie)


clock.schedule_interval(create_enemies,5.0)















pgzrun.go()
