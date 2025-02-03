# CSS Basics
*Date: 2025-01-30*

## TL;DR (Basic)
[One-sentence explanation]

## Deeper Dive (Intermediate)
Box Model
Because everything CSS displays is a box, understanding how the CSS Box Model works is a core foundation of CSS.

Selectors
To apply CSS to an element, you need to select it. CSS gives you a number of different ways to do this, and you can explore them in this module.

The cascade
Sometimes two or more competing CSS rules can apply to an element. Find out how the browser chooses which to use, and how to control this selection.

Specificity
This module takes a deeper look at specificity, a key part of the cascade.

Inheritance
Some CSS properties inherit if you don't specify a value for them. Find out how this works and how to use it to your advantage in this module.

Color
There are several different ways to specify color in CSS. This module examines the most commonly used color values.

Sizing Units
Find out how to size elements using CSS, working with the flexible medium of the web.

Layout
An overview of the various layout methods you have to choose from when building a component or page layout.

Flexbox
Flexbox is a layout mechanism designed for laying out groups of items in one dimension. Learn how to use it in this module.

Grid
CSS Grid Layout provides a two dimensional layout system, controlling layout in rows and columns. Discover everything the grid has to offer.

Logical Properties
Logical, flow-relative properties and values are linked to the flow of text, not the physical shape of the screen. Learn how to take advantage of this newer approach to CSS.

Spacing
Find out how to select the best method of spacing elements for the layout method you're using and the component you're building.

Pseudo-elements
A pseudo-element is like adding or targeting an extra element without having to add more HTML. They have a variety of roles, and you can learn about them in this module.

Pseudo-classes
Pseudo-classes let you apply CSS based on state changes. This means your design can react to user input, such as an invalid email address.

Borders
A border provides a frame for your boxes. Find out how to change the size, style, and color of borders using CSS.

Shadows
There are a number of ways to add shadows to text and elements in CSS. Learn how to use each option, and the tasks they were designed for.

Focus
Understand the importance of focus in your web applications. You'll learn how to manage focus, and how to make sure the path through your page works for both people using a mouse and people using the keyboard to navigate.

Z-index and stacking contexts
Find out how to control the order in which elements layer on top of each other by using z-index and the stacking context.

Functions
CSS has a range of inbuilt functions. Learn about some of the key functions and how to use them.

Gradients
In this module, you'll find out how to use the various types of gradients available in CSS. Gradients can create a whole host of useful effects, without the need for graphics apps to create images.

Animations
Animation is a great way to highlight interactive elements, and add interest and fun to your designs. Find out how to add and control animation effects with CSS.

Filters
Filters in CSS mean you can apply effects you might only think were possible in a graphics application. In this module, you can discover what is available.

Blend Modes
Create compositional effects by mixing two or more layers, and learn how to isolate an image with a white background in this module on blend modes.

Lists
A list, structurally, is composed of a list container element filled with list items. In this module, you'll learn how to style all the parts of a list.

Transitions
Learn how to define transitions between states of an element. Use transitions to improve user experience by providing visual feedback for user interaction.

Overflow
Overflow is how you deal with content that doesn't fit in a set parent size. In this module, you'll think outside the box and learn how to style overflowing content.

Backgrounds
Learn how to style boxes' backgrounds using CSS.

Text and typography
Learn how to style text on the web.

## In-Depth (Advanced)
### The Box Model
The box model represents all displayed information in the context of boxes, even representations that are not boxes. Their behavior is controled by their display value, which is controlled by extrinsic sizing (static, defined by user) or instrinsic sizing (dynamic, can be undeclared or declared in code).

Every box has four specific areas for specific jobs:
1. The contet box houses the specific information wished to be displayed (text, images, videos, etc.) and can usually control the size of the parent box (the other boxes). It is the center-most box.
2. The padding box essentially is open, transparent space between the content box and the border box. If overflow rules are set those box objects are placed in this space (`overflow: auto` or `overflow: scroll`)
3. The border box is a border defined by the `border` value and it represents the end of the css element and the beginning of what is not it.
4. The margin box is the open, transparent space around a box and is essentially like the padding box.

In order to make the size of the element defined by the outermost rendered area, rather than the content-box, the following can be used:

```CSS
.my-box {
  box-sizing: border-box;
    width: 200px;
    border: 10px solid;
    padding: 20px;
}
```

The following applies `box-sizing` to all elements.

```CSS
*,
*::before,
*::after {
  box-sizing: border-box;
}

```

### Selectors
A selector is comprised of a name and a CSS rule:

```CSS
.my-see-rule {
    backgorund: red;
    color: beige;
    font-size: 1.2rem;
}

```

Before the semicolon is the declaracion, which is given a property name. After the semicolon is a value for that property. The selector is the text between the period and the curly brackets. A simple selector modifies HTMl elements.
1. Universal selector can modify any element

```CSS
/* the universal selector uses the star symbol to mark it */

* {
  color: hotpink;
}
```

2. Type selector modifies a specific HTML such as `<section>`

```CSS
section {
  padding: 2em;
}
```

3. Class selector modifies elements with a specific class defined by the user. The `.` identifies that an attribute is being addressed.

```HTML
<div class="my-class"></div>
<button class="my-class"></button>
<p class="my-class"></p>
```

```CSS
.my-class {
  color: red;
}
```

4. ID selector works the same as the class selector, but uses `#` as the marker instead of `.`

5. The Attribute selector works the same, except that an attribute and it's value (optional) is declared within square brackets. The value can be case-sensitive (s) or case insensitive (i). Other modifications can be made with syntax shown below

```CSS
[data-type='primary'] {
  color: red;
}

[data-type] {
  color: red;
}

/* A href that contains "example.com" */
[href*='example.com'] {
  color: red;
}

/* A href that starts with https */
[href^='https'] {
  color: green;
}

/* A href that ends with .com */
[href$='.com'] {
  color: blue;
}
```

Multiple selectors can be groups together under a single CSS rule via comma separation:

```CSS
strong,
em,
.my-class,
[lang] {
  color: red;
}
```

> see also pseudo-classes and pseudo-elements

There is a set of **complex selectors** used for greater specificity and reduction of redundancy (applications can only cascade down, see the "cascading" section):
1. Combinator are bind a parent and child class, but not a child to its parent class. A child class is essentially an element that is within an encapsulating element.

```HTML
<p>A paragraph of text with some <strong>bold text for emphasis</strong>.</p>
```

The **descendant combinator** is a space and applies the style of the parent to and child (direct or simply within, but down in the hierarchy) as per the CSS definition given:

```CSS
p strong {
  color: blue;
}
```

Different selectors can be combined together to give specificity to say, only `div` elements with the `top` class

```CSS
/* Any descendant */
.top div {
  background: var(--color-primary-x-light);
  border-top: 1px solid var(--color-primary);
  border-left: 1px solid var(--color-primary);
}

/* only the direct descendant */
.top > div {
  border-bottom: 1px solid var(--color-primary);
  border-right: 1px solid var(--color-primary);
}
```

In order to reference the multiple following sibling elements (elements of the same hierarchical order (not the children of the chlidren)), `+` can be used as many times as needed.

```CSS
.top * + * {
  margin-top: 1.5em;
}
```

In order to reference all of the siblings of the child of the parent, `~` can be used. It is a general sibling selector.

The following allows the recursive application of the style definition to all child elements (all of the hierarchy, children of children and the rest) with the following syntax:

```CSS
.top * {
  margin-top: 1em;
}
```

```CSS
/* only all direct children */
.top > * {
  margin-top: 1em;
}

/* only all direct children except the first one */
.top > * + * {
  margin-top: 1em;
}
```

**Selectors can also be combined** as such (simply by writing each next to each other.):

```CSS
/* target <a> elements, that also have a class of .my-class */
a.my-class {
  color: red;
}
```

The different selectors must be distinguished by a symbol, hence the type must always come first. Using commas to separate the values identifies each selector individually.

### Pseudo-Classes
The various states of HTML elements can be used as a trigger for CSS styles, such as when an element is hovered over.

```CSS
/* Our link is hovered */
a:hover {
  outline: 1px dotted green;
}

/* Sets all even paragraphs to have a different background */
p:nth-child(even) {
  background: floralwhite;
}
```

### Pseudo-Elements
These modify the aspects of an element, as the the beginning, end, or specific features of it (like the numbers of numbered list). Before, pseudo elements utilized only one colon, but now they require two (but the old usages are still interpretable due to backwards-compatibility)

```CSS
.my-element::before {
  content: 'Prefix - ';
}

/* Your list will now either have red dots, or red numbers */
li::marker {
  color: red;
}

::selection {
  background: black;
  color: white;
}
```

### Cascading
Cascasing Stylesheets (CSS) utilizes an algorithin to resolve contesting CSS rules using these stages: order and position of appearance, specificity, origin, and importance. Hence, the CSS code become more specific down the file as more exceptions are noted and a style element within the HTML itself will have the most specificity (i.e. it will be rendered above the other CSS definitions made in the stylesheet) unless a declaration is defined with `!important` (in which case it is placed above the stages and the inline style).

```CSS
.text {
  color: green !important; /* Added !important */
}
```

The algorithm goes through each stage one at a time and falls back on the last one (4) if all else is equal.

1. Importance, affecting rule types (most important listed first):

```MD
1. transition rule type
2. !important rule type (following the same order as origin)
3. animation rule type
4. normal rule type, such as font-size, background or color
```

2. Origin has an order of importance of which the most importannt (listed first) override those less important:

```MD
1. User agent !important: !important from ser agent base styles
2. Local user styles !important: !important from local user styles
3. Authored !important: !important definitions of the webpage stylesheet
4. Authored CSS: stylesheet of the webpage
5. Local user styles. operating system level, browser preferences, and browser extensions form this layer.
6. User agent base styles: default browser applied styles.
```

3. Specificity includes an algorithm that will be gone over in the next section which calculates which calculates what it is called for each rule. Specificity is also cumulative. For example, an ID is more specific than a Type, so the rule given to the ID will override rules given to the Type.

4. The last rule defined is the rule that applies to the HTML element, meaning specificity is greater for those rules which are below others that deal with the same elements. 

```CSS
/* this creates a blue button */
button {
  color: red;
}

button {
  color: blue;
}
```


see also https://2019.wattenberger.com/blog/css-cascade and https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts

### Specifity
It is calculated with an algorithm which takes into consideration all of the specificity elements culmulatively. It should only be as high as needed in order for the CSS definitions that are intended to be rendered are actually rendered. The score is not a number but consists of three component values: (A, B, C).
1. `A` id-like specificity
2. `B` class-like specificity
3. `C` element-like specificity

When comparing, the values are compared A first and termintes whenever the primary value is greater than the other between two elements. If the two A values are unequal, then the element with the larger A value immediately is marked as more specific, B and C are not evaluated. If the A values are equal, the B values are evaluated. If the B values are equal, the C values are evaluated. The default specificity is (0, 0, 0).

1. The universal selector `*` has no specificty: (0, 0, 0).
2. Element/type or pseudo-element selectors add element-like specificity, incrementing C by 1.
3. Class, pseudo-class, or attribute selectors add class-like specificity, incrementing B by 1
4. The ID selector adds id-like specificity, incrementaing A by 1

Some selectors do not add specificity, but they always add specificity when added in an argument. The following never affect specificity:
1. Inline style attributes: `<div style="color: red"></div>`
2. !important declarations: it only changes the origin (Authored)

```CSS
/* specificity rules apply again if two definitions are marked with !important */
.branding {
  color: blue !important;
}

button {
  color: red !important;
}
```

Specificity can be boosted by writing the selector twice:

```CSS
.my-button.my-button {
  background: blue;
}

button[onclick] {
  background: grey;
}
```

This is not advisable, especially if it is done often as it may indicate that the specificity has become too complex and needs reductions.

If two declarations have the same specificity, the cascade falls back to the order position/order of appearance.

### Inheritance
It only cascades down to the children elements. All children elements inherit from their parent elements and may only have a different rendering according to the specificity rules.

The following CSS properties are inheritable:

- azimuth
- border-collapse
- border-spacing
- caption-side
- color
- cursor
- direction
- empty-cells
- font-family
- font-size
- font-style
- font-variant
- font-weight
- font
- letter-spacing
- line-height
- list-style-image
- list-style-position
- list-style-type
- list-style
- orphans
- quotes
- text-align
- text-indent
- text-transform
- visibility
- white-space
- widows
- word-spacing

In order to control inheritance, there are three keywords that can be used: `inherit`, 
1. `inherit` can be used to make a child inherit **any property**, even ones that are not inheritable by default. The parent selector must be indicated first, then the child.

```CSS
strong {
  font-weight: 900;
}

.my-component {
  font-weight: 500;
}

/* now strong will inherit from my-component */
.my-component strong {
  font-weight: inherit;
}

/* now my-component will inherit from strong */
strong .my-component  {
  font-weight: inherit;
}
```

2. `initial` rests the element to its default value (all properties have a default value in CSS)
3. `unset` behaves as `inherit` when the property is inherited by default and `initial` when the property is not inherited by default. it is useful when a reset is needed, but one does not know what the original value is.

see also https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types

### Color
Numerically defined colors include hex, RGB, or HSL.
1. `hex` can have a transperency using an alpha value, which are two digits at the end of the 6 digit hex code. These codes can also be written in shorthand by representing two digits with one: #b5s is identical to #bb55ss. To add alpha, then #bb55ss33 would expand to #bb55ss33.
2. `RGB` uses three numbers to identify the among of red, green, and blue that should be in the final output color (values 0-255). The lower the number the less of that color is added in. The alpha can be set in either of the following ways: rgb(0 0 0/ 50%), rgb(0 0 0 / 0.5), rgba(0, 0, 0, 50%), or rgba(0, 0, 0, 0.5). `rgba` has wider support. 
3. `HSL` uses hue, saturation, or lightness with hue being the color as designated by 0-360 (as in on a color wheel), and saturation (0% will make it grayscale) and lightness (100% gives a white color) being represented by respective percentages. Alpha is defined in `hsl` in the same was as `rgb` with the modded `hsl()` function or the use of the `hsla()` function.

In addition to these number values, there are 148 named CSS colors: https://developer.mozilla.org/en-US/docs/Web/CSS/named-color (see also https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#color_keywords and https://almanac.httparchive.org/en/2019/css).

These are some keywords: transparent (completely invinsible), color, text-shadow, text-decoration-color, background, linear-gradient, border-color, and outline-color. see also https://css-tricks.com/nerds-guide-color-web/

### Sizing Units
1. **Relative lengths: `ch` is the size of a single `0`, hence `ch` is a relative unit. `vw` is the width of the browser window.

```txt
Unit  Relative to:

Font-size-relative units

em  Relative to the font size, i.e. 1.5em will be 50% larger than the base computed font size of its parent. (Historically, the height of the capital letter "M").
ex	Heuristic to determine whether to use the x-height, a letter "x", or `.5em` in the current computed font size of the element.
cap	Height of the capital letters in the current computed font size of the element.
ch	Average character advance of a narrow glyph in the element's font (represented by the "0" glyph).
ic	Average character advance of a full width glyph in the element's font, as represented by the "水" (CJK water ideograph, U+6C34) glyph.
rem	Font size of the root element (default is 16px).
lh	Line height of the element.
rlh	Line height of the root element.

Viewport-relative units

vw	1% of viewport's width. People use this unit to do cool font tricks, like resizing a header font based on the width of the page so as the user resizes, the font will also resize.
vh	1% of viewport's height. You can use this to arrange items in a UI, if you have a footer toolbar for example.
vi	1% of viewport's size in the root element's inline axis. Axis refers to writing modes. In horizontal writing modes like English, the inline axis is horizontal. In vertical writing modes like some Japanese typefaces, the inline axis runs top to bottom.
vb	1% of viewport's size in the root element's block axis. For the block axis, this would be the directionality of the language. LTR languages like English would have a vertical block axis, since English language readers parse the page from top to bottom. A vertical writing mode has a horizontal block axis.
vmin	1% of the viewport's smaller dimension.
vmax	1% of the viewport's larger dimension.
```

2. numbers can come in the form of integers and decimals (0.1 or .1) and 1 usually represents 100%
3. absolute lengths should represent real lenghts (ex. 2cm can be measurred on a screen as really being 2cm)

```txt
Unit	Name	                  Equivalent to
cm  	Centimeters	            1cm = 96px/2.54
mm  	Millimeters	            1mm = 1/10th of 1cm
Q	    Quarter-millimeters	    1Q = 1/40th of 1cm
in    Inches	                1in = 2.54cm = 96px
pc    Picas	                  1pc = 1/6th of 1in
pt	  Points	                1pt = 1/72th of 1in
px	  Pixels	                1px = 1/96th of 1in
```

4. There are also angle units such as `deg` (degree) and `rad` (radian) or `dpi` (dots per int, useful for retina displays / high resolution displays)

see also https://developer.mozilla.org/docs/Learn/CSS/Building_blocks/Values_and_units

### Layout
view https://www.csszengarden.com/

