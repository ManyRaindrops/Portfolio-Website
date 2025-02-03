import os
import markdown

# Directories for notes and journals
NOTES_MD_DIR = "docs/notes_md"
NOTES_HTML_DIR = "docs/notes_html"
NOTES_HTML_FILE = "docs/notes.html"
JOURNAL_MD_DIR = "docs/journal_md"
JOURNAL_HTML_DIR = "docs/journal_html"
JOURNAL_HTML_FILE = "docs/journal.html"

# HTML template for individual pages
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en-US">
<head>
    <!-- metadata -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Bertrand Lee">
    <meta name="description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
    <meta name="keywords" content="Bertrand Lee, Portfolio, Computer Science, Machine Learning, AI, RAG, Web Development">
    <meta property="og:title" content="Bertrand - Computer Science Portfolio">
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
<body>
    <header>
        <h1 class="title">Bertrand's Portfolio</h1>
        <button class="gen-nav-menu">☰</button>
        <div class="header-links">
            <button class="general-button" id="homeButton">Home</button>
            <button class="general-button" id="aboutButton">About</button>
            <button class="general-button" id="projectsButton">Projects</button>
            <button class="general-button" id="resumeButton">Resume</button>
            <button class="general-button" id="notesButton">Notes</button>
            <button class="general-button" id="journalButton">Journal</button>
        </div>
    </header>
    <div class="container">
        <aside class="right-side card">
            <img src="https://media.licdn.com/dms/image/v2/D4E03AQH2X3hGofYJSA/profile-displayphoto-shrink_400_400/B4EZPiubCEHAAk-/0/1734675641392?e=1743638400&v=beta&t=m_WzShCEoK3i9xjb3ionYUf6NK03tXljwj1JEVoh_bQ" alt="Card Image" loading="lazy">
            <div class="card-content">
                <h2>Contact</h2>
                <button id="linkedinButton">LinkedIn</button>
                <button id="githubButton">GitHub</button>
            </div>
        </aside>
    
        <main>
            <article>
                {content}
            </article>
        </main>

        <nav class="left-side card">
            <div id="theme-selector">
                <button type="button" id="themesButton">Themes</button>
                <div class="dropdown">
                    <button type="button" id="auto" name="theme" value="auto">Auto</button>
                    <button type="button" id="dark" name="theme" value="dark">Dark</button>
                    <button type="button" id="light" name="theme" value="light">Light</button>
                    <button type="button" id="grayscale" name="theme" value="grayscale">Grayscale</button>
                    <button type="button" id="shadow" name="theme" value="shadow">Shadow</button>
                    <p id="spacer-text">-</p>
                </div>
            </div>
        </nav>
    </div>
    <footer>
        <p>© 2025 Bertrand Lee</p>
        <div id="footer-links">
            <a href="https://www.linkedin.com/in/bertrand-lee-76624b322/" target="_blank">Connect with me on LinkedIn!</a>
            <a href="{base_path}/about.html#backgrounds" target="_blank">Backgrounds</a>
            <a href="https://github.com/ManyRaindrops" target="_blank">Check out my GitHub!</a>
        </div>
    </footer>
    <script src="{base_path}/scripts/main.js"></script>
</body>
</html>"""

def convert_markdown_to_html(md_file, output_dir, base_path):
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
                base_path=base_path
            ))
    except Exception as e:
        print(f"Error writing {output_path}: {e}")
        return
    
    return file_name

def update_index_page(md_dir, html_dir, index_file, title, base_path):
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
        <ul>
{''.join(links)}        </ul>
        """,
        base_path=base_path
    )
    
    try:
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
    except Exception as e:
        print(f"Error writing {index_file}: {e}")

def process_all(md_dir, html_dir, index_file, title, base_path_index, base_path_entries):
    """Convert all Markdown files and update the index page."""
    if not os.path.exists(md_dir):
        print(f"Error: Directory {md_dir} does not exist.")
        return
    
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    
    # Convert individual entries with base_path = ".."
    for md_file in os.listdir(md_dir):
        if md_file.endswith(".md"):
            convert_markdown_to_html(os.path.join(md_dir, md_file), html_dir, base_path_entries)
    
    # Update index page with base_path = "" (or "/docs")
    update_index_page(md_dir, html_dir, index_file, title, base_path_index)

if __name__ == "__main__":
    # Define base paths
    base_path_index = "."  # For notes.html and journal.html (relative to docs/)
    base_path_entries = ".."  # For individual note and journal entry pages (relative to docs/notes_html/ or docs/journal_html/)
    
    process_all(NOTES_MD_DIR, NOTES_HTML_DIR, NOTES_HTML_FILE, "My Notes", base_path_index, base_path_entries)
    process_all(JOURNAL_MD_DIR, JOURNAL_HTML_DIR, JOURNAL_HTML_FILE, "My Journal", base_path_index, base_path_entries)