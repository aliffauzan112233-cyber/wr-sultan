import re

html_path = '/home/fauzan/wr_sultan/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The modal block we want to extract
modal_pattern = re.compile(r'(\s*<!-- Lightbox Modal.*?</div>\n    </div>\n)', re.DOTALL)
match = modal_pattern.search(content)

if match:
    modal_html = match.group(1)
    # Remove it from its current position
    content = content.replace(modal_html, '')
    
    # Insert it right before the floating WA button or javascript
    insert_target = '<!-- ==================== FLOATING WHATSAPP BUTTON ==================== -->'
    if insert_target in content:
        content = content.replace(insert_target, modal_html + '\n  ' + insert_target)
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modal successfully moved to the bottom of the body to fix z-index.")
else:
    print("Modal block not found.")
