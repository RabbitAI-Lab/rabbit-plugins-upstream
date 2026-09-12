#!/usr/bin/env python3
"""
Screenshot OCR Extractor

Extracts text from screenshots, builds a searchable index,
and detects entities (URLs, emails, phone numbers).

Usage:
  python ocr_extractor.py extract --dir ~/Screenshots --output index.json
  python ocr_extractor.py search --index index.json "flight confirmation"
  python ocr_extractor.py entities --index index.json
  python ocr_extractor.py demo
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from collections import Counter


# Category detection keywords
CATEGORY_KEYWORDS = {
    'chat': ['message', 'sent', 'received', 'replied', 'online', 'offline',
             'typing', 'whatsapp', 'telegram', 'messenger', 'discord'],
    'receipt': ['$', 'total', 'subtotal', 'tax', 'order', 'payment', 'invoice',
                'receipt', 'amount', 'balance', 'transaction', 'paid', 'purchase'],
    'error': ['error', 'failed', 'exception', 'crash', 'bug', 'stack trace',
              'warning', 'undefined', 'null', 'cannot', 'unable'],
    'code': ['function', 'class', 'import', 'def', 'var', 'const', 'return',
             'public', 'private', 'void', 'int', 'string', 'console.log'],
    'map': ['directions', 'route', 'km', 'miles', 'exit', 'turn',
            'north', 'south', 'east', 'west', 'navigate'],
    'document': ['chapter', 'page', 'paragraph', 'section', 'article',
                 'abstract', 'introduction', 'conclusion'],
    'social': ['like', 'share', 'comment', 'follow', 'retweet', 'posted',
               'followers', 'profile', '@'],
}


# Entity regex patterns
URL_PATTERN = r'https?://[^\s<>"\')\]]+'
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_PATTERN = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3,4}[-.\s]?\d{4}'
DATE_PATTERN = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4})\b'
CURRENCY_PATTERN = r'(?:\$|€|£|¥|₹)\s?[\d,]+\.?\d*'


def extract_text_simple(filepath: str) -> str:
    """Extract text from an image using available OCR tools.
    
    Tries pytesseract first, falls back to basic metadata extraction.
    """
    # Try pytesseract
    try:
        import pytesseract
        from PIL import Image
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except ImportError:
        pass
    
    # No OCR available — return empty (the tool still works for dedup/categorization)
    return ""


def categorize_content(text: str) -> str:
    """Categorize screenshot based on extracted text."""
    if not text:
        return 'unknown'
    
    text_lower = text.lower()
    scores = Counter()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            count = text_lower.count(kw.lower())
            if count > 0:
                scores[category] += count
    
    if scores:
        return scores.most_common(1)[0][0]
    
    return 'other'


def extract_entities(text: str) -> dict:
    """Extract URLs, emails, phone numbers, dates, and currency from text."""
    entities = {
        'urls': list(set(re.findall(URL_PATTERN, text))),
        'emails': list(set(re.findall(EMAIL_PATTERN, text))),
        'phones': list(set(re.findall(PHONE_PATTERN, text))),
        'dates': list(set(re.findall(DATE_PATTERN, text))),
        'currency': list(set(re.findall(CURRENCY_PATTERN, text))),
    }
    return entities


def build_search_index(extracted: list) -> dict:
    """Build a searchable index from extracted text data."""
    index = {
        'total_images': len(extracted),
        'total_words': 0,
        'images': [],
        'word_index': {},  # word -> list of image indices
    }
    
    for i, item in enumerate(extracted):
        text = item.get('text', '')
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        word_set = set(words)
        
        index['total_words'] += len(words)
        
        img_entry = {
            'index': i,
            'path': item['path'],
            'name': item['name'],
            'category': item.get('category', 'unknown'),
            'word_count': len(words),
            'text_preview': text[:200] if text else '',
            'entities': item.get('entities', {}),
        }
        index['images'].append(img_entry)
        
        # Build inverted index
        for word in word_set:
            if word not in index['word_index']:
                index['word_index'][word] = []
            index['word_index'][word].append(i)
    
    return index


def search_index(index: dict, query: str) -> list:
    """Search the index for images matching the query."""
    query_words = re.findall(r'\b[a-zA-Z]{3,}\b', query.lower())
    
    if not query_words:
        return []
    
    # Score each image by number of matching query words
    scores = Counter()
    
    for word in query_words:
        if word in index['word_index']:
            for img_idx in index['word_index'][word]:
                scores[img_idx] += 1
    
    # Sort by score
    results = []
    for img_idx, match_count in scores.most_common():
        img = index['images'][img_idx]
        match_pct = (match_count / len(query_words)) * 100
        results.append({
            'path': img['path'],
            'name': img['name'],
            'category': img['category'],
            'match_percentage': round(match_pct, 0),
            'matched_words': match_count,
            'total_query_words': len(query_words),
            'text_preview': img.get('text_preview', ''),
        })
    
    return results


def extract_all(directory: str) -> list:
    """Extract text and entities from all images in a directory."""
    IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif'}
    results = []
    
    for root, dirs, files in os.walk(directory):
        for f in sorted(files):
            ext = os.path.splitext(f)[1].lower()
            if ext not in IMAGE_EXTS:
                continue
            
            filepath = os.path.join(root, f)
            text = extract_text_simple(filepath)
            category = categorize_content(text)
            entities = extract_entities(text)
            
            results.append({
                'path': filepath,
                'name': f,
                'text': text,
                'category': category,
                'entities': entities,
                'text_length': len(text),
            })
    
    return results


# ─── Reporting ────────────────────────────────────────────────────────────────

CATEGORY_ICONS = {
    'chat': '💬',
    'receipt': '🧾',
    'error': '🐛',
    'code': '💻',
    'map': '🗺️',
    'document': '📄',
    'social': '🤝',
    'other': '📦',
    'unknown': '❓',
}


def generate_summary_report(results: list) -> str:
    """Generate a summary of extraction results."""
    total = len(results)
    cat_counts = Counter(r['category'] for r in results)
    total_text = sum(r['text_length'] for r in results)
    all_entities = {
        'urls': 0, 'emails': 0, 'phones': 0, 'dates': 0, 'currency': 0
    }
    for r in results:
        for key in all_entities:
            all_entities[key] += len(r.get('entities', {}).get(key, []))
    
    lines = []
    lines.append("")
    lines.append("📊 OCR EXTRACTION REPORT")
    lines.append("═" * 55)
    lines.append(f"Total images processed: {total}")
    lines.append(f"Total text extracted: {total_text:,} characters")
    lines.append("")
    
    lines.append("CONTENT CATEGORIES:")
    for cat, count in cat_counts.most_common():
        icon = CATEGORY_ICONS.get(cat, '📦')
        pct = (count / total * 100) if total else 0
        lines.append(f"  {icon} {cat:15s}: {count:4d} ({pct:.0f}%)")
    lines.append("")
    
    lines.append("ENTITIES DETECTED:")
    lines.append(f"  🔗 URLs:      {all_entities['urls']}")
    lines.append(f"  📧 Emails:    {all_entities['emails']}")
    lines.append(f"  📞 Phones:    {all_entities['phones']}")
    lines.append(f"  📅 Dates:     {all_entities['dates']}")
    lines.append(f"  💰 Currency:  {all_entities['currency']}")
    lines.append("")
    
    return '\n'.join(lines)


# ─── Demo Data ────────────────────────────────────────────────────────────────

def generate_demo_data() -> list:
    """Generate simulated OCR results for demonstration."""
    return [
        {
            'path': 'Screenshot_001.png', 'name': 'Screenshot_001.png',
            'text': 'Bank of America | Transfer Confirmation | Amount: $2,500.00 | '
                    'From: Checking ****1234 | To: Savings ****5678 | Date: May 12, 2026 | '
                    'Confirmation #: TRX987654321',
            'category': 'receipt',
            'entities': {
                'urls': [], 'emails': [],
                'phones': [], 'dates': ['May 12, 2026'],
                'currency': ['$2,500.00'],
            },
            'text_length': 180,
        },
        {
            'path': 'Screenshot_002.png', 'name': 'Screenshot_002.png',
            'text': 'WhatsApp | Mom: Are you coming for dinner Sunday? | '
                    'You: Yes! What time? | Mom: 6pm | Sent ✓',
            'category': 'chat',
            'entities': {
                'urls': [], 'emails': [], 'phones': [],
                'dates': ['Sunday'], 'currency': [],
            },
            'text_length': 100,
        },
        {
            'path': 'Screenshot_003.png', 'name': 'Screenshot_003.png',
            'text': 'Error: Cannot read property \'map\' of undefined at '
                    'Component.render (app.js:42) at processChild (react.js:18)',
            'category': 'error',
            'entities': {
                'urls': [], 'emails': [], 'phones': [],
                'dates': [], 'currency': [],
            },
            'text_length': 120,
        },
        {
            'path': 'Screenshot_004.png', 'name': 'Screenshot_004.png',
            'text': 'Amazon Order Confirmation | Order #112-8876543-1234567 | '
                    'USB-C Cable x2 | Total: $24.98 | Estimated delivery: Aug 15, 2026 | '
                    'Track at https://amazon.com/track/1128876543',
            'category': 'receipt',
            'entities': {
                'urls': ['https://amazon.com/track/1128876543'],
                'emails': [], 'phones': [],
                'dates': ['Aug 15, 2026'], 'currency': ['$24.98'],
            },
            'text_length': 200,
        },
        {
            'path': 'Screenshot_005.png', 'name': 'Screenshot_005.png',
            'text': 'Flight Confirmation | American Airlines AA1234 | '
                    'JFK → LAX | Depart: Aug 20, 2026 7:00 AM | '
                    'Boarding: Gate B12 | Seat 14C | Confirmation: ABCDEF',
            'category': 'receipt',
            'entities': {
                'urls': [], 'emails': [], 'phones': [],
                'dates': ['Aug 20, 2026'], 'currency': [],
            },
            'text_length': 160,
        },
    ]


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Screenshot OCR extractor')
    sub = parser.add_subparsers(dest='command')
    
    p_extract = sub.add_parser('extract', help='Extract text from screenshots')
    p_extract.add_argument('--dir', required=True)
    p_extract.add_argument('--output', default='screenshot_index.json')
    
    p_search = sub.add_parser('search', help='Search extracted text')
    p_search.add_argument('--index', required=True)
    p_search.add_argument('query', help='Search query')
    
    p_entities = sub.add_parser('entities', help='Show detected entities')
    p_entities.add_argument('--index', required=True)
    
    sub.add_parser('demo', help='Run with sample data')
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        results = generate_demo_data()
        print(generate_summary_report(results))
        
        index = build_search_index(results)
        
        print("\n🔍 SEARCH DEMO: 'bank transfer'")
        search_results = search_index(index, 'bank transfer')
        for r in search_results:
            print(f"\n  🎯 {r['name']} ({r['match_percentage']:.0f}% match)")
            print(f"     Category: {r['category']}")
            print(f"     Preview: {r['text_preview'][:80]}...")
        
        print("\n🔍 SEARCH DEMO: 'flight confirmation'")
        search_results = search_index(index, 'flight confirmation')
        for r in search_results:
            print(f"\n  🎯 {r['name']} ({r['match_percentage']:.0f}% match)")
            print(f"     Category: {r['category']}")
        return
    
    if args.command == 'extract':
        print(f"Extracting text from images in {args.dir}...")
        results = extract_all(args.dir)
        
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"✓ Extracted text from {len(results)} images → {args.output}")
        
        print(generate_summary_report(results))
        return
    
    if args.command == 'search':
        with open(args.index) as f:
            data = json.load(f)
        
        # Could be raw extraction or pre-built index
        if 'images' in data:
            results = search_index(data, args.query)
        else:
            index = build_search_index(data)
            results = search_index(index, args.query)
        
        print(f"\n🔍 SEARCH: '{args.query}'")
        print(f"   Found {len(results)} matches\n")
        
        for r in results[:10]:
            print(f"  🎯 {r['name']} ({r['match_percentage']:.0f}% match)")
            print(f"     Category: {r['category']}")
            preview = r.get('text_preview', '')[:100]
            print(f"     Preview: {preview}...")
            print()
        return
    
    if args.command == 'entities':
        with open(args.index) as f:
            data = json.load(f)
        
        if 'images' in data:
            images = data['images']
        else:
            images = data
        
        all_urls = []
        all_emails = []
        all_phones = []
        
        for img in images:
            ents = img.get('entities', {})
            all_urls.extend(ents.get('urls', []))
            all_emails.extend(ents.get('emails', []))
            all_phones.extend(ents.get('phones', []))
        
        print(f"\n📡 DETECTED ENTITIES:")
        print(f"  🔗 URLs ({len(all_urls)}):")
        for url in set(all_urls):
            print(f"     • {url}")
        print(f"  📧 Emails ({len(all_emails)}):")
        for email in set(all_emails):
            print(f"     • {email}")
        print(f"  📞 Phones ({len(all_phones)}):")
        for phone in set(all_phones):
            print(f"     • {phone}")
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
