# CSS
* CSS is the language we use to style an HTML document.

CSS describes how HTML elements should be displayed.

This tutorial will teach you CSS from basic to advanced.
* CSS is the language we use to style a Web page.
* CSS stands for Cascading Style Sheets
## Why Use CSS?
* CSS is used to define styles for your web pages, including the design, layout and variations in display for different devices and screen sizes.

```css
body {
  background-color: lightblue;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
```
## CSS Syntax
* A CSS rule consists of a selector and a declaration block.

* The selector points to the HTML element you want to style.

The declaration block contains one or more declarations separated by semicolons.

Each declaration includes a CSS property name and a value, separated by a colon.

Multiple CSS declarations are separated with semicolons, and declaration blocks are surrounded by curly braces.
## Example
```css
p {
  color: red;
  text-align: center;
}
```
##### Example Explained
* `p` is a selector in CSS (it points to the HTML element you want to style: <p>).
`color` is a property, and `red` is the property value
`text-align` is a property, and `center` is the property value

# CSS Selectors

* A CSS selector selects the HTML element(s) you want to style.

### We can divide CSS selectors into five categories:

* Simple selectors (select elements based on name, id, class)
Combinator selectors (select elements based on a specific relationship between them)
Pseudo-class selectors (select elements based on a certain state)
Pseudo-elements selectors (select and style a part of an element)
Attribute selectors (select elements based on an attribute or attribute value)
### example 
```css
p {
  text-align: center;
  color: red;
}
```
## The CSS id Selector

* The id selector uses the id attribute of an HTML element to select a specific element.

The id of an element is unique within a page, so the id selector is used to select one unique element!

To select an element with a specific id, write a hash (#) character, followed by the id of the element.
## example 
The CSS rule below will be applied to the HTML element with id="para1": 

```css
#para1 {
  text-align: center;
  color: red;
}
```
## The CSS class Selector

* The class selector selects HTML elements with a specific class attribute.

To select elements with a specific class, write a period (.) character, followed by the class name.

## Example 
* In this example all HTML elements with class="center" will be red and center-aligned: 

```css
.center {
  text-align: center;
  color: red;
}
```
```css
<p class="center large">This paragraph refers to two classes.</p>
```
## The CSS Universal Selector
* The universal selector (*) selects all HTML elements on the page.

## Example 
The CSS rule below will affect every HTML element on the page: 

```css
* {
  text-align: center;
  color: blue;
}
```
## The CSS Grouping Selector
* The grouping selector selects all the HTML elements with the same style definitions.

Look at the following CSS code (the h1, h2, and p elements have the same style definitions):
```css
h1, h2, p {
  text-align: center;
  color: red;
}
```
# How To Add CSS
* When a browser reads a style sheet, it will format the HTML document according to the information in the style sheet.

### Three Ways to Insert CSS

* There are three ways of inserting a style sheet:

External CSS

Internal CSS

Inline CSS

## External CSS

```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="mystyle.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
## Internal CSS
```html
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
## Inline CSS
* An inline style may be used to apply a unique style for a single element.

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>
```
## CSS Comments
* CSS comments are not displayed in the browser, but they can help document your source code.

* Comments are used to explain the code, and may help when you edit the source code at a later date.

Comments are ignored by browsers.

```css
/* This is a single-line comment */
p {
  color: red;
}
```

```css
p {
  color: red;  /* Set text color to red */
}
```
## HTML and CSS Comments

* From the HTML tutorial, you learned that you can add comments to your HTML source by using the `<!--...-->` syntax.
```html css
<!DOCTYPE html>
<html>
<head>
<style>
p {
  color: red; /* Set text color to red */
}
</style>
</head>
<body>

<h2>My Heading</h2>

<!-- These paragraphs will be red -->
<p>Hello World!</p>
<p>This paragraph is styled with CSS.</p>
<p>CSS comments are not shown in the output.</p>

</body>
</html>
```




