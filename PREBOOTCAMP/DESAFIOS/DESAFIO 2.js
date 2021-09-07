function printSum(x) {
    var sum = 0;
        for(var sum=0;sum<=x;sum++){
        console.log(sum);
        }
        if(sum>=x){
            console.log(((x*sum)/2))
        }
        // escribe tu código aquí
    return sum;
}
y = printSum(255) // debe imprimir todos los enteros desde el o hasta el 255, y la suma parcial en cada punto
console.log(y) // debe imprimir 32640