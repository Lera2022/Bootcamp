from random import randint
start = 0
end = 100
x = randint(start, end)

count_perebor = 0
# метод последовательного перебора
for i in range(0, 101):
    count_perebor +=1
    if i == x:
        print("Число найдено!")
        break
 
print("Загаданное число было", x, "и для его поиска потребовалось", count_perebor, "итераций методом 1")

count_random = 1
# метод случайного отгадывания
y = randint(0, 100)
while x != y:
    y = randint(0, 100)
    count_random += 1

print("Загаданное число было", x, "и для его поиска потребовалось", count_random, "итераций методом 2")

count_bin = 0
mid = end // 2
while x != mid:
    if x < mid: 
        end = mid - 1 
    else: 
        start = mid + 1
    mid = (start + end) // 2
    count_bin += 1

print("Загаданное число было", x, "и для его поиска потребовалось", count_bin, "итераций бинарным алгоритмом")
