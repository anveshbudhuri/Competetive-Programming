var text = 'outside';
function logIt(){
    console.log(text);
    var text = 'inside';
};
logIt();

//output : undefined

// because we declare var text again  
//inside of the function logit
// it is intepreted as a new variable inside the function

// this the following code which wii be intepreted

var text = 'outside';
function logIt(){
    var text ;
    console.log(text);
    text = 'inside';
};
logIt();

// output: inside