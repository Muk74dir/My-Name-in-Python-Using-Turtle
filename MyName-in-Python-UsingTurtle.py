import turtle

turtle.color("blue")
turtle.speed(3)
turtle.penup()
for _ in range(10):
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
turtle.right(90)
turtle.backward(100)
turtle.left(45)
for i in range(5):
    turtle.dot()
    turtle.forward(10)
turtle.left(90)
for i in range(5):
    turtle.dot()
    turtle.forward(10)
turtle.right(45)
for _ in range(10):
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

# Second Word [ U  ]

turtle.forward(30)
turtle.color("red")
turtle.right(90)
turtle.backward(100)
turtle.left(90)
turtle.speed(7)
for _ in range(6):
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
#curve Start Poinnt
turtle.dot()
turtle.forward(5)
turtle.backward(1)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
#curve Middle point
turtle.dot()
turtle.forward(10)
turtle.backward(5)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
#Curve End point
turtle.dot()
turtle.forward(15)
turtle.backward(10)
turtle.right(90)
turtle.forward(10)
turtle.left(90)

#base
turtle.dot()
turtle.forward(9)
turtle.dot()
turtle.forward(11)
turtle.dot()
turtle.forward(14)
turtle.dot()
turtle.forward(17)

#curve End Poinnt
turtle.dot()
turtle.forward(15)
turtle.backward(10)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
#curve Middle point
turtle.dot()
turtle.forward(10)
turtle.backward(5)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
#Curve Start point
turtle.dot()
turtle.forward(5)
turtle.backward(1)
turtle.left(90)
turtle.forward(10)
turtle.right(90)

for _ in range(7):
    turtle.dot()
    turtle.backward(1)
    turtle.forward(1)
    turtle.right(90)
    turtle.backward(10)
    turtle.left(90)

# third Word [ K ]
turtle.speed(7)
turtle.forward(30)
turtle.color("palevioletred4")
turtle.right(90)
for i in range(10):
    turtle.forward(10)
    turtle.left(90)
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)

turtle.backward(40)
turtle.left(135)
for i in range(7):
    turtle.forward(10)
    turtle.left(90)
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)

turtle.backward(50)
turtle.right(90)
for i in range(8):
    turtle.forward(10)
    turtle.left(90)
    turtle.dot()
    turtle.forward(1)
    turtle.backward(1)
    turtle.right(90)

# Forth word [ T ]
turtle.left(45)
turtle.forward(10)
turtle.color("olive")
turtle.left(90)
turtle.forward(90)
turtle.right(90)

for i in range(10):
    turtle.dot()
    turtle.forward(10)

turtle.backward(60)
turtle.right(90)
for i in range(10):
    turtle.dot()
    turtle.forward(10)

#Fifth word [ A ]

turtle.left(90)
turtle.color("black")
turtle.forward(50)

turtle.left(60)
turtle.forward(10)
for i in range(10):
    turtle.dot()
    turtle.forward(10)
turtle.right(120)
for i in range(11):
    turtle.dot()
    turtle.forward(10)

turtle.backward(50)
turtle.right(120)
for i in range(10):
    turtle.dot()
    turtle.forward(6)

#Exit from A

turtle.pendown()
turtle.color("darkgreen")
turtle.speed(3)
turtle.forward(600)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.color("darkorchid4")
turtle.forward(700)
turtle.right(90)
turtle.forward(140)
for i in range(10):
    turtle.dot()
    turtle.forward(10)


#sixth letter [ D ]
turtle.speed(0)
turtle.penup()
turtle.left(90)
for i in range(3):
    turtle.dot()
    turtle.forward(10)

for i in range(4):
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.dot()
    turtle.forward(10)

turtle.backward(10)
turtle.left(90)
for i in range(6):
    turtle.dot()
    turtle.forward(10)

for i in range(3):
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.dot()
    turtle.forward(10)

turtle.backward(10)
turtle.left(90)

for i in range(5):
    turtle.dot()
    turtle.forward(10)

turtle.backward(90)

#Seventh letter [ I ]
turtle.left(90)
turtle.color("darkorange4")
turtle.speed(5)
turtle.dot()
turtle.forward(10)

for i in range(10):
    turtle.dot()
    turtle.forward(10)

turtle.backward(10)
turtle.left(90)
turtle.forward(40)

# Eight letter [ R ]
turtle.color("maroon1")
turtle.left(90)

for i in range(11):
    turtle.dot()
    turtle.forward(10)

turtle.backward(10)
turtle.right(90)

for i in range(3):
    turtle.dot()
    turtle.forward(10)

a = 0
for i in range(11):
    turtle.right(90)
    turtle.dot()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(3)
    a += 1

turtle.backward(70)

for i in range(3):
    turtle.dot()
    turtle.forward(10)


a = 0
for i in range(7):
    turtle.left(90)
    turtle.dot()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(5)
    a += 1

turtle.speed(5)
turtle.pendown()
turtle.left(30)
turtle.backward(70)

turtle.left(45)
turtle.forward(25)
turtle.right(120)

for i in range(10):
    turtle.dot()
    turtle.forward(10)

turtle.exitonclick()
