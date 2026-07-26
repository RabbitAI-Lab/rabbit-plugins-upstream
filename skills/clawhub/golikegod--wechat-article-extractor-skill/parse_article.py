"""解析抓到的微信文章"""
import re
import json
from html.parser import HTMLParser

class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_js_content = False
        self.in_meta = False
        self.in_title = False
        self.in_account_nickname = False
        self.in_author = False
        self.in_publish_time = False
        self.capture_text = False
        self.text_buf = []
        self.depth_in_content = 0
        self.title = ''
        self.account_nickname = ''
        self.account_alias = ''
        self.account_desc = ''
        self.author = ''
        self.publish_time = ''
        self.desc = ''
        self.cover = ''
        self.paragraphs = []
        self.images = []
        self.videos = []
        self.accounts = []
        self.current_para = []
        self.in_paragraph = False
        self.in_image = False
        self.in_video = False
        self.current_attrs = {}
        self.in_section = 0
        self.skip = False
        self.script_data = []

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        self.current_attrs = attrs_d

        if attrs_d.get('id') == 'js_content':
            self.in_js_content = True
            self.depth_in_content = 1
            return
        if self.in_js_content and tag != 'br':
            self.depth_in_content += 1

        # Meta tags in <head>
        if tag == 'meta':
            if attrs_d.get('property') == 'og:title':
                self.title = attrs_d.get('content', '')
            elif attrs_d.get('property') == 'og:image':
                self.cover = attrs_d.get('content', '')
            elif attrs_d.get('name') == 'description':
                self.desc = attrs_d.get('content', '')
        if tag == 'title' and not self.title:
            self.in_title = True
        if attrs_d.get('id') == 'activity-name' and not self.title:
            self.in_title = True
            self.title_tag_depth = 1
        if attrs_d.get('id') == 'js_name':
            self.in_account_nickname = True
        if attrs_d.get('id') == 'js_account_nickname':
            self.in_account_nickname = True
        if attrs_d.get('id') == 'js_author_name':
            self.in_author = True
        if attrs_d.get('id') == 'publish_time':
            self.in_publish_time = True
        if attrs_d.get('class') == 'rich_media_meta_nickname' and not self.account_nickname:
            self.in_account_nickname = True

        if self.in_js_content:
            if tag == 'img' or tag == 'mp-common-videosnap' or tag == 'iframe' or tag == 'mpvideo':
                if tag == 'img':
                    src = attrs_d.get('data-src') or attrs_d.get('src') or ''
                    if src:
                        self.images.append(src)
                else:
                    src = attrs_d.get('data-url') or attrs_d.get('src') or ''
                    if src:
                        self.videos.append({
                            'tag': tag,
                            'src': src,
                            'desc': attrs_d.get('data-desc', ''),
                            'nickname': attrs_d.get('data-nickname', ''),
                            'headimg': attrs_d.get('data-headimgurl', ''),
                        })
            if tag == 'p' or tag == 'section' or tag == 'span':
                if not self.in_paragraph:
                    self.in_paragraph = True
                    self.current_para = []

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if self.in_js_content:
            self.depth_in_content -= 1
            if self.depth_in_content <= 0:
                self.in_js_content = False
                return
            if tag in ('p', 'section', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                if self.in_paragraph:
                    para_text = ''.join(self.current_para).strip()
                    if para_text:
                        self.paragraphs.append(para_text)
                    self.current_para = []
                    self.in_paragraph = False
        if tag == 'p' and self.in_paragraph and not self.in_js_content:
            self.in_paragraph = False
            self.current_para = []

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_account_nickname:
            self.account_nickname += data
        if self.in_author:
            self.author += data
        if self.in_publish_time:
            self.publish_time += data
        if self.in_paragraph and self.in_js_content:
            self.current_para.append(data)
        if self.in_js_content and not self.in_paragraph:
            # 记录所有可见文字
            text = data.strip()
            if text:
                self.paragraphs.append(text)

    def handle_entityref(self, name):
        if self.in_paragraph and self.in_js_content:
            self.current_para.append(f'&{name};')

    def handle_charref(self, name):
        if self.in_paragraph and self.in_js_content:
            self.current_para.append(f'&#{name};')


with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8', errors='replace')

# 提取 meta 信息
title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', text)
desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', text)
cover_match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', text)
pub_match = re.search(r'var\s+publish_time\s*=\s*["\']?(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2})', text)
account_match = re.search(r'var\s+nickname\s*=\s*["\']([^"\']+)["\']', text)
author_match = re.search(r'var\s+author\s*=\s*["\']([^"\']+)["\']', text)
biz_match = re.search(r'var\s+__biz\s*=\s*["\']([^"\']+)["\']', text)

# 提取 js_content 范围
js_start = text.find('id="js_content"')
if js_start < 0:
    print("No js_content found!")
    exit(1)
# 找到最近的 <div 起始
div_start = text.rfind('<div', 0, js_start)
# 找到 div 结束 - 大致用 </div> 平衡匹配
print(f"id=js_content at: {js_start}, div_start: {div_start}")
print(f"Total length: {len(text)}")

# 用 HTMLParser 解析
parser = ArticleParser()
parser.feed(text)

# 输出结果
result = {
    'title': (title_match.group(1) if title_match else parser.title).strip(),
    'desc': (desc_match.group(1) if desc_match else parser.desc).strip(),
    'cover': (cover_match.group(1) if cover_match else parser.cover).strip(),
    'publish_time': (pub_match.group(1) if pub_match else parser.publish_time).strip(),
    'account_nickname': (account_match.group(1) if account_match else parser.account_nickname).strip(),
    'author': (author_match.group(1) if author_match else parser.author).strip(),
    'biz': (biz_match.group(1) if biz_match else '').strip(),
    'paragraphs_count': len(parser.paragraphs),
    'images_count': len(parser.images),
    'videos_count': len(parser.videos),
    'videos': parser.videos,
    'paragraphs': parser.paragraphs,
    'images': parser.images[:20],
}

with open(r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\parsed.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("=== META ===")
print(f"Title: {result['title']}")
print(f"Author/Account: {result['author'] or result['account_nickname']}")
print(f"Account: {result['account_nickname']}")
print(f"Publish: {result['publish_time']}")
print(f"Cover: {result['cover'][:100]}")
print(f"Paragraphs: {result['paragraphs_count']}, Images: {result['images_count']}, Videos: {result['videos_count']}")
print()
print("=== VIDEOS ===")
for v in result['videos']:
    print(f"  {v['tag']} | src={v['src'][:120]}")
    if v.get('desc'):
        print(f"  desc: {v['desc'][:200]}")
    if v.get('nickname'):
        print(f"  nickname: {v['nickname']}")
print()
print("=== PARAGRAPHS (first 30) ===")
for i, p in enumerate(result['paragraphs'][:30]):
    p_clean = p.replace('\n', ' ').strip()
    if p_clean:
        print(f"  [{i}] {p_clean[:200]}")
