import os
from datetime import datetime

# Ensure the "journal" directory exists
journal_dir = "docs/journal_md"
os.makedirs(journal_dir, exist_ok=True)

# Get the journal entry title (optional)
title = input("Enter the journal title: ").strip()

# Get current date and time (down to the minute)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
filename = f"journal_entry_{timestamp}.md"
filepath = os.path.join(journal_dir, filename)

# Get current date for the entry
date = datetime.today().strftime('%Y-%m-%d')

# Markdown template for the journal entry
template = f"""# Journal Entry: {title if title else 'Untitled'}
*Date: {date}*
*Time: {timestamp.replace('_', ' ')}*

## Thoughts:
[Write your thoughts here...]

## Reflections:
[Write your reflections here...]
"""

# Write the journal entry to the markdown file
with open(filepath, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ Journal entry created: {filepath}")