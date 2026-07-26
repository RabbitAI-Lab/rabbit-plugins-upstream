import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\_mbpjmvg_clean.md'
print('size:', os.path.getsize(p))
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()
print('--- HEAD 5500 ---')
print(s[:5500])
print('--- TAIL 1500 ---')
print(s[-1500:])