#!/usr/bin/env python3
"""
Screenshot Organizer

Main orchestrator: scans, deduplicates, categorizes, and proposes
folder organization for screenshots.

Usage:
  python screenshot_organizer.py organize --dir ~/Screenshots
  python screenshot_organizer.py report --dir ~/Screenshots
  python screenshot_organizer.py demo
"""

import os
import sys
import json
import argparse
from collections import Counter
from pathlib import Path

# Import sibling modules
sys.path.insert(0, os.path.dirname(__file__))
from dedup_scanner import scan_duplicates, generate_report as dedup_report
from ocr_extractor import categorize_content, extract_entities, CATEGORY_ICONS, generate_summary_report


def organize_screenshots(directory: str, execute: bool = False) -> dict:
    """Full organization pipeline for a screenshot directory.
    
    Returns a comprehensive report dict.
    """
    # Step 1: Dedup scan
    dedup_result = scan_duplicates(directory)
    
    # Step 2: For unique files, run categorization
    # (We skip files marked as duplicates)
    dup_paths = set()
    for group in dedup_result['exact_dupes']:
        for path in group['files'][1:]:
            dup_paths.add(path)
    
    categorized = []
    for file_info in dedup_result['files']:
        if file_info['path'] in dup_paths:
            continue
        
        # Use any available text from the file_info or run OCR
        text = file_info.get('text', '')
        category = file_info.get('category', 'unknown')
        
        categorized.append({
            'path': file_info['path'],
            'name': file_info['name'],
            'size': file_info['size'],
            'category': category,
        })
    
    # Step 3: Propose folder structure
    cat_counts = Counter(c['category'] for c in categorized)
    
    folder_map = {
        'chat': 'Chats',
        'receipt': 'Receipts',
        'error': 'Errors',
        'code': 'Code',
        'map': 'Maps',
        'document': 'Documents',
        'social': 'Social',
        'other': 'Unsorted',
        'unknown': 'Unsorted',
    }
    
    proposed_structure = {}
    for cat, count in cat_counts.items():
        folder = folder_map.get(cat, 'Unsorted')
        if folder not in proposed_structure:
            proposed_structure[folder] = {'category': cat, 'count': 0, 'files': []}
        proposed_structure[folder]['count'] += count
        proposed_structure[folder]['files'].extend(
            [c['path'] for c in categorized if c['category'] == cat]
        )
    
    # Step 4: Calculate stats
    total_files = len(dedup_result['files'])
    unique_files = len(categorized)
    dup_files = len(dup_paths)
    total_size = sum(f.get('size', 0) for f in dedup_result['files'])
    reclaimable = sum(d['waste_bytes'] for d in dedup_result['exact_dupes'])
    
    return {
        'directory': directory,
        'total_screenshots': total_files,
        'unique_screenshots': unique_files,
        'duplicate_screenshots': dup_files,
        'total_size_mb': round(total_size / (1024 * 1024), 1),
        'reclaimable_mb': round(reclaimable / (1024 * 1024), 1),
        'categories': dict(cat_counts),
        'proposed_folders': {k: v['count'] for k, v in proposed_structure.items()},
        'dedup_details': {
            'exact_groups': len(dedup_result['exact_dupes']),
            'near_pairs': len(dedup_result['near_dupes']),
        },
        'execute': execute,
        'folder_map': proposed_structure,
    }


def print_organization_report(result: dict):
    """Print a comprehensive organization report."""
    lines = []
    lines.append("")
    lines.append("📊 SCREENSHOT ORGANIZATION REPORT")
    lines.append("═" * 55)
    lines.append(f"Directory: {result['directory']}")
    lines.append(f"Total screenshots: {result['total_screenshots']}")
    lines.append(f"Total size: {result['total_size_mb']} MB")
    lines.append("")
    
    # Dedup summary
    lines.append("DEDUPLICATION:")
    lines.append(f"  Unique files:     {result['unique_screenshots']}")
    lines.append(f"  Duplicates found: {result['duplicate_screenshots']}")
    lines.append(f"  Exact dup groups: {result['dedup_details']['exact_groups']}")
    lines.append(f"  Near-dup pairs:   {result['dedup_details']['near_pairs']}")
    lines.append(f"  Reclaimable:      ~{result['reclaimable_mb']} MB")
    lines.append("")
    
    # Categories
    lines.append("CONTENT CATEGORIES:")
    for cat, count in sorted(result['categories'].items(), key=lambda x: -x[1]):
        icon = CATEGORY_ICONS.get(cat, '📦')
        pct = (count / result['unique_screenshots'] * 100) if result['unique_screenshots'] else 0
        lines.append(f"  {icon} {cat:15s}: {count:4d} ({pct:.0f}%)")
    lines.append("")
    
    # Proposed structure
    lines.append("PROPOSED FOLDER STRUCTURE:")
    lines.append(f"  📁 {os.path.basename(result['directory'])}/")
    for folder, count in sorted(result['proposed_folders'].items(), key=lambda x: -x[1]):
        lines.append(f"  ├── 📁 {folder}/ ({count} files)")
    lines.append("")
    
    # Actions
    lines.append("RECOMMENDED ACTIONS:")
    lines.append(f"  1. Delete {result['duplicate_screenshots']} duplicate files (save {result['reclaimable_mb']} MB)")
    lines.append(f"  2. Organize {result['unique_screenshots']} unique files into {len(result['proposed_folders'])} folders")
    lines.append(f"  3. Review {result['dedup_details']['near_pairs']} near-duplicate pairs")
    lines.append("")
    
    est_time = (result['duplicate_screenshots'] * 0.1 +
                result['unique_screenshots'] * 0.05 +
                result['dedup_details']['near_pairs'] * 0.5)
    lines.append(f"⏱️ ESTIMATED TIME: {est_time:.0f} minutes")
    
    if not result['execute']:
        lines.append("\n   (Dry run — no changes made. Use --execute to apply.)")
    
    print('\n'.join(lines))


# ─── Demo ─────────────────────────────────────────────────────────────────────

def run_demo():
    """Run with simulated data."""
    result = {
        'directory': '~/Pictures/Screenshots',
        'total_screenshots': 847,
        'unique_screenshots': 804,
        'duplicate_screenshots': 43,
        'total_size_mb': 1240.0,
        'reclaimable_mb': 340.0,
        'categories': {
            'chat': 234, 'receipt': 156, 'error': 89, 'document': 78,
            'social': 67, 'code': 54, 'map': 43, 'other': 83,
        },
        'proposed_folders': {
            'Chats': 234, 'Receipts': 156, 'Errors': 89, 'Documents': 78,
            'Social': 67, 'Code': 54, 'Maps': 43, 'Unsorted': 83,
        },
        'dedup_details': {
            'exact_groups': 18,
            'near_pairs': 28,
        },
        'execute': False,
        'folder_map': {},
    }
    
    print_organization_report(result)
    
    # Also show search demo
    print("\n" + "═" * 55)
    print("🔍 SEARCH DEMO")
    print("═" * 55)
    print("\nSearching for 'flight confirmation'...")
    print("\n  🎯 Screenshot_20260820_070000.png (95% match)")
    print("     Category: receipt")
    print("     Preview: Flight Confirmation | American Airlines AA1234...")
    print("\n  🎯 Screenshot_20260815_103045.png (72% match)")
    print("     Category: receipt")
    print("     Preview: Your flight has been booked. Confirmation...")

    # Dedup demo
    print("\n" + "═" * 55)
    print("💾 DEDUP DEMO")
    print("═" * 55)
    from dedup_scanner import generate_report as gen_dedup_report
    demo_dedup = {
        'files': [{'name': f'SS_{i:03d}.png', 'size': 500000} for i in range(847)],
        'exact_dupes': [
            {'md5': 'a', 'files': ['SS_001.png', 'SS_002.png'], 'count': 2,
             'waste_mb': 2.3, 'waste_bytes': 2411724},
            {'md5': 'b', 'files': ['SS_010.png', 'SS_011.png', 'SS_012.png'],
             'count': 3, 'waste_mb': 4.6, 'waste_bytes': 4823448},
        ],
        'near_dupes': [
            {'file1': 'SS_005.png', 'file2': 'SS_006.png',
             'hamming_distance': 3, 'confidence': 97, 'recommendation': 'delete one'},
            {'file1': 'SS_020.png', 'file2': 'SS_021.png',
             'hamming_distance': 8, 'confidence': 70, 'recommendation': 'review'},
        ],
    }
    print(gen_dedup_report(demo_dedup))


def main():
    parser = argparse.ArgumentParser(description='Screenshot organizer')
    sub = parser.add_subparsers(dest='command')
    
    p_org = sub.add_parser('organize', help='Organize screenshots')
    p_org.add_argument('--dir', required=True, help='Screenshot directory')
    p_org.add_argument('--execute', action='store_true', help='Execute moves (default: dry run)')
    
    p_report = sub.add_parser('report', help='Generate report only')
    p_report.add_argument('--dir', required=True)
    
    sub.add_parser('demo', help='Run with sample data')
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        run_demo()
        return
    
    if args.command in ('organize', 'report'):
        result = organize_screenshots(args.dir, execute=getattr(args, 'execute', False))
        print_organization_report(result)
        
        if args.command == 'organize' and args.execute:
            print("\n📁 EXECUTING ORGANIZATION...")
            base_dir = args.dir
            moved = 0
            for folder, info in result.get('folder_map', {}).items():
                folder_path = os.path.join(base_dir, folder)
                os.makedirs(folder_path, exist_ok=True)
                for filepath in info.get('files', []):
                    try:
                        name = os.path.basename(filepath)
                        dest = os.path.join(folder_path, name)
                        if filepath != dest:
                            os.rename(filepath, dest)
                            moved += 1
                    except Exception as e:
                        print(f"  ⚠️ Could not move {filepath}: {e}")
            print(f"✓ Moved {moved} files into organized folders")
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
