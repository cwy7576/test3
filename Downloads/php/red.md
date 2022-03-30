# PHP
* PHP is a server scripting language, and a powerful tool for making dynamic and interactive Web pages.

PHP is a widely-used, free, and efficient alternative to competitors such as Microsoft's ASP.
## Example
```
<!DOCTYPE html>
<html>
<body>

<?php
echo "My first PHP script!";
?>

</body>
</html>
```
# What is PHP?
* PHP is an acronym for "PHP: Hypertext Preprocessor"

  PHP is a widely-used, open source scripting language
  PHP scripts are executed on the server

  PHP is free to download and use
# What is a PHP File?
* PHP files can contain text, HTML, CSS, JavaScript, and PHP code

   PHP code is executed on the server, and the result is returned to the browser as plain HTML

   PHP files have extension ".php"
   # What Can PHP Do?
   * PHP can generate dynamic page content
     PHP can create, open, read, write, delete, and close files on the server

    PHP can collect form data

    PHP can send and receive cookies

    PHP can add, delete, modify data in your database

    PHP can be used to control user-access
    PHP can encrypt data
    # Why PHP?
    * PHP runs on various platforms (Windows, Linux, Unix, Mac OS X, etc.)

      PHP is compatible with almost all servers used today (Apache, IIS, etc.)

      PHP supports a wide range of databases

      PHP is free. Download it from the official PHP resource: www.php.net

      PHP is easy to learn and runs efficiently on the server side
      # What's new in PHP 7
      * PHP 7 is much faster than the previous popular stable release (PHP 5.6)
        PHP 7 has improved Error Handling

        PHP 7 supports stricter Type Declarations for function arguments

        PHP 7 supports new operators (like the spaceship operator: <=>)
        # code 1 
        
      <!-- ```html -->
      <!DOCTYPE html>
 ```html
 <!DOCTYPE html>
<html>
<body>

<?php
$txt = "you";
echo "I love $txt!";
?>

</body>
</html>
```
# PHP Syntax
* A PHP script can be placed anywhere in the document.

   A PHP script starts with `<?php and ends with ?>`:
   * the default file extension for PHP files is `".php"`.
   
 

```html
<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>

<?php
echo "Hello World!";
?>

</body>
</html>
````
# PHP Case Sensitivity
* n PHP, keywords `(e.g. if, else, while, echo, etc.),` classes, functions, and user-defined functions are not case-sensitive.

In the example below, all three echo statements below are equal and legal:


```html
<!DOCTYPE html>
<html>
<body>

<?php
ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>

</body>
</html>
```
* Look at the example below; only the first statement will display the value of the $color variable! This is because $color, $COLOR, and $coLOR are treated as three different variables:

```html
<!DOCTYPE html>
<html>
<body>

<?php
$color = "red";
echo "My car is " . $color . "<br>";
echo "My house is " . $COLOR . "<br>";
echo "My boat is " . $coLOR . "<br>";
?>

</body>
</html>
```
# PHP Comments
* A comment in PHP code is a line that is not executed as a part of the program. Its only purpose is to be read by someone who is looking at the code.


# Example

```html
<!DOCTYPE html>
<html>
<body>

<?php
// This is a single-line comment

# This is also a single-line comment
?>

</body>
</html>
```
# Syntax for multiple-line comments:

```html
<!DOCTYPE html>
<html>
<body>

<?php
/*
This is a multiple-lines comment block
that spans over multiple
lines
*/
?>

</body>
</html>

```
# PHP Variables
* Variables are "containers" for storing information.
## Creating (Declaring) PHP Variables

* In PHP, a variable starts with the $ sign, followed by the name of the variable:
# Example
```html
<!DOCTYPE html>
<html>
<body>

<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;

echo $txt;
echo "<br>";
echo $x;
echo "<br>";
echo $y;
?>

</body>
</html>

```
# Rules for PHP variables
* A variable starts with the `$ `sign, followed by the name of the variable

A variable name must start with a letter or the underscore character

A variable name cannot start with a number

A variable name can only contain alpha-numeric characters and underscores 
(A-z, 0-9, and _ )

Variable names are case-sensitive   (`$age` and `$AGE` are two different variables) 

# Output Variables
* The PHP `echo` statement is often used to output data to the screen.

The following example will show how to output text and a variable:
 # example 
 
 ```html
 <?php
$txt = "W3Schools.com";
echo "I love $txt!";
?>
```
* The following example will output the sum of two variables:

```html
<?php
$x = 5;
$y = 4;
echo $x + $y;
?>
```
# PHP Variables Scope

* In PHP, variables can be declared anywhere in the script.

 The scope of a variable is the part of the script where the variable can be referenced/used.

 PHP has three different variable scopes:

local

global

static

```html
<!DOCTYPE html>
<html>
<body>

<?php
$x = 5; // global scope
 
function myTest() {
  // using x inside this function will generate an error
  echo "<p>Variable x inside function is: $x</p>";
} 
myTest();

echo "<p>Variable x outside function is: $x</p>";
?>

</body>
</html>

```
* A variable declared within a function has a `LOCAL SCOPE` and can only be accessed within that function:


```html
<!DOCTYPE html>
<html>
<body>

<?php
function myTest() {
  $x = 5; // local scope
  echo "<p>Variable x inside function is: $x</p>";
} 
myTest();

// using x outside the function will generate an error
echo "<p>Variable x outside function is: $x</p>";
?>

</body>
</html>
```

```html
!DOCTYPE html>
<html>
<body>

<?php
$x = 5;
$y = 10;

function myTest() {
  global $x, $y;
  $y = $x + $y;
} 

myTest();  // run function
echo $y; // output the new value for variable $y
?>

</body>
</html>
```

## PHP also stores all global variables in an array called `$GLOBALS[index]`. The index holds the name of the variable. This array is also accessible from within functions and can be used to update global variables directly.

The example above can be rewritten like this:

```html
<!DOCTYPE html>
<html>
<body>

<?php
$x = 5;
$y = 10;

function myTest() {
  $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
} 

myTest();
echo $y;
?>

</body>
</html>
```

# PHP echo and print Statements

* With PHP, there are two basic ways to get output: `echo` and `print`.

In this tutorial we use `echo` or `print` in almost every example. So, this chapter contains a little more info about those two output statements.

* `echo` and `print` are more or less the same. They are both used to output data to the screen.

The differences are small: `echo` has no return value while `print` has a return value of 1 so it can be used in expressions. echo can take multiple parameters (although such usage is rare) while print can take one argument. echo is marginally faster than print.

* The echo statement can be used with or without parentheses: `echo `or `echo()`.

```html
<!DOCTYPE html>
<html>
<body>

<?php
echo "<h2>PHP is Fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
?> 

</body>
</html>
```
### Display Variables

The following example shows how to output text and variables with the echo statement:

```html
<!DOCTYPE html>
<html>
<body>

<?php
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";
$x = 5;
$y = 4;

echo "<h2>" . $txt1 . "</h2>";
echo "Study PHP at " . $txt2 . "<br>";
echo $x + $y;
?>

</body>
</html>
```
# The PHP print Statement

* The `print` statement can be used with or without parentheses: print or print().

### Display Text

The following example shows how to output text with the `print` command (notice that the text can contain HTML markup):

```html 
<!DOCTYPE html>
<html>
<body>

<?php
print "<h2>PHP is Fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";
?> 

</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<body>

<?php
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";
$x = 5;
$y = 4;

print "<h2>" . $txt1 . "</h2>";
print "Study PHP at " . $txt2 . "<br>";
print $x + $y;
?>

</body>
</html>
```

# PHP Data Types
* Variables can store data of different types, and different data types can do different things.

* PHP supports the following data types:

* String

Integer

Float (floating point numbers - also called double)

Boolean

Array

Object

NULL

Resource

## PHP String

* A string is a sequence of characters, like "Hello world!".

A string can be any text inside quotes. You can use single or double quotes:

```html
<!DOCTYPE html>
<html>
<body>

<?php 
$x = "Hello world!";
$y = 'Hello world!';

echo $x;
echo "<br>"; 
echo $y;
?>

</body>
</html>\
```

## PHP Integer

* An integer data type is a non-decimal number between -2,147,483,648 and 2,147,483,647.

Rules for integers:

An integer must have at least one digit

An integer must not have a decimal point

An integer can be either positive or negative

Integers can be specified in: decimal (base 10), hexadecimal (base 16), octal (base 8), or binary (base 2) notation

## Example
```html
<!DOCTYPE html>
<html>
<body>

<?php  
$x = 5985;
var_dump($x);
?>  

</body>
</html>
```
## PHP Float

* A float (floating point number) is a number with a decimal point or a number in exponential form.

In the following example $x is a float. The PHP var_dump() function returns the data type and value:

```html
<!DOCTYPE html>
<html>
<body>

<?php  
$x = 10.365;
var_dump($x);
?>  

</body>
</html>
```
## PHP Boolean

* A Boolean represents two possible states: TRUE or FALSE.

## example 

``` 
$x = true;
$y = false;
```
## PHP Array

* An array stores multiple values in one single variable.

In the following example $cars is an array. The PHP var_dump() function returns the data type and value:

## Example
```html
<!DOCTYPE html>
<html>
<body>

<?php  
$cars = array("Volvo","BMW","Toyota");
var_dump($cars);
?>  

</body>
</html>

```
