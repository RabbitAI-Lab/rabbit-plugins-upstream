#!/usr/bin/env python3
"""
Memory Audit — Phase 1: Diagnosis
Analyze baseline metrics against DDIA+DDD checklist, output prioritized findings.

Usage:
  python3 audit_diagnose.py --baseline /tmp/baseline.json --output /tmp/audit-report.md
"""
import json
import argparse
import os
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

# --- DDIA + DDD Audit Checklist ---

CHECKS = [
    # P0: Data Integrity
    {
        'id': 'P0-1',
        'domain': 'Schema',
        'lens': 'DDD',
        'priority': 'P0',
        'title': 'Core file size & content health',
        'check': lambda b: any(f['bytes'] > 20000 for f in b.get('core_files', {}).values()),
        'detail': lambda b: [
            f"{name}: {f['lines']}行/{f['bytes']}bytes {'⚠️ '+f.get('warning','')}"
            for name, f in b.get('core_files', {}).items()
            if f['bytes'] > 15000
        ],
        'fix': 'GC pass: extract operational docs to TOOLS.md, supersede stale entries, update project status.',
    },
    {
        'id': 'P0-2',
        'domain': 'Schema',
        'lens': 'DDD',
        'priority': 'P0',
        'title': 'Core file bounded context separation',
        'check': lambda b: any(
            n == 'AGENTS.md' and f['bytes'] > 15000
            for n, f in b.get('core_files', {}).items()
        ),
        'detail': 'AGENTS.md exceeds 15KB — theory, ops, and rules are likely mixed.',
        'fix': 'Split: theory → docs/, ops → TOOLS.md, keep only rules + cross-refs in AGENTS.md.',
    },
    {
        'id': 'P0-3',
        'domain': 'Schema',
        'lens': 'DDIA',
        'priority': 'P0',
        'title': 'Daily log Front Matter coverage',
        'check': lambda b: b.get('memory', {}).get('fm_coverage', 100) < 90,
        'detail': lambda b: f"FM coverage: {b['memory']['fm_coverage']}% ({b['memory']['with_front_matter']}/{b['memory']['total']})",
        'fix': 'Batch add YAML Front Matter (date, topics, projects, sources) to all log files.',
    },
    {
        'id': 'P0-4',
        'domain': 'Consistency',
        'lens': 'DDIA',
        'priority': 'P0',
        'title': 'Search result duplication',
        'check': lambda b: False,  # Requires runtime test, not baseline
        'detail': 'Search may return duplicate (date, title) entries.',
        'fix': 'Add (date, title) unique key dedup in search_memories().',
    },

    # P1: Consistency
    {
        'id': 'P1-1',
        'domain': 'Lifecycle',
        'lens': 'DDIA',
        'priority': 'P1',
        'title': 'MEMORY.md auto-GC mechanism',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'scripts', 'memory', 'memory_gc.py')),
        'detail': 'No automated GC script found. MEMORY.md grows without cleanup.',
        'fix': 'Create memory_gc.py: scan recent N days of logs, extract candidates for MEMORY.md update.',
    },
    {
        'id': 'P1-2',
        'domain': 'Schema',
        'lens': 'DDD',
        'priority': 'P1',
        'title': 'References INDEX.md auto-generation',
        'check': lambda b: not b.get('references', {}).get('has_index', False),
        'detail': 'No INDEX.md found for references/. Manual curation is brittle.',
        'fix': 'Create gen_references_index.py: scan references/, group by topic, auto-generate INDEX.md.',
    },
    {
        'id': 'P1-3',
        'domain': 'Coupling',
        'lens': 'DDD',
        'priority': 'P1',
        'title': 'Knowledge routing rules documented',
        'check': lambda b: False,  # Requires content check
        'detail': 'No explicit routing rules for where different content types should go.',
        'fix': 'Add routing table to AGENTS.md: articles→references/, Q&A→aiwiki, decisions→MEMORY.md, etc.',
    },
    {
        'id': 'P1-4',
        'domain': 'Lifecycle',
        'lens': 'DDIA',
        'priority': 'P1',
        'title': 'Staleness detection',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'scripts', 'memory', 'staleness_check.py')),
        'detail': 'No automated staleness detection. Old project status may linger.',
        'fix': 'Create staleness_check.py: flag entries >60 days without update.',
    },

    # P2: Query
    {
        'id': 'P2-1',
        'domain': 'Query',
        'lens': 'DDIA',
        'priority': 'P2',
        'title': 'Tag-based filtering',
        'check': lambda b: False,
        'detail': 'Search may not support tag filtering.',
        'fix': 'Add tag_filter parameter to search_memories() + CLI --tag option.',
    },
    {
        'id': 'P2-2',
        'domain': 'Query',
        'lens': 'DDIA',
        'priority': 'P2',
        'title': 'Cross-store federated search',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'scripts', 'memory', 'unified_search.py')),
        'detail': 'No unified search across memory + aiwiki + references.',
        'fix': 'Create unified_search.py: merge results from all stores with normalized scores.',
    },
    {
        'id': 'P2-3',
        'domain': 'Query',
        'lens': 'DDIA',
        'priority': 'P2',
        'title': 'Archived files searchable',
        'check': lambda b: b.get('memory', {}).get('archives', 0) > 0,
        'detail': lambda b: f"{b['memory']['archives']} archived files may be excluded from search index.",
        'fix': 'Include memory/archive/*.md in load_all_memories() with [归档] prefix.',
    },

    # P3: Architecture
    {
        'id': 'P3-1',
        'domain': 'Coupling',
        'lens': 'DDD',
        'priority': 'P3',
        'title': 'AGENTS.md size bloat',
        'check': lambda b: b.get('core_files', {}).get('AGENTS.md', {}).get('bytes', 0) > 15000,
        'detail': lambda b: f"AGENTS.md: {b['core_files']['AGENTS.md']['lines']}行/{b['core_files']['AGENTS.md']['bytes']}bytes",
        'fix': 'Migrate theory sections to docs/. Keep only rules + cross-reference pointers.',
    },
    {
        'id': 'P3-2',
        'domain': 'Coupling',
        'lens': 'DDD',
        'priority': 'P3',
        'title': 'TOOLS.md ops reference',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'TOOLS.md')),
        'detail': 'No dedicated ops reference file.',
        'fix': 'Create TOOLS.md with ops notes (API keys, CLI usage, data source configs).',
    },
    {
        'id': 'P3-3',
        'domain': 'Consistency',
        'lens': 'DDIA',
        'priority': 'P3',
        'title': 'Automated review agent',
        'check': lambda b: False,
        'detail': 'No nightly review agent for pattern extraction.',
        'fix': 'Set up cron job: scan daily log → extract decisions/patterns → write to memory/review/.',
    },
    {
        'id': 'P3-4',
        'domain': 'Schema',
        'lens': 'DDIA',
        'priority': 'P3',
        'title': 'Duplicate date files',
        'check': lambda b: len(b.get('memory', {}).get('duplicates', [])) > 0,
        'detail': lambda b: f"Duplicate dates: {b['memory']['duplicates']}",
        'fix': 'Merge duplicate files: keep canonical name, append content from variants.',
    },

    # P4: Knowledge Systematization
    {
        'id': 'P4-1',
        'domain': 'Query',
        'lens': 'DDIA',
        'priority': 'P4',
        'title': 'Knowledge graph',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'scripts', 'memory', 'knowledge_graph.py')),
        'detail': 'No graph representation of project/topic/file relationships.',
        'fix': 'Create knowledge_graph.py: extract nodes (project/topic/file/decision) and edges, output JSON + Mermaid.',
    },
    {
        'id': 'P4-2',
        'domain': 'Consistency',
        'lens': 'DDIA',
        'priority': 'P4',
        'title': 'aiwiki reflux pipeline',
        'check': lambda b: not os.path.exists(os.path.join(b.get('workspace', '.'), 'scripts', 'memory', 'aiwiki_reflux.py')),
        'detail': 'No automated check for references not yet ingested into aiwiki.',
        'fix': 'Create aiwiki_reflux.py: detect gap, batch ingest missing files.',
    },
    {
        'id': 'P4-3',
        'domain': 'Lifecycle',
        'lens': 'DDIA',
        'priority': 'P4',
        'title': 'Agent execution traces',
        'check': lambda b: b.get('traces', {}).get('total', 0) == 0,
        'detail': 'No execution traces recorded.',
        'fix': 'Create trace_logger.py + integrate into spawn workflow.',
    },
]

def run_diagnosis(baseline):
    """Run all checks against baseline."""
    findings = []
    for check in CHECKS:
        try:
            triggered = check['check'](baseline)
        except Exception:
            triggered = False
        
        if triggered:
            detail = check.get('detail', '')
            if callable(detail):
                try:
                    detail = detail(baseline)
                except:
                    detail = ''
            findings.append({
                'id': check['id'],
                'priority': check['priority'],
                'domain': check['domain'],
                'lens': check['lens'],
                'title': check['title'],
                'detail': detail if isinstance(detail, str) else str(detail),
                'fix': check['fix'],
            })
    
    return findings

def generate_report(findings, baseline):
    """Generate Markdown report."""
    lines = [
        f"# Memory Audit Report",
        f"",
        f"Generated: {datetime.now(CST).strftime('%Y-%m-%d %H:%M')} CST",
        f"",
        f"## Baseline Summary",
        f"",
    ]
    
    # Baseline
    for name, info in baseline.get('core_files', {}).items():
        lines.append(f"- **{name}**: {info['lines']} lines / {info['bytes']:,} bytes")
    
    mem = baseline.get('memory', {})
    lines.append(f"- **Memory files**: {mem.get('total', 0)} ({mem.get('fm_coverage', 0)}% FM coverage)")
    lines.append(f"- **References**: {baseline.get('references', {}).get('total', 0)} files")
    lines.append(f"- **Traces**: {baseline.get('traces', {}).get('total', 0)} files")
    
    tk = baseline.get('token_estimate', {})
    lines.append(f"- **Token estimate**: ~{tk.get('estimated_tokens', 0):,} tokens (core files)")
    
    if not findings:
        lines.append(f"\n✅ All checks passed. No issues found.")
        return '\n'.join(lines)
    
    lines.append(f"\n## Findings ({len(findings)} issues)\n")
    
    # Group by priority
    for p in ['P0', 'P1', 'P2', 'P3', 'P4']:
        p_findings = [f for f in findings if f['priority'] == p]
        if not p_findings:
            continue
        
        labels = {
            'P0': '🔴 P0 — Data Integrity',
            'P1': '🟠 P1 — Consistency',
            'P2': '🟡 P2 — Query Capability',
            'P3': '🔵 P3 — Architecture Decoupling',
            'P4': '🟢 P4 — Knowledge Systematization',
        }
        lines.append(f"### {labels[p]}\n")
        
        for f in p_findings:
            lines.append(f"#### {f['id']}: {f['title']}")
            lines.append(f"- **Domain**: {f['domain']} ({f['lens']})")
            lines.append(f"- **Detail**: {f['detail']}")
            lines.append(f"- **Fix**: {f['fix']}")
            lines.append(f"")
    
    lines.append(f"## Execution Order\n")
    lines.append(f"Work P0 → P4 sequentially. Each fix must pass verification before moving to next.")
    lines.append(f"Record trace for each completed priority level.")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Memory Audit Diagnosis')
    parser.add_argument('--baseline', required=True, help='Baseline JSON path')
    parser.add_argument('--output', default=None, help='Output report path')
    args = parser.parse_args()
    
    with open(args.baseline) as f:
        baseline = json.load(f)
    
    findings = run_diagnosis(baseline)
    report = generate_report(findings, baseline)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    
    print(report)

if __name__ == '__main__':
    main()
