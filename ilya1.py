from turtle import *

shape('turtle')

for i in range(8):
    forward(50)
    left(45)

    for i in range(4):
        if i == 2:
            left(45)
            backward(100)
            forward(100)
            right(45)

        forward (50)
        left(90)

    right(45)
    forward(50)


    left(45)



