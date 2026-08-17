import sys
try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image
import os

img_dir = r'C:\Users\jackbikepf\Documents\The Food Point\img'
bg_path = os.path.join(img_dir, 'hero_bg.jpg')
logo_path = os.path.join(img_dir, 'logo_the_food_point.png')

try:
    bg = Image.open(bg_path).convert('RGBA')
    logo = Image.open(logo_path).convert('RGBA')

    bg_w, bg_h = bg.size
    logo_w, logo_h = logo.size

    # Target logo height: 60% of bg height
    target_h = int(bg_h * 0.6)
    target_w = int(logo_w * (target_h / logo_h))
    logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    # Position center-right
    x = int(bg_w * 0.75 - target_w/2)
    y = (bg_h - target_h) // 2

    bg.paste(logo, (x, y), logo)
    out_path = os.path.join(img_dir, 'hero_with_logo.jpg')
    bg.convert('RGB').save(out_path, quality=95)
    print('Composite saved!')
except Exception as e:
    print('Error:', e)
