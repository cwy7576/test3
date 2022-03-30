# html tutorial
## first example

```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>

```

## HTML ttributes 

* HTML attributes provide additional information about HTML elements.

* The `<a>` tag defines a hyperlink. The href attribute specifies the URL of the page the link goes to:

```html
<a href="https://www.w3schools.com">Visit W3Schools</a>
```
## The src Attribute



``` html
<img src="img_girl.jpg">

```

## The width and height Attributes

``` html
<img src="img_girl.jpg" width="500" height="600">

```
## The alt Attribute

``` html
<img src="img_girl.jpg" alt="Girl with a jacket">
```
## The style Attribute
``` html
<p style="color:red;">This is a red paragraph.</p>
```
## The lang Attribute
```html
<html lang="en">
```
## The title Attribute
``` html
<p title="I'm a tooltip">This is a paragraph.</p>
```
## HTML Headings
* HTML headings are titles or subtitles that you want to display on a webpage.



* <h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

## code

```html
<h1 style="font-size:60px;">Heading 1</h1>
```
## HTML Paragraphs
* A paragraph always starts on a new line, and is usually a block of text.


```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```
## HTML Horizontal Rules
``` html
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr>
<h2>This is heading 2</h2>
<p>This is some other text.</p>
<hr>
```
## HTML Line Breaks
``` html
<p>This is<br>a paragraph<br>with line breaks.</p>
```
## The Poem Problem
``` html
<p>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</p>
```
## The HTML pre Element
* The HTML style attribute is used to add styles to an element, such as color, font, size, and more.



``` html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```
## HTML Style 
## background color

The CSS `<background-color>`property defines the background color for an HTML element.



``` html
<body style="background-color:powderblue;">

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>

* Set background color for two different elements:

``` html
<body>

<h1 style="background-color:powderblue;">This is a heading</h1>
<p style="background-color:tomato;">This is a paragraph.</p>

</body>
```
## Text Color

The CSS `<color>` property defines the text color for an HTML element:


``` html
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```
## Fonts

The CSS <font-family>` property defines the font to be used for an HTML element:

``` html 
<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>
```
## Text Size
* The CSS `<font-size>` property defines the text size for an HTML element:
``` html
<h1 style="font-size:300%;">This is a heading</h1>
<p style="font-size:160%;">This is a paragraph.</p>
```
## Text Alignment
* The CSS `<text-align>` property defines the horizontal text alignment for an HTML element:
``` html

<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
```
# HTML Text Formatting
### HTML Formatting Elements
* Formatting elements were designed to display special types of text:

* `<b>`- Bold text
`<strong>` - Important text
`<i>` - Italic text
`<em>` - Emphasized text
`<mark>` - Marked text
`<small>` - Smaller text
`<del>` - Deleted text
`<ins>` - Inserted text
`<sub>` - Subscript text
`<sup>` - Superscript text

* The HTML `<b>` element defines bold text, without any extra importance.
```html
<b>This text is bold</b>
```
* The HTML `<strong>` element defines text with strong importance. The content inside is typically displayed in bold.
``` html 
<strong>This text is important!</strong>
```
* The HTML `<i>` element defines a part of text in an alternate voice or mood. The content inside is typically displayed in italic.
```html
<i>This text is italic</i>
```
* The HTML `<em>` element defines emphasized text. The content inside is typically displayed in italic.
```html
<em>This text is emphasized</em>
```
* The HTML `<small>` element defines smaller text:

```html
<small>This is some smaller text.</small>
```
* The HTML `<mark> `element defines text that should be marked or highlighted:

```html
<p>Do not forget to buy <mark>milk</mark> today.</p>
```
* The HTML `<del>` element defines text that has been deleted from a document. Browsers will usually strike a line through deleted text:
 ```html
 <p>My favorite color is <del>blue</del> red.</p>
```
* The HTML `<ins>` element defines a text that has been inserted into a document. Browsers will usually underline inserted text:
```html
<p>My favorite color is <del>blue</del> <ins>red</ins>.</p>
```

* The HTML `<sub>` element defines subscript text. Subscript text appears half a character below the normal line, and is sometimes rendered in a smaller font. Subscript text can be used for chemical formulas, like H2O:
```html
<p>This is <sub>subscripted</sub> text.</p>
```
```html
<p>This is <sup>superscripted</sup> text.</p>
```

# HTML Quotation and Citation Elements
 * In this chapter we will go through the `<blockquote>`,`<q>`, `<abbr>`, `<address>`, `<cite>`, and `<bdo>` HTML elements.

### HTML `<blockquote>` 
* The HTML <blockquote> element defines a section that is quoted from another source.

Browsers usually indent <blockquote> elements.
```html
<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 50 years, WWF has been protecting the future of nature.
The world's leading conservation organization,
WWF works in 100 countries and is supported by
1.2 million members in the United States and
close to 5 million globally.
</blockquote>
````
 ### HTML `<q>` for Short Quotations

* The HTML <q> tag defines a short quotation.

Browsers normally insert quotation marks around the quotation.
```html

<p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>
```
### HTML `<abbr>` for Abbreviations
* The HTML <abbr> tag defines an abbreviation or an acronym, like "HTML", "CSS", "Mr.", "Dr.", "ASAP", "ATM".
```html

<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
```
### HTML `<address>` for Contact Information
* The HTML `<address>` tag defines the contact information for the author/owner of a document or an article.
 ```html
 <address>
Written by John Doe.<br>
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```
### HTML `<cite>` for Work Title
* The HTML `<cite>` tag defines the title of a creative work (e.g. a book, a poem, a song, a movie, a painting, a sculpture, etc.).

```html
<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>
```
### HTML `<bdo> ` for Bi-Directional Override
```html

<bdo dir="rtl">This text will be written from right to left</bdo>
```
# HTML Comments
* HTML comments are not displayed in the browser, but they can help document your HTML source code.

```html 
<!-- Write your comments here -->
```
### Hide Content
* Comments can be used to hide content.

```html
<p>This is a paragraph.</p>

<!-- <p>This is another paragraph </p> -->

<p>This is a paragraph too.</p>
```
# HTML Colors
* HTML colors are specified with predefined color names, or with RGB, HEX, HSL, RGBA, or HSLA values.


### Background Color
```html
<h1 style="background-color:DodgerBlue;">Hello World</h1>
<p style="background-color:Tomato;">Lorem ipsum...</p>
```
### Text Color

* You can set the color of text:


```html
<h1 style="color:Tomato;">Hello World</h1>
<p style="color:DodgerBlue;">Lorem ipsum...</p>
<p style="color:MediumSeaGreen;">Ut wisi enim...</p>
```

### Border Color

* You can set the color of borders:

```html
<h1 style="border:2px solid Tomato;">Hello World</h1>
<h1 style="border:2px solid DodgerBlue;">Hello World</h1>
<h1 style="border:2px solid Violet;">Hello World</h1>
```
### Color Values
* In HTML, colors can also be specified using RGB values, HEX values, HSL values, RGBA values, and HSLA values.

```html
<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>
```
# HTML HSL and HSLA Colors
* HSL stands for hue, saturation, and lightness.
* Hue is a degree on the color wheel from 0 to 360. 0 is red, 120 is green, and 240 is blue.

Saturation is a percentage value, 0% means a shade of gray, and 100% is the full color.

Lightness is also a percentage value, 0% is black, and 100% is white.

# HTML Styles - CSS
* CSS stands for Cascading Style Sheets.

* CSS saves a lot of work. It can control the layout of multiple web pages all at once.

* Cascading Style Sheets (CSS) is used to format the layout of a webpage.
## Using CSS

* Inline - by using the `<style>` attribute inside HTML elements
Internal - by using a `<style>` element in the `<head> `section
External - by using a `<link>` element to link to an external CSS file

## Inline CSS
* An inline CSS is used to apply a unique style to a single HTML element.

```html
<h1 style="color:blue;">A Blue Heading</h1>

<p style="color:red;">A red paragraph.</p>
```
## Internal CSS
* An internal CSS is used to define a style for a single HTML page.

```html
<head>
<style>
body {background-color: powderblue;}
h1   {color: blue;}
p    {color: red;}
</style>
</head>
<body>

```
## External CSS

* An external style sheet is used to define the style for many HTML pages.

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
```

# styles.css

```css

body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}
```
# CSS Colors, Fonts and Sizes

* The `CSS color` property defines the text color to be used.

The `CSS font-family` property defines the font to be used.

The `CSS font-size` property defines the text size to be used.
```html
<style>
h1 {
  color: blue;
  font-family: verdana;
  font-size: 300%;
}
p {
  color: red;
  font-family: courier;
  font-size: 160%;
}
</style>

```
## CSS Border
* The CSS border property defines a border around an HTML element.

```html
<style>
p {
  border: 2px solid powderblue;
}
</style>

```

## CSS Padding

* The CSS `padding` property defines a padding (space) between the text and the border.

```html
<style>
p {
  border: 2px solid powderblue;
  padding: 30px;
}
</style>
```
## CSS Margin
* The `CSS margin` property defines a margin (space) outside the border.

```css
p {
  border: 2px solid powderblue;
  margin: 50px;
}
```
## Link to External CSS
* External style sheets can be referenced with a full URL or with a path relative to the current web page.

```html
<link rel="stylesheet" href="https://www.w3schools.com/html/styles.css">

```









