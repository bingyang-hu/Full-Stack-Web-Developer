/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop




// While Loop

alert("How are you?")

var i = 1;
while (i<=5) {
  console.log("hello!");
  i = i+1;
}


// For Loop

var i;
for (i=1;i<=5;i++){
  console.log("Hi!!");
}




/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop

var m =1;

while (m<=25){
  if (m%2 != 0){
    console.log(m);
  }
  m++;
}


// METHOD TWO
// For Loop

var m;

for (m=1; m<=25;m++){
  if(m%2 ===0){
    console.log(m);
  }
}
