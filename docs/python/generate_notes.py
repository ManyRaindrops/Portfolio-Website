import os
import markdown

# Directories for notes and journals
NOTES_MD_DIR = "docs/files/notes_md"
NOTES_HTML_DIR = "docs/notes_html"
NOTES_HTML_FILE = "docs/notes.html"

JOURNAL_MD_DIR = "docs/files/journal_md"
JOURNAL_HTML_DIR = "docs/journal_html"
JOURNAL_HTML_FILE = "docs/journal.html"

PROJECTS_MD_DIR = "docs/projects_md"
PROJECTS_HTML_DIR = "docs/projects_html"
PROJECTS_HTML_FILE = "docs/projects.html"

# HTML template for individual pages
HTML_TEMPLATE = """<!-- ===================================================== -->
<!--                                                       -->
<!-- BSD 3-Clause License Copyright (c) 2025, Bertrand Lee -->
<!--                                                       -->
<!-- ===================================================== -->





<!DOCTYPE html>
<html lang="en-US">
<head>
    <!-- metadata -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Bertrand Lee">
    <meta name="description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
    <meta name="keywords" content="Bertrand Lee, Portfolio, Computer Science, Machine Learning, AI, RAG, Web Development">
    <meta property="og:title" content="Bertrand's Portfolio">
    <meta property="og:description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
    <meta property="og:image" content="https://media.licdn.com/dms/image/v2/D4E03AQH2X3hGofYJSA/profile-displayphoto-shrink_400_400/B4EZPiubCEHAAk-/0/1734675641392?e=1743638400&v=beta&t=m_WzShCEoK3i9xjb3ionYUf6NK03tXljwj1JEVoh_bQ">
    <meta http-equiv="content-security-policy" content="default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' https: data:; font-src 'self'; connect-src 'self'; manifest-src 'self'; frame-src 'self';">
    
    <!-- favicons -->
    <link rel="apple-touch-icon" sizes="180x180" href="{base_path}/images/apple-touch-icon.png">
    <link rel="icon" type="image/x-icon" href="{base_path}/images/favicon.ico">
    <link rel="icon" type="image/png" sizes="16x16" href="{base_path}/images/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="{base_path}/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="{base_path}/images/android-chrome-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="{base_path}/images/android-chrome-512x512.png">

    <!-- other -->
    <title>{title}</title>
    <link rel="stylesheet" href="{base_path}/styles/style.css">
</head>
<body id="top">
    <header>
        <h1 class="title">Bertrand's Portfolio</h1>
        <button class="gen-nav-menu">☰</button>
        <div class="header-links">
            <button class="general-button {layer}" id="homeButton">Home</button>
            <button class="general-button {layer}" id="projectsButton">Projects</button>
            <button class="general-button {layer}" id="resumeButton">Resume</button>
            <button class="general-button {layer}" id="blogButton">Blog</button>
            <button class="general-button {layer}" id="notesButton">Notes</button>
            <button class="general-button {layer}" id="journalButton">Journal</button>
            <button class="general-button {layer}" id="aboutButton">About</button>
        </div>
    </header>
    <div class="container">
        <aside class="right-side">
            <img id="my-headshot-picture" src="{base_path}/images/Bertrand Lee Headshot Photo.png" alt="Card Image" loading="lazy">
            <div class="card-content">
                <h1>Contact</h1>
                <a href="https://www.linkedin.com/in/bertrand-lee-76624b322/" target="_blank" rel="noopener"><img src="{base_path}/images/LI-In-Bug.png" alt="Logo" class="logo linkedin">LinkedIn</a>
                <a href="https://github.com/ManyRaindrops" target="_blank" rel="noopener"><img src="{base_path}/images/github-mark-white.png" alt="Logo" class="logo github">GitHub</a>
            </div>
        </aside>
    
        <main>
            <article>
                {content}
            </article>
            
            <!-- include a line break-->

            <!-- Future consideration of making this a separate box that floats under <main> and above <footer> -->
            <section id="connect">
                <h2><em>GOT WORK?</em></h2>
                <p>Let's connect.</p>
            </section>
        </main>

        <nav class="left-side">
            <div id="nav-header">
                <h1>Overview</h1>
                <div id="theme-selector">
                    <button type="button" id="themesButton">Themes</button>
                    <div class="dropdown">
                        <button type="button" id="auto" name="theme" value="auto"><span>Auto</span></button>
                        <button type="button" id="dark" name="theme" value="dark"><span>Dark</span></button>
                        <button type="button" id="light" name="theme" value="light"><span>Light</span></button>
                        <button type="button" id="grayscale" name="theme" value="grayscale"><span>Gray</span></button>
                        <button type="button" id="shadow" name="theme" value="shadow"><span>Shadow</span></button>
                    </div>
                </div>
            </div>
            <div id="page-overview-container">
                <div id="page-overview"></div>
            </div>
            <div id="nav-buttons">
                <button type="button" id="searchButton">Search</button>
                <a href="#top" id="scroll-top-button">Top</a>
                <a href="#bottom" id="scroll-bottom-button">Bottom</a>
            </div>
        </nav>
    </div>

    <div id="search-bar"> 
        <input type="text" id="search" placeholder="Search...">
        <div id="search-results"></div>
    </div>

    <footer id="bottom">
        <p>© 2025 Bertrand Lee</p>
        <div id="footer-links">
            <a href="https://www.linkedin.com/in/bertrand-lee-76624b322/" target="_blank" rel="noopener"><img src="{base_path}/images/LI-In-Bug.png" alt="Logo" class="logo linkedin">Connect with me on LinkedIn!</a>
            <a href="https://cal.com/bertrand-lee-25" target="_blank" rel="noopener"><img src="{base_path}/images/calDOTcom.png" alt="Logo" class="logo calDOTcom">Schedule a Meeting</a>
            <a href="https://github.com/ManyRaindrops" target="_blank" rel="noopener"><img src="{base_path}/images/github-mark-white.png" alt="Logo" class="logo github">Check out my GitHub!</a>
        </div>
    </footer>
    <script src="{base_path}/scripts/main.js"></script>
</body>
</html>"""

def convert_markdown_to_html(md_file, output_dir, base_path, layer):
    """Convert a Markdown file to an HTML file with the standard format."""
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: File {md_file} not found.")
        return
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return

    html_content = markdown.markdown(md_content, extensions=['fenced_code'])
    file_name = os.path.splitext(os.path.basename(md_file))[0] + ".html"
    output_path = os.path.join(output_dir, file_name)
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.format(
                title=file_name,
                content=html_content,
                base_path=base_path,
                layer=layer
            ))
    except Exception as e:
        print(f"Error writing {output_path}: {e}")
        return
    
    return file_name

def update_index_page(md_dir, html_dir, index_file, title, base_path, layer):
    """Regenerate the index page with links to all notes/journal entries."""
    try:
        md_files = sorted(os.listdir(md_dir), reverse=True)
    except FileNotFoundError:
        print(f"Error: Directory {md_dir} not found.")
        return
    except Exception as e:
        print(f"Error listing files in {md_dir}: {e}")
        return

    # Generate links with consistent indentation
    links = []
    for f in md_files:
        if f.endswith(".md"):
            links.append(f'            <a class="button" href="{os.path.basename(html_dir)}/{os.path.splitext(f)[0]}.html">{os.path.splitext(f)[0]}</a>\n')
    
    index_content = HTML_TEMPLATE.format(
        title=title,
        content=f"""
        <h1>{title}</h1>
        <div>
{''.join(links)}        </div>
        """,
        base_path=base_path,
        layer=layer
    )
    
    try:
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
    except Exception as e:
        print(f"Error writing {index_file}: {e}")

def process_all(md_dir, html_dir, index_file, title):
    """Convert all Markdown files and update the index page."""
    if not os.path.exists(md_dir):
        print(f"Error: Directory {md_dir} does not exist.")
        return
    
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    
    # Convert individual entries with base_path = ".."
    for md_file in os.listdir(md_dir):
        if md_file.endswith(".md"):
            convert_markdown_to_html(os.path.join(md_dir, md_file), html_dir, "..", "second-layer")
    
    # Update index page with base_path = "" (or "/docs")
    update_index_page(md_dir, html_dir, index_file, title, ".", "first-layer")

if __name__ == "__main__":
    process_all(NOTES_MD_DIR, NOTES_HTML_DIR, NOTES_HTML_FILE, "My Notes")
    process_all(JOURNAL_MD_DIR, JOURNAL_HTML_DIR, JOURNAL_HTML_FILE, "My Journal")
    """process_all(JOURNAL_MD_DIR, JOURNAL_HTML_DIR, JOURNAL_HTML_FILE, "My Projects")"""