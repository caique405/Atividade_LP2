from turtle import *
#Turtle é um módulo que desenha na tela de acordo com os comandos.
pencolor('red')
fillcolor('Blue')
begin_fill()
for c in range(0, 4):
    forward(90)# frente
    right(90)#direita

end_fill()
backward(90)
left(90) #esquerda
backward(90) #para tras
setx(90) #cordenada para x
sety(90) # cordenada para y
setposition(100, 100) #estabelece coodenadas x e y
setheading(45) #altera o angulo da seta

done()





# from turtle import *
# from random import choice
# corCaneta = ('Yellow', 'Red', 'Blue', 'Purple', 'Pink')
# for c in range(0, 4):
#     pencolor(choice(corCaneta))
#     forward(90)
#     right(90)
#     pencolor(choice(corCaneta))

# setposition(65, 65)

# for c in range(0, 4):
#     pencolor(choice(corCaneta))
#     forward(90)
#     right(90)
#     pencolor(choice(corCaneta))
# forward(90)
# setposition(90, 0)
# right(90)
# forward(90)
# done()


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
