"""修复 mojibake 并提取文章，写到 UTF-8 文件"""
import re

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html', 'rb') as f:
    raw = f.read()

def try_fix(s):
    """修复 mojibake：GBK bytes 被当 UTF-8 解释后产生的乱码"""
    try:
        encoded = s.encode('latin-1', errors='replace')
        decoded = encoded.decode('gbk', errors='replace')
        return decoded
    except Exception as e:
        return s

text = raw.decode('utf-8', errors='replace')

# Find js_content range
js_start = text.find('id="js_content"')
gt_pos = text.find('>', js_start) + 1
end_search = text.find('</div></div>', gt_pos)
if end_search < 0:
    end_search = gt_pos + 200000
content_html = text[gt_pos:end_search] if end_search > 0 else text[gt_pos:gt_pos+200000]

# Extract visible text snippets
snippets = re.findall(r'>([^<>]{2,})<', content_html)

# Fix and dedupe
fixed_all = []
seen = set()
for t in snippets:
    t = t.strip()
    if not t or t in ('\n', ' ', '　'):
        continue
    if not re.search(r'[\u4e00-\u9fff]{2,}', t):
        continue
    fixed = try_fix(t)
    if fixed != t and any('\u4e00' <= c <= '\u9fff' for c in fixed):
        if fixed not in seen:
            seen.add(fixed)
            fixed_all.append(fixed)

# Video desc
video_desc_match = re.search(r'data-desc="([^"]+)"', content_html)
video_desc = try_fix(video_desc_match.group(1)) if video_desc_match else ''

# Video nickname
nick_match = re.search(r'data-nickname="([^"]+)"', content_html)
video_nick = try_fix(nick_match.group(1)) if nick_match else ''

# Title
title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', text)
title = try_fix(title_match.group(1)) if title_match else ''

# Account
acct_match = re.search(r'class="profile_nickname">([^<]+)<', text)
if not acct_match:
    acct_match = re.search(r'js_name[^>]*>([^<]+)<', text)
if not acct_match:
    acct_match = re.search(r'class="account_nickname">([^<]+)<', text)
acct = try_fix(acct_match.group(1).strip()) if acct_match else ''

# Author
author_match = re.search(r'class="rich_media_meta_text[^"]*"[^>]*>([^<]+)<', text)
author = try_fix(author_match.group(1)) if author_match else ''

# Time
pub_match = re.search(r'var\s+create_time\s*=\s*"([^"]+)"', text) or re.search(r'var\s+publish_time\s*=\s*"([^"]+)"', text)
pub = pub_match.group(1) if pub_match else ''

# Write to file
out = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\article_extracted.txt'
with open(out, 'w', encoding='utf-8-sig') as f:
    f.write("=" * 60 + "\n")
    f.write(f"标题: {title}\n")
    f.write(f"账号: {acct}\n")
    f.write(f"作者: {author}\n")
    f.write(f"发布时间: {pub}\n")
    f.write("=" * 60 + "\n\n")
    f.write("--- 视频作者（世界经济论坛）---\n")
    f.write(f"{video_nick}\n\n")
    f.write("--- 视频描述 ---\n")
    f.write(f"{video_desc}\n\n")
    f.write("--- 文章正文段落 ---\n\n")
    for p in fixed_all:
        p = p.strip()
        if p and len(p) > 3:
            f.write(f"{p}\n\n")

print(f"Saved to: {out}")
print(f"Total paragraphs: {len(fixed_all)}")
print(f"Title: {title}")
print(f"Account: {acct}")
print(f"Author: {author}")
