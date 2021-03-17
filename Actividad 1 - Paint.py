#Diego  Esparza - A01652327
#Edgar Federico González Aguirre - A01383154

from turtle import *
from freegames import vector

#Método para generar lineas
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Método para generar un círculo
def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    circumference = 2 * (abs(start.x-end.x)+abs(start.y-end.y)) * math.pi
    step_size = circumference / 360
    
    for count in range(360):
        forward(step_size)
        left(1)
    
    end_fill()

# Método para generar un rectángulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if count%2 == 0:
            forward(end.x - start.x)
            left(90)
        else:
            forward((end.y - start.y))
            left(90)

    end_fill()

#Método para generar un triángulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()                          #"levantar" pluma
    goto(start.x, start.y)        #graficar
    down()                        #comienza relleno
    begin_fill()
    
    for i in range(3):            #realiza el trazo
        forward(end.x - start.x)  #distancia cualquiera
        left(120)                 #angulo (120°)
        forward(end.x - start.x)  # continúa el trazo
        
        #repite para terminar triángulo
    
    end_fill()                    #Termina ciclo de llenado
    pass                          # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

#Colores
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
  #se añade color amarillo
onkey(lambda: color('yellow'), 'Y')

#Trazos
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
