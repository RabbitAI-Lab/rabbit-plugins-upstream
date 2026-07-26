#!/usr/bin/env python3
"""
Sync newsletter markdown to Ghost as a draft post.
Downloads images, uploads them to Ghost, and creates a Lexical-format post.
"""

import re
import json
import os
import sys
import subprocess
import tempfile
import requests
from pathlib import Path
from urllib.parse import urlparse

# Configuration
MARKDOWN_FILE = "cache/newsletter_markdown_1.md"
GHST_BIN = "./node_modules/.bin/ghst"
GHOST_IMAGE_UPLOAD_CMD = [GHST_BIN, "image", "upload", "--json"]
GHOST_POST_CREATE_CMD = [GHST_BIN, "post", "create", "--json"]

def find_existing_post_by_title(title):
    """Check if a post with similar title already exists in Ghost."""
    try:
        # Use NQL filter to search for posts with similar title
        # The ~ operator does a partial match
        result = subprocess.run(
            [GHST_BIN, "post", "list", "--filter", f"title:~'{title[:30]}'", "--json"],
            capture_output=True,
            text=True,
            check=True
        )
        
        data = json.loads(result.stdout)
        if 'posts' in data and len(data['posts']) > 0:
            # Check for exact or near-exact match
            for post in data['posts']:
                existing_title = post.get('title', '')
                # Normalize both titles for comparison (lowercase, strip emoji)
                normalized_existing = re.sub(r'[^\w\s]', '', existing_title.lower())
                normalized_new = re.sub(r'[^\w\s]', '', title.lower())
                
                # If titles are very similar (80% match threshold)
                if normalized_existing == normalized_new or \
                   (len(normalized_existing) > 0 and 
                    len(normalized_new) > 0 and 
                    (normalized_existing in normalized_new or normalized_new in normalized_existing)):
                    return post
        
        return None
    except subprocess.CalledProcessError:
        return None
    except json.JSONDecodeError:
        return None

def extract_title_and_content(md_path):
    """Extract title (first # heading) and content from markdown."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    title = None
    body_lines = []
    
    for line in lines:
        if title is None and line.startswith('# '):
            title = line[2:].strip()
        else:
            body_lines.append(line)
    
    if not title:
        title = "Newsletter Post"
    
    body = '\n'.join(body_lines).strip()
    return title, body

def extract_image_urls(markdown):
    """Extract all image URLs from markdown."""
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, markdown)
    return [(alt, url) for alt, url in matches]

def download_image(url, temp_dir):
    """Download an image to a temporary file."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Determine extension from URL or content-type
        parsed = urlparse(url)
        path = parsed.path
        ext = Path(path).suffix
        if not ext:
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            elif 'webp' in content_type:
                ext = '.webp'
            else:
                ext = '.jpg'
        
        # Create safe filename
        filename = f"image_{hash(url) % 10000:04d}{ext}"
        filepath = os.path.join(temp_dir, filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return filepath
    except Exception as e:
        print(f"Failed to download {url}: {e}", file=sys.stderr)
        return None

def upload_image_to_ghost(image_path):
    """Upload an image to Ghost and return the new URL."""
    try:
        result = subprocess.run(
            GHOST_IMAGE_UPLOAD_CMD + [image_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the JSON response
        data = json.loads(result.stdout)
        
        # Extract the image URL from response
        # Response structure: {"images": [{"images": [{"url": "..."}]}]}
        if 'images' in data and len(data['images']) > 0:
            first_image = data['images'][0]
            if 'images' in first_image and len(first_image['images']) > 0:
                return first_image['images'][0].get('url')
        return None
    except subprocess.CalledProcessError as e:
        print(f"Failed to upload {image_path}: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse upload response: {e}", file=sys.stderr)
        return None

def markdown_to_lexical(markdown, image_url_map):
    """Convert markdown to Ghost Lexical JSON format."""
    
    # Replace image URLs in markdown first
    for old_url, new_url in image_url_map.items():
        markdown = markdown.replace(old_url, new_url)
    
    # Split into lines and process
    lines = markdown.split('\n')
    nodes = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
        
        # Headings
        if line.startswith('### '):
            nodes.append(create_heading_node(line[4:], 3))
        elif line.startswith('## '):
            nodes.append(create_heading_node(line[3:], 2))
        elif line.startswith('# '):
            # Skip H1 - it's the title
            pass
        # Images (standalone)
        elif line.startswith('!['):
            match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if match:
                alt, url = match.groups()
                nodes.append(create_image_node(url, alt))
        # Linked images: [![alt](image-url)](link-url)
        elif line.startswith('[!'):
            # Match the pattern [![alt](image)](link)
            match = re.match(r'\[!\[([^\]]*)\]\(([^)]+)\)\]\(([^)]+)\)', line)
            if match:
                alt, img_url, link_url = match.groups()
                # Create an image node with href for click-through linking
                # Ghost image cards support href directly; nesting image inside link is invalid
                nodes.append(create_image_node(img_url, alt, href=link_url))
        # Button pattern: [button: text](url)
        elif line.strip().startswith('[button:'):
            match = re.match(r'\[button:\s*([^\]]+)\]\(([^)]+)\)', line.strip())
            if match:
                button_text, button_url = match.groups()
                nodes.append(create_button_node(button_text.strip(), button_url.strip()))
                i += 1
                continue
        # Horizontal rule
        elif line.strip() == '---':
            nodes.append(create_horizontal_rule_node())
        # Blockquote
        elif line.startswith('> '):
            quote_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                quote_lines.append(lines[i][2:])
                i += 1
            nodes.append(create_quote_node('\n'.join(quote_lines)))
            continue
        # Regular paragraph
        else:
            # Collect consecutive non-empty lines as a paragraph
            # Preserve newlines between lines (for <br> style breaks)
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '!', '>', '---', '- ')):
                para_lines.append(lines[i])
                i += 1
            # Join with newlines to preserve line breaks within paragraph
            para_text = '\n'.join(para_lines)
            nodes.append(create_paragraph_node(para_text))
            continue
        
        i += 1
    
    # Build the Lexical root
    lexical = {
        "root": {
            "children": nodes,
            "direction": None,
            "format": "",
            "indent": 0,
            "type": "root",
            "version": 1
        }
    }
    
    return lexical

def create_button_node(text, url, alignment="center"):
    """Create a Ghost Lexical button node.
    
    Args:
        text: Button label text
        url: Button destination URL
        alignment: Button alignment ("center", "left", or "right"). Default is "center".
    
    Returns:
        Dict representing a Ghost Lexical button node.
    """
    return {
        "type": "button",
        "version": 1,
        "buttonText": text,
        "alignment": alignment,
        "buttonUrl": url
    }

def create_paragraph_node(text):
    """Create a Lexical paragraph node with inline formatting."""
    children = parse_inline_formatting(text)
    return {
        "children": children,
        "direction": None,
        "format": "",
        "indent": 0,
        "type": "paragraph",
        "version": 1
    }

def parse_inline_formatting(text):
    """Parse bold, italic, and link markdown into Lexical format nodes."""
    children = []
    
    # First, handle links - they need special link nodes
    # Pattern: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    # Split text by links first
    parts = []
    last_end = 0
    for match in re.finditer(link_pattern, text):
        # Add text before link
        if match.start() > last_end:
            parts.append({'type': 'text', 'content': text[last_end:match.start()]})
        
        # Add link
        link_text = match.group(1)
        link_url = match.group(2)
        parts.append({'type': 'link', 'content': link_text, 'url': link_url})
        
        last_end = match.end()
    
    # Add remaining text after last link
    if last_end < len(text):
        parts.append({'type': 'text', 'content': text[last_end:]})
    
    # If no links found, treat entire text as single text part
    if not parts:
        parts = [{'type': 'text', 'content': text}]
    
    # Now process each part for bold/italic
    final_parts = []
    
    # Patterns for bold and italic
    format_patterns = [
        (r'\*\*\*(.+?)\*\*\*', 'bold', 'italic'),  # Bold + italic
        (r'\*\*(.+?)\*\*', 'bold'),
        (r'\*(.+?)\*', 'italic'),
        (r'___(.+?)___', 'bold', 'italic'),
        (r'__(.+?)__', 'bold'),
        (r'_(.+?)_', 'italic'),
    ]
    
    for part in parts:
        if part['type'] == 'link':
            # Process link text for bold/italic
            link_children = process_formatting(part['content'], format_patterns)
            final_parts.append({
                'type': 'link',
                'url': part['url'],
                'children': link_children
            })
        else:
            # Process text for bold/italic
            text_children = process_formatting(part['content'], format_patterns)
            final_parts.extend(text_children)
    
    # Convert to Lexical nodes
    for part in final_parts:
        if part.get('type') == 'link':
            # Create link node
            children.append({
                "children": part['children'],
                "direction": None,
                "format": "",
                "indent": 0,
                "type": "link",
                "url": part['url'],
                "version": 1
            })
        else:
            children.append(part)
    
    # If no children, add empty text node
    if not children:
        children.append({
            "detail": 0,
            "format": 0,
            "mode": "normal",
            "style": "",
            "text": "",
            "type": "text",
            "version": 1
        })
    
    return children

def process_formatting(text, patterns):
    """Process bold/italic formatting and return list of text nodes."""
    if not text:
        return []
    
    # First, split by newlines to handle line breaks
    lines = text.split('\n')
    all_children = []
    
    for line_idx, line in enumerate(lines):
        if line_idx > 0:
            # Add linebreak node between lines
            all_children.append({
                "type": "linebreak",
                "version": 1
            })
        
        if not line:
            continue
        
        # Process formatting for this line
        parts = [{'text': line, 'format': 0}]
        
        for pattern, *formats in patterns:
            new_parts = []
            for part in parts:
                if part.get('type'):  # Already a formatted node
                    new_parts.append(part)
                    continue
                
                current_text = part['text']
                matches = list(re.finditer(pattern, current_text))
                
                if not matches:
                    new_parts.append(part)
                    continue
                
                last_end = 0
                for match in matches:
                    # Add text before match
                    if match.start() > last_end:
                        new_parts.append({'text': current_text[last_end:match.start()], 'format': part['format']})
                    
                    # Add formatted text
                    format_val = 0
                    if 'bold' in formats:
                        format_val |= 1
                    if 'italic' in formats:
                        format_val |= 2
                    
                    new_parts.append({'text': match.group(1), 'format': format_val, 'type': 'formatted'})
                    last_end = match.end()
                
                # Add remaining text
                if last_end < len(current_text):
                    new_parts.append({'text': current_text[last_end:], 'format': part['format']})
            
            parts = new_parts
        
        # Convert to Lexical text nodes
        for part in parts:
            node = {
                "detail": 0,
                "format": part.get('format', 0),
                "mode": "normal",
                "style": "",
                "text": part['text'],
                "type": "text",
                "version": 1
            }
            all_children.append(node)
    
    return all_children

def create_heading_node(text, level):
    """Create a Lexical heading node."""
    tag = f"h{level}"
    return {
        "children": parse_inline_formatting(text),
        "direction": None,
        "format": "",
        "indent": 0,
        "tag": tag,
        "type": "heading",
        "version": 1
    }

def create_image_node(src, alt, href=""):
    """Create a Lexical image node.
    
    Args:
        src: Image source URL
        alt: Alt text for the image
        href: Optional click-through URL for the image
    
    Returns:
        Dict representing a Ghost Lexical image card node.
    """
    return {
        "type": "image",
        "version": 1,
        "src": src,
        "width": None,
        "height": None,
        "title": "",
        "alt": alt or "",
        "caption": "",
        "cardWidth": "regular",
        "href": href or ""
    }

def create_horizontal_rule_node():
    """Create a Lexical horizontal rule node."""
    return {
        "type": "horizontalrule",
        "version": 1
    }

def create_quote_node(text):
    """Create a Lexical quote node."""
    return {
        "children": [create_paragraph_node(text)],
        "direction": None,
        "format": "",
        "indent": 0,
        "type": "quote",
        "version": 1
    }

def create_ghost_post(title, lexical_data, tags=None):
    """Create a Ghost post as draft using ghst CLI."""
    
    # Convert lexical to JSON string
    lexical_json = json.dumps(lexical_data)
    
    # Build command
    cmd = [
        GHST_BIN, "post", "create",
        "--title", title,
        "--status", "draft",
        "--json"
    ]
    
    if tags:
        cmd.extend(["--tags", ",".join(tags)])
    
    # Write lexical to temp file and use --lexical-file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write(lexical_json)
        lexical_file = f.name
    
    try:
        cmd.extend(["--lexical-file", lexical_file])
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create post: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse create response: {e}", file=sys.stderr)
        return None
    finally:
        os.unlink(lexical_file)


def update_ghost_post(post_id, title, lexical_data, tags=None):
    """Update an existing Ghost post using ghst CLI."""
    
    # Convert lexical to JSON string
    lexical_json = json.dumps(lexical_data)
    
    # Build command
    cmd = [
        GHST_BIN, "post", "update", post_id,
        "--title", title,
        "--json"
    ]
    
    if tags:
        cmd.extend(["--tags", ",".join(tags)])
    
    # Write lexical to temp file and use --lexical-file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write(lexical_json)
        lexical_file = f.name
    
    try:
        cmd.extend(["--lexical-file", lexical_file])
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to update post: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse update response: {e}", file=sys.stderr)
        return None
    finally:
        os.unlink(lexical_file)

def main():
    # Check for flags
    force_flag = '--force' in sys.argv
    update_flag = '--update' in sys.argv
    
    # Check if markdown file exists
    if not os.path.exists(MARKDOWN_FILE):
        print(f"Error: {MARKDOWN_FILE} not found. Run fetch_markdown.py first.", file=sys.stderr)
        sys.exit(1)
    
    # Extract title and content
    title, markdown = extract_title_and_content(MARKDOWN_FILE)
    print(f"Title: {title}")
    print(f"Content length: {len(markdown)} chars")
    
    # Check for existing post with similar title
    print("Checking for existing posts...")
    existing = find_existing_post_by_title(title)
    
    if existing:
        existing_id = existing.get('id')
        print(f"\n⚠️  A post with this title already exists!")
        print(f"   ID: {existing_id}")
        print(f"   Title: {existing.get('title')}")
        print(f"   Status: {existing.get('status')}")
        print(f"   Created: {existing.get('created_at')}")
        
        if update_flag:
            print(f"\n   --update flag detected, updating existing post...")
        elif force_flag:
            print(f"\n   --force flag detected, creating duplicate anyway...")
        else:
            print(f"\n   Use --update to update the existing post, or --force to create a duplicate.")
            sys.exit(1)
    
    # Find all images
    images = extract_image_urls(markdown)
    print(f"Found {len(images)} images")
    
    # Download and upload images
    image_url_map = {}
    
    if images:
        with tempfile.TemporaryDirectory() as temp_dir:
            for alt, url in images:
                print(f"Downloading: {url[:60]}...")
                local_path = download_image(url, temp_dir)
                
                if local_path:
                    print(f"Uploading to Ghost...")
                    new_url = upload_image_to_ghost(local_path)
                    
                    if new_url:
                        print(f"Uploaded: {new_url}")
                        image_url_map[url] = new_url
                    else:
                        print(f"Failed to upload, keeping original URL")
                else:
                    print(f"Failed to download, keeping original URL")
    
    # Convert to Lexical
    print("Converting to Lexical format...")
    lexical = markdown_to_lexical(markdown, image_url_map)
    
    if update_flag and existing:
        # Update existing post
        print(f"Updating Ghost post {existing_id}...")
        result = update_ghost_post(existing_id, title, lexical, tags=["newsletter"])
        
        if result:
            print(f"\n✅ Success! Post updated.")
            if 'posts' in result and len(result['posts']) > 0:
                post = result['posts'][0]
                print(f"   ID: {post.get('id')}")
                print(f"   Slug: {post.get('slug')}")
                print(f"   URL: {post.get('url')}")
        else:
            print("\n❌ Failed to update post", file=sys.stderr)
            sys.exit(1)
    else:
        # Create Ghost post as draft
        print("Creating Ghost post as draft...")
        result = create_ghost_post(title, lexical, tags=["newsletter"])
        
        if result:
            print(f"\n✅ Success! Post created as draft.")
            if 'posts' in result and len(result['posts']) > 0:
                post = result['posts'][0]
                print(f"   ID: {post.get('id')}")
                print(f"   Slug: {post.get('slug')}")
                print(f"   URL: {post.get('url')}")
        else:
            print("\n❌ Failed to create post", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
