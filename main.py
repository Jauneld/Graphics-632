from cmu_graphics import *

# Write your code here
# Not sure where to start?
# Check out README.md under "Files"

app.background = 'darkSlateGray'
def name():
  Label(('Johack'), 20, 20, fill='yellow', size=30, font='cinzel', bold=True)

def background():
  Circle(200,200,150,fill=gradient('deepSkyBlue','lightBlue', 'lightCyan',start='bottom-right'),border = 'black', borderWidth=5)

def face():
  Circle(200,200,70,fill="burlyWood")
  Oval(170, 190, 40, 40, fill='black')
  Oval(230, 190, 20, 20, fill='oliveDrab',opacity=70)
  Line(150, 150, 200, 270, fill='black', lineWidth=5, opacity=70)
  Line(170, 243, 230, 243, fill='black', lineWidth=7, dashes = True)
  Polygon(200, 225, 200, 200, 230, 210, fill = 'brown',opacity=60)

def body():
  Rect(160,275,80,20,fill=gradient('wheat','burlyWood', 'sienna', start='left'), rotateAngle=90)
  Circle(200,360,70,fill="red")
  Oval(200, 350, 200, 10, fill='black', opacity=60)

def fillIn():
  Circle(200,425,98,fill="darkSlateGray")
  Rect(100,330,200,30,fill="darkSlateGray")

background()
body()
fillIn()
face()
name()

cmu_graphics.run()