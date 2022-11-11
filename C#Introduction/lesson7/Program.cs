// Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.

// m = 3, n = 4.

// 0,5 7 -2 -0,2

// 1 -3,3 8 -9,9

// 8 7,8 -7,1 9

// Console.Write("Введите первое число: ");
// int m =Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите второе число: ");
// int n =Convert.ToInt32(Console.ReadLine());
// double [,] numbers=new double[m,n];
// FillArrayRandomNumbers(numbers);
// PrintArray(numbers);
// void FillArrayRandomNumbers(double[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             array[i, j] = Convert.ToDouble(new Random().Next(-100, 100)) / 10;
//         }
//     }
// }

// void PrintArray(double[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         Console.Write("[ ");
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j] + " ");
//         }
//         Console.Write("]");
//         Console.WriteLine("");
//     }
// }

// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.

// Например, задан массив:

// 1 4 7 2

// 5 9 2 3

// 8 4 2 4

// 17 -> такого числа в массиве нет

// Console.WriteLine("Введите номер столбца: ");
// int m= Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Введите номер строки: ");
// int n =Convert.ToInt32(Console.ReadLine());
// int [,] array=new int[3,8];
// FillArrayRandomNumbers(array);

// void FillArrayRandomNumbers(int [,] array)
// {
// for(int i=0; i<array.GetLength(0); i++ ) 
//   {
//     for(int j=0; j<array.GetLength(1);j++)

//      {
//         array[i,j]=new Random().Next(-100,100)/10;
//      }
//   }
// }
// if (m > array.GetLength(0) || n > array.GetLength(1))
// {
//     Console.WriteLine("такого элемента нет");
// }
// else
// {
//     Console.WriteLine($"значение элемента {m} столбца и {n} строки равно {array[m-1,n-1]}");
// }


///////////////////////////////////////////////////////////////////////////////

// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
int n=5;
int m=6;
int [,] array=new int[n, m];

for (int i=0; i<n; i++)
{ 
    Console.Write("[ ");
    for(int j=0; j<m; j++)
    {
        array[i, j] = new Random().Next(0, 100);

        Console.Write(array[i, j] + " ");
    }
    Console.Write("]");
    Console.WriteLine("");
}


