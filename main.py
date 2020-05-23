from ufo import *
import turtle as tr
import time

start_time = time.time()
timer = 15                                     # Time of flight UFO.
tr.tracer(0)
tr.hideturtle()

ufo1 = Ufo('Пришелец-1', 100, -50, 50, 'green', 'black', 'yellow', 'blue', 5, 6, 5)
ufo2 = Ufo('Пришелец-2', 200, -50, 70, 'red', 'pink', 'blue', 'yellow', 3, 4, 10)
ufo3 = Ufo('Пришелец-3', 300, -50, 100, 'pink', 'green', 'red', 'purple', 3, 4, 10)
ufo4 = Ufo('Пришелец-4', 400, -20, 200, 'blue', 'black', 'yellow', 'green', 3, 4, 10)
ufo5 = Ufo('Пришелец-5', 500, -50, 150, 'darkblue', 'green', 'blue', 'white', 3, 4, 10)
ufo1.show()
ufo2.show()
ufo3.show()
ufo4.show()
ufo5.show()
while (time.time() - start_time) < timer:
    tr.clear()
    ufo1.move()
    ufo2.move()
    ufo3.move()
    ufo4.move()
    ufo5.move()
tr.done()



