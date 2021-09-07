function maxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];
    for (var i = 1; i < arr.length; i++){
        sum += arr[i];
        if (arr[i] > max){
            max = arr[i];
        }else if (arr[i] < min){
            min = arr[i];
        }
    }
    console.log("Max:", max,"Min:", min,"Average:", sum/arr.length);
}
maxMinAvg([95,-15,70,4,2600,20])