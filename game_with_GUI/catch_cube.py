from tkinter import Tk, Canvas, PhotoImage, Label, CENTER,font
from random import randint as rand, randrange

height = 700
width = 900

window = Tk()
window.title("Catch the cubes!")
window.geometry("1920x1080")
window.configure(background="black")

sky = PhotoImage(file = "background.png")
label = Label( window, image = sky)
label.place(x = 0, y = 0)

canvas = Canvas(window, width=width, height=height, bg="black")
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

arcWidth = 115
arcHeight = 155

#arcx1 is short for "catcher x1", the top left x coordinate of the arc
arcx1 = width / 2 - arcWidth / 2
arcy1 = height - arcHeight - 20
arcx2 = arcx1 + arcWidth
arcy2 = arcy1 + arcHeight

arcfigure = canvas.create_arc(arcx1, arcy1, arcx2, arcy2, start=200, extent=140, width=4, outline="#FFFFFF", style="arc")

difficulty = 0.85
speed = 700
interval = 7000

remainingLives = 3
livesText = canvas.create_text(width-10, 10, anchor="ne", fill="#4ADEDE", font="Sans-Serif 26 bold", text="Lives: "+ str(remainingLives))

score = 0
scoreText = canvas.create_text(10, 10, anchor="nw", fill="#4ADEDE", font='Sans-Serif 26 bold', text="Score: "+ str(score))

cubes = []
size = 40

userName=input("Hello!\nPlease enter your name:")
cubeColor=input("Choose a color (cyan, magenta or yellow):")

def creating_cube():
    x = randrange(20, 880)
    y = 40
    cubeFigure = canvas.create_rectangle(x, y, x+size,y+size, fill=cubeColor)
    cubes.append(cubeFigure)
    window.after(interval, creating_cube)

def move_cube():
    for cube in cubes:
        (x, y, x2, y2) = canvas.coords(cube)
        canvas.move(cube, 0, 10)
        if y2 > height:
            drop_cube(cube)
    window.after(speed, move_cube)

def drop_cube(cube):
    global text1,text2,text3
    
    
    life()
    if remainingLives == 0:
        canvas2 = Canvas(window, width=width, height=height, bg="black")
        canvas2.place(relx=0.5, rely=0.5, anchor=CENTER)
        text1=canvas2.create_text(460, 200, font='Arial 60 bold', text='GAME OVER!',fill='white')
        text2=canvas2.create_text(460, 270, font='Arial 40',text='You ran out of lives',fill='white')
        text3=canvas2.create_text(460, 320, font='Arial 30',text='Final Score: '+ str(score), fill='white')

        global userName
        leaderboard=open("leaderboard.txt","a")
        leaderboard.write(str(score)+"  ---- "+userName+"\n")
        leaderboard.close()

        file = open("leaderboard.txt","r")
        readFile = file.readlines()
        sortedData = sorted(readFile,reverse=True)

        print("Best 5 Players' scores:")
        for line in range(5):
            print(str(line+1)+"\\" + "\t"+str(sortedData[line]))

def life():
    global remainingLives
    remainingLives -= 1
    canvas.itemconfigure(livesText,text="Lives: "+str(remainingLives))

def catch_cube():
    (arcx1, arcy1, arcx2, arcy2) = canvas.coords(arcfigure)
    for cube in cubes:
        (x1, y1, x2, y2) = canvas.coords(cube)
        if arcx1 < x1 and x2 < arcx2 and arcy2 - y2 < 40:
            cubes.remove(cube)
            canvas.delete(cube)
            increment_score(1)
    window.after(100, catch_cube)

def increment_score(points):
    global score, speed, interval
    score += points
    speed = int(speed * difficulty)
    interval = int(interval * difficulty)
    canvas.itemconfigure(scoreText, text="Score: "+str(score))

def left(event):
    (x, y, x1, y1) = canvas.coords(arcfigure)
    if x > 0:
        canvas.move(arcfigure, -25, 0)

def right(event):
    (x, y, x1, y1) = canvas.coords(arcfigure)
    if x1 < width:
        canvas.move(arcfigure, 25, 0)

paused = False

def pause(event):
    global speed, paused, pauseText
    speed = 0
    if paused == False:
        paused = True
        pauseText = canvas.create_text(450, 450, text = 'PAUSED', fill = "yellow", font='Arial 50 bold')

def unpause2(event):
    global speed, paused, pauseText, text1, text2, text3
    speed = 400
    if paused == True:
        paused = False
        canvas.delete(pauseText)
        canvas2.delete('all')
        
def unpause1(event):
    global remainingLives
    remainingLives = 3
    canvas.itemconfigure(livesText,text="Lives: "+str(remainingLives))

canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.bind("<Y>", unpause1)
canvas.bind("<U>", unpause2)
canvas.bind("<Escape>", pause)

canvas.focus_set()

window.after(1000, creating_cube)
window.after(1000, move_cube)
window.after(1000, catch_cube)

window.mainloop()

# Resources used
# for the background:
# https://stock.adobe.com/sk/search/images?k=2d+game+background