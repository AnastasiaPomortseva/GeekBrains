// Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.

//3, 5 -> 243 (3⁵)

//2, 4 -> 16

//Console.WriteLine("Введите 1 число: ");
//int number1 = Convert.ToInt32 (Console.ReadLine());
//Console.WriteLine("Введите 2 число: ");
//int number2 = Convert.ToInt32 (Console.ReadLine());
//double result=Math.Pow (number1,number2);
//Console.WriteLine(result);

/////////////////////////////////////////////////////////////////////////////////

//Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
//452 -> 11
//82 -> 10
//9012 -> 12


// int DigitSum(int n)
// {
//     int result=0;
//     int digit=0;
//     if (n==1) return 1;
//     while(n>0)
//     {
//         digit= n % 10;
//         result=result+digit;
//         n=n/10;
//     }
// return result;

// }

// Console.Write("Введите число: ");
// int n= Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Сумма цифр в числе: " + DigitSum(n));


/////////////////////////////////////////////////////////////////////////////////////////
//Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.

//1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]

//6, 1, 33 -> [6, 1, 33]/


int [] numbers=new int[4] {2,4,6,8};
int n=numbers.Length;
for (int i=0; i<n; i++)
{
    int result=numbers[i];
    Console.Write(result + ", ");
    
}