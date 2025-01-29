
# HTML Basics
*Date: 2025-01-28*

## TL;DR (Basic)
The Hypertext Markup Language (HTML) is a coding language used to define the essential content and layout of a website as if to define a body but without skin, clothes, or a brain. The looks and functionality of a website is primarily taken care of with CSS and JavaScript.

## Deeper Dive (Intermediate)
1. `<!DOCTYPE html>` declares that the file is HTML5: "Document type"
2. `<html>` is the root element that holds the content of the page
3. `<head>` contains the neccessary meta-data and links to external files
4. `<body>` contains the visible content structure of the page, which is formed by the arrangment of sub-elements within it
5. `<header>` and `<footer>` define the corresponding sections of a page
6. `<section>` is a general definition for a part of the page that is neither at the very top or bottom
7. Content in html files are wrapped (tag-text-tag) with tags like `<h1>` (headings) or `<p>` (paragraphs)
8. `<a href="mailto:...">...</a>` is used for links such as urls or email addresses
9. `<link rel="stylesheet" href="style.css">` links the CSS to the page, allowing for further customization of the appearance of the page
10. "href" (for links) and "src" (for images) can be added to tags, these are called attributes.
11. `<script src="main.js"></script>` links the JavaScript file to the page for interactive purposes such as smooth scrolling

Example:
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
        <p>Here's a brief introduction about me.</p>
    </header>

    <section>
        <h2>Projects</h2>
        <p>Details of my projects will go here.</p>
    </section>

    <footer>
        <p>Contact me at: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
    </footer>

    <script src="main.js"></script>
</body>
</html>

```
## In-Depth (Advanced)
Nesting and wrapping are essential techniques used in the formating of HTML code. Nested elements terminate at an identical element that includes an backslash to signify it's purpose as an end marker.

```HTML
<header>
    <h1>Welcome to My Portfolio</h1>
    <p>Here's a brief introduction about me.</p>
</header>
```

There are 7 main HTML document elements:
1. **Structural elements** (e.g., `<header>`, `<footer>`, `<section>`, `<nav>`, `<main>` (should only be one per page), `<article>` (distinct from the page content as independent bit of information), and `<aside>` (ex. info on a sidebar)).
2. **Content tags** (e.g. `<p>` (paragraph), `<h1>` (header one), `<ul>` (unordered list), `<li>` (list element), `<a>` (link), `<img>`, `<video>`)

```HTML
<img src="image.jpg" alt="Description of the image">

<video controls>
    <source src="video.mp4" type="video/mp4">
</video>

<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
</audio>

<form action="/submit" method="POST">
    <input type="text" name="name" placeholder="Enter your name">
    <input type="submit" value="Submit">
</form>
```

3. **Meta-data elements**, placed in the `<head>` section (e.g. `<meta>` (character encoding, viewport settings, or author name), `<link>` (links to external resources), `<title>` (text to appear in the browser's title bar), and `<base>` (specifies a root URL for all relative URLs in the document) )

```HTML
<title>Bertrand's Portfolio</title>
<base href="https://manyraindrops.github.io/Portfolio-Website/">
```

4. **Form elements**, for user interaction (e.g. `<input>` (ex. text fields, checkboxes, buttons), `<textarea>` (multi-line text input area), `<button>`, `<select>` or `<option>` (dropdown menu), )

```HTML
<select name="country">
    <option value="usa">United States</option>
    <option value="canada">Canada</option>
</select>
```

5. **Interactive elements**, often used in conjunction with JavaScript (e.g. `<details>` (collapsible section) or `<dialog>` (popup box or window),)

6. **Style & Script Elements**, embedding CSS or JavaScript in the HTML

```HTML
<style>
    body {
        background-color: lightblue;
    }
</style>

<script>
    console.log('Hello, world!');
</script>
```

7. **Embedded content elements**, usually fonts or external media

```HTML
<iframe src="https://www.youtube.com/embed/example" width="560" height="315"></iframe>
```

Those elements can be modified by Attributes, which modify the behavior or add information to the element. They are always written with with a value and are always written with the additional text:

```MD
1. id="about"
2.  "id="about">[*content goes here*]<"
3. <div id="about">[*content goes here*]</div>
```
1. is the name-value pair
2. is the name-value pair with the additional text
3. is the name-value pair with a marker to show where the content goes

The following are common attributes:
1. `id` gives a unique identity to an element
2. `class` gives a collective identity to an element, useful for the purposes of styling or manipulation with JavaScript
3. `src` specifices the source of an image or script, usually its directory in the system computer.
4. `href` identifies a link, i.e. the destination URL
5. `alt` identifies a text description for an image (for accessibility)

```HTML
<img src="logo.png" alt="Website Logo">
```

6. `style` allows inline CSS styling

```HTML
<div style="color: red;">Red text</div>
```

Comments are written as such:
```HTML
<!-- This is a comment -->
```

When a character is to be written that is of the HTML syntax set, an alternative "entity" is used to represent the same symbol such that it can still be used without interfering with the code. The following are examples:
1. &lt; for <
2. &gt; for >
3. &amp; for &
4. &quot; for "

Other useful features such as tables, lists (ordered, unordered, definition; numbered, bulleted, and term+definition), HTML5 APIs are also available but not overviewed in this note.

In addition to being able to present a functional website to the world, the acceibility of the site to those without common levels of sense abilities, such as eyesight, highly benefit from the inclusion of alt text for images, `<label>` tags for forms, keyboard-navigability (such as using the "tabindex" attribute for custom elements such as divs or spans), ARIA attributes (Accessible Rich Internet Applications), and focus management (ex. when a drop-down menu is selected the first item is focused and a visual indication occurs). With JavaScript, keyboard shortcuts can be made to help with faster navigation.

```HTML
<div tabindex="0">This is a custom focusable element</div>

<button aria-label="Close" onclick="closeWindow()">X</button>
```

While the website may be accessible, it must also be searchable through the internet. The process of making it easily searchable is called Search Engine Optimization (SEO). Here are some common practices that improve SEO:
1. Title tags with relevant keywords
```HTML
<title>Bertrand - Computer Science Portfolio</title>
```

2. Meta descriptions for page content
```HTML
<meta name="description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
```

3. Meta keywords for page content
```HTML
<meta name="keywords" content="Bertrand Lee, Portfolio, Computer Science, Machine Learning, AI, RAG, Web Development">
```

4. Descriptive header tags
```HTML
<h2>Linknet: RAG from Scratch Project</h2>
```

If it is searchable, the webpage code must be interpretable by the browsers of the target audience. HTML verification can done with online tools such as https://validator.w3.org/.

When a technology is not supported, the webpage should be able to fallback onto simpler technologies that are generally more widespread. For example, if a computer cannot run JavaScript, the webpage should still be viewable and moderately functional. Or, if a video cannot be played, there can be an option to download it.

While the website may be accessible, it must also be quick to load. Reducing the size of HTML, CSS, and JavaScript code as much as possible, using loss-less compressed images, and loading data-heavy content after the rest helps reduce latency time.