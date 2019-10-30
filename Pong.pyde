x=60
y=60
xrect2=0
xrect1=0
xVers=1
yVers=1
raggio=35
xracc=0
xracc2=0
yracc=0
score1=0
score2=0

def setup():
    background(13,255)
    size(900,600)
    
    
def draw():
    global x,y,xVers,yVers,raggio,xracc,xracc2,yracc,score1,score2,rect1,rect2
    
    
    background(13,255)
    fill(255,255,255)
    ellipse(x,y,raggio,raggio)
    
    rect(xracc,575,100,25)
    rect(xracc2,yracc,100,25)
    
  
    
    if (y+25>height-25) and (x+25)>xracc and (x-25)<(xracc+100) :
        yVers  = -1
        score1 = score1 + 1
        
    if (y-25<25) and (x+25)>xracc2 and (x-25)<(xracc2+100) :
        yVers = +1
        score2 = score2 + 1
        
        
        
        
    if (x+25 > width or x-25 < 0):
        xVers = xVers * (-1)

    if (y+25 > height or y-25 < 0):
        yVers = yVers * (-1)


    x += 3*xVers
    y += 3*yVers



    
    fill(255,128,128)
    textSize(20)
    text(score1,10,400)
    
    fill(255,128,128)
    textSize(20)
    text(score2,0,40)   
    
    
def keyPressed():
    global xracc,xracc2
    if  keyCode == LEFT:
        xracc = xracc-20
    if  keyCode == RIGHT:
        xracc = xracc+20
        
    if key== "a":
        xracc2 = xracc2-20
    if key== "d":
        xracc2 = xracc2+20


    
