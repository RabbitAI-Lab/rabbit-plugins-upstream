"""修复 mojibake 并提取文章"""
import re

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html', 'rb') as f:
    raw = f.read()

# 微信文章内容经常是 GBK 编码，HTML 头说 UTF-8 但 body 是 GBK
# 找出 HTML 中含乱码的段
text_bytes = raw

# 方法：找一段含 "智能" 应该是 mojibake 的文本，尝试修复
# mojibake 字符：包含拉丁字符和很多 Chinese chars 错位

# 智能 = GBK CE C4，UTF-8 误读为 CE C4 = Î Ä；又 二次编码：Î Ä 编码 UTF-8 是 c3 8e c3 84，被当 Latin1 写入文件...
# 实际上对于 GBK 字节流被嵌入 UTF-8 HTML 的情况：
# raw 是 utf-8 字符串（含 mojibake chars），需要将这些 mojibake 字符串转回 GBK
# mojibake char "鏅" 在 unicode 码点是 U+93D5，对应 UTF-8 bytes = E9 8F 95
# 实际 GBK 中 "智" 字节 = CE C4
# 所以解码过程：把 mojibake 字符当 UTF-8 反编码成原始 bytes，再用 GBK 解码
# 但 mojibake chars 是 Unicode code point，需要找到原始 bytes...

# 简单办法：试 UTF-8 编码 -> GBK 解码
def try_fix(s):
    """尝试把 mojibake 字符串修复回中文"""
    try:
        # mojibake 字符串的每个 char 是 Unicode code point
        # 实际原文是：GBK bytes 被错误地作为 UTF-8 字节解释
        # 修复：把 mojibake 字符串用 latin-1 编码（保留 bytes）→ 用 GBK 解码
        encoded = s.encode('latin-1', errors='replace')
        decoded = encoded.decode('gbk', errors='replace')
        return decoded
    except Exception as e:
        return s

# 找出 mojibake 段
text = raw.decode('utf-8', errors='replace')
js_start = text.find('id="js_content"')
gt_pos = text.find('>', js_start) + 1
end_search = text.find('</div></div>', gt_pos)
if end_search < 0:
    end_search = gt_pos + 200000
content_html = text[gt_pos:end_search] if end_search > 0 else text[gt_pos:gt_pos+200000]

# 提取所有 visible text
texts = re.findall(r'>([^<>]{2,})<', content_html)
fixed_all = []
for t in texts:
    t = t.strip()
    if not t or t in ('\n', ' '):
        continue
    # 启发式：包含 mojibake 模式的 chars
    if re.search(r'[\u4e00-\u9fff]{3,}', t):
        fixed = try_fix(t)
        if fixed != t and any('\u4e00' <= c <= '\u9fff' for c in fixed):
            fixed_all.append(fixed)

# 修复 video desc
video_desc_match = re.search(r'data-desc="([^"]+)"', content_html)
video_desc = try_fix(video_desc_match.group(1)) if video_desc_match else ''

# 修复 video nickname
nick_match = re.search(r'data-nickname="([^"]+)"', content_html)
video_nick = try_fix(nick_match.group(1)) if nick_match else ''

# 修复 title
title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', text)
title = try_fix(title_match.group(1)) if title_match else ''

# 修复 account_nickname
acct_match = re.search(r'class="profile_nickname">([^<]+)<', text)
if not acct_match:
    acct_match = re.search(r'class="account_nickname">([^<]+)<', text)
if not acct_match:
    acct_match = re.search(r'js_name.*?>([^<]+)<', text)
acct = try_fix(acct_match.group(1).strip()) if acct_match else ''

# 修复 author
author_match = re.search(r'class="rich_media_meta_text[^"]*"[^>]*>([^<]+)<', text)
author = try_fix(author_match.group(1)) if author_match else ''

# publish time
pub_match = re.search(r'var\s+create_time\s*=\s*"([^"]+)"', text) or re.search(r'var\s+publish_time\s*=\s*"([^"]+)"', text) or re.search(r"createTime\s*=\s*['\"]([^'\"]+)['\"]", text)
pub = pub_match.group(1) if pub_match else ''

# 输出
print("=" * 60)
print(f"标题: {title}")
print(f"账号: {acct}")
print(f"作者: {author}")
print(f"发布时间: {pub}")
print("=" * 60)
print()
print("--- 视频描述 ---")
print(video_desc)
print()
print("--- 视频作者 ---")
print(video_nick)
print()
print("--- 文章段落 ---")
for p in fixed_all:
    p = p.strip()
    if p:
        print(p)
        print()
