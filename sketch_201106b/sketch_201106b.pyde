def setup():
    size(800,800)
    frameRate(60)
    colorMode(HSB,255,100,100,100)
def draw():
    background(20,50,15)
    n=0
    for d in range(10):
        for i in range(10):
            stroke(0)
            fill(0)
            rect(x(i),y(d),40,40)
            if (mousePressed == True):
                        if (x(i)<mouseX<x(i)+40):
                            if (y(d)<mouseY<y(d)+40):
                                fill(35,100,100)
                                rect(x(i),y(d),40,40)  
                                for a in range(100):
                                    noStroke()
                                    fill(35,100,100,1)
                                    ellipse(x(i)+20,y(d)+20,1*a,1*a)
            stroke(0)
            line(x(i)+20,y(d),x(i)+20,y(d)+40)  
def x(i):
    x=20+(800//10)*i
    return(x)
def y(d):
    y=20+(800//10)*d
    return(y)
    
