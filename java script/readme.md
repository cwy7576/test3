# JavaScript <br>is the world's most popular programming language.

* JavaScript Can Change HTML Content
* One of many JavaScript HTML methods is `getElementById().`

# Example 

```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p id="demo">JavaScript can change HTML content.</p>

<button type="button" onclick="document.getElementById('demo').innerHTML = 'Hello JavaScript!'">Click Me!</button>

</body>
</html>
```
## JavaScript Can Change HTML Attribute Values
* In this example JavaScript changes the value of the `src` (source) attribute of an `<img>` tag:

## Example

```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p>JavaScript can change HTML attribute values.</p>

<p>In this case JavaScript changes the value of the src (source) attribute of an image.</p>

<button onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn on the light</button>

<img id="myImage" src="pic_bulboff.gif" style="width:100px">

<button onclick="document.getElementById('myImage').src='pic_bulboff.gif'">Turn off the light</button>

</body>
</html>
```
### JavaScript Can Change HTML Styles (CSS)

* Changing the style of an HTML element, is a variant of changing an HTML attribute:

## Example 
```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p id="demo">JavaScript can change the style of an HTML element.</p>

<button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">Click Me!</button>

</body>
</html> 
```
## JavaScript Can Hide HTML Elements

* Hiding HTML elements can be done by changing the `display` style:

```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p id="demo">JavaScript can hide HTML elements.</p>

<button type="button" onclick="document.getElementById('demo').style.display='none'">Click Me!</button>

</body>
</html> 
```

## JavaScript Can Show HTML Elements
* Showing hidden HTML elements can also be done by changing the `display `style:

```html
<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p>JavaScript can show hidden HTML elements.</p>

<p id="demo" style="display:none">Hello JavaScript!</p>

<button type="button" onclick="document.getElementById('demo').style.display='block'">Click Me!</button>

</body>
</html> 
```
# JavaScript Where To
## The `<script>` Tag
The `<script> `Tag


* In HTML, JavaScript code is inserted between `<script> and </script>` tags.

## Example
```html
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript in Body</h2>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>

</body>
</html> 
```
## JavaScript Functions and Events
* A JavaScript `function `is a block of JavaScript code, that can be executed when "called" for.

For example, a function can be called when an event occurs, like when the user clicks a button.
## JavaScript in `<head>` or `<body>`
* You can place any number of scripts in an HTML document.

Scripts can be placed in the `<body>,` or in the `<head>` section of an HTML page, or in both.
## JavaScript in `<head>`
* In this example, a JavaScript `function` is placed in the `<head>` section of an HTML page.

The function is invoked (called) when a button is clicked:

## Example 
```html
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>
</head>
<body>
<h2>Demo JavaScript in Head</h2>

<p id="demo">A Paragraph</p>
<button type="button" onclick="myFunction()">Try it</button>

</body>
</html>
```

## JavaScript in <body>
* In this example, a JavaScript `function` is placed in the `<body>` section of an HTML page.

The function is invoked (called) when a button is clicked:

## Example 
```html
<!DOCTYPE html>
<html>
<body>

<h2>Demo JavaScript in Body</h2>

<p id="demo">A Paragraph</p>

<button type="button" onclick="myFunction()">Try it</button>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>

</body>
</html>
```
## External JavaScript
* Scripts can also be placed in external files:

```html

function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
```
* External scripts are practical when the same code is used in many different web pages.

JavaScript files have the file extension .js.

To use an external script, put the name of the script file in the `src` (source) attribute of a `<script>` tag:
## Example 
```html
<script src="myScript.js"></script>
```
*ou can place an external script reference in `<head>` or `<body>` as you like.

The script will behave as if it was located exactly where the `<script>` tag is located.

## External JavaScript Advantages
* Placing scripts in external files has some advantages:

It separates HTML and code

It makes HTML and JavaScript easier to read and maintain

Cached JavaScript files can speed up page loads

## Example 
```html
<script src="myScript1.js"></script>
<script src="myScript2.js"></script>
```
## External References
* An external script can be referenced in 3 different ways:

With a full URL (a full web address)

With a file path (like /js/)

Without any path

## This example uses a full URL to link to myScript.js:
## Exaample
```html

<script src="https://www.w3schools.com/js/myScript.js"></script>
```
## This example uses a `file path` to link to myScript.js:

## Example

```html
<script src="/js/myScript.js"></script>

```
## This example uses no path to link to myScript.js:

## Example 

```html
<script src="myScript.js"></script>
```
# JavaScript Output
## JavaScript Display Possibilities
* JavaScript can "display" data in different ways:

* Writing into an HTML element, using `innerHTML.`

Writing into the HTML output using `document.write()`
.

Writing into an alert box, using `window.alert().`

Writing into the browser console, using `console.log().`
## Using innerHTML
* To access an HTML element, JavaScript can use the `document.getElementById(id)` method.

The `id` attribute defines the HTML element. The `innerHTML` property defines the HTML content:

* Example 
```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My First Paragraph</p>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = 5 + 6;
</script>

</body>
</html>
```
## Using document.write()
* For testing purposes, it is convenient to use `document.write():`
* EXample
```html 
<!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My first paragraph.</p>

<script>
document.write(5 + 6);
</script>

</body>
```
* an other Example 
```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My first paragraph.</p>

<button type="button" onclick="document.write(5 + 6)">Try it</button>

</body>
</html>
```

## Using window.alert()
* You can use an alert box to display data:

```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My first paragraph.</p>

<script>
window.alert(5 + 6);
</script>

</body>
</html>
```
* You can skip the window keyword.

## Example
```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My first paragraph.</p>

<script>
alert(5 + 6);
</script>

</body>
</html>
```
## Using console.log()
* For debugging purposes, you can call the `console.log()` method in the browser to display data.
* Example 
```html
<!DOCTYPE html>
<html>
<body>

<script>
console.log(5 + 6);
</script>

</body>
</html>
```
## JavaScript Print
* JavaScript does not have any print object or print methods.

You cannot access output devices from JavaScript.

The only exception is that you can call the `window.print()` method in the browser to print the content of the current window.

* Example
```html
<!DOCTYPE html>
<html>
<body>

<button onclick=15447
</html>
```

# JavaScript Statements
* Example 
```html
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Statements</h2>

<p>A <b>JavaScript program</b> is a list of <b>statements</b> to be executed by a computer.</p>

<p id="demo"></p>

<script>
let x, y, z;  // Statement 1
x = 5;        // Statement 2
y = 6;        // Statement 3
z = x + y;    // Statement 4

document.getElementById("demo").innerHTML =
"The value of z is " + z + ".";  
</script>

</body>
</html>
```

## JavaScript Programs
* A computer program is a list of "instructions" to be "executed" by a computer.

In a programming language, these programming instructions are called statements.

A JavaScript program is a list of programming statements.
## JavaScript Statements
* JavaScript statements are composed of:

Values, Operators, Expressions, Keywords, and Comments.

This statement tells the browser to write "Hello Dolly." inside an HTML element with id="demo":

* Example
```html
document.getElementById("demo").innerHTML = "Hello Dolly.";
```
## Semicolons  ;
* Semicolons separate JavaScript statements.

Add a semicolon at the end of each executable statement:

## Examples
```html
let a, b, c;  // Declare 3 variables
a = 5;        // Assign the value 5 to a
b = 6;        // Assign the value 6 to b
c = a + b;    // Assign the sum of a and b to c
```
* When separated by semicolons, multiple statements on one line are allowed:

```html
a = 5; b = 6; c = a + b;
```
## JavaScript White Space
* JavaScript ignores multiple spaces. You can add white space to your script to make it more readable.

The following lines are equivalent:
```html
let person = "Hege";
let person="Hege";
```
* A good practice is to put spaces around operators ( = + - * / ):

```html
let x = y + z;
```
## JavaScript Line Length and Line Breaks
* For best readability, programmers often like to avoid code lines longer than 80 characters.

If a JavaScript statement does not fit on one line, the best place to break it is after an operator:

* Example 
```html
document.getElementById("demo").innerHTML =
"Hello Dolly!";
```
## JavaScript Code Blocks
* JavaScript statements can be grouped together in code blocks, inside curly brackets {...}.

The purpose of code blocks is to define statements to be executed together.

One place you will find statements grouped together in blocks, is in JavaScript functions:
* Example
```html
function myFunction() {
  document.getElementById("demo1").innerHTML = "Hello Dolly!";
  document.getElementById("demo2").innerHTML = "How are you?";
}
```
# JavaScript Syntax
* JavaScript syntax is the set of rules, how JavaScript programs are constructed:

```html
// How to create variables:
var x;
let y;

// How to use variables:
x = 5;
y = 6;
let z = x + y;
```
## JavaScript Values
* The JavaScript syntax defines two types of values:

Fixed values

Variable value
## JavaScript Literals
* The two most important syntax rules for fixed values are:

* 1. Numbers are written with or without decimals:

```html
10.50

1001
```
* 2. Strings are text, written within double or single quotes:

```html
"John Doe"

'John Doe'
```
## JavaScript Variables
* In a programming language, variables are used to store data values.


* JavaScript uses the keywords `var,` `let` and `const` to declare variables.

An equal sign is used to assign values to variables.

In this example, x is defined as a variable. Then, x is assigned (given) the value 6:
```html
let x;
x = 6;
```
## JavaScript Operators
* JavaScript uses arithmetic operators `( + - * / )` to compute values:
```html
(5 + 6) * 10
```
* JavaScript uses an assignment operator ( = ) to assign values to variables:

```html

let x, y;
x = 5;
y = 6;
```
## JavaScript Expressions
* An expression is a combination of values, variables, and operators, which computes to a value.

## Example 
```
5 * 10
```
* Expressions can also contain variable values:

```
x * 10
```
* The values can be of various types, such as numbers and strings.

### Example 
```
"John" + " " + "Doe"
```
## JavaScript Keywords
* JavaScript keywords are used to identify actions to be performed.

The `let` keyword tells the browser to create variables:
```css
let x, y;
x = 5 + 6;
y = x * 10;
```
* The `var` keyword also tells the browser to create variables:

```html
var x, y;
x = 5 + 6;
y = x * 10;
```
## JavaScript Comments
* Code after double slashes `// `or between `/*` and `*/ `is treated as a comment.

Comments are ignored, and will not be executed:

```html
let x = 5;   // I will be executed

// x = 6;   I will NOT be executed
```
## JavaScript Identifiers / Names
* Identifiers are used to name variables and keywords, and functions.

*  JavaScript name must begin with:

A letter (A-Z or a-z)

A dollar sign ($)

Or an underscore (_)
## JavaScript is Case Sensitive
* All JavaScript identifiers are case sensitive. 

The variables `lastName` and `lastname,` are two different variables:
```html
let lastname, lastName;
lastName = "Doe";
lastname = "Peterson";
````
# JavaScript Comments
* JavaScript comments can be used to explain JavaScript code, and to make it more readable.

## Single Line Comments
* Single line comments start with `//.`

Any text between `// `and the end of the line will be ignored by JavaScript (will not be executed).

```
let x = 5;      // Declare x, give it the value of 5
let y = x + 2;  // Declare y, give it the value of x + 2
```
## Multi-line Comments
* Multi-line comments start with `/*` and end with `*/.`
```
/*
The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
in my web page:
*/
document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
````
# JavaScript Variables
* 4 Ways to Declare a JavaScript Variable:
* Using var

Using let

Using const

Using nothing

## What are Variables?
* Variables are containers for storing data (storing data values).


* In this example, `x,` `y,` and `z,` are variables, declared with the var keyword:

## Example
```
var x = 5;
var y = 6;
var z = x + y;
```
* In this example, `x,`` y,` and `z,` are variables, declared with the `let` keyword:

* Example 
```
let x = 5;
let y = 6;
let z = x + y;
```
* In this example, `x,` `y,` and `z,` are undeclared variables:

### Example 

```x = 5;
y = 6;
z = x + y;
```

## When to Use JavaScript const?

* If you want a general rule: always declare variables with `const.`

If you think the value of the variable can change, use `let.`

In this example, `price1,` `price2,` and `total,` are variables:

### Example
```html
const price1 = 5;
const price2 = 6;
let total = price1 + price2;
```
### Just Like Algebra
```
let x = 5;
let y = 6;
```
## The Assignment Operator

 * In JavaScript, the equal sign `(=)` is an "assignment" operator, not an "equal to" operator.

```
x = x + 5
```

## JavaScript Data Types

* JavaScript variables can hold numbers like 100 and text values like "John Doe".

## Example
```
const pi = 3.14;
let person = "John Doe";
let answer = 'Yes I am!';
```
## Declaring a JavaScript Variable
```
var carName;
or:
let carName;
```
```html
<p id="demo"></p>

<script>
let carName = "Volvo";
document.getElementById("demo").innerHTML = carName;
</script>
```

## One Statement, Many Variables

* You can declare many variables in one statement.

Start the statement with `var` and separate the variables by comma:

Example

```html
let person = "John Doe", carName = "Volvo", price = 200;
```
* A declaration can span multiple lines:

```html
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Variables</h1>

<p>You can declare many variables in one statement.</p>

<p id="demo"></p>

<script>
let person = "John Doe",
carName = "Volvo",
price = 200;
document.getElementById("demo").innerHTML = carName;
</script>

</body>
</html>
```
## Value = undefined
* A variable declared without a value will have the value `undefined.`

### Example
```
let carName;
```
## Re-Declaring JavaScript Variables
* If you re-declare a JavaScript variable declared with `var,` it will not lose its value.

The variable `carName` will still have the value "Volvo" after the execution of these statements:

## Example

```html
var carName = "Volvo";
var carName;
```
## JavaScript Arithmetic

* As with algebra, you can do arithmetic with JavaScript variables, using operators like `= `and` +:`

```html
let x = 5 + 2 + 3;
```

## JavaScript Dollar Sign $

* Since JavaScript treats a dollar sign as a letter, identifiers containing $ are valid variable names:

### Example

```html
let $ = "Hello World";
let $$$ = 2;
let $myMoney = 5;
```
## JavaScript Underscore (_)
* Since JavaScript treats underscore as a letter, identifiers containing _ are valid variable names:
### Example 
```
let _lastName = "Johnson";
let _x = 2;
let _100 = 5;
```
# JavaScript Let
* Variables defined with `let `cannot be Redeclared.

Variables defined with `let` must be Declared before use.

Variables defined with `let` have Block Scope.

## Cannot be Redeclared
* Variables defined with `let` cannot be redeclared.

You cannot accidentally redeclare a variable.

With `let` you can not do this:

### Example 
```html
let x = "John Doe";

let x = 0;
```
* With `var` you can:

## Example
```
var x = "John Doe";

var x = 0;
```
## Block Scope
* ES6 introduced two important new JavaScript keywords: `let` and `const.`

These two keywords provide Block Scope in JavaScript.

Variables declared inside a { } block cannot be accessed from outside the block:

### Example
```
{
  let x = 2;
}
```
* Variables declared with the `var `keyword can NOT have block scope.

Variables declared inside a { } block can be accessed from outside the block.

### Example
```
{
  var x = 2;
}
```
## Redeclaring Variables
* Redeclaring a variable using the `var` keyword can impose problems.

Redeclaring a variable inside a block will also redeclare the variable outside the block:
## Example 
```
var x = 10;
// Here x is 10

{
var x = 2;
// Here x is 2
}

// Here x is 2
Redeclaring a variable using the let keyword can solve this problem.

Redeclaring a variable inside a block will not redeclare the variable outside the block:

Example
let x = 10;
// Here x is 10

{
let x = 2;
// Here x is 2
}

// Here x is 10
```
## Redeclaring
* Redeclaring a JavaScript variable with `var` is allowed anywhere in a program:

### Example
```
var x = 2;
// Now x is 2

var x = 3;
// Now x is 3
```
* With `let,` redeclaring a variable in the same block is NOT allowed:

### Example

```
var x = 2;    // Allowed
let x = 3;    // Not allowed

{
let x = 2;    // Allowed
let x = 3     // Not allowed
}

{
let x = 2;    // Allowed
var x = 3     // Not allowed
}
```
* Redeclaring a variable with `let,` in another block, IS allowed:

### Example

```
let x = 2;    // Allowed

{
let x = 3;    // Allowed
}

{
let x = 4;    // Allowed
}
```

## Let Hoisting

* Variables defined with `var` are hoisted to the top and can be initialized at any time.

Meaning: You can use the variable before it is declared:

### Example

```
carName = "Volvo";
var carName;
```

### Example

```
carName = "Saab";
let carName = "Volvo";
```
# JavaScript `Const`
 * Variables defined with `const` cannot be Redeclared.

Variables defined with `const `cannot be Reassigned.

Variables defined with `const` have Block Scope.
## Cannot be Reassigned

* A `const` variable cannot be reassigned:

## Example 
```css
const PI = 3.141592653589793;
PI = 3.14;      // This will give an error
PI = PI + 10;   // This will also give an error
```
## Must be Assigned
* JavaScript `const` variables must be assigned a value when they are declared:

## Correct
```
const PI = 3.14159265359;
```
## Incorrect
```
const PI;
PI = 3.14159265359;
```
## Constant Objects and Arrays
* The keyword `const` is a little misleading.

## Constant Arrays

```html
// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];

// You can change an element:
cars[0] = "Toyota";

// You can add an element:
cars.push("Audi");
```
## Constant Objects
* You can change the properties of a constant object:

### Example
```
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";
```

## Block Scope

* Declaring a variable with `const` is similar to `let` when it comes to Block Scope.

The x declared in the block, in this example, is not the same as the x declared outside the block:

### Example
```
const x = 10;
// Here x is 10

{
const x = 2;
// Here x is 2
}

// Here x is 10
```
## Redeclaring
* Redeclaring a JavaScript `var` variable is allowed anywhere in a program:

### Example

```
 var x = 2;     // Allowed
var x = 3;     // Allowed
x = 4;         // Allowed
```
* Redeclaring an existing `var` or `let` variable to `const`, in the same scope, is not allowed:

```
var x = 2;     // Allowed
const x = 2;   // Not allowed

{
let x = 2;     // Allowed
const x = 2;   // Not allowed
}

{
const x = 2;   // Allowed
const x = 2;   // Not allowed
}
````
* Reassigning an existing `const` variable, in the same scope, is not allowed:

```
const x = 2;     // Allowed
x = 2;           // Not allowed
var x = 2;       // Not allowed
let x = 2;       // Not allowed
const x = 2;     // Not allowed

{
  const x = 2;   // Allowed
  x = 2;         // Not allowed
  var x = 2;     // Not allowed
  let x = 2;     // Not allowed
  const x = 2;   // Not allowed
}
```

* Redeclaring a variable with `const,` in another scope, or in another block, is allowed:

```
Vconst x = 2;       // Allowed

{
  const x = 3;   // Allowed
}

{
  const x = 4;   // Allowed
}
```
## Const Hoisting
* Variables defined with `var` are hoisted to the top and can be initialized at any time.

Meaning: You can use the variable before it is declared:

```
carName = "Volvo";
var carName;
```

# JavaScript Operators
* Assign values to variables and add them together:

```

let x = 5;         // assign the value 5 to x
let y = 2;         // assign the value 2 to y
let z = x + y;     // assign the value 7 to z (5 + 2)
```
* The assignment operator `(=) `assigns a value to a variable.
```
let x = 10;
```
* The addition operator `(+)` adds numbers:

### Adding

```
let x = 5;
let y = 2;
let z = x + y;
```
* The multiplication operator (*) multiplies numbers.

## MULTiplying
```
let x = 5;
let y = 2;
let z = x * y;
```

* The addition assignment operator `(+=)` adds a value to a variable.

```
let x = 10;
x += 5;
```
## JavaScript String Operators

* The `+ `operator can also be used to add (concatenate) strings.

```
let text1 = "John";
let text2 = "Doe";
let text3 = text1 + " " + text2;`
```
* The `+=` assignment operator can also be used to add (concatenate) strings:

```
let text1 = "What a very ";
text1 += "nice day";
```


* Adding Strings and Numbers
```
let x = 5 + 5;
let y = "5" + 5;
let z = "Hello" + 5;
```
### JavaScript Logical Operators
* &&	logical and

  ||	logical or

  !	logical not

### JavaScript Type Operators

* `typeof`	Returns the type of a variable
`instanceof`	Returns true if an object is an instance of an object type

# JavaScript Arithmetic
* Arithmetic operators perform arithmetic on numbers (literals or variables).
### Adding
The addition operator `(+)` adds numbers:
* Example
```
let x = 5;
let y = 2;
let z = x + y;
```

### Subtracting

* The subtraction operator `(-)` subtracts numbers.

```
let x = 5;
let y = 2;
let z = x - y;
```

### Multiplying

* The multiplication operator (*) multiplies numbers.

```
let x = 5;
let y = 2;
let z = x * y;
```
### Dividing
* The division operator `(/)` divides numbers.

```
let x = 5;
let y = 2;
let z = x / y;
```

### Remainder

```
let x = 5;
let y = 2;
let z = x % y;
```
### Incrementing
* The increment operator `(++)` increments numbers.


```
let x = 5;
x++;
let z = x;
```
### Decrementing
* The decrement operator `(--)` decrements numbers.

```
let x = 5;
x--;
let z = x;
```
### Exponentiation
* The exponentiation operator `(**)` raises the first operand to the power of the second operand.

```
let x = 5;
let z = x ** 2;          // result is 25
```







## // for loops //
### examples code 
```javascript
const cars =  ["Saab", "Volvo", "BMW","tangu","jacker", "scudeto"];
for ( let i = 0; i <= cars.length; i++){
    console.log(cars [i]);
    

 



// for loop// 
const color = [" balack", "white","yellow", "green"];
for ( let i = 0; i <= color.length; i++){
    console.log (color [i]);  
}
}
```

## foreach loop 

```javascript 
names.forEach(function (name, index) {
    console.log(name, index);
    
});
```
## for in while loop 
### Example

```javascript
    name:'cabdiwali',
    age:20,
    subscribers: 200,
    money: 'somalia'

}
for ( let x in user ){
    console.log(user [x]);

}
console.log( user.subscribers);
```
##  game for math 

### Example

```javascipt
function guessGame() {
    let rendomNr = Math.floor(Math.random() * 11);
    let guess;
    do {
        guess = prompt("Guess a number between 1-10");
        console.log(guess, rendomNr);
        if (rendomNr > guess){
            console.log("you guesses too low ");
        } else if (rendomNr < guess){
            console.log(" Cuess too high");
        }
        } while (guess != rendomNr);
        console.log ("you won");
    
}

guessGame();
````
# chapter two  DOM
### dom is document object model 
## 1 window 
## 2 document 
## 3 console 

 * document can generate heed,body,h1,button.


 #  Selecting elements 
 * getElementById() – select an element by id.

getElementsByName() – select elements by name.

getElementsByTagName()  – select elements by a tag name.

getElementsByClassName() – select elements by one or more class names.

querySelector()  – select elements by CSS selectors.


# Events 
 * An event is an action that occurs in the web browser, which the web browser feedbacks to you so that you can respond to it.

For example, when users click a button on a webpage, you may want to respond to this click event by displaying a dialog box.


``` html
<button id="btn">Click Me!</button>
```


