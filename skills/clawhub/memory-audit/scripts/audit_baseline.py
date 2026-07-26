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

def collect_memory_files(workspace):
    """Collect metrics for memory/ directory."""
    mem_dir = os.path.join(workspace, 'memory')
    files = {
        'total': 0,
        'with_front_matter': 0,
        'without_front_matter': 0,
        'fm_coverage': 0.0,
        'files': [],
        'duplicates': [],
        'archives': 0,
    }
    
    if not os.path.isdir(mem_dir):
        return files
    
    all_files = glob.glob(os.path.join(mem_dir, '*.md'))
    archive_files = glob.glob(os.path.join(mem_dir, 'archive', '*.md'))
    clawcast_files = glob.glob(os.path.join(mem_dir, 'clawcast', '*.md'))
    
    all_files.extend(archive_files)
    all_files.extend(clawcast_files)
    
    # Deduplicate paths
    all_files = sorted(set(all_files))
    
    files['total'] = len(all_files)
    files['archives'] = len(archive_files)
    
    fm_count = 0
    dates = []
    
    for f in all_files:
        has_fm = has_front_matter(f)
        if has_fm:
            fm_count += 1
            meta = extract_front_matter(f)
            d = meta.get('date', '')
            if d:
                dates.append(d)
        
        files['files'].append({
            'path': os.path.relpath(f, workspace),
            'lines': count_lines(f),
            'has_front_matter': has_fm,
        })
    
    files['with_front_matter'] = fm_count
    files['without_front_matter'] = len(all_files) - fm_count
    files['fm_coverage'] = round(fm_count / len(all_files) * 100, 1) if all_files else 0
    
    # Check duplicate dates
    date_counts = Counter(dates)
    files['duplicates'] = [d for d, c in date_counts.items() if c > 1]
    
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
    print(f"\nMemory Files: {mem['total']} total | FM coverage: {mem['fm_coverage']}%")
    if mem['duplicates']:
        print(f"  ⚠️ Duplicate dates: {mem['duplicates']}")
    
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
