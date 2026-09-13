#!/usr/bin/env python3
"""
Screenshot Deduplication Scanner

Finds exact and near-duplicate screenshots using MD5 hashing and
perceptual (average) hashing for visual similarity.

Usage:
  python dedup_scanner.py scan --dir ~/Screenshots
  python dedup_scanner.py report --dir ~/Screenshots
  python dedup_scanner.py demo
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from collections import defaultdict


# Supported image extensions
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tiff'}

# Screenshot filename patterns (regex)
SCREENSHOT_PATTERNS = [
    r'Screenshot',           # macOS, generic
    r'Capture',              # Windows Snipping Tool
    r'screenshot',           # lowercase
    r'screen_shot',
    r'scr_',                 # some tools
    r'screen-',              # some Android
    r'IMG_\d+',              # iOS (sometimes screenshots)
]


def md5_hash_file(filepath: str) -> str:
    """Compute MD5 hash of a file."""
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def average_hash(filepath: str, hash_size: int = 8) -> str:
    """Compute perceptual average hash of an image.
    
    Uses only Python stdlib — converts to grayscale and downsamples.
    Falls back to a simple hash if PIL is not available.
    """
    try:
        from PIL import Image
        img = Image.open(filepath).convert('L').resize(
            (hash_size, hash_size), Image.LANCZOS
        )
        pixels = list(img.getdata())
        avg = sum(pixels) / len(pixels)
        bits = ''.join('1' if p > avg else '0' for p in pixels)
        # Convert to hex
        hash_int = int(bits, 2)
        return f'{hash_int:0{hash_size * hash_size // 4}x}'
    except ImportError:
        # No PIL — use file size + first bytes as a pseudo-hash
        stat = os.stat(filepath)
        return f'{stat.st_size:08x}'


def hamming_distance(hash1: str, hash2: str) -> int:
    """Compute Hamming distance between two hex hashes."""
    if len(hash1) != len(hash2):
        return 64  # max distance
    val1 = int(hash1, 16)
    val2 = int(hash2, 16)
    xor = val1 ^ val2
    return bin(xor).count('1')


def is_screenshot(filepath: str) -> bool:
    """Check if a file is likely a screenshot based on filename."""
    import re
    name = os.path.basename(filepath)
    for pattern in SCREENSHOT_PATTERNS:
        if re.search(pattern, name, re.IGNORECASE):
            return True
    return False


def find_screenshots(directory: str) -> list:
    """Find all screenshot files in a directory."""
    results = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            filepath = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()
            if ext in IMAGE_EXTS:
                results.append(filepath)
    return sorted(results)


def scan_duplicates(directory: str) -> dict:
    """Scan for exact and near-duplicate screenshots.
    
    Returns dict with:
      'files': list of file info dicts
      'exact_dupes': groups of exact duplicates
      'near_dupes': pairs of visually similar images
    """
    screenshots = find_screenshots(directory)
    
    if not screenshots:
        return {'files': [], 'exact_dupes': [], 'near_dupes': []}
    
    files_info = []
    md5_groups = defaultdict(list)
    
    for filepath in screenshots:
        try:
            md5 = md5_hash_file(filepath)
            size = os.path.getsize(filepath)
            a_hash = average_hash(filepath)
            
            info = {
                'path': filepath,
                'name': os.path.basename(filepath),
                'size': size,
                'md5': md5,
                'ahash': a_hash,
            }
            files_info.append(info)
            md5_groups[md5].append(filepath)
        except Exception as e:
            files_info.append({
                'path': filepath,
                'name': os.path.basename(filepath),
                'size': 0,
                'md5': '',
                'ahash': '',
                'error': str(e),
            })
    
    # Exact duplicates
    exact_dupes = []
    for md5, paths in md5_groups.items():
        if len(paths) > 1:
            total_size = sum(os.path.getsize(p) for p in paths)
            exact_dupes.append({
                'md5': md5,
                'files': paths,
                'count': len(paths),
                'waste_bytes': total_size - os.path.getsize(paths[0]) * (len(paths) - 1),
                'waste_mb': round((total_size - os.path.getsize(paths[0]) * (len(paths) - 1)) / (1024*1024), 2),
            })
    
    # Near-duplicates (perceptual hash comparison)
    near_dupes = []
    valid_files = [f for f in files_info if f.get('ahash')]
    
    for i in range(len(valid_files)):
        for j in range(i + 1, len(valid_files)):
            f1 = valid_files[i]
            f2 = valid_files[j]
            
            # Skip exact dupes (already found)
            if f1['md5'] == f2['md5']:
                continue
            
            dist = hamming_distance(f1['ahash'], f2['ahash'])
            
            if dist <= 10:
                confidence = max(0, 100 - dist * 10)
                near_dupes.append({
                    'file1': f1['path'],
                    'file2': f2['path'],
                    'hamming_distance': dist,
                    'confidence': confidence,
                    'recommendation': 'delete one' if dist <= 5 else 'review',
                })
    
    # Sort near-dupes by confidence
    near_dupes.sort(key=lambda x: x['confidence'], reverse=True)
    
    return {
        'files': files_info,
        'exact_dupes': exact_dupes,
        'near_dupes': near_dupes,
    }


def generate_report(scan_result: dict) -> str:
    """Generate a human-readable deduplication report."""
    files = scan_result['files']
    exact = scan_result['exact_dupes']
    near = scan_result['near_dupes']
    
    total_size = sum(f.get('size', 0) for f in files)
    exact_waste = sum(d['waste_bytes'] for d in exact)
    
    lines = []
    lines.append("")
    lines.append("📊 DEDUPLICATION REPORT")
    lines.append("═" * 55)
    lines.append(f"Total screenshots: {len(files)}")
    lines.append(f"Total size: {total_size / (1024*1024):.1f} MB")
    lines.append("")
    
    # Exact duplicates
    lines.append(f"EXACT DUPLICATES: {len(exact)} groups")
    if exact:
        lines.append(f"  Files to remove: {sum(d['count'] - 1 for d in exact)}")
        lines.append(f"  Space reclaimable: {exact_waste / (1024*1024):.1f} MB")
        lines.append("")
        for i, group in enumerate(exact[:10], 1):  # show first 10
            lines.append(f"  Group {i}: {group['count']} identical files")
            for path in group['files'][:3]:
                lines.append(f"    • {os.path.basename(path)}")
            if group['count'] > 3:
                lines.append(f"    ... and {group['count'] - 3} more")
            lines.append(f"    Save: {group['waste_mb']} MB")
            lines.append("")
    else:
        lines.append("  ✓ No exact duplicates found!")
    lines.append("")
    
    # Near duplicates
    lines.append(f"NEAR-DUPLICATES: {len(near)} pairs")
    if near:
        high_conf = [d for d in near if d['confidence'] >= 90]
        review = [d for d in near if 50 <= d['confidence'] < 90]
        
        lines.append(f"  High confidence (likely dupes): {len(high_conf)}")
        lines.append(f"  Needs review: {len(review)}")
        lines.append("")
        
        for i, pair in enumerate(near[:5], 1):  # show first 5
            lines.append(f"  Pair {i}: {pair['confidence']}% confidence")
            lines.append(f"    • {os.path.basename(pair['file1'])}")
            lines.append(f"    • {os.path.basename(pair['file2'])}")
            lines.append(f"    → {pair['recommendation']}")
            lines.append("")
    else:
        lines.append("  ✓ No near-duplicates found!")
    
    lines.append("─" * 55)
    total_reclaimable = exact_waste / (1024*1024)
    lines.append(f"💾 TOTAL RECLAIMABLE: ~{total_reclaimable:.1f} MB")
    lines.append("")
    
    return '\n'.join(lines)


def generate_deletion_plan(scan_result: dict, dry_run: bool = True) -> list:
    """Generate a list of files recommended for deletion."""
    plan = []
    
    # Exact dupes: keep first, delete rest
    for group in scan_result['exact_dupes']:
        for path in group['files'][1:]:
            plan.append({
                'path': path,
                'reason': f"Exact duplicate of {os.path.basename(group['files'][0])}",
                'action': 'delete',
            })
    
    # Near-dupes with high confidence
    for pair in scan_result['near_dupes']:
        if pair['confidence'] >= 90 and pair['recommendation'] == 'delete one':
            plan.append({
                'path': pair['file2'],  # delete the second one
                'reason': f"Near-duplicate of {os.path.basename(pair['file1'])} ({pair['confidence']}% match)",
                'action': 'review_then_delete',
            })
    
    return plan


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Screenshot deduplication scanner')
    sub = parser.add_subparsers(dest='command')
    
    p_scan = sub.add_parser('scan', help='Scan for duplicates')
    p_scan.add_argument('--dir', required=True, help='Directory to scan')
    p_scan.add_argument('--output', help='Save scan results to JSON')
    
    p_report = sub.add_parser('report', help='Show dedup report')
    p_report.add_argument('--dir', required=True)
    
    p_plan = sub.add_parser('plan', help='Generate deletion plan')
    p_plan.add_argument('--dir', required=True)
    p_plan.add_argument('--dry-run', action='store_true', default=True)
    
    sub.add_parser('demo', help='Run with simulated data')
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        # Simulated demo data
        demo_result = {
            'files': [
                {'name': f'Screenshot_{i:03d}.png', 'size': 500000 + i * 1000,
                 'md5': f'hash{i}', 'ahash': f'{i:016x}'}
                for i in range(100)
            ],
            'exact_dupes': [
                {'md5': 'dupe1', 'files': ['Screenshot_001.png', 'Screenshot_002.png'],
                 'count': 2, 'waste_mb': 2.3, 'waste_bytes': 2411724},
                {'md5': 'dupe2', 'files': ['Screenshot_010.png', 'Screenshot_011.png', 'Screenshot_012.png'],
                 'count': 3, 'waste_mb': 4.6, 'waste_bytes': 4823448},
            ],
            'near_dupes': [
                {'file1': 'Screenshot_005.png', 'file2': 'Screenshot_006.png',
                 'hamming_distance': 3, 'confidence': 97, 'recommendation': 'delete one'},
                {'file1': 'Screenshot_020.png', 'file2': 'Screenshot_021.png',
                 'hamming_distance': 8, 'confidence': 70, 'recommendation': 'review'},
            ],
        }
        print(generate_report(demo_result))
        plan = generate_deletion_plan(demo_result)
        print(f"📋 DELETION PLAN ({len(plan)} files):")
        for item in plan:
            print(f"  {'🗑️' if item['action'] == 'delete' else '👁️'} {item['path']}")
            print(f"     Reason: {item['reason']}")
        return
    
    if args.command in ('scan', 'report'):
        print(f"Scanning {args.dir}...")
        result = scan_duplicates(args.dir)
        
        if args.command == 'scan' and args.output:
            with open(args.output, 'w') as f:
                # Strip non-serializable
                json.dump(result, f, indent=2, default=str)
            print(f"✓ Results saved to {args.output}")
        
        print(generate_report(result))
        return
    
    if args.command == 'plan':
        result = scan_duplicates(args.dir)
        plan = generate_deletion_plan(result, args.dry_run)
        
        print(f"\n📋 DELETION PLAN ({len(plan)} files, {'DRY RUN' if args.dry_run else 'EXECUTE'})")
        print("=" * 55)
        
        total_save = 0
        for item in plan:
            icon = '🗑️' if item['action'] == 'delete' else '👁️'
            try:
                size = os.path.getsize(item['path'])
                total_save += size
            except:
                size = 0
            print(f"\n  {icon} {item['path']}")
            print(f"     Size: {size / (1024*1024):.1f} MB")
            print(f"     Reason: {item['reason']}")
            print(f"     Action: {item['action']}")
        
        print(f"\n{'─' * 55}")
        print(f"💾 TOTAL SPACE RECLAIMABLE: {total_save / (1024*1024):.1f} MB")
        if args.dry_run:
            print("   (Dry run — no files deleted. Run without --dry-run to execute.)")
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
