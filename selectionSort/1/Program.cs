// [6, 15, 2, 9, -3]
// MIN = 6
// 6 < 15
// 6 > 2
// MIN = 2
// 2 < 9
// 2 > -3
// MIN = -3
// [-3, 6, 15, 2, 9]
// [6, 15, 2, 9]
// MIN = 6
// 6 < 15
// 6 > 2
// MIN = 2
// 2 < 9
// [-3, 2, 6, 15, 9]
// MIN = 6
// 6 < 15
// 6 < 9
// [-3, 2, 6, 15, 9]
// MIN = 15
// 15 > 9
// [-3, 2, 6, 9, 15]

Console.WriteLine("Введите кол-во элементов массива:");
int n = Convert.ToInt32(Console.ReadLine());
// Заполнение массива
int[] array = new int[n];
for (int i = 0; i < n; i++)
{
    Console.Write("Введите число: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine();
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
// Cортировка
for (int i = 0; i < n - 1; i++)
{
    int MinIndex = i;
    for (int j = i + 1; j < n; j++)
    {
        if (array[j] < array[MinIndex])
            MinIndex = j; 
    }
    int temp;
    temp = array[MinIndex];
    array[MinIndex] = array[i];
    array[i] = temp;
}
Console.WriteLine("Конечный массив: [" + string.Join(", ", array) + "]");
