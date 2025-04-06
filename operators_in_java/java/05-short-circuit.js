//short circuit //falsy


   // ALL THIS VALUES  CALL FALSY
//false
//false
//0
//''
//null
//undefined
//Nan

let name = "happy piggy";
let username = name || 'anonymous';
console.log(username);


function fn1(){
    console.log('I am function 1');
    return true;
}

function fn2(){
    console.log('I am function 2');
    return true;
}

let x = fn1() && fn2()

