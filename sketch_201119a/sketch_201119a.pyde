n=0
def setup():
    size(600,600)
    frameRate(200)
def mode_1():
    global n
    ellipseMode(CENTER)
    background(255)
    ellipse(n,300,40,40)
    n=(n+1)%601
def mode_2():
    global n
    ellipseMode(CENTER)
    background(255)
    ellipse(300,n,40,40)
    n=(n+1)%601
def draw():
    if (keyCode== RIGHT):
        mode_1()
    elif (keyCode==DOWN):
        mode_2()
    
    
        


    
