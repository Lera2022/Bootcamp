from turtle import *
from random import randint
from time import *

finish = 200    # дистанция гонки

t1 = Turtle()   # создали объект класса черепахи
t1.shape("turtle")  # поменяли форму объекта
t1.color("red")     # меняем цвет объекта
t1.penup()          #  поднимаем черепаху чтоб не рисовала
t1.goto(-200, 20)   # перемещаем черепашку по координатам
t1.pendown()        # опускаем черепашку чтоб потом рисовала
t1.speed(3)

t2 = Turtle()   # создали объект класса черепахи
t2.shape("turtle")  # поменяли форму объекта
t2.color("blue")     # меняем цвет объекта
t2.penup()          #  поднимаем черепаху чтоб не рисовала
t2.goto(-200, -20)   # перемещаем черепашку по координатам
t2.pendown()        # опускаем черепашку чтоб потом рисовала
t2.speed(3)

def razmetka():     # функция рисует разметку поля
    t = Turtle()
    for i in range(1, 21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()

razmetka()

def catch1(x, y):   # это обработчик события нажатия 
    t1.write('Ouch!', font=('Arial', 14, 'normal')) # пишем на экране Ауч
    t1.fd(randint(10, 15))  # черепашка делает случайный шаг от 10 до 15

t1.onclick(catch1)  # прикрепляю обработчик к событию нажатия на 1 черепашку

def catch2(x, y):   # это обработчик события нажатия 
    t2.write('Мне больно!', font=('Arial', 14, 'normal')) # пишем на экране Ауч
    t2.fd(randint(10, 15))  # черепашка делает случайный шаг от 10 до 15

t2.onclick(catch2)  # прикрепляю обработчик к событию нажатия на 2 черепашку

while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2, 7))   # здесь черепаха двигается вперёд и рисует на случайное число в диапазоне от 2 до 7
    t2.forward(randint(2, 7))
    sleep(0.05)