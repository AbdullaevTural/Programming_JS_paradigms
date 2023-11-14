// Задача №1
// Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
// сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

const numbers = [1,8,9,4,5,2,6,3,7];

for (let j = numbers.length - 1; j > 0; j--) {  // Пузырьковая сортировка
    for (let i = 0; i < j; i++) {
      if (numbers[i] < numbers[i + 1]) {
        let temp = numbers[i];
        numbers[i] = numbers[i + 1];
        numbers[i + 1] = temp;
      }
    }
  }
  console.log(numbers);

// 💡 Задача №2
// Написать точно такую же процедуру, но в декларативном стиле

 numbers.sort((a, b) => b - a);
 console.log(numbers);