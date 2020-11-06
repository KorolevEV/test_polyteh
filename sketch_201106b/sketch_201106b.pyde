def setup():
    size(800,800)
    frameRate(60)
    println(str(mouseX)+ " : " +str(mouseY))
def draw():
    background(255//1.1,255//2,0)
    for d in range(10):
        for i in range(10):
            stroke(0)
            fill(255,255,0)
            rect(20+(800//10)*i,40+(800//10)*d,40,40)
            line(40+(800//10)*i,40+(800//10)*d,40+(800//10)*i,40+(800//10)*d+40)
    if (mousePressed == True):
        noStroke()
        fill(255,255,0,255//2)
        ellipse(mouseX, mouseY, 100,100)
