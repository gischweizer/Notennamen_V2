tonv = ["c1","d1","e1","f1","g1","a1","h1","c2","d2","e2","f2","g2"]
tonb = ["G","A","H","c","d","e","f","g","a","h","c1"]
#globale Variabel

def setup():
    size(2100, 1000)
    #Grösse des Fensters
    background(255,255,255)
    #Hintergrundfarbe(weiss)
    img=loadImage("cursor.png")
    cursor(img)
    #cursorbild wird importiert (Note) und anstatt des Cursors angezeigt.
 
def draw(): #wird einmal pro Frame ausgeführt
    background(255,255,255)
    img = loadImage("notensystem.jpg")
    image(img,100,10, 1700, 1000)
    #Position (x, y) und Grösse (Breite, Höhe) des Bildes
    b = 1
    #wenn b=1, dann ist die Mausposition noch unbekannt
    for i in range(12):        
        if mouseY < 215+ 29*i and b == 1:
            #29 ist ca. Abstand in px zwischen zwei Tönen auf Notenlinien
            a = 11-i
            b = 0
        elif b == 1:
            a = 0

    textSize(82)
    #Schriftgrösse
    fill(236,64,122)
    #Schriftfarbe
    if mouseY < 535:
        text(tonv[a],20,64)
    #fixe Position des Notennamens, wird nur bis zu einem Threshold angezeigt
    
    #dasselbe nochmals mit dem Bassschlüssel. a und b sind nun x und y
    y = 1
    for t in range(11):        
        if mouseY < 570 + 31*t and y == 1:
            x = 10-t
            y = 0
        elif y == 1:
            x = 0

    textSize(82)
    #Schriftgrösse
    fill(236,64,122)
    #Schriftfarbe
    if mouseY > 560:
        text(tonb[x],20,64)
    #fixe Position des Notennamens, wird nur bis zu einem Threshold angezeigt

    #print mouseY
        #Um den Abstand zwischen den Linien zu messen
    #print x
    
     
