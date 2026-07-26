"""从 raw.html 提取文章正文并修复 mojibake"""
import re
import json

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html', 'rb') as f:
    raw = f.read()

# 1. 提取 js_content 之间的内容
text = raw.decode('utf-8', errors='replace')
js_start = text.find('id="js_content"')
if js_start < 0:
    print("No js_content")
    exit(1)

# 找到 js_content 后的 div 开始
div_start = text.rfind('<div', 0, js_start)
# 找到 js_content 后的 > 位置
gt_pos = text.find('>', js_start) + 1
# 找到结束 </div> 大致位置 - 找 js_content 后的下一个 </section> 之后 </div>
# 简单办法：找 </div></div> 结束标记
end_search = text.find('</div></div>', gt_pos)
if end_search < 0:
    end_search = text.find('</div>\n', gt_pos)
content_html = text[gt_pos:end_search] if end_search > 0 else text[gt_pos:gt_pos+100000]

# 2. 修复 mojibake - 微信文章内容是 GBK 编码但放在 UTF-8 页面里
# 找包含大量 mojibake 的字符串
def try_fix_mojibake(s):
    """尝试 GBK->UTF-8 反转"""
    try:
        # 先把字符串按 utf-8 编码（替换坏字符为?），再尝试 latin1 解析，再 gbk 解码
        # mojibake: utf-8 bytes 被当成 latin1 显示，现在用 gbk 解码回去
        encoded = s.encode('utf-8', errors='replace')
        # 错误的 utf-8 bytes 实际是 GBK bytes
        decoded = encoded.decode('gbk', errors='replace')
        return decoded
    except Exception as e:
        return s

# 3. 找所有可读文本
# 简单的：从 content 提取 text 和 visible content
visible_texts = re.findall(r'>([^<>]{2,})<', content_html)
fixed_texts = []
for t in visible_texts:
    t = t.strip()
    if not t or t in ('\n', ' '):
        continue
    # 如果包含 mojibake 模式（看起来像乱码）
    if any(c in t for c in ['闆嗕腑', '绐佺牬', '绯荤粺', '鎶€鏈', '鏅鸿兘', '鐢熶骇', '鍒堕€', '浜哄櫒', '浜烘満', '鍗忎綔', '宸ヤ笟', '鏂瑰紡', '灏嗕細', '鎴愮啛', '瀹炵敤', '鍖哄潡', '鍒嗗壊', '鐨勪竴']):
        fixed = try_fix_mojibake(t)
        fixed_texts.append(fixed)
    elif re.search(r'[\u4e00-\u9fff]{3,}', t):
        fixed_texts.append(t)

# 4. 找视频描述
video_desc_match = re.search(r'data-desc="([^"]+)"', content_html)
if video_desc_match:
    raw_desc = video_desc_match.group(1)
    fixed = try_fix_mojibake(raw_desc)
    print("=== VIDEO DESC (fixed) ===")
    print(fixed)
    print()

# 5. 找 account_nickname
nickname_match = re.search(r'var\s+nickname\s*=\s*"([^"]+)"', text)
if not nickname_match:
    nickname_match = re.search(r'class="profile_nickname">([^<]+)<', text)
acct = nickname_match.group(1) if nickname_match else ''

# 6. 找 publish_time
pub_match = re.search(r'var\s+create_time\s*=\s*"([^"]+)"', text) or re.search(r'var\s+publish_time\s*=\s*"([^"]+)"', text) or re.search(r"createTime\s*=\s*['\"]([^'\"]+)['\"]", text)
pub = pub_match.group(1) if pub_match else ''

# 7. 找 author
author_match = re.search(r'class="rich_media_meta_text[^"]*"[^>]*>([^<]+)<', text)
author = author_match.group(1) if author_match else ''

# 8. Title
title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', text)
title = title_match.group(1) if title_match else ''

# 9. 提取段落
paras_from_content = []
# 找 mp-common-videosnap
videosnap_pos = content_html.find('mp-common-videosnap')
if videosnap_pos > 0:
    # 找 vSection 结束后的 section
    end_vid = content_html.find('</section>', videosnap_pos)
    if end_vid < 0:
        end_vid = videosnap_pos + 5000
    after_vid = content_html[end_vid:]
    # 提取所有 text
    paras = re.findall(r'>([^<>]{3,})<', after_vid)
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if re.search(r'[\u4e00-\u9fff]{3,}', p) or len(p) > 3:
            # 修复 mojibake
            if any(c in p for c in ['鏅鸿兘', '鍒堕€', '浜烘満', '浜哄櫒', '鍗忎綔', '绯荤粺', '鎶€鏈']):
                p = try_fix_mojibake(p)
            paras_from_content.append(p)

# 修复 video_desc 和所有 paras
all_texts = []
if video_desc_match:
    all_texts.append(('视频描述', try_fix_mojibake(video_desc_match.group(1))))
for i, p in enumerate(paras_from_content):
    all_texts.append((f'段落{i+1}', p))

print("=" * 60)
print(f"标题: {title}")
print(f"账号: {acct}")
print(f"作者: {author}")
print(f"发布时间: {pub}")
print("=" * 60)
print()
for label, text in all_texts:
    print(f"[{label}]")
    print(text.strip())
    print()
