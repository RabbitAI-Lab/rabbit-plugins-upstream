import re
import html
import sys
import io

# 强制 stdout UTF-8，绕开 Windows GBK
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\_mbpjmvg.html', 'r', encoding='utf-8') as f:
    s = f.read()

# 公众号常见结构：<p>...</p>、<section>、图片 data-src/src
s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
# 段落
s = re.sub(r'<(/?)p[^>]*>', '\n\n', s)
s = re.sub(r'<br\s*/?>', '\n', s)
s = re.sub(r'<(/?)section[^>]*>', '\n', s)
s = re.sub(r'<(/?)h[1-6][^>]*>', '\n\n', s)
# 图片
s = re.sub(r'<img[^>]*data-src="([^"]+)"[^>]*>', '\n\n[IMG] \\1\n\n', s)
s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', '\n\n[IMG] \\1\n\n', s)
# 链接文本
s = re.sub(r'<a[^>]*>(.*?)</a>', r'\\1', s, flags=re.DOTALL)
# 粗体
s = re.sub(r'<(/?)strong[^>]*>', r'**\\1**', s)
s = re.sub(r'<(/?)b[^>]*>', r'**\\1**', s)
# 删除其它标签
s = re.sub(r'<[^>]+>', '', s)
s = html.unescape(s)
# 清理空行
s = re.sub(r'\n{3,}', '\n\n', s)
s = re.sub(r'[ \t]+\n', '\n', s)

# 写到文件再读，绕开 PS 控制台编码
out_path = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\_mbpjmvg.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(s.strip())

print('TOTAL CHARS:', len(s))
print('SAVED:', out_path)