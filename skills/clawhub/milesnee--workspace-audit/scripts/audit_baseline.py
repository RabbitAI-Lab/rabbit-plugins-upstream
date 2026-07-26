#!/usr/bin/env python3
"""
Memory Audit — Phase 0: Baseline Collection
Collect workspace metrics for diagnosis.

Usage:
  python3 audit_baseline.py --workspace /path/to/workspace --report /tmp/baseline.json
"""
import os
import re
import json
import argparse
import glob
from collections import Counter
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

def count_lines(path):
    try:
        with open(path, 'r') as f:
            return len(f.readlines())
    except:
        return 0

def count_bytes(path):
    try:
        return os.path.getsize(path)
    except:
        return 0

def has_front_matter(path):
    try:
        with open(path, 'r') as f:
            return f.read(4) == '---\n'
    except:
        return False

def extract_front_matter(path):
    """Parse YAML front matter, return dict."""
    try:
        with open(path, 'r') as f:
            content = f.read()
        m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not m:
            return {}
        meta = {}
        for line in m.group(1).split('\n'):
            if ':' in line:
                key, _, val = line.partition(':')
                key = key.strip()
                val = val.strip()
                if val.startswith('[') and val.endswith(']'):
                    items = [i.strip().strip("'\"") for i in val[1:-1].split(',') if i.strip()]
                    meta[key] = items
                else:
                    meta[key] = val
        return meta
    except:
        return {}

def collect_core_files(workspace):
    """Collect metrics for core config files."""
    core_files = {}
    targets = ['MEMORY.md', 'AGENTS.md', 'SOUL.md', 'TOOLS.md', 'IMPLEMENT.md']
    
    for t in targets:
        path = os.path.join(workspace, t)
        if os.path.exists(path):
            core_files[t] = {
                'path': path,
                'lines': count_lines(path),
                'bytes': count_bytes(path),
                'sections': len(re.findall(r'^## ', open(path).read(), re.MULTILINE)),
            }
            # Size warning
            if core_files[t]['bytes'] > 15000:
                core_files[t]['warning'] = 'oversized'
            elif core_files[t]['bytes'] > 10000:
                core_files[t]['warning'] = 'large'
    return core_files

def _collect_md_files(mem_dir, subdir=None):
    """Collect .md files from mem_dir (top-level) or a named subdir."""
    if subdir:
        pattern = os.path.join(mem_dir, subdir, '*.md')
    else:
        pattern = os.path.join(mem_dir, '*.md')
    return sorted(glob.glob(pattern))


def _analyze_files(file_list, workspace):
    """Analyze a list of file paths for FM coverage and dates."""
    fm_count = 0
    dates = []
    details = []
    for f in file_list:
        has_fm = has_front_matter(f)
        if has_fm:
            fm_count += 1
            meta = extract_front_matter(f)
            d = meta.get('date', '')
            if d:
                dates.append(d)
        details.append({
            'path': os.path.relpath(f, workspace),
            'lines': count_lines(f),
            'has_front_matter': has_fm,
        })
    return {
        'count': len(file_list),
        'fm_count': fm_count,
        'fm_coverage': round(fm_count / len(file_list) * 100, 1) if file_list else 0,
        'dates': dates,
        'files': details,
    }


def collect_memory_files(workspace):
    """Collect metrics for memory/ directory.
    
    Separates top-level daily logs from archive/ and clawcast/ subdirs,
    so duplicate detection only flags true duplicates (same dir, same date).
    """
    mem_dir = os.path.join(workspace, 'memory')
    files = {
        'total': 0,
        'with_front_matter': 0,
        'without_front_matter': 0,
        'fm_coverage': 0.0,
        'files': [],
        'duplicates': [],
        'archives': 0,
        'breakdown': {},
    }
    
    if not os.path.isdir(mem_dir):
        return files
    
    # Collect separately by directory
    categories = {
        'toplevel': _collect_md_files(mem_dir, None),
        'archive': _collect_md_files(mem_dir, 'archive'),
        'clawcast': _collect_md_files(mem_dir, 'clawcast'),
    }
    
    # Also detect other subdirs dynamically
    for entry in os.listdir(mem_dir):
        full = os.path.join(mem_dir, entry)
        if os.path.isdir(full) and entry not in ('archive', 'clawcast'):
            md_files = _collect_md_files(mem_dir, entry)
            if md_files:
                categories[entry] = md_files
    
    all_files = []
    breakdown = {}
    
    for cat, fl in categories.items():
        analysis = _analyze_files(fl, workspace)
        breakdown[cat] = analysis
        all_files.extend(fl)
        # Duplicate dates within this category only
        date_counts = Counter(analysis['dates'])
        cat_dups = [d for d, c in date_counts.items() if c > 1]
        if cat_dups:
            files['duplicates'].extend([f"{cat}:{d}" for d in cat_dups])
    
    files['total'] = len(all_files)
    files['archives'] = breakdown.get('archive', {}).get('count', 0)
    files['breakdown'] = {k: {'count': v['count'], 'fm_coverage': v['fm_coverage']} for k, v in breakdown.items()}
    
    # FM coverage: report toplevel separately as the primary metric
    top = breakdown.get('toplevel', {'count': 0, 'fm_count': 0, 'fm_coverage': 0})
    files['with_front_matter'] = sum(v['fm_count'] for v in breakdown.values())
    files['without_front_matter'] = files['total'] - files['with_front_matter']
    # Use toplevel FM coverage as the headline metric
    files['fm_coverage'] = top['fm_coverage'] if top['count'] > 0 else 0
    files['fm_coverage_all'] = round(files['with_front_matter'] / files['total'] * 100, 1) if files['total'] else 0
    
    files['files'] = []
    for v in breakdown.values():
        files['files'].extend(v['files'])
    
    return files

def collect_references(workspace):
    """Collect references/ metrics."""
    refs_dir = os.path.join(workspace, 'references')
    return {
        'total': len(glob.glob(os.path.join(refs_dir, '*.md'))) - (1 if os.path.exists(os.path.join(refs_dir, 'INDEX.md')) else 0),
        'has_index': os.path.exists(os.path.join(refs_dir, 'INDEX.md')),
    }

def collect_traces(workspace):
    """Collect traces/ metrics."""
    traces_dir = os.path.join(workspace, 'traces', 'sessions')
    if not os.path.isdir(traces_dir):
        return {'total': 0, 'dates': []}
    
    date_dirs = [d for d in os.listdir(traces_dir) if d != 'TEMPLATE.md']
    total = sum(len(glob.glob(os.path.join(traces_dir, d, '*.json'))) for d in date_dirs)
    return {
        'total': total,
        'dates': sorted(date_dirs),
    }

def collect_docs(workspace):
    """Collect docs/ metrics."""
    docs_dir = os.path.join(workspace, 'docs')
    if not os.path.isdir(docs_dir):
        return {'total': 0, 'files': []}
    
    files = glob.glob(os.path.join(docs_dir, '*.md'))
    return {
        'total': len(files),
        'files': [os.path.basename(f) for f in files],
    }

def check_token_estimate(core_files):
    """Estimate token consumption of core files."""
    total_bytes = sum(f['bytes'] for f in core_files.values())
    # Rough: 1 token ≈ 4 bytes for mixed CJK/English
    total_tokens = total_bytes // 4
    return {
        'total_bytes': total_bytes,
        'estimated_tokens': total_tokens,
        'per_file': {k: v['bytes'] // 4 for k, v in core_files.items()},
    }

def main():
    parser = argparse.ArgumentParser(description='Memory Audit Baseline')
    parser.add_argument('--workspace', required=True, help='Workspace root path')
    parser.add_argument('--report', default=None, help='Output report path')
    args = parser.parse_args()
    
    ws = args.workspace
    
    baseline = {
        'workspace': ws,
        'timestamp': datetime.now(CST).isoformat(),
        'core_files': collect_core_files(ws),
        'memory': collect_memory_files(ws),
        'references': collect_references(ws),
        'traces': collect_traces(ws),
        'docs': collect_docs(ws),
        'token_estimate': None,
    }
    
    baseline['token_estimate'] = check_token_estimate(baseline['core_files'])
    
    # Summary
    print(f"\n{'='*60}")
    print(f"  Memory Audit Baseline — {os.path.basename(ws)}")
    print(f"{'='*60}\n")
    
    print("Core Files:")
    for name, info in baseline['core_files'].items():
        warn = f" ⚠️ {info.get('warning','')}" if info.get('warning') else ''
        print(f"  {name:20s} {info['lines']:5d} lines / {info['bytes']:6d} bytes{warn}")
    
    tk = baseline['token_estimate']
    print(f"\nToken Estimate: ~{tk['estimated_tokens']:,} tokens (core files only)")
    
    mem = baseline['memory']
    print(f"\nMemory Files: {mem['total']} total | FM coverage (toplevel): {mem['fm_coverage']}% | All: {mem.get('fm_coverage_all', 0)}%")
    if mem.get('breakdown'):
        for cat, info in mem['breakdown'].items():
            print(f"  {cat:15s} {info['count']:4d} files | FM: {info['fm_coverage']}%")
    if mem['duplicates']:
        print(f"  ⚠️ Duplicate dates (by category): {mem['duplicates']}")
    else:
        print(f"  ✅ No duplicate dates")
    
    refs = baseline['references']
    print(f"\nReferences: {refs['total']} files | INDEX.md: {'✅' if refs['has_index'] else '❌'}")
    
    traces = baseline['traces']
    print(f"\nTraces: {traces['total']} files across {len(traces['dates'])} dates")
    
    docs = baseline['docs']
    print(f"\nDocs: {docs['total']} files")
    
    print(f"\n{'='*60}")
    
    if args.report:
        with open(args.report, 'w') as f:
            json.dump(baseline, f, ensure_ascii=False, indent=2)
        print(f"Report saved to {args.report}")

if __name__ == '__main__':
    main()
