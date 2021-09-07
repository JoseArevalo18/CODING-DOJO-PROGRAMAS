
function swapTowardCenter(arr){
    for (var i = 0; i < arr.length/2; i+=2){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}
console.log(swapTowardCenter([true,42,'ada',2,'pizza']));
console.log(swapTowardCenter([1,2,3,4,5,6]));