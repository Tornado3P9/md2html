"""
pip install -r requirements.txt
"""

import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import argparse
import os

# Create the parser
parser = argparse.ArgumentParser(description='Process a filename.')

# Add the filename argument
parser.add_argument('filename', help='The file to process')

# Parse the arguments
args = parser.parse_args()

# Extract the base name of the file without the extension
base_name = os.path.splitext(args.filename)[0]

# Now you can use args.filename to access the filename provided
print(f'Processing file: {args.filename} -> {base_name}.html')

# Read markdown file
with open(args.filename, 'r') as file:
    markdown_text = file.read()

# Convert markdown to HTML with colored syntax highlighting
html = markdown.markdown(markdown_text, extensions=['fenced_code', 'codehilite'])

# Save HTML to file with the same base name as the source
output_filename = f'{base_name}.html'
with open(output_filename, 'w') as file:
    file.write('<link rel="stylesheet" href="codehilite.css"/>\n' + html)

"""
# see different default styles:
pygmentize -L
# Also don't forget to create the css file within your terminal:
# Styles default or monokai or nord do look quite nice:
pygmentize -S default -f html -a .codehilite > codehilite.css
"""
