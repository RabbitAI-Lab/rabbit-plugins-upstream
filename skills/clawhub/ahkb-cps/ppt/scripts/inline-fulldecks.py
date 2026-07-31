#!/usr/bin/env python3
"""Inline all external assets into full-deck templates, making them self-contained.

Developer tool — run from the ppt/scripts/ directory or set SKILL_ROOT env var.
The script auto-detects its location relative to the skill directory structure.
"""

import os, re

# Dynamically resolve skill paths relative to this script's location.
# Structure: ppt/scripts/inline-fulldecks.py → ppt/ → skill_root/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(_SCRIPT_DIR)  # ppt/ directory
WS = os.path.dirname(SKILL)           # skill root (ahkb-cps/)
FULL_DECKS = os.path.join(SKILL, 'templates', 'full-decks')

# 1. Read CSS files from workspace assets
with open(os.path.join(WS, 'assets', 'base.css'), encoding='utf-8') as f:
    base_css = f.read()
with open(os.path.join(WS, 'assets', 'fonts.css'), encoding='utf-8') as f:
    fonts_css = f.read()
with open(os.path.join(WS, 'assets', 'animations', 'animations.css'), encoding='utf-8') as f:
    anim_css = f.read()

# 2. Extract runtime.js from master.html (inlined)
with open(os.path.join(SKILL, 'templates', 'master.html'), encoding='utf-8') as f:
    master = f.read()

# Find the runtime.js script block: starts with /* AHKB-CPS :: runtime.js
marker = '/* AHKB-CPS :: runtime.js'
start_idx = master.find(marker)
if start_idx == -1:
    print('[ERR] Cannot find runtime.js marker in master.html')
    exit(1)

# Find the <script> tag just before this marker
script_open = master.rfind('<script>', 0, start_idx)
if script_open == -1:
    print('[ERR] Cannot find <script> tag before runtime.js')
    exit(1)

# Find the closing </script> for runtime.js
script_close = master.find('</script>', start_idx)
if script_close == -1:
    print('[ERR] Cannot find </script> after runtime.js')
    exit(1)

runtime_block = master[script_open:script_close + 9]  # include </script>

# 3. Process each full-deck template
for name in sorted(os.listdir(FULL_DECKS)):
    tdir = os.path.join(FULL_DECKS, name)
    index_path = os.path.join(tdir, 'index.html')
    if not os.path.isfile(index_path):
        continue

    with open(index_path, encoding='utf-8') as f:
        html = f.read()

    original = html  # for comparison

    # Inline fonts.css
    html = html.replace(
        '<link rel="stylesheet" href="../../../assets/fonts.css">',
        f'<style>\n{fonts_css}\n</style>'
    )

    # Inline base.css
    html = html.replace(
        '<link rel="stylesheet" href="../../../assets/base.css">',
        f'<style>\n{base_css}\n</style>'
    )

    # Inline animations.css
    html = html.replace(
        '<link rel="stylesheet" href="../../../assets/animations/animations.css">',
        f'<style>\n{anim_css}\n</style>'
    )

    # Inline runtime.js
    html = html.replace(
        '<script src="../../../assets/runtime.js"></script>',
        runtime_block
    )

    # Remove theme link reference (only in presenter-mode-reveal)
    html = html.replace(
        '<link rel="stylesheet" id="theme-link" href="../../../assets/themes/tokyo-night.css">',
        ''
    )

    if html == original:
        print(f'[SKIP] {name} (no external refs found)')
        continue

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Stats
    added_styles = html.count('<style>') - original.count('<style>')
    added_scripts = html.count('<script>') - original.count('<script>')
    print(f'[OK]   {name} (+{added_styles} styles, +{added_scripts} scripts)')

print('\nDone! All full-deck templates are now self-contained.')
