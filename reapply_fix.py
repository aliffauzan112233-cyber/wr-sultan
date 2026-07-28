import re

html_path = '/home/fauzan/wr_sultan/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the modal block (which the user accidentally moved back to line 457)
modal_pattern = re.compile(r'(\s*<!-- Lightbox Modal.*?</div>\n    </div>\n)', re.DOTALL)
match = modal_pattern.search(content)

if match:
    modal_html = match.group(1)
    
    # Remove it from its current position
    content = content.replace(modal_html, '')
    
    # Let's apply our improvements to the extracted modal html
    # 1. z-index 9999
    modal_html = modal_html.replace('z-[100]', 'z-[9999]')
    if 'style="z-index: 9999;"' not in modal_html:
        modal_html = modal_html.replace('transition-opacity duration-300"', 'transition-opacity duration-300" style="z-index: 9999;"')
    
    # 2. Fix the image container and responsiveness
    old_img_container = '<div class="flex-grow overflow-auto p-2 bg-sultanCream-light">\n          <!-- Gambar besar / jelas dari menu harga -->\n          <img src="img/daftar_menu.jpg" alt="Daftar Menu Warung Makan Sultan" class="w-full h-auto object-contain">\n        </div>'
    new_img_container = '<div class="flex-grow overflow-y-auto p-0 sm:p-4 bg-sultanCream-light flex justify-center">\n          <!-- Gambar besar / jelas dari menu harga -->\n          <img src="img/daftar_menu.jpg" alt="Daftar Menu Warung Makan Sultan" class="w-full h-auto object-contain block mx-auto">\n        </div>'
    modal_html = modal_html.replace(old_img_container, new_img_container)

    # Insert it right before the floating WA button (bottom of the body)
    insert_target = '<!-- ==================== FLOATING WHATSAPP BUTTON ==================== -->'
    if insert_target in content:
        content = content.replace(insert_target, modal_html + '\n  ' + insert_target)
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modal successfully fixed and moved.")
else:
    print("Modal block not found.")
