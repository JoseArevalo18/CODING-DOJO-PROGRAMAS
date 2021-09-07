var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

// print John's age
console.log(users[1].age);

// print the name of the first object
console.log(users[0].name);


for (var i = 0; i < users.length; i++){// imprime el nombre y la edad de cada usuario usando un bucle for
    console.log(users[i].name, "-", users[i].age);
}