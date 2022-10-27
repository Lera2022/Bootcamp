string[] array = {"Monday", "Tuersday", "Wednesday", "Thirsday", "Friday"};

Console.Write("[" + string.Join(", ", array) + "]");
for (int i = 0; i < 4; i++)
{
    int MinIndex = i;
    for (int j = i + 1; j < 5; j++)
    {
        if (array[j].Length < array[MinIndex].Length)
            MinIndex = j; 
    }
    string temp;
    temp = array[MinIndex];
    array[MinIndex] = array[i];
    array[i] = temp;
}
Console.WriteLine("Конечный массив: [" + string.Join(", ", array) + "]");