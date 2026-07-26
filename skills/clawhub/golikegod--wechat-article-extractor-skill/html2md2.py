import re, html, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\_mbpjmvg.html'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()

# 移除脚本/样式
s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)

# 段落 -> 双换行
s = re.sub(r'</?p[^>]*>', '\n\n', s, flags=re.IGNORECASE)
s = re.sub(r'<br\s*/?>', '\n', s, flags=re.IGNORECASE)
s = re.sub(r'</?(section|h\d|div|li)[^>]*>', '\n', s, flags=re.IGNORECASE)

# 图片（公众号正文图一般在 data-src 或 src）
s = re.sub(r'<img[^>]*data-src="([^"]+)"[^>]*>', r'\n\n![img](\1)\n\n', s)
s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'\n\n![img](\1)\n\n', s)

# 粗体：先去标签，再单独把被包文本加 **（避免反向引用坑）
def bold_repl(m):
    return '**' + m.group(1) + '**'
s = re.sub(r'<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>', bold_repl, s, flags=re.DOTALL | re.IGNORECASE)

# 链接：保留文本
def a_repl(m):
    return m.group(1)
s = re.sub(r'<a[^>]*>(.*?)</a>', a_repl, s, flags=re.DOTALL)

# 去除所有剩余标签
s = re.sub(r'<[^>]+>', '', s)

# 实体反转义
s = html.unescape(s)

# 清理：去 nbsp 行首、压缩空行
s = s.replace('\u00a0', ' ')
s = re.sub(r' *\n *', '\n', s)
s = re.sub(r'\n{3,}', '\n\n', s)
s = s.strip()

out = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\_mbpjmvg_clean.md'
with open(out, 'w', encoding='utf-8') as f:
    f.write(s)

print('TOTAL CHARS:', len(s))
print('SAVED:', out)
print('IMG COUNT:', s.count('![img]'))