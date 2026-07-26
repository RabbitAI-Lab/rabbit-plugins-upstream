from bs4 import BeautifulSoup, Comment
import requests
import feedparser
import re
from markdownify import MarkdownConverter

OUTPUT_FILENAME_PREFIX = "cache/newsletter_markdown_"

class ImageFilterConverter(MarkdownConverter):
    """Custom converter to filter out social icons and spacers, preserve image links."""
    
    def convert_img(self, el, text, **kwargs):
        src = el.get('src', '')
        alt = el.get('alt', '')
        
        # Filter out social icons and known boilerplate images
        ignore_patterns = [
            'social-block', 'facebook', 'instagram', 'twitter', 
            'tiktok', 'website', 'linkedin', 'pinterest',
            'icons-v3', 'mailchimp.com/icons'
        ]
        if any(p in src.lower() for p in ignore_patterns) or any(p in alt.lower() for p in ignore_patterns):
            return ''
            
        # Filter out tiny spacers/dots
        # Real animated GIFs (like the sign-off) are typically larger than spacers
        width = el.get('width', '')
        if width:
            try:
                # Handle cases like "361.08"
                if int(float(width)) < 50:
                    return ''
            except ValueError:
                pass
        
        # Check if image had a link parent (marked before unwrapping)
        # or is currently wrapped in a link
        href = el.get('data-link-href', '')
        if not href:
            parent_a = el.find_parent('a')
            if parent_a:
                href = parent_a.get('href', '')
        
        if href:
            # Clean up tracking URLs
            href = re.sub(r'\?e=\[UNIQID\]', '', href)
            if href:
                return f'[![{alt}]({src})]({href})'
        
        return super().convert_img(el, text, **kwargs)
    
    def convert_a(self, el, text, **kwargs):
        """Convert links, handling button-styled links specially."""
        href = el.get('href', '')
        if not href:
            return text
        
        # Clean up tracking URLs
        href = re.sub(r'\?e=\[UNIQID\]', '', href)
        
        # Check if this is a button-styled link
        # Mailchimp buttons have specific class patterns
        parent_classes = []
        parent = el.parent
        while parent and parent.name:
            parent_classes.extend(parent.get('class', []) if isinstance(parent.get('class', []), list) else [parent.get('class', '')])
            parent = parent.parent
        
        parent_class_str = ' '.join(parent_classes).lower()
        is_button = 'mcebutton' in parent_class_str or 'button' in parent_class_str
        
        # If it's a button with meaningful text, format it prominently
        if is_button and text and len(text.strip()) > 0:
            # Use special button pattern that sync_to_ghost.py will convert to Lexical button nodes
            return f'[button: {text}]({href})'
        
        return super().convert_a(el, text, **kwargs)



def md_clean(html, **options):
    return ImageFilterConverter(**options).convert(html)

def purge_invisible_chars(text):
    invisible_chars = re.compile(r'[\u200b-\u200f\ufeff\xad\x80-\x9f]')
    text = invisible_chars.sub('', text)
    text = re.sub(r'[\u034f\u180e\u202a-\u202e\u2060-\u206f]', '', text)
    return text

import os

def process_entry(entry):
    """Processes a single RSS entry into clean markdown."""
    title = entry.title
    raw_html = entry.get('summary', '') or entry.get('description', '')
    
    # Remove all HTML comments (including Mailchimp's conditional blocks)
    raw_html = re.sub(r'<!--.*?-->', '', raw_html, flags=re.DOTALL)

    soup = BeautifulSoup(raw_html, 'lxml')
    
    # 1. CLEANUP
    for tag in ['style', 'script', 'head', 'meta', 'link']:
        for match in soup.find_all(tag):
            match.decompose()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for preview in soup.find_all(class_=re.compile(r'PreviewText|mcnPreviewText')):
        preview.decompose()
    
    for hidden in soup.find_all(style=re.compile(r'display:\s*none')):
        hidden.decompose()

    # 2. EXTRACTION
    # Include text, image, divider, and button containers
    # Note: Only match mceDividerBlockContainer (not mceDividerBlock) to avoid nested duplicates
    potential_blocks = soup.find_all(['div', 'td'], class_=re.compile(r'mceText|mceImageBlockContainer|mceDividerBlockContainer|mceButtonBlockContainer'))
    content_blocks = []
    for block in potential_blocks:
        # Avoid nested blocks
        if any(parent in potential_blocks for parent in block.parents):
            continue
        content_blocks.append(block)
    
    all_paragraphs = []
    ignore_list = [
        "View this email", "unsubscribe", "update subscription", 
        "forward to a friend", "Copyright", "Rewards", 
        "sent this email", "Add us to your address book",
        "Our mailing address is", "Want to change how you receive",
        "Grow your business with Mailchimp"
    ]

    for block in content_blocks:
        # Check if this is a divider block
        block_classes = block.get('class', [])
        if isinstance(block_classes, str):
            block_classes = [block_classes]
        if any('mceDividerBlockContainer' in cls or 'mceDividerBlock' in cls for cls in block_classes):
            # Add horizontal rule for divider blocks
            all_paragraphs.append("---")
            continue
        
        # Check if this is a button block - handle specially to preserve links
        is_button_block = any('mceButton' in cls for cls in block_classes)
        
        if is_button_block:
            # For button blocks, find the actual link and text
            button_link = block.find('a', class_=re.compile(r'mceButtonLink'))
            if not button_link:
                button_link = block.find('a')  # fallback to any link
            
            if button_link:
                href = button_link.get('href', '')
                # Clean up tracking URLs
                href = re.sub(r'\?e=\[UNIQID\]', '', href)
                text = button_link.get_text(strip=True)
                if text and href:
                    # Use special button pattern that sync_to_ghost.py will convert to Lexical button nodes
                    all_paragraphs.append(f"[button: {text}]({href})")
                    continue
        
        # Before converting, we "unwrap" the block to remove table/div noise but keep content
        # First, handle Mailchimp's conditional comment structure where <a> and <table> are siblings
        # The pattern is: <a href="..."></a><table>...</table> due to Outlook conditional comments
        link_wrapped_images = {}
        
        # Find all <a> tags in the block
        for a_tag in block.find_all('a'):
            href = a_tag.get('href', '')
            if not href:
                continue
            
            # Check if this <a> is empty (due to conditional comment parsing)
            # and is immediately followed by a table containing an image
            if not a_tag.find('img'):
                # The <a> is empty, check if next sibling is a table with an image
                next_sibling = a_tag.find_next_sibling()
                if next_sibling and next_sibling.name == 'table':
                    img_in_table = next_sibling.find('img')
                    if img_in_table:
                        src = img_in_table.get('src', '')
                        if src:
                            link_wrapped_images[src] = href
                            img_in_table['data-link-href'] = href
            else:
                # Normal case: <a> contains images
                for img in a_tag.find_all('img'):
                    src = img.get('src', '')
                    if src:
                        link_wrapped_images[src] = href
                        img['data-link-href'] = href
        
        # Unwrap layout tags but preserve <a> tags (they contain important links around images)
        for layout_tag in block.find_all(['table', 'tr', 'td', 'tbody', 'thead', 'div', 'span']):
            # Don't unwrap <a> tags - they contain image links we want to preserve
            if layout_tag.name == 'a':
                continue
            layout_tag.unwrap()
        
        # After unwrapping, check if any images lost their links and restore them
        for img in block.find_all('img'):
            src = img.get('src', '')
            if not img.get('data-link-href') and src in link_wrapped_images:
                img['data-link-href'] = link_wrapped_images[src]
        
        block_html = block.decode_contents()
            
        block_md = md_clean(
            block_html, 
            heading_style="ATX"
        )
        
        lines = block_md.splitlines()
        current_block_lines = []
        
        for line in lines:
            line = purge_invisible_chars(line).strip()
            if not line:
                continue
            
            if any(phrase.lower() in line.lower() for phrase in ignore_list):
                continue
            
            current_block_lines.append(line)
        
        if current_block_lines:
            all_paragraphs.append("\n".join(current_block_lines))

    # 3. POST-PROCESSING
    final_paragraphs = []
    seen = set()
    img_count = 0
    heading_count = 0
    
    for p in all_paragraphs:
        p = p.strip()
        if not p:
            continue
        
        # Keep horizontal rules early (before dedup logic)
        if p == '---':
            final_paragraphs.append(p)
            continue
            
        # Count and potentially skip images
        # Standalone images start with !, linked images start with [ followed by !
        if p.startswith('!') or p.startswith('[!'):
            img_count += 1
            if img_count == 1:
                continue
        
        # Count and potentially skip headings (note: title at the top is handled later)
        if p.startswith('#'):
            heading_count += 1
            if heading_count == 1: # This is the first heading encountered in content
                continue
            
        # Dedup based on content, but always keep images (that weren't skipped)
        if not p.startswith('!'):
            norm = re.sub(r'\W+', '', p).lower()
            if not norm or norm in seen:
                continue
            seen.add(norm)
        
        p = p.replace('|', '')
            
        if len(p) < 5 and not p.startswith('#') and not p.startswith('!'):
            continue
            
        final_paragraphs.append(p)

    return f"# {title}\n\n" + "\n\n".join(final_paragraphs)

def rss_to_clean_markdown(rss_url, limit=1):
    # Ensure cache directory exists
    os.makedirs("cache", exist_ok=True)
    cache_file = "cache/feed_cache.xml"
    if os.path.exists(cache_file):
        print(f"Using cached feed from {cache_file}")
        with open(cache_file, "rb") as f:
            content = f.read()
    else:
        print(f"Fetching feed from {rss_url}")
        resp = requests.get(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        content = resp.content
        with open(cache_file, "wb") as f:
            f.write(content)
            
    feed = feedparser.parse(content)
    
    if not feed.entries:
        print("No entries found.")
        return

    # Process entries up to the limit
    for i, entry in enumerate(feed.entries[:limit]):
        markdown = process_entry(entry)
        
        # Determine filename
        filename = OUTPUT_FILENAME_PREFIX + str(i + 1) + ".md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown)
        
        print(f"Entry '{entry.title}' saved to {filename}")

if __name__ == "__main__":
    # Hard code JESSA JOY'S newsletter RSS feed
    RSS_URL = "https://us2.campaign-archive.com/feed?u=984af73050afc815da6f667e6&id=2eccb870f9"
    rss_to_clean_markdown(RSS_URL, limit=1)
