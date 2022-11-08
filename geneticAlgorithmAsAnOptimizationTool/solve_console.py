import random
from tkinter import *


c=[9.95, 3.66, 57.05, 10.485, 11.97, 18.17, 13.425, 3.28, 18.16]  #средства, выделяемых конкретным ЦФО на реализацию собственных инвестиционых программ , всего 9 ЦФО значит 9 значений
M=55.83  #плановый годовой объем финансовых средств, выделяемый центральной компанией на реализацию нововведений ЦФО
r=11   #допустимая средняя прибыль на 1 руб.затрат (норма прибыли на капитал)
p=1 #ограничение на суммарную рискованность инвестиционного портфеля;
risk=[]   #риск по проектам
marja=[]   #прибыль от проектов
costs=[]    #стоимость проектов
names=[]   #имена проектов
#0 регион
risk.append([2.73, 1.63])
marja.append([15.31, 14.68])
costs.append([10.42, 9.48])
names.append(["реконструкция офисных зданий и сооружений","выделение группы технологического аудита в обособленную структуру"])
#1 регион

risk.append([1.7])
marja.append([14.77])
costs.append([7.32])
names.append(["разработка и внедрение специальных средств упаковки ценных грузов"])
#2 регион

risk.append([1.52,1.64,2.32,1.12])
marja.append([14.03,15.76,15.7,13.08])
costs.append([11.31,10.85,13.51,10.87])
names.append(["приобретение и оборудование бронеавтомобилей","разработка и внедрение специальных средств упаковки ценных грузов",
"установка спутниковых датчиков GPS по отслеживанию выполнения маршрута","приобретение и доукомплектование грузового и легкового автотранспорта"])
#3 регион
risk.append([1.44, 2.83])
marja.append([15.25,14.49])
costs.append([6.38,14.59])
names.append(["приобретение и доукомплектование грузового и легкового автотранспорта","сдача в аренду сторонним организациям части площадей"])
#4 регион
risk.append([1.73,1.42])
marja.append([13.39,14.95])
costs.append([13.71,10.23])
names.append(["приобретение и доукомплектование грузового и легкового автотранспорта","установка спутниковых датчиков GPS по отслеживанию выполнения маршрута"])
#5 регион
risk.append([1.19,2.54,1.51])
marja.append([17.39,13.18,13.27])
costs.append([13.16,12.15,11.03])
names.append([" закупка запчастей",
              "реконструкция офисных зданий и сооружений",
              "приобретение и оборудование бронеавтомобилей"])
#6 регион
risk.append([2.57,2.63])
marja.append([17.05,16.81])
costs.append([14.95,11.9])
names.append(["переход на заправки по топливным картам, отказ от заправок за наличные средства",
              "установка спутниковых датчиков GPS по отслеживанию выполнения маршрута"])
#7 регион
risk.append([2.24])
marja.append([14.41])
costs.append([6.56])
names.append(["приобретение и оборудование бронеавтомобилей"])
#8 регион
risk.append([1.05,1.08,1.14])
marja.append([13.93,14.05,16.41])
costs.append([11.55,13.69,11.08])
names.append(["приобретение базы (г.Находка)","приобретение и доукомплектование грузового и легкового автотранспорта",
              "разработка и внедрение специальных средств упаковки ценных грузов"])

projects_in_region=[2,1,4,2,2,3,2,1,3] #количество проектов по регионам
regions=9

childs=100 #количество экземпляров в одном
generations=100 #количество поколений

x=[] #пока пустой массив с экземплярами
pokolenie=[]  #пустое поколение

up_cost=0   # с+М , надо посчитать
pobeditel=[]

def first_x(): #заполнили поколение случайным образом
    global pokolenie
    for k in range(childs):
         x=[]
         for i in range(regions):   #создаем случаный ответ
             pr=[]
             for y in range(projects_in_region[i]):
                 pr.append(random.randint(0,1))
             x.append(pr)
         pokolenie.append(x)

def fitness(X):   #функция определения значения целевой функции (считается прибыль этого варианта)
        max = 0
        for i in range(regions):
            for j in range(len(X[i])):
                # исходная функция, которую нужно максимизировать
                max=max+X[i][j]*marja[i][j]
        return max

def seek_max():      #функция нахождения максимального значения ЦФ во всем поколении
    #old_generation=x.copy()  # копируем всё поколение
    f_max=0
    for i in range(childs):
        f=fitness(pokolenie[i])
        if f>f_max:
            f_max=f
    return f_max

def up_limit():   #находим предел затрат, то есть считаем край бюджета и сохраняем в up_cost
    global up_cost
    up_cost=M
    for i in c:
        up_cost+=c[0]

def test_costs(X):  #функция определения стоимости реализации особо, то есть надо сравнивать это 
    #значение и чтоб не было больше c+M
    s=True
    stoimost=0
    for i in range(regions):
        for j in range(len(X[i])):
            # исходная функция, которую нужно максимизировать
            stoimost= stoimost + X[i][j] * costs[i][j]
    return stoimost

def test_one_project(X):  #функция определения наличия хотя бы одного проекта
    rez=True
    s=0
    for i in range(regions):
        s=0
        for j in range(len(X[i])):
            # исходная функция, которую нужно максимизировать
            s=s + X[i][j]
        if s==0:
            rez=False
    return rez


def new_generation():
    global pokolenie
    old_generation = pokolenie.copy()  # копируем всё поколение
    s=seek_max()    #находим чемпиона и его значение ЦФ (находим максимальную прибыль в прошлом поколени)
    pokolenie=[]
    for i in range(childs):          #оставляем все особи у которых целевая функция больше чем 80% от максимального значения
        if fitness(old_generation[i])>=0.8*s and test_costs(old_generation[i])<=up_cost and test_one_project(old_generation[i]):
            pokolenie.append(old_generation[i])
    for k in range(childs-len(pokolenie)):                #далее дозаполняем случайными значениями
         x=[]
         for i in range(regions):
             pr=[]
             for y in range(projects_in_region[i]):
                 pr.append(random.randint(0,1))
             x.append(pr)
         pokolenie.append(x)

def seek_winner():  #нахождение чемпиона в поколении
    winners=[]
    for i in range(childs):
        if fitness(pokolenie[i]) >= seek_max()*0.5 and test_costs(pokolenie[i])<=up_cost and test_one_project(pokolenie[i]) :
            winners.append([pokolenie[i],fitness(pokolenie[i])])
    max_cf=0
    for i in winners:
        if i[1]>max_cf:
            return i[0]


up_limit() #находим предел затрат, то есть считаем край бюджета

first_x()   #генерируем случайные значения первого поколения

new_generation()   #генериуем новое поколение, но оставляем часть старого


for i in range(generations*10): #проводим эволюцию заданное количество поколений
    new_generation()

w=seek_winner()
print(w) #вывод победителя
print("Прибыль от победителя - ",fitness(w))   #вывод прибыли от победители, должно быть 246,82
print("Затраты на реализацию проектов  победителя - ",test_costs(w)) #проверка стоимости реализации победителя
print("Лимит трат на реализацию ",up_cost)  #вывод на экран