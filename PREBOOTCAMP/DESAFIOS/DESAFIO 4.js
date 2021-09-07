function mayorElem(x) {
    var mayorHastaAhora = x[0];
    if(x[0]<x[1]){
        console.log(x[1]);
    }
        else if(x[0]<x[2]){
            console.log(x[2]);
        }
            else if(x[0]<x[3]){
                console.log(x[3]);
            }
                else if (x[0]<x[4]){
                    console.log(x[4]);
                }
                else{
                    console.log("no hay valor alto");
                }
                return mayorHastaAhora;
                }

console.log( mayorElem([8,3,11,2,-8]) ); // debe imprimir 11