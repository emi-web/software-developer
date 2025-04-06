// character  tv

let name = "tanjiro";
let anime = "demon slayer"
let age = 16;

let character = {
    name: "tanjiro",
    anime: "demon slayer",
    age: "16,"
};

console.log(character);

console.log(character.name);  // ways to print only one
console.log(character['anime'])


//if i want modify

character.age = 13;
character['age'] = 14;


//if i want delete

delete character.anime;
console.log(character);