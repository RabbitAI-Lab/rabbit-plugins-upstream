#!/usr/bin/env python3
"""
engram-migrate.py — Import existing markdown memory into Engram.

Parses MEMORY.md, memory/*.md, and AGENTS.md into typed Engram nodes
(rule/lesson/contact/fact/project), each tagged with source:<file>#<line>.

TWO MODES:
  --dry-run (default): emits migration-report.md showing what WOULD be stored.
  --apply: actually stores nodes via engram.py's CLI. Originals NEVER modified.

Usage:
  python3 engram/engram-migrate.py --dry-run
  python3 engram/engram-migrate.py --apply
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Engram config
try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WORKSPACE = _cfg["workspace"]
    ENGRAM_CLI = os.path.join(_cfg["engram_dir"], "engram.py")
    BQ_CLI = os.path.join(_cfg["engram_dir"], "bq.py")
except Exception:
    WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENGRAM_CLI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "engram.py")
    BQ_CLI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bq.py")


# ── Node type classification ────────────────────────────────────────────────

# Patterns that indicate a rule/instruction
RULE_PATTERNS = [
    r'\bnever\b', r'\balways\b', r'\bmust\b', r'\bdo not\b', r"\bdon't\b",
    r'\bshall\b', r'\brequired\b', r'\bforbidden\b', r'\brule\b',
    r'\bpolicy\b', r'\bmandate\b', r'\binstruction\b',
]

# Patterns that indicate a contact/person
CONTACT_PATTERNS = [
    r'@\w+\.\w+',  # email-like
    r'\bphone\b', r'\btel\b', r'\btelegram\b', r'\bcontact\b',
    r'\bemail\b.*\b@', r'\breach\b.*\bat\b',
]

# Patterns that indicate a lesson
LESSON_PATTERNS = [
    r'\blesson\b', r'\blearned\b', r'\bmistake\b', r'\bcorrection\b',
    r'\bwrong\b', r'\bshould have\b', r'\bnext time\b',
    r'\bremember\b', r'\bnote\b.*\b:', r'\bWARNING\b',
]

# Patterns that indicate a project/task
PROJECT_PATTERNS = [
    r'\bproject\b', r'\btask\b', r'\bsprint\b', r'\bphase\b',
    r'\bTODO\b', r'\bWIP\b', r'\bin progress\b', r'\bworking on\b',
]


EXPLICIT_MARKERS = {
    "rule": "rule", "lesson": "lesson", "learned": "lesson", "warning": "lesson",
    "contact": "contact", "decision": "decision", "fact": "fact",
    "project": "project", "task": "project", "todo": "project",
}


def classify_text(text: str, heading_context: str = "") -> str:
    """Classify a text block into a node type."""
    combined = (heading_context + " " + text).lower()

    # Explicit marker prefix wins over all heuristics: "- LESSON: ..." IS a lesson
    m = re.match(r"\s*[-*]?\s*\**([A-Za-z]+)\**\s*:", text)
    if m and m.group(1).lower() in EXPLICIT_MARKERS:
        return EXPLICIT_MARKERS[m.group(1).lower()]

    # Check contact first (specific indicators)
    if re.search(r'[\w.]+@[\w.]+\.\w+', text):
        return "contact"
    if any(re.search(p, combined, re.IGNORECASE) for p in CONTACT_PATTERNS):
        # Only if it really looks like contact info, not just a mention
        if re.search(r'(phone|tel|telegram|email|reach|contact)\s*[:=]', combined, re.IGNORECASE):
            return "contact"

    # Rules (imperative language)
    if any(re.search(p, combined, re.IGNORECASE) for p in RULE_PATTERNS):
        return "rule"

    # Lessons
    if any(re.search(p, combined, re.IGNORECASE) for p in LESSON_PATTERNS):
        return "lesson"

    # Projects
    if any(re.search(p, combined, re.IGNORECASE) for p in PROJECT_PATTERNS):
        return "project"

    # Default: fact
    return "fact"


def extract_tags(text: str) -> list:
    """Extract potential tags from text."""
    tags = set()
    # #hashtags
    for m in re.finditer(r'#(\w+)', text):
        tags.add(m.group(1).lower())
    # Common entity patterns
    for m in re.finditer(r'\b(Engram|OpenClaw|WordPress|Telegram|GitHub|Slack)\b', text):
        tags.add(m.group(1).lower())
    return sorted(tags)


def extract_name(text: str, max_len: int = 80) -> str:
    """Extract a concise node name from a text block."""
    # Skip markdown headings and find first substantive line
    lines = text.strip().split('\n')
    first = ''
    for line in lines:
        stripped = line.strip()
        # Skip headings, empty lines, and pure punctuation
        if not stripped or stripped.startswith('#') or stripped.startswith('|'):
            continue
        # Skip list markers for first content word
        if stripped.startswith('- ') or stripped.startswith('* '):
            stripped = stripped[2:].strip()
        first = stripped
        break
    if not first:
        # Fallback: use heading text without #
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                first = stripped.lstrip('#').strip()
                break
    if not first:
        first = lines[0].strip() if lines else ''
    # Truncate at first period if reasonable
    if '.' in first and first.index('.') < max_len:
        first = first[:first.index('.') + 1]
    if len(first) > max_len:
        first = first[:max_len - 3] + '...'
    return first


# ── Markdown parser ─────────────────────────────────────────────────────────

def parse_markdown(filepath: str, source_label: str = None) -> list:
    """Parse a markdown file into (line_no, heading, text, type) tuples.

    Returns list of dicts: {line, heading, text, source, type, name, tags}
    """
    if source_label is None:
        source_label = os.path.relpath(filepath, WORKSPACE)

    results = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except (OSError, FileNotFoundError):
        return results

    current_heading = ""
    current_section_lines = []
    section_start_line = 0

    def emit(text, line_no):
        text = text.strip()
        if not text or len(text) < 20:  # skip trivially short
            return
        node_type = classify_text(text, current_heading)
        name = extract_name(text)
        tags = extract_tags(text)
        results.append({
            "line": line_no,
            "heading": current_heading,
            "text": text,
            "source": f"{source_label}#{line_no}",
            "type": node_type,
            "name": name,
            "tags": tags,
        })

    def flush_section():
        if not current_section_lines:
            return
        # Split the section into per-bullet items so one email in a list
        # doesn't type every sibling bullet as a contact. Top-level bullets
        # start an item; continuation/indented lines stay with their bullet;
        # non-bullet prose is emitted as its own block.
        item_lines, item_start = [], section_start_line
        for off, ln in enumerate(current_section_lines):
            line_no = section_start_line + off
            if re.match(r"^[-*]\s+", ln):
                if item_lines:
                    emit("".join(item_lines), item_start)
                item_lines, item_start = [ln], line_no
            else:
                item_lines.append(ln)
        if item_lines:
            emit("".join(item_lines), item_start)

    for i, line in enumerate(lines, 1):
        # Detect headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)', line)
        if heading_match:
            # Flush previous section
            flush_section()
            current_heading = heading_match.group(2).strip()
            current_section_lines = [line]
            section_start_line = i
        else:
            current_section_lines.append(line)

    # Flush last section
    flush_section()
    return results


def parse_memory_dir(workspace: str) -> list:
    """Parse MEMORY.md and memory/*.md files."""
    all_nodes = []

    # MEMORY.md
    mem_path = os.path.join(workspace, "MEMORY.md")
    if os.path.isfile(mem_path):
        all_nodes.extend(parse_markdown(mem_path, "MEMORY.md"))

    # memory/*.md
    mem_dir = os.path.join(workspace, "memory")
    if os.path.isdir(mem_dir):
        for md_file in sorted(glob_files(mem_dir, "*.md")):
            label = os.path.relpath(md_file, workspace)
            all_nodes.extend(parse_markdown(md_file, label))

    return all_nodes


def parse_agents_file(workspace: str) -> list:
    """Parse AGENTS.md for rules and instructions."""
    agents_path = os.path.join(workspace, "AGENTS.md")
    if not os.path.isfile(agents_path):
        return []

    nodes = parse_markdown(agents_path, "AGENTS.md")
    # AGENTS.md sections are predominantly rules
    for n in nodes:
        if n["type"] == "fact":
            n["type"] = "rule"
    return nodes


def glob_files(directory: str, pattern: str) -> list:
    """Simple glob without importing glob (keep deps minimal)."""
    import fnmatch
    result = []
    try:
        for fname in sorted(os.listdir(directory)):
            if fnmatch.fnmatch(fname, pattern):
                result.append(os.path.join(directory, fname))
    except OSError:
        pass
    return result


# ── Dry-run report ──────────────────────────────────────────────────────────

def generate_report(nodes: list, output_path: str) -> str:
    """Generate a human-readable migration report."""
    lines = [
        "# Engram Migration Report (DRY RUN)",
        f"\n_Generated: {datetime.now(timezone.utc).isoformat()}_\n",
        f"**Total items to migrate:** {len(nodes)}\n",
        "## Summary by Type\n",
    ]

    type_counts = {}
    for n in nodes:
        type_counts[n["type"]] = type_counts.get(n["type"], 0) + 1

    for t in sorted(type_counts):
        lines.append(f"- **{t}**: {type_counts[t]}")

    lines.append("\n## Items\n")
    for i, n in enumerate(nodes, 1):
        lines.append(f"### {i}. [{n['type'].upper()}] {n['name']}")
        lines.append(f"- **Source:** `{n['source']}`")
        lines.append(f"- **Heading:** {n['heading'] or '(none)'}")
        if n['tags']:
            lines.append(f"- **Tags:** {', '.join(n['tags'])}")
        # Truncate text in report
        preview = n['text'][:300]
        if len(n['text']) > 300:
            preview += "..."
        lines.append("- **Content preview:**")
        lines.append("  ```")
        lines.append(f"  {preview}")
        lines.append("  ```")
        lines.append("")

    lines.append("\n---\n")
    lines.append("## Skipped\n")
    lines.append("(Items too short or empty after parsing are skipped)\n")
    lines.append("\n## Apply\n")
    lines.append("To actually store these nodes, run:\n")
    lines.append("```")
    lines.append(f"python3 {os.path.relpath(__file__, WORKSPACE)} --apply")
    lines.append("```\n")

    report = '\n'.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    return report


# ── Apply migration ─────────────────────────────────────────────────────────

def apply_migration(nodes: list) -> tuple:
    """Store nodes via engram.py CLI. Returns (stored, skipped, errors)."""
    stored = 0
    skipped = 0
    errors = []

    for n in nodes:
        # Build store command
        tags_str = ",".join(n["tags"] + [f"source:{n['source']}"])
        # Truncate content for CLI safety
        content = n["text"][:4000]
        name = n["name"][:200]

        cmd = [
            sys.executable, ENGRAM_CLI, "store",
            "--name", name,
            "--type", n["type"],
            "--content", content,
            "--tags", tags_str,
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30,
                cwd=WORKSPACE,
            )
            if result.returncode == 0:
                stored += 1
            else:
                # Try update if node already exists
                cmd_update = [
                    sys.executable, ENGRAM_CLI, "update",
                    "--name", name,
                    "--content", content,
                    "--tags", tags_str,
                    "--merge",
                ]
                result2 = subprocess.run(
                    cmd_update, capture_output=True, text=True, timeout=30,
                    cwd=WORKSPACE,
                )
                if result2.returncode == 0:
                    stored += 1
                else:
                    errors.append(f"Failed to store '{name}': {result.stderr[:200]}")
                    skipped += 1
        except subprocess.TimeoutExpired:
            errors.append(f"Timeout storing '{name}'")
            skipped += 1
        except Exception as e:
            errors.append(f"Error storing '{name}': {e}")
            skipped += 1

    return stored, skipped, errors


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Migrate markdown memory into Engram")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Generate report only (default)")
    parser.add_argument("--apply", action="store_true",
                        help="Actually store nodes in Engram")
    parser.add_argument("--workspace", default=WORKSPACE,
                        help="Workspace root (default: from config)")
    args = parser.parse_args()

    ws = args.workspace if args.workspace != WORKSPACE else WORKSPACE

    print(f"Engram Migration — scanning workspace: {ws}")

    # Collect all nodes
    all_nodes = []
    all_nodes.extend(parse_memory_dir(ws))
    all_nodes.extend(parse_agents_file(ws))

    # Deduplicate by name
    seen_names = set()
    unique_nodes = []
    for n in all_nodes:
        if n["name"] not in seen_names:
            seen_names.add(n["name"])
            unique_nodes.append(n)
        else:
            # Merge tags into existing
            for existing in unique_nodes:
                if existing["name"] == n["name"]:
                    existing["tags"] = sorted(set(existing["tags"] + n["tags"]))
                    break

    print(f"Found {len(all_nodes)} items, {len(unique_nodes)} unique after dedup")

    if args.apply:
        print("APPLY mode: storing nodes in Engram...")
        stored, skipped, errors = apply_migration(unique_nodes)
        print(f"\nMigration complete:")
        print(f"  Stored: {stored}")
        print(f"  Skipped: {skipped}")
        if errors:
            print(f"  Errors: {len(errors)}")
            for e in errors[:10]:
                print(f"    - {e}")
        sys.exit(0 if skipped == 0 else 1)
    else:
        report_path = os.path.join(ws, "migration-report.md")
        report = generate_report(unique_nodes, report_path)
        print(f"\nDRY RUN complete. Report written to: {report_path}")
        print(f"Review the report, then run with --apply to store nodes.")
        sys.exit(0)


if __name__ == "__main__":
    main()