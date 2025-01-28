import os
from datetime import datetime

# Ensure the "notes" directory exists
notes_dir = "notes"
os.makedirs(notes_dir, exist_ok=True)

# Get topic title
topic = input("Enter the topic title: ").strip()
filename = f"{topic.lower().replace(' ', '_')}.md"
filepath = os.path.join(notes_dir, filename)

# Get current date
date = datetime.today().strftime('%Y-%m-%d')

# Markdown template
template = f"""# {topic}
*Date: {date}*

## TL;DR (Basic)
[One-sentence explanation]

## Deeper Dive (Intermediate)
[Key concepts, examples, and explanations]

## In-Depth (Advanced)
[Technical details, real-world applications, code snippets]
"""

# Write the Markdown file
with open(filepath, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ Note created: {filepath}")
