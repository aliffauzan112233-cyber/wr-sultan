import os
import re

html_path = '/home/fauzan/wr_sultan/index.html'
css_dir = '/home/fauzan/wr_sultan/assets/css'
js_dir = '/home/fauzan/wr_sultan/assets/js'

os.makedirs(css_dir, exist_ok=True)
os.makedirs(js_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
style_pattern = re.compile(r'<style>\n(.*?)\n  </style>', re.DOTALL)
style_match = style_pattern.search(content)
if style_match:
    css_content = style_match.group(1).strip()
    with open(os.path.join(css_dir, 'style.css'), 'w', encoding='utf-8') as f:
        f.write(css_content + '\n')
    
    # Replace style block with link
    link_tag = '  <link rel="stylesheet" href="assets/css/style.css">'
    content = content[:style_match.start()] + link_tag + content[style_match.end():]

# Extract JS
script_pattern = re.compile(r'<!-- ==================== VANILLA JAVASCRIPT ==================== -->\s*<script>\s*(.*?)\s*</script>', re.DOTALL)
script_match = script_pattern.search(content)
if script_match:
    js_content = script_match.group(1).strip()
    with open(os.path.join(js_dir, 'main.js'), 'w', encoding='utf-8') as f:
        f.write(js_content + '\n')
    
    # Replace script block with external script
    script_tag = '<!-- ==================== VANILLA JAVASCRIPT ==================== -->\n  <script src="assets/js/main.js" defer></script>'
    content = content[:script_match.start()] + script_tag + content[script_match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactoring complete.")
