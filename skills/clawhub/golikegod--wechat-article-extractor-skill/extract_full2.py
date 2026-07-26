"""用 ftfy 修复 mojibake 并提取文章"""
import re
import ftfy

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html', 'rb') as f:
    raw = f.read()

# 关键：原始文件可能是 GBK 编码，先尝试用 GBK 读
# 但 HTML 头是 UTF-8，浏览器当 UTF-8 处理导致 mojibake
# 我们的 raw 是 utf-8 字符串，里面含 mojibake
# 用 ftfy 修复
text = raw.decode('utf-8', errors='replace')
text_fixed = ftfy.fix_text(text)

# Find js_content range
js_start = text_fixed.find('id="js_content"')
gt_pos = text_fixed.find('>', js_start) + 1
end_search = text_fixed.find('</div></div>', gt_pos)
if end_search < 0:
    end_search = gt_pos + 200000
content_html = text_fixed[gt_pos:end_search] if end_search > 0 else text_fixed[gt_pos:gt_pos+200000]

# Extract visible text snippets
snippets = re.findall(r'>([^<>]{2,})<', content_html)
fixed_all = []
seen = set()
for t in snippets:
    t = t.strip()
    if not t or t in ('\n', ' ', '　'):
        continue
    if not re.search(r'[\u4e00-\u9fff]{2,}', t):
        continue
    if t not in seen:
        seen.add(t)
        fixed_all.append(t)

# Video desc
video_desc_match = re.search(r'data-desc="([^"]+)"', content_html)
video_desc = video_desc_match.group(1) if video_desc_match else ''

# Video nickname
nick_match = re.search(r'data-nickname="([^"]+)"', content_html)
video_nick = nick_match.group(1) if nick_match else ''

# Title
title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', text_fixed)
title = title_match.group(1) if title_match else ''

# Account
acct_match = re.search(r'class="profile_nickname">([^<]+)<', text_fixed)
if not acct_match:
    acct_match = re.search(r'js_name[^>]*>([^<]+)<', text_fixed)
if not acct_match:
    acct_match = re.search(r'class="account_nickname">([^<]+)<', text_fixed)
acct = acct_match.group(1).strip() if acct_match else ''

# Author
author_match = re.search(r'class="rich_media_meta_text[^"]*"[^>]*>([^<]+)<', text_fixed)
author = author_match.group(1) if author_match else ''

# Time
pub_match = re.search(r'var\s+create_time\s*=\s*"([^"]+)"', text_fixed) or re.search(r'var\s+publish_time\s*=\s*"([^"]+)"', text_fixed)
pub = pub_match.group(1) if pub_match else ''

# Write to UTF-8 file
out = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\article_extracted.txt'
with open(out, 'w', encoding='utf-8-sig') as f:
    f.write("=" * 60 + "\n")
    f.write(f"标题: {title}\n")
    f.write(f"账号: {acct}\n")
    f.write(f"作者: {author}\n")
    f.write(f"发布时间: {pub}\n")
    f.write("=" * 60 + "\n\n")
    f.write("--- 视频作者 ---\n")
    f.write(f"{video_nick}\n\n")
    f.write("--- 视频描述 ---\n")
    f.write(f"{video_desc}\n\n")
    f.write("--- 文章正文段落 ---\n\n")
    for p in fixed_all:
        p = p.strip()
        if p and len(p) >= 2:
            f.write(f"{p}\n\n")

print(f"Saved to: {out}")
print(f"Total paragraphs: {len(fixed_all)}")
