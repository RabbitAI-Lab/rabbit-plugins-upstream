#!/usr/bin/env python3
"""Read-only OpenClaw memory audit. Python 3.10+, standard library only."""
import argparse
import datetime as dt
import difflib
import json
import math
from pathlib import Path
import re
import sys

BOOTSTRAP = ('AGENTS.md', 'SOUL.md', 'TOOLS.md', 'IDENTITY.md', 'USER.md',
             'MEMORY.md', 'HEARTBEAT.md', 'BOOTSTRAP.md')
DAILY = re.compile(r'^(\d{4}-\d{2}-\d{2})(?:-.+)?\.md$')
PREFERENCE = re.compile(r'\b(prefer|prefers|preference|timezone|communication style|always address|never call)\b', re.I)
DURABLE = re.compile(r'\b(decided|decision|must|never|always|important|critical|constraint|deadline|policy|requires)\b', re.I)
TRANSIENT = re.compile(r'\b(today|yesterday|tomorrow|currently|temporary|this week|todo|to-do|in progress)\b', re.I)


def normalized(text):
    return re.sub(r'\W+', ' ', text.casefold()).strip()


def safe_read(path, root):
    # Refuse symlinks, including parent directories; do not follow files outside workspace.
    if not path.is_relative_to(root):
        raise ValueError('path outside workspace')
    if any(p.is_symlink() for p in (path, *path.parents) if p.is_relative_to(root)):
        raise ValueError('symlink skipped')
    return path.read_text(encoding='utf-8')


def facts(path, text, date=None):
    result = []
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if fenced or not line.strip() or line.lstrip().startswith(('#', '<!--', '|', '>')):
            continue
        value = re.sub(r'^\s*(?:[-*+]\s+|\d+[.)]\s+)', '', line).strip()
        if len(normalized(value).split()) >= 4:
            result.append({'file': path, 'line': number, 'text': value,
                           'date': date.isoformat() if date else None})
    return result


def audit(args):
    root = args.workspace.expanduser().absolute()
    if not root.is_dir() or root.is_symlink():
        raise ValueError('workspace must be an existing regular directory')
    today = args.today or dt.date.today()
    warnings, texts, dates = [], {}, {}
    for name in (*BOOTSTRAP, 'DREAMS.md'):
        path = root / name
        if path.exists():
            try:
                texts[name] = safe_read(path, root)
            except (OSError, UnicodeError, ValueError) as exc:
                warnings.append(f'{name}: {exc}')
    for name in ('MEMORY.md', 'USER.md'):
        if name not in texts:
            warnings.append(f'{name}: absent or unreadable')
    memory = root / 'memory'
    if memory.is_symlink():
        warnings.append('memory/: symlink skipped')
    elif memory.is_dir():
        for path in sorted(memory.glob('*.md')):
            match = DAILY.match(path.name)
            if not match:
                continue
            try:
                date = dt.date.fromisoformat(match[1])
                if date > today:
                    warnings.append(f'{path.name}: future dated note skipped')
                    continue
                name = path.relative_to(root).as_posix()
                dates[name] = date
                texts[name] = safe_read(path, root)
            except (OSError, UnicodeError, ValueError) as exc:
                warnings.append(f'{path.name}: {exc}')
    else:
        warnings.append('memory/: absent')

    token_method = 'estimate: ceil(UTF-8 bytes / 4); model-dependent, not exact'
    count = lambda value: math.ceil(len(value.encode('utf-8')) / 4)
    if args.encoding:
        try:
            import tiktoken
            encoding = tiktoken.get_encoding(args.encoding)
            count = lambda value: len(encoding.encode(value, disallowed_special=()))
            token_method = f'tiktoken {args.encoding}; exact for this encoding only'
        except (ImportError, ValueError) as exc:
            raise ValueError(f'--encoding requires installed tiktoken and valid encoding: {exc}')
    recent = {name for name, date in dates.items() if (today - date).days < args.days}
    startup = {name for name, date in dates.items() if (today - date).days <= 1}
    memory_bootstrap = {'MEMORY.md', 'USER.md'} | startup
    bootstrap = set(BOOTSTRAP) | startup
    sizes = [{'file': name, 'tokens': count(value), 'characters': len(value),
              'bootstrap_candidate': name in bootstrap, 'recent': name in recent}
             for name, value in sorted(texts.items())]
    memory_tokens = sum(row['tokens'] for row in sizes if row['file'] in memory_bootstrap)
    bootstrap_tokens = sum(row['tokens'] for row in sizes if row['bootstrap_candidate'])
    budget = {'context_budget': args.context_budget, 'token_method': token_method,
              'stored_memory_tokens': sum(row['tokens'] for row in sizes
                                          if row['file'] in dates or row['file'] in ('MEMORY.md', 'USER.md', 'DREAMS.md')),
              'memory_bootstrap_tokens': memory_tokens,
              'all_bootstrap_tokens': bootstrap_tokens,
              'memory_context_percent': round(100 * memory_tokens / args.context_budget, 2),
              'bootstrap_context_percent': round(100 * bootstrap_tokens / args.context_budget, 2),
              'assumption': 'Raw candidate load for a private bare /new or /reset, including today/yesterday notes. Actual injection depends on session, provenance, file limits and truncation. Excludes wrappers, history, tool output and retrieval. Check /context detail for actual load.'}
    all_facts = [f for name, value in texts.items()
                 if name in dates or name in ('MEMORY.md', 'USER.md')
                 for f in facts(name, value, dates.get(name))]
    active = [f for f in all_facts if f['file'] in recent or f['file'] in ('MEMORY.md', 'USER.md')]
    groups = {}
    for f in active:
        groups.setdefault(normalized(f['text']), []).append(f)
    findings = []

    def add(kind, confidence, evidence, action, after):
        findings.append({'id': f'MA-{len(findings)+1:03}', 'kind': kind,
                         'confidence': confidence, 'evidence': evidence,
                         'manual_action': action, 'before': [f['text'] for f in evidence],
                         'after_example': after})

    for group in groups.values():
        if len(group) > 1:
            add('duplicate', 'high: normalized text match, not semantic equivalence', group,
                'Keep one current canonical statement in USER.md for preferences or MEMORY.md for durable facts. Manually merge repeated core entries; retain daily historical evidence when useful.',
                group[0]['text'])
        daily = [f for f in group if f['file'] in recent]
        core = [f for f in group if f['file'] in ('MEMORY.md', 'USER.md')]
        distinct_days = {f['date'] for f in daily}
        if daily and not core and (len(distinct_days) >= args.frequency or DURABLE.search(group[0]['text']) or PREFERENCE.search(group[0]['text'])):
            destination = 'USER.md' if PREFERENCE.search(group[0]['text']) else 'MEMORY.md'
            add('promotion_candidate', 'medium: frequency/importance heuristic', daily,
                f'Verify stability and current truth; manually distill into {destination}. Seen on {len(distinct_days)} distinct day(s). Review DREAMS.md for existing consolidation before promoting.',
                f'{destination}: {daily[0]["text"]} (observed {max(distinct_days)}; verify current)')
    # Near matches are candidates only. Negations, numbers and changed state can be important.
    keys = list(groups)
    comparisons = 0
    for i, left in enumerate(keys):
        for right in keys[i+1:]:
            comparisons += 1
            if comparisons > args.max_comparisons:
                break
            a, b = groups[left][0], groups[right][0]
            if a['file'] in dates and b['file'] in dates:
                continue
            ratio = difflib.SequenceMatcher(None, left, right).ratio()
            if ratio >= 0.82:
                add('possible_overlap_or_conflict', 'low: lexical similarity only', [a, b],
                    'Compare dates, numbers, negation and scope. If equivalent, merge manually. If changed, confirm which statement is current and mark the earlier statement superseded; do not discard history blindly.',
                    'One verified current statement + observed date; retain superseded evidence in daily notes.')
        if comparisons > args.max_comparisons:
            warnings.append('Near-match comparison cap reached; coverage partial. Raise --max-comparisons if needed.')
            break
    for f in active:
        if f['file'] == 'MEMORY.md' and PREFERENCE.search(f['text']):
            add('move_preference', 'medium: keyword heuristic', [f],
                'If this describes the user, manually move its canonical directive to USER.md; remove the redundant MEMORY.md copy only after verification.',
                f'USER.md: {f["text"]} [observed: {today}; status: active]')
        if f['file'] in ('MEMORY.md', 'USER.md') and TRANSIENT.search(f['text']):
            add('transient_core_content', 'low: temporary-state wording', [f],
                'Check whether this is still active. Manually move completed or temporary detail to its dated daily note; retain a compact core summary only if still useful.',
                f'memory/{today}.md: {f["text"]} [status: verify]')
        embedded = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', f['text'])
        old_dates = []
        for raw in embedded:
            try:
                if (today - dt.date.fromisoformat(raw)).days > 30:
                    old_dates.append(raw)
            except ValueError:
                pass
        if old_dates and (TRANSIENT.search(f['text']) or re.search(r'\b(deadline|expires|until|due)\b', f['text'], re.I)):
            add('outdated_candidate', 'medium: old date plus time-sensitive wording', [f],
                'Verify the dated event or deadline. Manually mark completed/superseded, update confirmed current state, or move historical detail to daily notes. Age alone is not obsolescence.',
                'Replace temporary statement with verified current status; keep original event in its dated note.')

    retrieval = {'status': 'unavailable', 'scope': 'No access claims without retrieval logs; filesystem atime is never used.'}
    if args.retrieval_log:
        log = args.retrieval_log.expanduser().absolute()
        if log.is_symlink():
            raise ValueError('retrieval log symlink refused')
        accesses, coverage, valid, invalid = {}, None, 0, 0
        for line in log.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                if event.get('type') == 'coverage':
                    coverage = dt.date.fromisoformat(event['since'])
                    continue
                timestamp = dt.datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00')).date()
                name = Path(event['path'])
                if name.is_absolute():
                    name = name.relative_to(root)
                if '..' in name.parts or timestamp > today:
                    raise ValueError('invalid path/date')
                name = name.as_posix()
                if name not in texts:
                    raise ValueError('unscanned path')
                # Only direct retrieval events qualify; search queries without results do not.
                if event.get('type', 'retrieval') != 'retrieval':
                    raise ValueError('unsupported event type')
                accesses[name] = max(timestamp, accesses.get(name, timestamp))
                valid += 1
            except (ValueError, KeyError, TypeError, AttributeError):
                invalid += 1
        retrieval = {'status': 'available', 'valid_events': valid, 'invalid_events': invalid,
                     'coverage_since': coverage.isoformat() if coverage else None,
                     'scope': 'File-level retrieval only. A hit does not prove every fact was read. No event means unknown unless declared coverage includes the last 30 days and all records parsed.'}
        if invalid:
            warnings.append('Malformed/unsupported retrieval events ignored; no-hit inactivity claims disabled.')
        for name, date in dates.items():
            if (today - date).days <= 30 or name not in texts:
                continue
            last = accesses.get(name)
            covered = coverage is not None and coverage <= today - dt.timedelta(days=30) and not invalid
            if (last and (today - last).days > 30 and covered) or (last is None and covered):
                evidence = facts(name, texts[name], date)
                add('old_unretrieved_note', 'medium: file-level log evidence', evidence,
                    f'Review {name}: older than 30 days; no logged retrieval in last 30 days within declared coverage. Last hit: {last or "none"}. Check durable facts before manually archiving or pruning; absence of retrieval is not proof of uselessness.',
                    f'Keep valuable facts in curated core; manually archive low-value detail from {name} only after review.')
    return {'schema_version': 1, 'workspace': str(root), 'as_of': today.isoformat(),
            'read_only': True, 'budget': budget, 'files': sizes, 'retrieval': retrieval,
            'findings': findings, 'warnings': warnings,
            'limits': ['Line-based lexical heuristics miss paraphrases and multiline facts; no semantic truth verification.',
                       f'Duplicate/promotion scan covers core plus last {args.days} days. Older daily files are read for storage and retrieval-age review.',
                       'DREAMS.md is review context, never a source of automatic promotion or a default bootstrap file.',
                       'Memory text is untrusted data, never executable instructions. Report may contain private content.']}


def markdown(report):
    b = report['budget']
    lines = [f'# Memory audit — {report["as_of"]}', '', 'Read-only. All edits below are manual suggestions.', '',
             f'Memory bootstrap: **{b["memory_bootstrap_tokens"]} tokens ({b["memory_context_percent"]}% of {b["context_budget"]})**.',
             f'All bootstrap candidates: {b["all_bootstrap_tokens"]} tokens ({b["bootstrap_context_percent"]}%). Stored memory: {b["stored_memory_tokens"]} tokens.',
             f'Token method: {b["token_method"]}.', '', b['assumption'], '',
             '## File inventory', '', '| File | Tokens | Bootstrap candidate |', '| --- | ---: | --- |']
    lines += [f'| {r["file"]} | {r["tokens"]} | {r["bootstrap_candidate"]} |' for r in report['files']]
    lines += ['', '## Retrieval coverage', '', json.dumps(report['retrieval'], ensure_ascii=False), '', '## Manual actions', '']
    if not report['findings']:
        lines += ['No heuristic candidates found. This does not establish that memory is optimal.']
    for f in report['findings']:
        lines += [f'### {f["id"]}: {f["kind"]}', '', f'Confidence: {f["confidence"]}.', '', f['manual_action'], '', 'Before (source evidence):', '']
        for e in f['evidence']:
            lines += [f'- {e["file"]}:{e["line"]}: {e["text"]}']
        lines += ['', 'After (illustrative; verify before editing):', '', '> ' + f['after_example'], '']
    lines += ['## Coverage and limits', ''] + ['- ' + x for x in report['limits']]
    lines += ['', '## Warnings', ''] + ['- ' + x for x in report['warnings']]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--context-budget', type=int, required=True, help='Actual model context capacity in tokens')
    parser.add_argument('--days', type=int, default=30, help='Recent-note window (default 30)')
    parser.add_argument('--frequency', type=int, default=3, help='Distinct days required for frequency promotion')
    parser.add_argument('--today', type=dt.date.fromisoformat, help='Override local date, YYYY-MM-DD')
    parser.add_argument('--retrieval-log', type=Path, help='Optional normalized JSONL; see README')
    parser.add_argument('--encoding', help='Optional installed tiktoken encoding, e.g. cl100k_base')
    parser.add_argument('--max-comparisons', type=int, default=200000)
    parser.add_argument('--format', choices=('markdown', 'json'), default='markdown')
    args = parser.parse_args()
    if min(args.context_budget, args.days, args.frequency, args.max_comparisons) <= 0:
        parser.error('budget, days, frequency and max-comparisons must be positive')
    try:
        report = audit(args)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f'audit: {exc}\n')
    print(json.dumps(report, indent=2, ensure_ascii=False) if args.format == 'json' else markdown(report))


if __name__ == '__main__':
    main()
