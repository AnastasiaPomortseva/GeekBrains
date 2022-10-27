//  10 задача. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
//456 -> 5 ; 782 -> 8 ; 918 -> 1

//Console.WriteLine("Введите трехзначное число");
//String number = Console.ReadLine();
//char[] charArray = number.ToCharArray();
//Console.WriteLine(charArray[1]);

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Задача 13: Напишите программу, которая выводит третью цифру СЛЕВА заданного числа или сообщает, что третьей цифры нет.
// 645 -> 5 78 -> третьей цифры нет 3267912 -> 6

// Console.WriteLine("Введите число");
// String number = Console.ReadLine();
// char[] charArray = number.ToCharArray();
// if (charArray.Length < 3) Console.WriteLine("третьей цифры нет");
// else Console.WriteLine(charArray[2]);

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
// 6 -> да 7 -> да 1 -> нет

// Console.WriteLine("Введите цифру обозначающую день недели");
// char[] workDays = {'1','2','3','4','5'};
// char[] weekends = {'6','7'}; 
// String number = Console.ReadLine();
// char[] charArray = number.ToCharArray();
// if (workDays.Contains(charArray[0])) Console.WriteLine("нет");
// else if (weekends.Contains(charArray[0])) Console.WriteLine("да");
// else Console.WriteLine("неправильные входные данные");

// Задача 19
// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 12821 -> да
// 23432 -> да

//  Console.WriteLine("Введите число");
//  String number = Console.ReadLine();
// char[] charArray = number.ToCharArray();
// int counter = 0;
// for(; counter < 2; counter++) {
//     if (charArray[counter] == charArray[charArray.Length - counter - 1]) continue;
//     else break;
// }
// if(counter == 2) Console.WriteLine("да");
// else Console.WriteLine("нет");

/////////////////////////////////////////////////////////////////////
// Задача 21
// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// // A (7,-5, 0); B (1,-1,9) -> 11.53

// Console.WriteLine("Введите три координаты точки А :");
// int[] aCoordinates = new int[3];
// int[] bCoordinates = new int[3];

// for(int i = 0; i < 3; i++) {
//     Console.WriteLine(i+1 + "я координата точки А :");
//     String value = Console.ReadLine();
//     aCoordinates[i] = Int32.Parse(value);
// }

// Console.WriteLine("Введите три координаты точки B :");
// for(int i = 0; i < 3; i++) {
//     Console.WriteLine(i+1 + "я координата точки B :");
//     String value = Console.ReadLine();
//     bCoordinates[i] = Int32.Parse(value);
// }
// double result = Math.Sqrt(Math.Pow(bCoordinates[0] - aCoordinates[0], 2) + Math.Pow(bCoordinates[1] - aCoordinates[1], 2) + Math.Pow(bCoordinates[2] - aCoordinates[2], 2));

// Console.WriteLine("Расстояние между двумя точками :" + result);


//////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Задача 23

// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125

Console.WriteLine("Введите число :");
String value = Console.ReadLine();
int n = Int32.Parse(value);
for(int i = 1; i <= n; i++) {
    double result = Math.Pow(i, 3);
    if(i != n) Console.Write(result + ", ");
    else Console.Write(result);
}
