import re, shutil, os
from datetime import datetime

SRC = '双色球2026099期预测报告_V1_全面修复_V15_增强版.html'
html = open(SRC, encoding='utf-8').read()
orig_len = len(html)

# 1) strip all <script ...>...</script> blocks
html_no_script = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)

# 2) strip inline event-handler attributes on*=...
html_clean = re.sub(r'\s+on[a-z]+\s*=\s*"[^"]*"', '', html_no_script, flags=re.IGNORECASE)
html_clean = re.sub(r"\s+on[a-z]+\s*=\s*'[^']*'", '', html_clean, flags=re.IGNORECASE)

# 3) neutralize any leftover javascript: hrefs
html_clean = re.sub(r'javascript:[^"\')\s]*', '#', html_clean, flags=re.IGNORECASE)

ts = datetime.now().strftime('%Y%m%d_%H%M%S')
preview = '_preview_yuce_2026099_' + ts + '.html'
open(preview, 'w', encoding='utf-8').write(html_clean)
print('STATIC PREVIEW:', preview, 'orig=', orig_len, 'clean=', len(html_clean),
      'scripts_removed=', orig_len - len(html_no_script))

# E) copy full interactive version to Desktop
dst = 'C:/Users/www74/Desktop/双色球2026099期预测报告_最新增强版.html'
shutil.copy2(SRC, dst)
print('DESKTOP COPY:', dst, os.path.getsize(dst))
