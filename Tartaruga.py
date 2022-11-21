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