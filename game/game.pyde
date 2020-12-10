rectx=random(150,450)
recty=-25
prsx=300
prsy=450
score=0
speed=1
fr=150
def setup():
    global f
    size(600,600)
    f = createFont("Impact",24,True)
#draw############################    
def draw(): 
    frameRate(fr)
    background(0)
    obstmove()
    prsmove()
    scoreboard()
    lose()

    
#################################
def obstmove():
    global recty, rectx, speed,fr
    fill(255,0,0)
    rectMode(CENTER)
    rect(rectx,recty,400,50)
    recty=recty+speed
    if (recty>=625):
        recty=0
        rectx=random(150,450)
    if (score==5):
        fr=250
    if (score==10):
        fr=350
    if (score==25):
        fr=450
    if (score>35):
        fr=fr+0.1
#################################    
def prsmove(): 
    global prsx
    fill(0,255,0)
    rectMode(CENTER)
    rect(prsx,prsy,40,40)
    if (keyPressed==True):
        if (keyCode==LEFT):
            prsx=prsx-2
        if (keyCode==RIGHT):
            prsx=prsx+2
    if prsx<=20:
        prsx=20
    if prsx>=580:
        prsx=580
        
####################################
def scoreboard(): #score
    global score, f
    textFont(f,24)
    textAlign(CENTER)
    fill(255)
    text("SCORE:",50,25)
    text(score,110,25)
    if (recty>=624):
        score=score+1
        
def lose():
    global recty,rectx,prsx,prsy,f,speed
    if (recty-25<prsy+20<recty+25) or (recty-25<prsy-20<recty+25):
        if (rectx-200<prsx-20<rectx+200) or (rectx-200<prsx+20<rectx+200):
            finalscore=score
            textFont(f,40)
            textAlign(CENTER)
            fill(255,0,0)
            text("YOU LOSE!",300,250)
            text("SCORE:",275,300)
            text(finalscore,375,300)
            noLoop()
