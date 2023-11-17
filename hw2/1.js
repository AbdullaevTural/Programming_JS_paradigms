const number = prompt("Ведите число")
function multiplicationTable(n) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        console.log(`${i} * ${j} = ${i * j}`);
      }
      console.log('-----------------');
    }
  }
  
  // Вызов функции для n = 5 (можно изменить значение n)
  multiplicationTable(number);