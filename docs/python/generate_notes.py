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
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=1">
        <meta name="author" content="Bertrand Lee">
    <meta name="description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
    <meta name="keywords" content="Bertrand Lee, Portfolio, Computer Science, Machine Learning, AI, RAG, Web Development">
    <meta http-equiv="content-security-policy" content="default-src https:">
    <meta property="og:title" content="Bertrand - Computer Science Portfolio">
    <meta property="og:description" content="Bertrand Lee's portfolio showcasing programming skills and projects in machine learning, AI, RAG, web-development, and more.">
    <meta property="og:image" content="https://media.licdn.com/dms/image/v2/D4E03AQH2X3hGofYJSA/profile-displayphoto-shrink_400_400/B4EZPiubCEHAAk-/0/1734675641392?e=1743638400&v=beta&t=m_WzShCEoK3i9xjb3ionYUf6NK03tXljwj1JEVoh_bQ">

    <!-- favicons -->
    <link rel="apple-touch-icon" sizes="180x180" href="{base_path}/images/apple-touch-icon.png">
    <link rel="icon" type="image/x-icon" href="{base_path}/images/favicon.ico">
    <link rel="icon" type="image/png" sizes="16x16" href="{base_path}/images/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="{base_path}/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="{base_path}/images/android-chrome-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="{base_path}/images/android-chrome-512x512.png">
    <link rel="manifest" href="{base_path}/images/site.webmanifest">

    <!-- other -->
    <title>{title}</title>
    <link rel="stylesheet" href="{base_path}/styles/style.css">
</head>
<body>
    <nav class="navbar">
        <fieldset>
            <legend>Navigation</legend>
            <ul>
                <li><a href="{base_path}/index.html">Home</a></li>
                <li><a href="{base_path}/about.html">About</a></li>
                <li><a href="{base_path}/projects.html">Projects</a></li>
                <li><a href="{base_path}/resume.html">Resume</a></li>
                <li><a href="{base_path}/notes.html">Notes</a></li>
                <li><a href="{base_path}/journal.html">Journal</a></li>
            </ul>
        </fieldset>
    </nav>

    <aside id="connections">
        <fieldset>
            <legend>Connections</legend>
            <ul>
                <li><a href="https://www.linkedin.com/in/bertrand-lee-76624b322/" target="_blank">LinkedIn</a></li>
                <!-- add link for my CV-->
                <!-- add link for the linknet project-->
                <!-- add link for any pertinent stuff-->
            </ul>
        </fieldset>
        <div id="controls">
            <div id="movement">
                <button id="Top" href="#">Move Up</button>
                <button id="Bottom" href="#">Move Down</button>
            <div id="ui-look">
                <button id="switch" alt="light switch" class="light">Mode</button>
            </div>
        </div>
    </aside>

    <main>
        <article>
            {content}
        </article>
    </main>

    <footer>
        <p>© 2025 Bertrand Lee</p>
        <a href="https://www.linkedin.com/in/bertrand-lee-76624b322/" target="_blank">Connect with me on LinkedIn!</a>
    </footer>
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

    links = [f'<li><a href="{os.path.basename(html_dir)}/{os.path.splitext(f)[0]}.html">{os.path.splitext(f)[0]}</a></li>' 
             for f in md_files if f.endswith(".md")]
    
    index_content = HTML_TEMPLATE.format(
        title=title,
        content=f"""
        <h1>{title}</h1>
        <ul>
            {''.join(links)}
        </ul>
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