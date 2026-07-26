#!/usr/bin/env python3
"""Generate a Table of Contents from Markdown headings."""

import argparse
import re
import sys
import unicodedata


def slugify(text):
    """Convert heading text to an anchor slug (GitHub/CommonMark compatible)."""
    # Normalize Unicode (NFD) and strip combining marks for accented chars
    slug = unicodedata.normalize('NFD', text)
    slug = ''.join(c for c in slug if unicodedata.category(c) != 'Mn')
    # Lowercase
    slug = slug.lower()
    # Replace spaces/colons with hyphens
    slug = re.sub(r'[\s:]+', '-', slug)
    # Strip remaining punctuation except hyphens and underscores
    slug = re.sub(r'[^a-z0-9\-_]', '', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    # Strip leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def extract_headings(content):
    """Extract (level, text) pairs from Markdown headings in order."""
    pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    headings = []
    for match in pattern.finditer(content):
        level = len(match.group(1))
        text = match.group(2).strip()
        # Strip any trailing # (e.g. "Section ##" at end of line)
        text = re.sub(r'\s*#+\s*$', '', text)
        headings.append((level, text))
    return headings


def build_toc(headings, ordered=False, min_level=1, flat=False):
    """Build TOC string from list of (level, text) pairs."""
    if not headings:
        return ""

    # Filter by min_level first
    filtered = [(l, t) for l, t in headings if l >= min_level]
    if not filtered:
        return ""

    lines = []
    counters = {}  # level -> counter

    for level, text in filtered:
        if flat:
            indent = 0
        else:
            indent = level - min_level

        spaces = '  ' * indent
        anchor = slugify(text)

        if ordered:
            # Reset counters at or below current level (start fresh at this level)
            counters = {k: v for k, v in counters.items() if k < level}
            counters[level] = counters.get(level, 0) + 1
            # Include all ancestor counters for full hierarchical number
            parts = [str(counters[l]) for l in range(min_level, level + 1)]
            number = '.'.join(parts)
            lines.append(f'{spaces}{number}. [{text}](#{anchor})')
        else:
            lines.append(f'{spaces}- [{text}](#{anchor})')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate a Table of Contents from Markdown headings.'
    )
    parser.add_argument('file', help='Path to Markdown file')
    parser.add_argument('--ol', action='store_true', help='Ordered list (1. 2. 3.)')
    parser.add_argument('--min', type=int, default=1, metavar='N',
                        help='Minimum heading level to include (default: 1)')
    parser.add_argument('--flat', action='store_true',
                        help='No indentation, flat list')
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Error: file not found: {args.file}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'Error reading file: {e}', file=sys.stderr)
        sys.exit(1)

    headings = extract_headings(content)
    if not headings:
        print('No headings found.', file=sys.stderr)
        sys.exit(1)

    toc = build_toc(headings, ordered=args.ol, min_level=args.min, flat=args.flat)
    print(toc)


if __name__ == '__main__':
    main()
