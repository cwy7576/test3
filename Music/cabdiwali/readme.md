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

#  HTML Links
* Links are found in nearly all web pages. Links allow users to click their way from page to page.
* The HTML `<a> `tag defines a hyperlink. It has the following syntax:


```html
<a href="url">link text</a>
```
## HTML Links - The target Attribute
 *
 The target attribute specifies where to open the linked document.

The target attribute can have one of the following values:

`_self` - Default. Opens the document in the same window/tab as it was clicked
_`blank` - Opens the document in a new window or tab
`_parent `- Opens the document in the parent frame
`_top - Opens` the document in the full body of the window

* Use target="_`blank`" to open the linked document in a new browser window or tab:
```html
<a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a>
```
## Absolute URLs vs. Relative URLs

* Both examples above are using an absolute URL (a full web address) in the href attribute.

```html
<h2>Absolute URLs</h2>
<p><a href="https://www.w3.org/">W3C</a></p>
<p><a href="https://www.google.com/">Google</a></p>

<h2>Relative URLs</h2>
<p><a href="html_images.asp">HTML Images</a></p>
<p><a href="/css/default.asp">CSS Tutorial</a></p>

```
## HTML Links - Use an Image as a Link

* To use an image as a link, just put the `<img> `tag inside the `<a>` tag:

```html
<a href="default.asp">
<img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
</a>
 ```


 ## Link to an Email Address

 * Use mailto: inside the href attribute to create a link that opens the user's email program (to let them send a new email):

```html
<a href="mailto:someone@example.com">Send email</a>
```
 ## Button as a Link

 * To use an HTML button as a link, you have to add some JavaScript code.

JavaScript allows you to specify what happens at certain events, such as a click of a button:

 
```html
<button onclick="document.location='default.asp'">HTML Tutorial</button>
```
## Link Titles

```html
<a href="https://www.w3schools.com/html/" title="Go to W3Schools HTML section">Visit our HTML Tutorial</a>
```
## More on Absolute URLs and Relative URLs

* Use a full URL to link to a web page: 

```html
<a href="https://www.w3schools.com/html/default.asp">HTML tutorial</a>

```
# HTML Link Colors

* By default, a link will appear like this (in all browsers):

```html
<style>
a:link {
  color: green;
  background-color: transparent;
  text-decoration: none;
}

a:visited {
  color: pink;
  background-color: transparent;
  text-decoration: none;
}

a:hover {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

a:active {
  color: yellow;
  background-color: transparent;
  text-decoration: underline;
}
</style>
```
## Link Buttons

* A link can also be styled as a button, by using CSS:

```html
<style>
a:link, a:visited {
  background-color: #f44336;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: red;
}
</style>
```
# Create a Bookmark in HTML
*  HTML links can be used to create bookmarks, so that readers can jump to specific parts of a web page.

```html

<h2 id="C4">Chapter 4</h2>
```
* Then, add a link to the bookmark ("Jump to Chapter 4"), from within the same page:

```html
<a href="#C4">Jump to Chapter 4</a>
```
* You can also add a link to a bookmark on another page:

```html
<a href="html_demo.html#C4">Jump to Chapter 4</a>
```
# HTML Images
* Images can improve the design and the appearance of a web page.

```html
<img src="pic_trulli.jpg" alt="Italian Trulli">
```
## HTML Images Syntax

```html
<img src="url" alt="alternatetext">
```
## The src Attribute

* The required src attribute specifies the path (URL) to the image.

```html
<img src="img_chania.jpg" alt="Flowers in Chania">
```
## The alt Attribute
```html
<img src="img_chania.jpg" alt="Flowers in Chania">
```
## Image Size - Width and Height

* You can use the `style `attribute to specify the width and height of an image.

```html
<img src="img_girl.jpg" alt="Girl in a jacket" style="width:500px;height:600px;">
```
## Width and Height, or Style?

```html
<!DOCTYPE html>
<html>
<head>
<style>
img {
  width: 100%;
}
</style>
</head>
<body>

<img src="html5.gif" alt="HTML5 Icon" width="128" height="128">

<img src="html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">

</body>
</html>
```
## Images in Another Folder
* If you have your images in a sub-folder, you must include the folder name in the src attribute:

```html
<img src="/images/html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
```
## Images on Another Server/Website

* To point to an image on another server, you must specify an absolute (full) URL in the src attribute:

```html
<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com">
```
## Animated Images
* HTML allows animated GIFs:

```html
<img src="programming.gif" alt="Computer Man" style="width:48px;height:48px;">
```
## Image as a Link

* To use an image as a link, put the `<img>` tag inside the `<a>` tag:

```html
<a href="default.asp">
  <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
</a>
```
## Image Floating

* Use the CSS float property to let the image float to the right or to the left of a text:
```html
<p><img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
The image will float to the right of the text.</p>

<p><img src="smiley.gif" alt="Smiley face" style="float:left;width:42px;height:42px;">
The image will float to the left of the text.</p>
```
# HTML Background Images

* To add a background image on an HTML element, use the HTML `style` attribute and the CSS `background-image` property:

```html
<div style="background-image: url('img_girl.jpg');">
```
* Specify the background image in the `<style>` element:
``` html
<style>
div {
  background-image: url('img_girl.jpg');
}
</style>
```
## Background Image on a Page
* If you want the entire page to have a background image, you must specify the background image on the `<body>` element:
```html
<style>
body {
  background-image: url('img_girl.jpg');
}
</style>
```
## Background Repeat
* If the background image is smaller than the element, the image will repeat itself, horizontally and vertically, until it reaches the end of the element:

```html

<style>
body {
  background-image: url('example_img_girl.jpg');
}
</style>
```
* To avoid the background image from repeating itself, set the background-repeat property to `<no-repeat.>`

```html
<style>
body {
  background-image: url('example_img_girl.jpg');
  background-repeat: no-repeat;
}
</style>
```
## Background Cover

* If you want the background image to cover the entire element, you can set the `background-size` property to `cover.`

Also, to make sure the entire element is always covered, set the `background-attachment` property to `fixed:`
`
This way, the background image will cover the entire element, with no stretching (the image will keep its original proportions):

```html

<style>
body {
  background-image: url('img_girl.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
```
## Background Stretch
* If you want the background image to stretch to fit the entire element, you can set the background-size property to 100% 100%:

```html
<style>
body {
  background-image: url('img_girl.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
</style>
```
## The HTML <picture> Element
*  The HTML <picture> element gives web developers more flexibility in specifying image resources.

The <picture> element contains one or more <source> elements, each referring to different images through the srcset attribute. This way the browser can choose the image that best fits the current view and/or device.

Each <source> element has a media attribute that defines when the image is the most suitable.

```html
<picture>
  <source media="(min-width: 650px)" srcset="img_food.jpg">
  <source media="(min-width: 465px)" srcset="img_car.jpg">
  <img src="img_girl.jpg">
</picture>
```

* The browser will use the first image format it recognizes:

```html
<picture>
  <source srcset="img_avatar.png">
  <source srcset="img_girl.jpg">
  <img src="img_beatles.gif" alt="Beatles" style="width:auto;">
</picture>
```
# HTML Favicon
* A favicon is a small image displayed next to the page title in the browser tab.

* Next, add a `<link>` element to your "index.html" file, after the `<title>` element, like this:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Page Title</title>
  <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
# HTML Tables
* A table in HTML consists of table cells inside rows and columns

```html
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>
```
## Table Cells
* Each table cell is defined by a `<td>` and a `</td>` tag.

```html
<table>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
</table>
```
## Table Rows
```html
<table>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
  <tr>
    <td>16</td>
    <td>14</td>
    <td>10</td>
  </tr>
</table>
```
## Table Headers
* Sometimes you want your cells to be headers, in those cases use the <th> tag instead of the <td> tag:

```html

<table>
  <tr>
    <th>Person 1</th>
    <th>Person 2</th>
    <th>Person 3</th>
  </tr>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
  <tr>
    <td>16</td>
    <td>14</td>
    <td>10</td>
  </tr>
</table>
```
# HTML Table Borders
* HTML tables can have borders of different styles and shapes.

* To add a border, use the CSS `border` property on `table, th`, and` td` elements:

```css
table, th, td {
  border: 1px solid black;
}
```
## Collapsed Table Borders
 *  To avoid having double borders like in the example above, set the CSS `border-collapse` property to `collapse.`
```css
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
```
## Style Table Borders

* If you set a background color of each cell, and give the border a white color (the same as the document background), you get the impression of an invisible border:

```css
table, th, td {
  border: 1px solid white;
  border-collapse: collapse;
}
th, td {
  background-color: #96D4D4;
}
```

## Round Table Borders
* With the `border-radius` property, the borders get rounded corners:

```css
table, th, td {
  border: 1px solid black;
  border-radius: 10px;
}
```
## Dotted Table Borders
* With the `border-style` property, you can set the appereance of the border.

* `dotted`     
`dashed`     
`solid`     
`double`     
`groove `    
`ridge `    
`inset`     
`outset `    
`none `    
`hidden`


```css
 th, td {
  border-style: dotted;
}
```
## Border Color
* With the `border-color` property, you can set the color of the border.

```css
th, td {
  border-color: #96D4D4;
}
```
# Table Sizes

```html
<table style="width:100%">
```
# HTML Table Headers
```css
<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  ```
  ## Vertical Table Headers
* To use the first column as table headers, define the first cell in each row as a th element:

```css
<table>
  <tr>
    <th>Firstname</th>
    <td>Jill</td>
    <td>Eve</td>
  </tr>
  ```
* o left-align the table headers, use the CSS text-align property:
```css
th {
  text-align: left;
}
```
## Table Caption
* To add a caption to a table, use the <caption> tag:

```css
<table style="width:100%">
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  ```
  # HTML Table - Cell Padding
* Cell padding is the space between the cell edges and the cell content.

```css
th, td {
  padding: 15px;
}
```
* To add padding only above the content, use the `padding-top `property.

And the others sides with the `padding-bottom`,` padding-left,` and `padding-right `properties:

```css
th, td {
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 40px;
}
```
## HTML Table - Cell Spacing
* Cell spacing is the space between each cell.

By default the space is set to 2 pixels.

```css
table {
  border-spacing: 30px;
}
```

# HTML Table Colspan & Rowspan
* HTML tables can have cells that spans over multiple rows and/or columns.

```html
<table>
  <tr>
    <th colspan="2">Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>43</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>57</td>
  </tr>
</table>
```
 ## HTML Table - Rowspan

* To make a cell span over multiple rows, use the rowspan attribute:

```css
<table>
  <tr>
    <th>Name</th>
    <td>Jill</td>
  </tr>
  <tr>
    <th rowspan="2">Phone</th>
    <td>555-1234</td>
  </tr>
  <tr>
    <td>555-8745</td>
</tr>
</table>
```
# HTML Table Styling
* Use CSS to make your tables look better.
* To style every other table row element, use the `:nth-child(even)` selector like this:
```css
tr:nth-child(even) {
  background-color: #D6EEEE;
}
```

## HTML Table - Vertical Zebra Stripes
* To make vertical zebra stripes, style every other column, instead of every other row.

* Set the `:nth-child(even)` for table data elements like this:

```css
td:nth-child(even), th:nth-child(even) {
  background-color: #D6EEEE;
}
```
## Combine Vertical and Horizontal Zebra Stripes

* You can combine the styling from the two examples above and you will have stripes on every other row and every other column.


* Use an `rgba()` color to specify the transparency of the color:
```css
tr:nth-child(even) {
  background-color: rgba(150, 212, 212, 0.4);
}

th:nth-child(even),td:nth-child(even) {
  background-color: rgba(150, 212, 212, 0.4);
}
```
## Horizontal Dividers
* Add the `border-bottom` property to all `tr` elements to get horizontal dividers:

```css
tr {
  border-bottom: 1px solid #ddd;
}
```
## Hoverable Table
* Use the `:hover`selector on `tr` to highlight table rows on mouse over:
```html
tr:hover {background-color: #D6EEEE;}
```
# HTML Table Colgroup
* The `<colgroup>` element should be used as a container for the column specifications.

Each group are specified with a`<col>` element.

The `span` attribute specifies how many columns that gets the style.

The `style` attribute specifies the style to give the columns.

```css 
<table>
  <colgroup>
    <col span="2" style="background-color: #D6EEEE">
  </colgroup>
  <tr>
    <th>MON</th>
    <th>TUE</th>
    <th>WED</th>
    <th>THU</th>
 </table>
```
## Multiple Col Elements
```css
<table>
  <colgroup>
    <col span="2" style="background-color: #D6EEEE">
    <col span="3" style="background-color: pink">
  </colgroup>
  <tr>
    <th>MON</th>
    <th>TUE</th>
    <th>WED</th>
    <th>THU</th>
</table>
```
## Hide Columns
* You can hide columns with the `visibility: collapse` property:


  
     



```css
<table>
  <colgroup>
    <col span="2">
    <col span="3" style="visibility: collapse">
  </colgroup>
  <tr>
    <th>MON</th>
    <th>TUE</th>
    <th>WED</th>
    <th>THU</th>
</table>
```

# HTML Lists
* HTML lists allow web developers to group a set of related items in lists.

* An unordered HTML list:

Item
Item
Item
Item
* An ordered HTML list:

First item
Second item
Third item
Fourth item
## Unordered HTML List

```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

```
## Ordered HTML List
```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```
## HTML Description Lists
```html
<dl>
  <dt>Coffee</dt>
  <dd>- black hot drink</dd>
  <dt>Milk</dt>
  <dd>- white cold drink</dd>
</dl>
```
## Ordered HTML List with style
 * Example - Disc
```html
<ul style="list-style-type:disc;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

* Example - Circle
```html
<ul style="list-style-type:circle;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
* example squere
```html
<ul style="list-style-type:square;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
* eaxmple Nane
```html
 <ul style="list-style-type:none;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

 * Nested HTML Lists
```html
<ul>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea</li>
    </ul>
  </li>
  <li>Milk</li>
</ul>
```
## Horizontal List with CSS
```html
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 16px;
  text-decoration: none;
}

li a:hover {
  background-color: #111111;
}
</style>
</head>
```
## start list 
```html
<ol start="50">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```
# html block level element 
* A block-level element always starts on a new line.
* example =
```html
<div>Hello World</div>
```
## Inline Elements
* An inline element does not start on a new line.

```html
<span>Hello World</span>
```
## The `<div> `Element
* The `<div>` element is often used as a container for other HTML elements.

```html
<div style="background-color:black;color:white;padding:20px;">
  <h2>London</h2>
  <p>London is the capital city of England. It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>
</div>
```
## The `<span> `Element
* The`<span> `element is an inline container used to mark up a part of a text, or a part of a document.
```html
<p>My mother has <span style="color:blue;font-weight:bold">blue</span> eyes and my father has <span style="color:darkolivegreen;font-weight:bold">dark green</span> eyes.</p>
```
# HTML class Attribute
* The HTML class attribute is used to specify a class for an HTML element.

### Using The class Attribute
* he class attribute is often used to point to a class name in a style sheet. 
```html
<!DOCTYPE html>
<html>
<head>
<style>
.city {
  background-color: tomato;
  color: white;
  border: 2px solid black;
  margin: 20px;
  padding: 20px;
}
</style>
</head>
<body>

<div class="city">
  <h2>London</h2>
  <p>London is the capital of England.</p>
</div>

<div class="city">
  <h2>Paris</h2>
  <p>Paris is the capital of France.</p>
</div>

<div class="city">
  <h2>Tokyo</h2>
  <p>Tokyo is the capital of Japan.</p>
</div>

</body>
</html>
```
* In the following example we have two `<span>` elements with a `class` attribute with the value of "note". Both `<span>` elements will be styled equally according to the `.note `style definition in the head section:

```html
<!DOCTYPE html>
<html>
<head>
<style>
.note {
  font-size: 120%;
  color: red;
}
</style>
</head>
<body>

<h1>My <span class="note">Important</span> Heading</h1>
<p>This is some <span class="note">important</span> text.</p>

</body>
</html>
```
## The Syntax For Class
### To create a class; write a period `(.) `character, followed by a class name. Then, define the CSS properties within curly braces `{}`:

```css
.city {
  background-color: tomato;
  color: white;
  padding: 10px;
}
```
## Multiple Classes
* HTML elements can belong to more than one class.

```html 
<h2 class="city main">London</h2>
<h2 class="city">Paris</h2>
<h2 class="city">Tokyo</h2>
```
## Different Elements Can Share Same Class

```html
<h2 class="city">Paris</h2>
<p class="city">Paris is the capital of France</p>
```
## Use of The class Attribute in JavaScript

* The class name can also be used by JavaScript to perform certain tasks for specific elements.

JavaScript can access elements with a specific class name with the `getElementsByClassName() `method:

```html
<script>
function myFunction() {
  var x = document.getElementsByClassName("city");
  for (var i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
}
</script>
```
# HTML id Attribute
* The HTML `id `attribute is used to specify a unique id for an HTML element.

```html
<!DOCTYPE html>
<html>
<head>
<style>
#myHeader {
  background-color: lightblue;
  color: black;
  padding: 40px;
  text-align: center;
}
</style>
</head>
<body>

<h1 id="myHeader">My Header</h1>

</body>
</html>
```
## Difference Between Class and ID

*  A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page:
```html
<style>
/* Style the element with the id "myHeader" */
#myHeader {
  background-color: lightblue;
  color: black;
  padding: 40px;
  text-align: center;
}

/* Style all elements with the class name "city" */
.city {
  background-color: tomato;
  color: white;
  padding: 10px;
}
</style>

<!-- An element with a unique id -->
<h1 id="myHeader">My Cities</h1>

<!-- Multiple elements with same class -->
<h2 class="city">London</h2>
<p>London is the capital of England.</p>

<h2 class="city">Paris</h2>
<p>Paris is the capital of France.</p>

<h2 class="city">Tokyo</h2>
<p>Tokyo is the capital of Japan.</p>
```
## HTML Bookmarks with ID and Links

* HTML bookmarks are used to allow readers to jump to specific parts of a webpage.

* Bookmarks can be useful if your page is very long.

```html
 <h2 id="C4">Chapter 4</h2>
```
### Or, add a link to the bookmark `("Jump to Chapter 4"),` from another page:
```html
<a href="html_demo.html#C4">Jump to Chapter 4</a>
```
## Using The id Attribute in JavaScript

* Use the id attribute to manipulate text with JavaScript:

```html
<script>
function displayResult() {
  document.getElementById("myHeader").innerHTML = "Have a nice day!";
}
</script>
```
# HTML Iframes
#### An HTML iframe is used to display a web page within a web page.


```html
<iframe src="url" title="description"></iframe>
```
## Iframe - Set Height and Width
```html
<iframe src="demo_iframe.htm" height="200" width="300" title="Iframe Example"></iframe>
```
#### Or you can add the `style` attribute and use the CSS `height` and `width` properties:

```html
<iframe src="demo_iframe.htm" style="height:200px;width:300px;" title="Iframe Example"></iframe>
```

## Iframe - Target for a Link
* An iframe can be used as the target frame for a link.

The `target `attribute of the link must refer to the `name` attribute of the iframe:
```html
<iframe src="demo_iframe.htm" name="iframe_a" title="Iframe Example"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>
```
# HTML JavaScript
## JavaScript makes HTML pages more dynamic and interactive.

```html
<h1>My First JavaScript</h1>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<p id="demo"></p>
```
## The HTML `<script>` tag is used to define a client-side script (JavaScript).
```html
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
```
## A Taste of JavaScript

### document.getElementById("demo").innerHTML = "Hello JavaScript!";

## JavaScript can change styles:

```css
document.getElementById("demo").style.fontSize = "25px";
document.getElementById("demo").style.color = "red";
document.getElementById("demo").style.backgroundColor = "yellow";
```
## JavaScript can change attributes:


```css
document.getElementById("image").src = "picture.gif";
```
## The HTML <noscript> Tag
```html
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
<noscript>Sorry, your browser does not support JavaScript!</noscript>
```
# HTML File Paths
## A file path describes the location of a file in a web site's folder structure.

* File paths are used when linking to external files, like:

Web pages
Images
Style sheets
JavaScripts
## Absolute File Paths

```html
<img src="https://www.w3schools.com/images/picture.jpg" alt="Mountain">

```
## Relative File Paths
* A relative file path points to a file relative to the current page.

```html
<img src="/images/picture.jpg" alt="Mountain">

```
# HTML - The Head Element
* The HTML `<head> `element is a container for the following elements: `<title>,` `<style>`, `<meta>`, `<link>,` `<script>`, and `<base>.`
## The HTML `<title>` Element
```html
<head>
  <title>A Meaningful Page Title</title>
</head>
```
# The HTML `<`style>` Element
* The `<style> `element is used to define style information for a single HTML page:

```html
<style>
  body {background-color: powderblue;}
  h1 {color: red;}
  p {color: blue;}
</style>
```
## The HTML <link> Element

* The `<link> `element defines the relationship between the current document and an external resource.
```html
<link rel="stylesheet" href="mystyle.css">
```
## The HTML <meta> Element
* The `<meta>` element is typically used to specify the character set, page description, keywords, author of the document, and viewport settings.
### Define the character set used:


```html
<meta charset="UTF-8">
```
### Define keywords for search engines:


```html
<meta name="keywords" content="HTML, CSS, JavaScript">
```
### Define a description of your web page:


```html
<meta name="description" content="Free Web tutorials">
```
###  Define the author of a page:


```html
<meta name="author" content="John Doe">
```
### Refresh document every 30 seconds:


```html
<meta http-equiv="refresh" content="30">
```
### Setting the viewport to make your website look good on all devices:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
### Example
```html
<meta charset="UTF-8">
<meta name="description" content="Free Web tutorials">
<meta name="keywords" content="HTML, CSS, JavaScript">
<meta name="author" content="John Doe">
````
###  Setting The Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
## The HTML `<script> `Element
*  The `<script>` element is used to define client-side JavaScripts.

```html
<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello JavaScript!";
}
</script>
````
## The HTML <`base> `Element
* The `<base>` element specifies the base URL and/or target for all relative URLs in a page.
`
The ``<base>` tag must have either an href or a target attribute present, or both.
```html

<head>
<base href="https://www.w3schools.com/" target="_blank">
</head>

<body>
<img src="images/stickman.gif" width="24" height="39" alt="Stickman">
<a href="tags/tag_base.asp">HTML base Tag</a>
</body>
```
# HTML Layout Elements and Techniques
## HTML Layout Elements
#### `<header> `- Defines a header for a document or a section
`<nav> >` Defines a set of navigation links

`<section>` - Defines a section in a document\
`<article> ` Defines an independent, `self-contained content

`<aside>` Defines content aside from the `content (like a sidebar)

`<footer> -` Defines a footer for a document or a section

`<details> ` Defines additional details that the user can open and close on demand

`<summary>` Defines a heading for the `<details>` element`
* There are four different techniques to create multicolumn layouts. Each technique has its pros and cons

* CSS framework

  CSS float property

  CSS flexbox

  CSS grid
## CSS Layout Float
```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Template</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
}

/* Create two columns/boxes that floats next to each other */
nav {
  float: left;
  width: 30%;
  height: 300px; /* only for demonstration, should be removed */
  background: #ccc;
  padding: 20px;
}

/* Style the list inside the menu */
nav ul {
  list-style-type: none;
  padding: 0;
}

article {
  float: left;
  padding: 20px;
  width: 70%;
  background-color: #f1f1f1;
  height: 300px; /* only for demonstration, should be removed */
}

/* Clear floats after the columns */
section::after {
  content: "";
  display: table;
  clear: both;
}

/* Style the footer */
footer {
  background-color: #777;
  padding: 10px;
  text-align: center;
  color: white;
}

/* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
@media (max-width: 600px) {
  nav, article {
    width: 100%;
    height: auto;
  }
}
</style>
</head>
<body>

<h2>CSS Layout Float</h2>
<p>In this example, we have created a header, two columns/boxes and a footer. On smaller screens, the columns will stack on top of each other.</p>
<p>Resize the browser window to see the responsive effect (you will learn more about this in our next chapter - HTML Responsive.)</p>

<header>
  <h2>Cities</h2>
</header>

<section>
  <nav>
    <ul>
      <li><a href="#">London</a></li>
      <li><a href="#">Paris</a></li>
      <li><a href="#">Tokyo</a></li>
    </ul>
  </nav>
  
  <article>
    <h1>London</h1>
    <p>London is the capital city of England. It is the most populous city in the  United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>
    <p>Standing on the River Thames, London has been a major settlement for two millennia, its history going back to its founding by the Romans, who named it Londinium.</p>
  </article>
</section>

<footer>
  <p>Footer</p>
</footer>

</body>
</html>

```
## CSS Flexbox Layout
* Use of flexbox ensures that elements behave predictably when the page layout must accommodate different screen sizes and different display devices.

```html
<style>
* {
  box-sizing: border-box;
}
```
# HTML Responsive Web Design
Responsive web design is about creating web pages that look good on all devices!

* A responsive web design will automatically adjust for different screen sizes and viewports.

#### Responsive Web Design is about using HTML and CSS to automatically resize,
## Responsive Images
* Responsive images are images that scale nicely to fit any browser size.

### Using the width Property
* If the CSS `width `property is set to 100%, the image will be responsive and scale up and down:
```html
<img src="img_girl.jpg" style="width:100%;">
```
### Using the max-width Property

#### If the `<max-width>` property is set to 100%, the image will scale down if it has to, but never scale up to be larger than its original size
```html
<img src="img_girl.jpg" style="max-width:100%;height:auto;">
```
### Show Different Images Depending on Browser Width
* The HTML `<picture>` element allows you to define different images for different browser window sizes.
```html
<picture>
  <source srcset="img_smallflower.jpg" media="(max-width: 600px)">
  <source srcset="img_flowers.jpg" media="(max-width: 1500px)">
  <source srcset="flowers.jpg">
  <img src="img_smallflower.jpg" alt="Flowers">
</picture>
```
## Responsive Text Size
* The text size can be set with a "vw"
```html
<h1 style="font-size:10vw">Hello World</h1>
```
## Media Queries
 ### In addition to resize text and images, it is also common to use media queries in responsive web pages.

```html
<style>
.left, .right {
  float: left;
  width: 20%; /* The width is 20%, by default */
}

.main {
  float: left;
  width: 60%; /* The width is 60%, by default */
}

/* Use a media query to add a breakpoint at 800px: */
@media screen and (max-width: 800px) {
  .left, .main, .right {
    width: 100%; /* The width is 100%, when the viewport is 800px or smaller */
  }
}
</style>
```
## Bootstrap

#### Another popular CSS framework is Bootstrap. Bootstrap uses HTML, CSS and jQuery to make responsive web pages.


```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Bootstrap Example</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <div class="jumbotron">
    <h1>My First Bootstrap Page</h1>
  </div>
  <div class="row">
    <div class="col-sm-4">
      ...
    </div>
    <div class="col-sm-4">
      ...
    </div>
    <div class="col-sm-4">
    ...
    </div>
  </div>
</div>

</body>
</html>
```
# HTML Computer Code Elements

### HTML contains several elements for defining user input and computer code.

* Example

```html
<code>
x = 5;
y = 6;
z = x + y;
</code>
```
## HTML `<kbd>` For Keyboard Input
* The HTML `<kbd>` element is used to define keyboard input. The content inside is displayed in the browser's default monospace font.
```html
<p>Save the document by pressing <kbd>Ctrl + S</kbd></p>
```

## HTML <samp> For Program Output
* The HTML `<samp>` element is used to define sample output from a computer program. The content inside is displayed in the browser's default monospace font.
```html
<p>Message from my computer:</p>
<p><samp>File not found.<br>Press F1 to continue</samp></p>
```
## HTML `<code>` For Computer Code

* The HTML `<code>` element  is used to define a piece of computer code. The content inside is displayed in the browser's default monospace font.

```html
<code>
x = 5;
y = 6;
z = x + y;
</code>
```
#### to  fix this, you can put the `<code>` element inside a `<pre>` element:
```html
<pre>
<code>
x = 5;
y = 6;
z = x + y;
</code>
</pre>
```
## HTML `<var> `For Variables
#### The HTML `<var>` element  is used to define` a variable in programming or in a mathematical expression. The content inside is typically displayed in italic.

```html
<p>The area of a triangle is: 1/2 x <var>b</var> x <var>h</var>, where <var>b</var> is the base, and <var>h</var> is the vertical height.</p>
```
# HTML Semantic Elements

* Semantic elements = elements with a meaning.

##### Examples of non-semantic elements: `<div>` and `<span>` - Tells nothing about its content.
##### Examples of semantic elements: `<form>,` `<table>,` and <`article>` - Clearly defines its content.

* In HTML there are some semantic elements that can be used to define different parts of a web page:  

## HTML `<section>` Element

* The <section> element defines a section in a document.

```html
<section>
<h1>WWF's Panda symbol</h1>
<p>The Panda has become the symbol of WWF. The well-known panda logo of WWF originated from a panda named Chi Chi that was transferred from the Beijing Zoo to the London Zoo in the same year of the establishment of WWF.</p>
</section>
```
## HTML `<article>` Element
* The `<article>`element specifies independent, self-contained content.
```html
<article>
<h2>Mozilla Firefox</h2>
<p>Mozilla Firefox is an open-source web browser developed by Mozilla. Firefox has been the second most popular web browser since January, 2018.</p>
</article>

<article>
<h2>Microsoft Edge</h2>
<p>Microsoft Edge is a web browser developed by Microsoft, released in 2015. Microsoft Edge replaced Internet Explorer.</p>
</article>
```
*Use CSS to style the `<article> `element:`

```html
<!DOCTYPE html>
<html>
<head>
<style>
.all-browsers {
  margin: 0;
  padding: 5px;
  background-color: lightgray;
}

.all-browsers > h1, .browser {
  margin: 10px;
  padding: 5px;
}

.browser {
  background: white;
}

.browser > h2, p {
  margin: 4px;
  font-size: 90%;
}
</style>
</head>
<body>

<article class="all-browsers">
  <h1>Most Popular Browsers</h1>
  <article class="browser">
    <h2>Google Chrome</h2>
    <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
  </article>
  <article class="browser">
    <h2>Mozilla Firefox</h2>
    <p>Mozilla Firefox is an open-source web browser developed by Mozilla. Firefox has been the second most popular web browser since January, 2018.</p>
  </article>
  <article class="browser">
    <h2>Microsoft Edge</h2>
    <p>Microsoft Edge is a web browser developed by Microsoft, released in 2015. Microsoft Edge replaced Internet Explorer.</p>
  </article>
</article>

</body>
</html>

````
#### A header for an `<article>: `
```html

<article>
  <header>
    <h1>What Does WWF Do?</h1>
    <p>WWF's mission:</p>
  </header>
  <p>WWF's mission is to stop the degradation of our planet's natural environment,
  and build a future in which humans live in harmony with nature.</p>
</article>
```
## HTML `<footer>` Element
```html
<footer>
  <p>Author: Hege Refsnes</p>
  <p><a href="mailto:hege@example.com">hege@example.com</a></p>
</footer>
```
## HTML `<nav>` Element
* The `<nav>` element defines a set of navigation links.

```html
<nav>
  <a href="/html/">HTML</a> |
  <a href="/css/">CSS</a> |
  <a href="/js/">JavaScript</a> |
  <a href="/jquery/">jQuery</a>
</nav>
```
## HTML `<aside>` Element
* The `<aside> `element defines some content aside from the content it is placed in (like a sidebar).
```html

aside>
<h4>Epcot Center</h4>
<p>Epcot is a theme park at Walt Disney World Resort featuring exciting attractions, international pavilions, award-winning fireworks and seasonal special events.</p>
</aside>
```
## HTML `<figure>` and `<figcaption> `Elements
* The `<figure>` tag specifies self-contained content, like illustrations, diagrams, photos, code listings, etc.

*  The `<figcaption> `tag defines a caption for a `<figure>` element. The `<figcaption> `element can be placed as the first or as the last child of a `<figure>` element.
```html
<figure>
  <img src="pic_trulli.jpg" alt="Trulli">
  <figcaption>Fig1. - Trulli, Puglia, Italy.</figcaption>
</figure>
```
# HTML Style Guide
##### A consistent, clean, and tidy HTML code makes it easier for others to read and understand your code.

* this is correct document type for html  is 
```html 
<!DOCTYPE html>
```
## Omitting <html> and <body>?

``` html
<!DOCTYPE html>
<head>
  <title>Page Title</title>
</head>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>
```
## Omitting <head>?
```html
<!DOCTYPE html>
<html>
<title>Page Title</title>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
## Add the lang Attribute

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <title>Page Title</title>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
## Meta Data
*  To ensure proper interpretation and correct search engine indexing, both the language and the character encoding `<meta charset="charset">`should be defined as early as possible in an HTML document:

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>
```
## Loading JavaScript in HTML
* Use simple syntax for loading external scripts (the `type `attribute is not necessary):

```html
<script src="myscript.js">
```
## Accessing HTML Elements with JavaScript
* Example
```css
getElementById("Demo").innerHTML = "Hello";

getElementById("demo").innerHTML = "Hello";
```
# HTML Entities

* Reserved characters in HTML must be replaced with character entities.

* Some characters are reserved in HTML.

If you use the less than (<) or greater than (>) signs in your text, the browser might mix them with tags.

Character entities are used to display reserved characters in HTML.

A character entity looks like this:]
```html
&entity_name;
OR

&#entity_number;
```
### Non-breaking Space
* A commonly used entity in HTML is the non-breaking space: `&nbsp;`
# HTML Symbols

* Symbols that are not present on your keyboard can also be added by using entities.

### HTML Symbol Entities

* HTML entities were described in the previous chapter.

Many mathematical, technical, and currency symbols, are not present on a normal keyboard.

To add such symbols to an HTML page, you can use the entity name or the entity number (a decimal or a hexadecimal reference) for the symbol.
```html
<!DOCTYPE html>
<html>
<body>

<p>I will display &euro;</p>
<p>I will display &#8364;</p>
<p>I will display &#x20AC;</p>

</body>
</html>
```
# Using Emojis in HTML
 * Emojis are characters from the UTF-8 character set: 😄 😍 💗
 ## What are Emojis?
 ### Emojis look like images, or icons, but they are not.

They are letters (characters) from the UTF-8 (Unicode) character set.
## The HTML charset Attribute
* To display an HTML page correctly, a web browser must know the character set used in the page.

This is specified in the `<meta>` tag:
```html
<meta charset="UTF-8">
```
## UTF-8 Characters
* Many UTF-8 characters cannot be typed on a keyboard, but they can always be displayed using numbers (called entity numbers)
* A is 65

   B is 66

   C is 67
 
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<p>I will display A B C</p>
<p>I will display &#65; &#66; &#67;</p>

</body>
</html>
```
## Example Explained
*  The <meta charset=`"UTF-8">` element defines the character set.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<h1>My First Emoji</h1>

<p>&#128512;</p>

</body>
</html>
```
#### font size Emojis 
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<h1>Sized Emojis</h1>

<p style="font-size:48px">
&#128512; &#128516; &#128525; &#128151;
</p>

</body>
</html>
````

## Some Emoji Symbols in UTF-8

#### Emoji	Value	Try it
🗻	&#128507;	

🗼	&#128508;	

🗽	&#128509;	

🗾	&#128510;	

🗿	&#128511;	

😀	&#128512;	
😁	&#128513;	
😂	&#128514;	
😃	&#128515;	
😄	&#128516;	
😅	&#128517;

# HTML Encoding (Character Sets)

* To display an HTML page correctly, a web browser must know which character set to use.

## From ASCII to UTF-8

* ASCII was the first character encoding standard. ASCII defined 128 different characters that could be used on the internet: numbers (0-9), English letters `(A-Z),` and some special characters like ! $ + - ( ) @ < > .

 * ISO-8859-1 was the default character set for HTML 4. This character set supported 256 different character codes. HTML 4 also supported UTF-8.

 * ANSI (Windows-1252) was the original Windows character set. ANSI is identical to ISO-8859-1, except that ANSI has 32 extra characters.


## The HTML charset Attribute

```html

<meta charset="UTF-8">
```

# HTML Uniform Resource Locators

#### A URL is another word for a web address.

A URL can be composed of words (e.g. w3schools.com), or an Internet Protocol (IP) address (e.g. 192.68.20.50).

```html
scheme://prefix.domain:port/path/filename
```
  ### Explanation:

`scheme `- defines the type of Internet service (most common is `http or https)`
`prefix` - defines a domain `prefix` (default for http is www)
`domain` - defines the Internet `domain name `(like w3schools.com)
`port -` defines the `port number `at the host (default for http is `80)`
`path` - defines a `path` at the server (If omitted: the root directory of the site)
`filename `- defines the name of a document or resource

# HTML Versus XHTML
* XHTML is a stricter, more XML-based version of HTML.

### What is XHTML?
* XHTML stands for EXtensible HyperText Markup Language
* XHTML is a stricter, more XML-based version of HTML
* XHTML is HTML defined as an XML application
XHTML is supported by all major browsers
### Why XHTML?
* XML is a markup language where all documents must be marked up correctly (be "well-formed").

## The Most Important Differences from HTML

* `<!DOCTYPE>` is `mandatory`

The xmlns attribute in `<html>` is `mandatory`

`<html>,` `<head>,` `<title>`, and `<body> `are `mandatory`

Elements must always be `properly nested`

Elements must always be `closed`

Elements must always be in `lowercase`

Attribute names must always be in `lowercase`

Attribute values must always be `quoted`

Attribute minimization is `forbidden`

# HTML Forms
* An HTML form is used to collect user input. The user input is most often sent to a server for processing.

```html
<html>
<body>

<h2>HTML Forms</h2>

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

</body>
</html>
```
### The `<form>` Element

The HTML `<form> `element is used to create an HTML form for user input:

## Text Fields
* The `<input type="text"> `defines a single-line input field for text input.
```html
<!DOCTYPE html>
<html>
<body>

<h2>Text input fields</h2>

<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>

<p>Note that the form itself is not visible.</p>

<p>Also note that the default width of text input fields is 20 characters.</p>

</body>
</html>
```
## The `<label> `Element

* Notice the use of the `<label> `element in the example above.

## Radio Buttons
* he `<input type="radio">` defines a radio button.

* Radio buttons let a user select ONE of a limited number of choices.
```html
<form>
  <input type="radio" id="html" name="fav_language" value="HTML">
  <label for="html">HTML</label><br>
  <input type="radio" id="css" name="fav_language" value="CSS">
  <label for="css">CSS</label><br>
  <input type="radio" id="javascript" name="fav_language" value="JavaScript">
  <label for="javascript">JavaScript</label>
</form> 
```
## Checkboxes
* The `<input type="checkbox">` defines a checkbox.

Checkboxes let a user select ZERO or MORE options of a limited number of choices.
```html
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label>
</form>
```
## The Submit Button
* The `<input type="submit">` defines a button for submitting the form data to a form-handler.
```html
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```
## The Name Attribute for `<input>`
* Notice that each input field must have a name attribute to be submitted.

If the name attribute is omitted, the value of the input field will not be sent at all.
```html
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" value="John"><br><br>
  <input type="submit" value="Submit">
</form>
```
# HTML Form Attributes

* This chapter describes the different attributes for the HTML `<form>` element.
* the `action` attribute defines the action to be performed when the form is submitted.

### Example

* On submit, send form data to "action_page.php":

```html

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```
## The Target Attribute

* The `target` attribute specifies where to display the response that is received after submitting the form.

The `target` attribute can have one of the following values:
* blank
* sell
* parent 
* top

```html
<form action="/action_page.php" target="_blank">
  ```
  ## The Method Attribute

* The `method` attribute specifies the HTTP method to be used when submitting the form data.

The form-data can be sent as URL variables (with `method="get"`) or as HTTP post transaction (with `method="post")`.

The default HTTP method when submitting form data is `GET.` 
* example 
```html
<form action="/action_page.php" method="get">

```
* This example uses the `POST` method when submitting the form data:

```html 
<form action="/action_page.php" method="post">
```
## The Autocomplete Attribute
* The `autocomplete` attribute specifies whether a form should have autocomplete on or off.

### Example
```html
<form action="/action_page.php" autocomplete="on">
```
## The Novalidate Attribute
* The `novalidate` attribute is a boolean attribute.

When present, it specifies that the form-data (input) should not be validated when submitted.
# HTML Form Elements
### The HTML `<form>` Elements
* The HTML `<form>` element can contain one or more of the following form elements:
`<input>`
`<label>`
`<select>`
`<textarea>`
`<button>`
`<fieldset>`
`<legend>`
`<datalist>`
`<output>`
`<option>`
`<optgroup>`
## The `<input>` Element

* One of the most used form element is the `<input> `element.
* The `<input>` element can be displayed in several ways, depending on the type attribute.

```html
 <form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br><br>
  <input type="submit" value="Submit">
</form>
```
## The `<label>` Element
* The `<label>` element is useful for screen-reader users, because the screen-reader will read out loud the label when the user focus on the input element.
## The `<select>` Element

* The `<select>` element defines a drop-down list:
```html
<form action="/action_page.php">
  <label for="cars">Choose a car:</label>
  <select id="cars" name="cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat">Fiat</option>
    <option value="audi">Audi</option>
  </select>
  <input type="submit">
</form>
```
## Pre-selected Option
```html
p>You can preselect an option with the selected attribute:</p>

<form action="/action_page.php">
  <label for="cars">Choose a car:</label>
  <select id="cars" name="cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat" selected>Fiat</option>
    <option value="audi">Audi</option>
  </select>
  <input type="submit">
</form>
```
## visible option 
* use the attribute to spacify the number of visible values
```html
<h2>Visible Option Values</h2>

<p>Use the size attribute to specify the number of visible values.</p>

<form action="/action_page.php">
  <label for="cars">Choose a car:</label>
  <select id="cars" name="cars" size="3">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat">Fiat</option>
    <option value="audi">Audi</option>
  </select><br><br>
  <input type="submit">
</form>
```
## Allow Multiple Selections
* use the multiple attribute to allow the user to select more than one value 

```html
<h2>Allow Multiple Selections</h2>

<p>Use the multiple attribute to allow the user to select more than one value.</p>

<form action="/action_page.php">
  <label for="cars">Choose a car:</label>
  <select id="cars" name="cars" size="4" multiple>
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat">Fiat</option>
    <option value="audi">Audi</option>
  </select><br><br>
  <input type="submit">
</form>
```
## Textarea

```html
<h2>Textarea</h2>
<p>The textarea element defines a multi-line input field.</p>

<form action="/action_page.php">
  <textarea name="message" rows="10" cols="30">The cat was playing in the garden.</textarea>
  <br><br>
  <input type="submit">
</form>
```
* The `rows` attribute specifies the visible number of lines in a text area.

 * The `cols` attribute specifies the visible width of a text area.

* You can also define the size of the text area by using CSS:

```html
<textarea name="message" style="width:200px; height:600px;">
The cat was playing in the garden.
</textarea>
```
## The `<button> `Element

* The `<button>` element defines a clickable button:

```html
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```
## The `<fieldset>` and `<legend> `Elements

The `<fieldset>` element is used to group related data in a form.

The <`legend>` element defines a caption for the `<fieldset>` element.
```html

<form action="/action_page.php">
  <fieldset>
    <legend>Personalia:</legend>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    <input type="submit" value="Submit">
  </fieldset>
</form>
```
## The `<datalist>` Element
* The `<datalist> `element specifies a list of pre-defined options for an `<input>` element.

Users will see a drop-down list of the pre-defined options as they input data.

The list attribute of the `<input> `element, must refer to the id attribute of the `<datalist>` element.

```html
<form action="/action_page.php">
  <input list="browsers">
  <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
  </datalist>
</form>
```
## The `<output>` Element
* The `<output>` element represents the result of a calculation (like one performed by a script).
```html
<form action="/action_page.php"
  oninput="x.value=parseInt(a.value)+parseInt(b.value)">
  0
  <input type="range"  id="a" name="a" value="50">
  100 +
  <input type="number" id="b" name="b" value="50">
  =
  <output name="x" for="a b"></output>
  <br><br>
  <input type="submit">
</form>
```
# HTML Input Types
* This chapter describes the different types for the HTML `<input>` element.
* `<input type="button">`
`<input type="checkbox">`
`<input type="color">`
`<input type="date">`
`<input type="datetime-local">`
`<input type="email">`
`<input type="file">`
`<input type="hidden">`
`<input type="image">`
`<input type="month">`
`<input type="number">`
`<input type="password">`
`<input type="radio">`
`<input type="range">`
`<input type="reset">`
`<input type="search">`
`<input type="submit">`
`<input type="tel">`
`<input type="text">`
`<input type="time">`
`<input type="url">`
`<input type="week">`

## Input Type Text

* `<input type="text">` defines a single-line text input field:


```html

<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```
## Input Type Password

* `<input type="password">` defines a password field:

```html
<form>
  <label for="username">Username:</label><br>
  <input type="text" id="username" name="username"><br>
  <label for="pwd">Password:</label><br>
  <input type="password" id="pwd" name="pwd">
</form>
```
## Input Type Submit

* `<input type="submit">` defines a button for submitting form data to a form-handler.

The form-handler is typically a server page with a script for processing input data.

The form-handler is specified in the form's `action` attribute:

```html
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```
## Input Type Reset

* `<input type="reset">` defines a reset button that will reset all form values to their default values:

```html

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
  <input type="reset">
</form>
```
## Input Type Radio
* `<input type="radio">` defines a radio button.

Radio buttons let a user select ONLY ONE of a limited number of choices:

```html
<p>Choose your favorite Web language:</p>

<form>
  <input type="radio" id="html" name="fav_language" value="HTML">
  <label for="html">HTML</label><br>
  <input type="radio" id="css" name="fav_language" value="CSS">
  <label for="css">CSS</label><br>
  <input type="radio" id="javascript" name="fav_language" value="JavaScript">
  <label for="javascript">JavaScript</label>
</form>
```
## Input Type Checkbox

* `<input type="checkbox">` defines a checkbox.

Checkboxes let a user select ZERO or MORE options of a limited number of choices.
```html
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label>
</form>
```
## Input Type Button

```html
<input type="button" onclick="alert('Hello World!')" value="Click Me!">
```
## Input Type Color
* The `<input type="color">`is used for input fields that should contain a color.

Depending on browser support, a color picker can show up in the input field.
```html
<form>
  <label for="favcolor">Select your favorite color:</label>
  <input type="color" id="favcolor" name="favcolor">
</form>
```
## Input Type Date
* The `<input type="date">` is used for input fields that should contain a date.

Depending on browser support, a date picker can show up in the input field.
```html
<form>
  <label for="birthday">Birthday:</label>
  <input type="date" id="birthday" name="birthday">
</form>
```
* You can also use the `min` and `max` attributes to add restrictions to dates:

```html
<form>
  <label for="datemax">Enter a date before 1980-01-01:</label>
  <input type="date" id="datemax" name="datemax" max="1979-12-31"><br><br>
  <label for="datemin">Enter a date after 2000-01-01:</label>
  <input type="date" id="datemin" name="datemin" min="2000-01-02">
</form>
```
## Input Type Datetime-local
* The `<input type="datetime-local"> `specifies a date and time input field, with no time zone.
```html
<form>
  <label for="birthdaytime">Birthday (date and time):</label>
  <input type="datetime-local" id="birthdaytime" name="birthdaytime">
</form>
```
## Input Type Email
* The `<input type="email">` is used for input fields that should contain an e-mail address.

```html
<form>
  <label for="email">Enter your email:</label>
  <input type="email" id="email" name="email">
</form>
```
## Input Type File
* The `<input type="file">` defines a file-select field and a "Browse" button for file uploads.
```html
<form>
  <label for="myfile">Select a file:</label>
  <input type="file" id="myfile" name="myfile">
</form>
```
## Input Type Hidden
* The `<input type="hidden">` defines a hidden input field (not visible to a user).
``` html

<form>
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <input type="hidden" id="custId" name="custId" value="3487">
  <input type="submit" value="Submit">
</form>
```
## Input Type Month

* The `<input type="month">` allows the user to select a month and year.

```html
<form>
  <label for="bdaymonth">Birthday (month and year):</label>
  <input type="month" id="bdaymonth" name="bdaymonth">
</form>
```
## Input Type Number

```html 
<form>
  <label for="quantity">Quantity (between 1 and 5):</label>
  <input type="number" id="quantity" name="quantity" min="1" max="5">
</form>
```
## Input Type Range
* The `<input type="range">` defines a control for entering a number whose exact value is not important (like a slider control). Default range is 0 to 100. However, you can set restrictions on what numbers are accepted with the `min,` `max` and `step` attributes:
```html
<form>
  <label for="vol">Volume (between 0 and 50):</label>
  <input type="range" id="vol" name="vol" min="0" max="50">
</form>
```
## Input Type Search

* The `<input type="search">` is used for search fields (a search field behaves like a regular text field).

```html
<form>
  <label for="gsearch">Search Google:</label>
  <input type="search" id="gsearch" name="gsearch">
</form>
```
## Input Type Tel
* The `<input type="tel">` is used for input fields that should contain a telephone number.
```html
<form>
  <label for="phone">Enter your phone number:</label>
  <input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}">
</form>
```
## Input Type Time
* The `<input type="time">` allows the user to select a time (no time zone).
```html
<form>
  <label for="appt">Select a time:</label>
  <input type="time" id="appt" name="appt">
</form>
```
## Input Type Url
* The `<input type="url">` is used for input fields that should contain a URL address.

```html
<form>
  <label for="homepage">Add your homepage:</label>
  <input type="url" id="homepage" name="homepage">
</form>
```
## Input Type Week

* The `<input type="week">` allows the user to select a week and year.

```html
<form>
  <label for="week">Select a week:</label>
  <input type="week" id="week" name="week">
</form>
```
## HTML Input Attributes
* This chapter describes the different attributes for the HTML `<input>` element.
## The value Attribute
* The input value attribute specifies an initial value for an input field:

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```
## The readonly Attribute
* The input readonly attribute specifies that an input field is read-only.

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John" readonly><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```
## The disabled Attribute
* The input disabled attribute specifies that an input field should be disabled.

* A disabled input field is unusable and un-clickable.

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John" disabled><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe">
</form>
```

## The size Attribute

* The input `size` attribute specifies the visible width, in characters, of an input field.
```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" size="50"><br>
  <label for="pin">PIN:</label><br>
  <input type="text" id="pin" name="pin" size="4">
</form>
```
## The maxlength Attribute

* The input `maxlength` attribute specifies the maximum number of characters allowed in an input field.

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" size="50"><br>
  <label for="pin">PIN:</label><br>
  <input type="text" id="pin" name="pin" maxlength="4" size="4">
</form>
```
## The min and max Attributes


*  The input `min` and `max` attributes specify the minimum and maximum values for an input field.

The `min` and `max` attributes work with the following input types: number, range, date, datetime-local, month, time and week.

```html
<form>
  <label for="datemax">Enter a date before 1980-01-01:</label>
  <input type="date" id="datemax" name="datemax" max="1979-12-31"><br><br>

  <label for="datemin">Enter a date after 2000-01-01:</label>
  <input type="date" id="datemin" name="datemin" min="2000-01-02"><br><br>

  <label for="quantity">Quantity (between 1 and 5):</label>
  <input type="number" id="quantity" name="quantity" min="1" max="5">
</form>
```
## The multiple Attribute

* The input `multiple` attribute specifies that the user is allowed to enter more than one value in an input field.

The `multiple` attribute works with the following input types: email, and file.
```html
<form>
  <label for="files">Select files:</label>
  <input type="file" id="files" name="files" multiple>
</form>
```
## The pattern Attribute
*  The input  `pattern` attribute specifies a regular expression that the input field's value is checked against, when the form is submitted.

* The `pattern` attribute works with the following input types: text, date, search, url, tel, email, and password.
```html
<form>
  <label for="country_code">Country code:</label>
  <input type="text" id="country_code" name="country_code"
  pattern="[A-Za-z]{3}" title="Three letter country code">
</form>
```
## The placeholder Attribute
* The input `placeholder `attribute specifies a short hint that describes the expected value of an input field (a sample value or a short description of the expected format).
```html

<form>
  <label for="phone">Enter a phone number:</label>
  <input type="tel" id="phone" name="phone"
  placeholder="123-45-678"
  pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}">
</form>
```
## The required Attribute
* The input `required` attribute specifies that an input field must be filled out before submitting the form.
* The `required` attribute works with the following input types: text, search, url, tel, email, password, date pickers, number, checkbox, radio, and file.
```html
<form>
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required>
</form>
```
## The step Attribute
* The input `step` attribute specifies the legal number intervals for an input field.

```html
<form>
  <label for="points">Points:</label>
  <input type="number" id="points" name="points" step="3">
</form>
```

## The autofocus Attribute
* The input `autofocus` attribute specifies that an input field should automatically get focus when the page loads.

```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" autofocus><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```
## The height and width Attributes
* The input `height` and `width` attributes specify the height and width of an `<input type="image"> `element.

```html
<form>
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="image" src="img_submit.gif" alt="Submit" width="48" height="48">
</form>
```
## The list Attribute
* The input `list` attribute refers to a `<datalist>` element that contains pre-defined options for an `<input>` element.
```html
<form>
  <input list="browsers">
  <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
  </datalist>
</form>

```
## The autocomplete Attribute
* The input autocomplete attribute specifies whether a form or an input field should have autocomplete on or off.
* The `autocomplete` attribute works with `<form>` and the following `<input>` types: text, search, url, tel, email, password, datepickers, range, and color.
```html
<form action="/action_page.php" autocomplete="on">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" autocomplete="off"><br><br>
  <input type="submit" value="Submit">
</form>
```
## HTML Input form* Attributes
* This chapter describes the different form* attributes for the HTML `<input>` element.
## The form Attribute
* The input `form `attribute specifies the form the `<input>` element belongs to.

```html
<form action="/action_page.php" id="form1">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <input type="submit" value="Submit">
</form>

<label for="lname">Last name:</label>
<input type="text" id="lname" name="lname" form="form1">
```
## The formaction Attribute

* The input `formaction `attribute specifies the URL of the file that will process the input when the form is submitted.
* The `formaction `attribute works with the following input types: submit and image.
```html
<form action="/action_page.php">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
  <input type="submit" formaction="/action_page2.php" value="Submit as Admin">
</form>
```
## The formenctype Attribute
* The input `formmethod` attribute defines the HTTP method for sending form-data to the action URL.

* Notes on the `"get"` method:

 * This method appends the form-data to the URL in name/value pairs

* Notes on the `"post"` method:

* This method sends the form-data as an HTTP post transaction
Form submissions with the "post" method cannot be bookmarked
The "post" method is more robust and secure than "get", and "post" does not have size limitations

```html
<form action="/action_page.php" method="get">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit using GET">
  <input type="submit" formmethod="post" value="Submit using POST">
</form>
```
## The formtarget Attribute

* The input `formtarget `attribute specifies a name or a keyword that indicates where to display the response that is received after submitting the form.
```html
<form action="/action_page.php">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
  <input type="submit" formtarget="_blank" value="Submit to a new window/tab">
</form>
```
## The formnovalidate Attribute

* The input `formnovalidate` attribute specifies that an `<input>`element should not be validated when submitted.
```HTML
<form action="/action_page.php">
  <label for="email">Enter your email:</label>
  <input type="email" id="email" name="email"><br><br>
  <input type="submit" value="Submit">
  <input type="submit" formnovalidate="formnovalidate"
  value="Submit without validation">
</form>
```
## The novalidate Attribute

* The `novalidate` attribute is a `<form>` attribute.

When present, novalidate specifies that all of the form-data should not be validated when submitted.

```HTML
<form action="/action_page.php" novalidate>
  <label for="email">Enter your email:</label>
  <input type="email" id="email" name="email"><br><br>
  <input type="submit" value="Submit">
</form>
```
# HTML Canvas Graphics
* The HTML `<canvas> `element is used to draw graphics on a web page.

The graphic to the left is created with `<canvas>`. It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.
### What is HTML Canvas?
* he HTML <`canvas>` element is used to draw graphics, on the fly, via JavaScript.

The `<canvas>` element is only a container for graphics. You must use JavaScript to actually draw the graphics.

Canvas has several methods for drawing paths, boxes, circles, text, and adding images.
* Canvas Examples
```html
<canvas id="myCanvas" width="200" height="100"></canvas>
```

```html
<!DOCTYPE html>
<html>
<body>

<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;">
Your browser does not support the HTML canvas tag.
</canvas>

</body>
</html>
```
### Add a JavaScript
* After creating the rectangular canvas area, you must add a JavaScript to do the drawing.

Here are some examples:
```html
<canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
Your browser does not support the HTML canvas tag.</canvas>

<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.moveTo(0,0);
ctx.lineTo(200,100);
ctx.stroke();
</script>
```
#### Draw a Circle

* Example
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.arc(95, 50, 40, 0, 2 * Math.PI);
ctx.stroke();
</script>
```
#### Draw a Text
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.font = "30px Arial";
ctx.fillText("Hello World", 10, 50);
</script>
```
#### Stroke Text
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.font = "30px Arial";
ctx.strokeText("Hello World", 10, 50);
</script>
```
### Draw Linear Gradient
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

// Create gradient
var grd = ctx.createLinearGradient(0, 0, 200, 0);
grd.addColorStop(0, "red");
grd.addColorStop(1, "white");

// Fill with gradient
ctx.fillStyle = grd;
ctx.fillRect(10, 10, 150, 80);
</script>
```

#### Draw Circular Gradient
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

// Create gradient
var grd = ctx.createRadialGradient(75, 50, 5, 90, 60, 100);
grd.addColorStop(0, "red");
grd.addColorStop(1, "white");

// Fill with gradient
ctx.fillStyle = grd;
ctx.fillRect(10, 10, 150, 80);
</script>
```
#### Draw Image
```html
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var img = document.getElementById("scream");
ctx.drawImage(img, 10, 10);
</script>
````
# HTML SVG Graphics
* SVG defines vector-based graphics in XML format.

### What is SVG?
* SVG stands for Scalable Vector Graphics
SVG is used to define graphics for the Web

* The HTML `<svg>` element is a container for SVG graphics.
* SVG has several methods for drawing paths, boxes, circles, text, and graphic images.


#### SVG Circle
```html
<!DOCTYPE html>
<html>
<body>

<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>

</body>
</html>
```
### SVG Rectangle
```html
<svg width="400" height="100">
  <rect width="400" height="100" style="fill:rgb(0,0,255);stroke-width:10;stroke:rgb(0,0,0)" />
</svg>
```
### SVG Rounded Rectangle
```html
<svg width="400" height="180">
  <rect x="50" y="20" rx="20" ry="20" width="150" height="150"
  style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
</svg>
```
### SVG Star

```html
<svg width="300" height="200">
  <polygon points="100,10 40,198 190,78 10,78 160,198"
  style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;" />
</svg>
```
### SVG Logo

```html
<svg height="130" width="500">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
    </linearGradient>
  </defs>
  <ellipse cx="100" cy="70" rx="85" ry="55" fill="url(#grad1)" />
  <text fill="#ffffff" font-size="45" font-family="Verdana" x="50" y="86">SVG</text>
  Sorry, your browser does not support inline SVG.
</svg>
````
### Differences Between SVG and Canvas

* SVG is a language for describing 2D graphics in XML.

* Canvas draws 2D graphics, on the fly (with a JavaScript).


# HTML Multimedia

* Multimedia on the web is sound, music, videos, movies, and animations.

### What is Multimedia?
* Multimedia comes in many different formats. It can be almost anything you can hear or see, like images, music, sound, videos, records, films, animations, and more.

### Browser Support
* The first web browsers had support for text only, limited to a single font in a single color.

Later came browsers with support for colors, fonts, images, and multimedia!

## Multimedia Formats
Multimedia elements (like audio or video) are stored in media files.

The most common way to discover the type of a file, is to look at the file extension.

Multimedia files have formats and different extensions like: .wav, .mp3, .mp4, .mpg, .wmv, and .avi.

## Common Audio Formats
* MP3 is the best format for compressed recorded music. The term MP3 has become synonymous with digital music.
# HTML Video

* The HTML `<video>` element is used to show a video on a web page.

```html
<!DOCTYPE html>
<html>
<body>

<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>

</body>
</html>
```
## HTML `<video>` Autoplay
* To start a video `<automatically`>, use the autoplay attribute:
```html

<video width="320" height="240" autoplay>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
```
### Add `muted` after `autoplay `to let your video start playing automatically (but muted):


``` html
<video width="320" height="240" autoplay muted>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
```
# HTML Audio

* The HTML `<audio>` element is used to play an audio file on a web page.


```html
<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
```
## HTML `<audio>` Autoplay
* To start an audio file automatically, use the `autoplay` attribute:
```html

<audio controls autoplay>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
```
#### Add `muted` after `autoplay `to let your audio file start playing automatically (but muted):

```html
<audio controls autoplay muted>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
```
# HTML Plug-ins
* Plug-ins are computer programs that extend the standard functionality of the browser.


#### Plug-ins were designed to be used for many different purposes:

* To run Java applets<br>
To run Microsoft ActiveX controls<br>
To display Flash movies<br>
To display maps<br>
To scan for viruses<br>
To verify a bank id

## The `<object>` Element

* The `<object>` element is supported by all browsers.

The `<object>` element defines an embedded object within an HTML document.

```html
<object width="100%" height="500px" data="snippet.html"></object>
```
#### Or images if you like:


```html
<object data="audi.jpeg"></object>
```
### the `<embed>` element 
```html
<embed width="100%" height="500px" src="snippet.html">
```
### HTML YouTube Videos
* The easiest way to play videos in HTML, is to use YouTube.

## Struggling with Video Formats?

* Converting videos to different formats can be difficult and time-consuming.

An easier solution is to let YouTube play the videos in your web page

## Playing a YouTube Video in HTML

* Upload the video to YouTube<br>
Take a note of the video id<br>
Define an `<iframe>` element in your web page<br>
Let the src attribute point to the video URL<br>
Use the width and height attributes to specify the dimension of the player<br>
Add any other parameters to the URL (see below)
```css
<iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
</iframe>
````
* example example 
```html
<!DOCTYPE html>
<html>

<body>

  <iframe width="560" height="315"
   src="https://www.youtube.com/embed/CU58htwn6Ho" title="YouTube video player"
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>

</body>

</html>
````
## YouTube Loop

* Add loop=1 to let your video loop forever.

```html
<iframe width="420" height="315"
src="https://www.youtube.com/embed/tgbNymZ7vqY?playlist=tgbNymZ7vqY&loop=1">
</iframe>
```
## YouTube Controls

* Add `controls=0` to not display controls in the video player.

```html
<iframe width="420" height="315"
src="https://www.youtube.com/embed/tgbNymZ7vqY?controls=0">
</iframe>
```
#  HTML Geolocation API
*  The HTML Geolocation API is used to locate a user's position.

## Using HTML Geolocation
* The `getCurrentPosition()` method is used to return the user's position.

```html
<script>
var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>
```
## Handling Errors and Rejections

* The second parameter of the `getCurrentPosition()` method is used to handle errors. It specifies a function to run if it fails to get the user's location:
```html
function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred."
      break;
  }
}
```
## Geolocation Object - Other interesting Methods

* The Geolocation object also has other interesting methods:

`watchPosition()` - Returns the current position of the user and continues to return updated position as the user moves (like the GPS in a car).
`clearWatch()` - Stops the `watchPosition()` method.
The example below shows the `watchPosition()` method. You need an accurate GPS device to test this (like smartphone):
```html
<script>
var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>
```
# HTML Drag and Drop API
* In HTML, any element can be dragged and dropped.

### HTML Drag and Drop Example
```html
<!DOCTYPE HTML>
<html>
<head>
<script>
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
</script>
</head>
<body>

<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>

<img id="drag1" src="img_logo.gif" draggable="true" ondragstart="drag(event)" width="336" height="69">

</body>
</html>
```
### Make an Element Draggable
```html
<img draggable="true">
```
## What to Drag - ondragstart and setData()
* Then, specify what should happen when the element is dragged.

In the example above, the `ondragstart` attribute calls a function, drag(event), that specifies what data to be dragged.

The `dataTransfer.setData()` method sets the data type and the value of the dragged data:

```html
function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}
````
### Where to Drop - ondragover
```html
event.preventDefault()
```

### Do the Drop - ondrop
```html
function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
```
# HTML Web Storage API
* HTML web storage; better than cookies.
## What is HTML Web Storage?
* With web storage, web applications can store data locally within the user's browser.

## HTML Web Storage Objects
* HTML web storage provides two objects for storing data on the client:

  `window.localStorage` - stores data with no expiration date
  `window.sessionStorage` - stores data for one session (data is lost when the browser tab is closed)
  ```css
  if (typeof(Storage) !== "undefined") {
  // Code for localStorage/sessionStorage.
} else {
  // Sorry! No Web Storage support..
}
## The localStorage Object
* The localStorage object stores the data with no expiration date. The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

```html
<!DOCTYPE html>
<html>
<body>

<div id="result"></div>

<script>
// Check browser support
if (typeof(Storage) !== "undefined") {
  // Store
  localStorage.setItem("lastname", "Smith");
  // Retrieve
  document.getElementById("result").innerHTML = localStorage.getItem("lastname");
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
}
</script>

</body>
</html>
```
* another example
```html
<!DOCTYPE html>
<html>
<head>
<script>
function clickCounter() {
  if (typeof(Storage) !== "undefined") {
    if (localStorage.clickcount) {
      localStorage.clickcount = Number(localStorage.clickcount)+1;
    } else {
      localStorage.clickcount = 1;
    }
    document.getElementById("result").innerHTML = "You have clicked the button " + localStorage.clickcount + " time(s).";
  } else {
    document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
  }
}
</script>
</head>
<body>

<p><button onclick="clickCounter()" type="button">Click me!</button></p>
<div id="result"></div>
<p>Click the button to see the counter increase.</p>
<p>Close the browser tab (or window), and try again, and the counter will continue to count (is not reset).</p>

</body>
</html>
```
## The sessionStorage Object
* The `sessionStorage` object is equal to the localStorage object, except that it stores the data for only one session. The data is deleted when the user closes the specific browser tab.

```html
<!DOCTYPE html>
<html>
<head>
<script>
function clickCounter() {
  if (typeof(Storage) !== "undefined") {
    if (sessionStorage.clickcount) {
      sessionStorage.clickcount = Number(sessionStorage.clickcount)+1;
    } else {
      sessionStorage.clickcount = 1;
    }
    document.getElementById("result").innerHTML = "You have clicked the button " + sessionStorage.clickcount + " time(s) in this session.";
  } else {
    document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
  }
}
</script>
</head>
<body>

<p><button onclick="clickCounter()" type="button">Click me!</button></p>
<div id="result"></div>
<p>Click the button to see the counter increase.</p>
<p>Close the browser tab (or window), and try again, and the counter is reset.</p>

</body>
</html>
```

# HTML Web Workers API
* A web worker is a JavaScript running in the background, without affecting the performance of the page.

## What is a Web Worker?
* When executing scripts in an HTML page, the page becomes unresponsive until the script is finished.

* A web worker is a JavaScript that runs in the background

## Count numbers:
```html
<!DOCTYPE html>
<html>
<body>

<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button> 
<button onclick="stopWorker()">Stop Worker</button>

<p><strong>Note:</strong> Internet Explorer 9 and earlier versions do not support Web Workers.</p>

<script>
var w;

function startWorker() {
  if(typeof(Worker) !== "undefined") {
    if(typeof(w) == "undefined") {
      w = new Worker("demo_workers.js");
    }
    w.onmessage = function(event) {
      document.getElementById("result").innerHTML = event.data;
    };
  } else {
    document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Workers...";
  }
}

function stopWorker() { 
  w.terminate();
  w = undefined;
}
</script>

</body>
</html>


```
## Full Web Worker Example Code
```html
<!DOCTYPE html>
<html>
<body>

<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button>
<button onclick="stopWorker()">Stop Worker</button>

<script>
var w;

function startWorker() {
  if (typeof(Worker) !== "undefined") {
    if (typeof(w) == "undefined") {
      w = new Worker("demo_workers.js");
    }
    w.onmessage = function(event) {
      document.getElementById("result").innerHTML = event.data;
    };
  } else {
    document.getElementById("result").innerHTML = "Sorry! No Web Worker support.";
  }
}

function stopWorker() {
  w.terminate();
  w = undefined;
}
</script>

</body>
</html>
```
#  HTML SSE API
 
* Server-Sent Events (`SSE)` allow a web page to get updates from a server.
* first code SSE 
```html
<!DOCTYPE html>
<html>
<body>

<h1>Getting server updates</h1>
<div id="result"></div>

<script>
if(typeof(EventSource) !== "undefined") {
  var source = new EventSource("demo_sse.php");
  source.onmessage = function(event) {
    document.getElementById("result").innerHTML += event.data + "<br>";
  };
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
}
</script>

</body>
</html>
````
## Server-Side Code Example
```html
<?php
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

$time = date('r');
echo "data: The server time is: {$time}\n\n";
flush();
?>
````

