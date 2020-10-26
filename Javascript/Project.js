var firstName=prompt("Hello and welcome, please enter your first name:");

var lastName=prompt("Please enter your last name:")

var age=prompt("How old are you?")

var height=prompt("How tall are you in centimeters? ")

var petName= prompt("What is the name of your pet?")

alert("Thank you so much for the information!! ")


if (firstName[0]===lastName[0] && age>20 && age<30 && height>=170 && petName[petName.length-1]==="y")
{
	console.log("You passed the test!");

}
	else

{
	console.log("Nothing!");
}
