#!/usr/bin/env python3
"""
Memory Audit — Phase 3: Validation
Re-run baseline check after fixes, compare with initial report.

Usage:
  python3 audit_validate.py --baseline /tmp/baseline-after.json --initial /tmp/baseline-before.json
"""
import json
import argparse
import os
import re

def validate_fixes(before, after):
    """Compare before/after baselines, check which fixes resolved."""
    results = []
    
    # P0-1: Core file size
    before_oversized = [n for n, f in before.get('core_files', {}).items() if f['bytes'] > 20000]
    after_oversized = [n for n, f in after.get('core_files', {}).items() if f['bytes'] > 20000]
    p01_resolved = len(after_oversized) == 0 and len(before_oversized) == 0 or len(after_oversized) < len(before_oversized)
    results.append({
        'id': 'P0-1',
        'title': 'Core file size',
        'before': f"{len(before_oversized)} oversized",
        'after': f"{len(after_oversized)} oversized",
        'resolved': p01_resolved,
        'detail': f"{'✅' if p01_resolved else '❌'} {'No oversized files' if not after_oversized else after_oversized}",
    })
    
    # P0-3: Front Matter coverage
    before_fm = before.get('memory', {}).get('fm_coverage', 100)
    after_fm = after.get('memory', {}).get('fm_coverage', 100)
    results.append({
        'id': 'P0-3',
        'title': 'Front Matter coverage',
        'before': f"{before_fm}%",
        'after': f"{after_fm}%",
        'resolved': after_fm >= 90,
        'detail': f"{'✅' if after_fm >= 90 else '❌'} {after_fm}% " + ("(≥90% target)" if after_fm >= 90 else "(<90% target)"),
    })
    
    # P3-4: Duplicate dates (only within same subdirectory)
    def get_dups_by_dir(baseline):
        from collections import Counter
        dups = set()
        for dir_key in ['memory']:
            files = [f for f in baseline.get('memory', {}).get('files', [])]
            # Group by parent dir + date
            date_dir = Counter()
            for f in files:
                path = f.get('path', '')
                parts = path.split('/')
                parent = parts[-2] if len(parts) > 1 else 'root'
                fm = f.get('has_front_matter', False)
                # Extract date from filename
                import re
                m = re.search(r'(\d{4}-\d{2}-\d{2})', path)
                if m:
                    key = (parent, m.group(1))
                    date_dir[key] = date_dir.get(key, 0) + 1
            for (d, n), c in date_dir.items():
                if c > 1:
                    dups.add(f"{d}/{n}")
        return dups
    before_dups = get_dups_by_dir(before)
    after_dups = get_dups_by_dir(after)
    p34_resolved = len(after_dups) == 0
    results.append({
        'id': 'P3-4',
        'title': 'Duplicate date files (same dir)',
        'before': f"{len(before_dups)} duplicates",
        'after': f"{len(after_dups)} duplicates",
        'resolved': p34_resolved,
        'detail': f"{'✅' if p34_resolved else '⚠️'} {list(after_dups)[:5] if after_dups else 'None'}",
    })
    
    # Token estimate
    before_tokens = before.get('token_estimate', {}).get('estimated_tokens', 0)
    after_tokens = after.get('token_estimate', {}).get('estimated_tokens', 0)
    delta = after_tokens - before_tokens
    # Pass if delta <= 0 (same or reduced), or if both are small (<10000)
    meta_resolved = delta <= 0 or after_tokens < 10000
    results.append({
        'id': 'META',
        'title': 'Token consumption',
        'before': f"~{before_tokens:,}",
        'after': f"~{after_tokens:,}",
        'resolved': meta_resolved,
        'detail': f"{'✅' if meta_resolved else '⚠️'} {delta:+,} tokens ({delta/max(before_tokens,1)*100:+.1f}%)",
    })
    
    # Script existence checks
    ws = after.get('workspace', '.')
    script_checks = [
        ('P1-1', 'memory_gc.py', 'scripts/memory/memory_gc.py'),
        ('P1-2', 'gen_references_index.py', 'scripts/memory/gen_references_index.py'),
        ('P1-4', 'staleness_check.py', 'scripts/memory/staleness_check.py'),
        ('P2-2', 'unified_search.py', 'scripts/memory/unified_search.py'),
        ('P4-1', 'knowledge_graph.py', 'scripts/memory/knowledge_graph.py'),
        ('P4-2', 'aiwiki_reflux.py', 'scripts/memory/aiwiki_reflux.py'),
        ('P4-3', 'trace_logger.py', 'scripts/memory/trace_logger.py'),
    ]
    
    for sid, name, rel_path in script_checks:
        exists = os.path.exists(os.path.join(ws, rel_path))
        results.append({
            'id': sid,
            'title': f'{name} exists',
            'before': '❌',
            'after': '✅' if exists else '❌',
            'resolved': exists,
            'detail': f"{'✅' if exists else '❌'} {rel_path}",
        })
    
    # Docs directory
    docs_count = after.get('docs', {}).get('total', 0)
    results.append({
        'id': 'P3-1',
        'title': 'Docs directory (decoupled theory)',
        'before': f"{before.get('docs', {}).get('total', 0)} files",
        'after': f"{docs_count} files",
        'resolved': docs_count > 0,
        'detail': f"{'✅' if docs_count > 0 else '❌'} {docs_count} doc files",
    })
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Memory Audit Validation')
    parser.add_argument('--baseline', required=True, help='After-fix baseline JSON')
    parser.add_argument('--initial', required=True, help='Before-fix baseline JSON')
    args = parser.parse_args()
    
    with open(args.baseline) as f:
        after = json.load(f)
    with open(args.initial) as f:
        before = json.load(f)
    
    results = validate_fixes(before, after)
    
    print(f"\n{'='*60}")
    print(f"  Memory Audit Validation Report")
    print(f"{'='*60}\n")
    
    passed = sum(1 for r in results if r['resolved'])
    total = len(results)
    
    for r in results:
        print(f"  {r['detail']}")
    
    print(f"\n{'='*60}")
    print(f"  {passed}/{total} checks passed")
    print(f"{'='*60}")
    
    if passed == total:
        print("  ✅ ALL CHECKS PASSED")
    else:
        failed = [r['id'] for r in results if not r['resolved']]
        print(f"  ❌ Failed: {failed}")
    
    return 0 if passed == total else 1

if __name__ == '__main__':
    exit(main())
