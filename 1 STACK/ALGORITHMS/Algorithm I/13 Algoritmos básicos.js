// Obtén del 1 al 255: Escribe una función
// que devuelve un array con todos los números del 1 al 255. 

for (var i = 1; i <= 255; i++) {

    console.log(i)
}
// OUTPUT: 1..255

// Consigue pares hasta 1000: Escribe una función
// que entregue la suma de todos los números
// pares del 1 al 1000 - Puedes usar un operador
// de módulo para este ejercicio.
function getSum() {
    var sum = 0;
    for (var i = 1; i <= 1000; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    return sum;
}
console.log(getSum());
// OUTPUT: 250500

// Sum odd 5000 - Write a function that returns
//  the sum of all the odd numbers
// from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
function getSumOdd() {
    var sum = 0;
    for (var i = 1; i <= 5000; i += 2) {
        if (i % 2 == 1) {
            sum = sum + i;
            console.log(i);
        }
    }
    return sum;
}
console.log(getSumOdd());
// OUTPUT: 1, 3,...5000

// Iterate an array - Write a function that returns
//  the sum of all the values within a given array.
//   (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function iterate(numArr) {
    var sum = 0;
    for (var i = 0; i < numArr.length; i++) {
        sum = sum + numArr[i];
    }
    return sum;
}
console.log(iterate([-9, 27, 4, 78, 0.86]));
// OUTPUT: 100.86

//  Find max - Given an array with multiple values, write a function that
// returns the maximum number in the array. 
// (e.g. for [-3,-5,-6,-2] max is 7)

function maxArr(arr) {
    var max = arr[0];
    var sum = arr[0];

    for (var i = 1; i < arr.length; i++) {
        sum += arr[i];
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    console.log("Max:", max);
}
maxArr([479, 0.47, -3, 33])
// OUTPUT: Max: 479

// Find average - Given an array with multiple values,
// write a function that returns the average of the values in the array.
// (e.g. for [1,3,5,7,20] average is 7.2)

function Avg(arr) {
    var max = arr[0];
    var sum = arr[0];
    for (var i = 1; i < arr.length; i++) {
        sum += arr[i];
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    console.log("Average:", sum / arr.length);
}
Avg([95, -1, 70, 4, 3400, 20])
// OUTPUT: Average: 598

// Array de impares: Escribe una función que devuelva un array
// de todos los números impares entre 1 y 50
// (ej: [1, 3, 5, …, 47, 49]).Pista: Usa el método‘ push’.
function returnOddArray() {
    var arr = [];
    for (var i = 1; i <= 50; i += 2) {
        arr.push(i);
    }
    return arr;
}
var y = returnOddArray();
console.log(y);
// OUTPUT: [
//     1, 3, 5, 7, 9, 11, 13, 15,
//     17, 19, 21, 23, 25, 27, 29, 31,
//     33, 35, 37, 39, 41, 43, 45, 47,
//     49
// ]

// Mayor que Y: Dado un valor Y, escribe una función que toma
//  un array y devuelve los valores mayores que Y.Por ejemplo,
//   si arr = [1, 3, 5, 7] y Y = 3, tu función devolverá
// 2(hay 2 números en el array mayores que 3, esto son 5 y 7).
function greaterThanY(arr, y) {
    var counter = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > y) {
            counter++;
        }
    }
    console.log("Values greater than", y, ":", counter);
}
greaterThanY([50, -3, -60, 10], 0);
// OUTPUT: Values greater than 0: 2

// Cuadrados: Dado un array con múltiples valores, escribe una función
// que reemplace cada valor por el cuadrado del mismo valor
// (ej: [1, 5, 10, -2] será[1, 25, 100, 4]).
function squareValue(x) {
    for (var i = 0; i < x.length; i++) {
        x[i] = x[i] * x[i];
    }
    return x;
}
var y = squareValue([1, 2, 3]);
console.log(y); // should log [1,4,9]

var y = squareValue([2, 5, 8]);
console.log(y); // should log [4,25,64]
// OUTPUT:[1, 4, 9]
//        [4, 25, 64]

// Negativos: Dado un array con múltiples valores, escribe una función
// que reemplace cualquier número negativo dentro del array por 0.
// Cuando el programa esté listo, el array no debiera contener
// números negativos(ej: [1, 5, 10, -2] se convertirá en[1, 5, 10, 0]).
function replaceNegatives(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 0;
        }
    }
    return arr;
}

var result = replaceNegatives([-9, 45, 60, -50]);
console.log(result);
// OUTPUT: [0, 45, 60, 0]

// Max / Min / Avg: Dado un array con múltiples valores, escribe una función
//  que devuelva un nuevo array que solo contenga el valor
//   mayor(max), menor(min) y promedio(avg) del array original
//   (ej: [1, 5, 10, -2] devolverá[10, -2, 3.5]).
function maxMinAvg(arr) {
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];
    for (var i = 1; i < arr.length; i++) {
        sum += arr[i];
        if (arr[i] > max) {
            max = arr[i];
        } else if (arr[i] < min) {
            min = arr[i];
        }
    }
    console.log("Max:", max, "Min:", min, "Average:", sum / arr.length);
}
maxMinAvg([95, -1, 70, 4, 3400, 20])
// OUTPUT: Max: 3400 Min: -1 Average: 598

// Intercambia Valores: Escribe una función que intercambie el primer y el último valor
// de cualquier array.La extensión mínima predeterminada del array es 2
// (ej: [1, 5, 10, -2] será[-2, 5, 10, 1]).
function swap(arr) {
    var temp = arr[arr.length - 1];
    arr[arr.length - 1] = arr[0];
    arr[0] = temp;
}
var tester = [1, 4, 10, -2];
swap(tester);
console.log(tester);
// OUTPUT: [-2, 4, 10, 1]


// De Número a String: Escribe una función que tome un array de números y reemplace cualquier
// valor negativo por el string‘ Dojo’.Por ejemplo,
// dado el array = [-1, -3, 2], tu función devolverá[‘Dojo’, ‘Dojo’, 2].
function replaceNegatives(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = "Dojo";
        }
    }
    return arr;
}

var result = replaceNegatives([-9, 45, 60, -50]);
console.log(result);

// OUTPUT: ['Dojo', 45, 60, 'Dojo']