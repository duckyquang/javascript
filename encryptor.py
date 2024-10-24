const equation = "levigay";
const alphabet = "abcdefghijklmnopqrstuvwxyz"
let list = [];
let finallist = [];
let key = 3;

for (let i=0; i < equation.length; i++) {
    list += equation[i];
};

let i = 0;

while (i < list.length) {
    letter = equation[i];
    indexofletter = alphabet.indexOf(letter);

    finallist += alphabet[(indexofletter + key) % alphabet.length];
    
    i++;
};

console.log("Initial text: ", list);
console.log("Key: ", key);
console.log("Final text: ", finallist);
