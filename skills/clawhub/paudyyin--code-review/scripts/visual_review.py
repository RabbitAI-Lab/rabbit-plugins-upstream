#!/usr/bin/env python3
"""
visual_review.py - Main entry point for the visual code review system.

Provides a unified CLI for:
1. Parsing git diffs
2. Rendering colored terminal output
3. Managing annotations
4. Generating reports (JSON + HTML)

Usage:
    # Full review with terminal output
    python visual_review.py diff HEAD~1

    # Generate HTML report
    python visual_review.py report --html review.html

    # Add annotation
    python visual_review.py annotate src/main.py 42 --severity warning -m "Potential null pointer"

    # Export structured JSON
    python visual_review.py export --json review.json

    # Quick summary
    python visual_review.py summary HEAD~1

Zero external dependencies. Pure Python 3.7+.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from typing import Optional, List

# Add scripts dir to path for imports
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from diff_parser import DiffParser, DiffResult, parse_diff, parse_diff_file
from diff_renderer import DiffRenderer, InlineDiffRenderer, get_colors
from annotation_store import AnnotationStore, Annotation, AnnotationFormatter, Severity
from report_generator import ReviewReport


def run_git(*args, cwd: Optional[str] = None) -> str:
    """Run a git command and return output."""
    cmd = ["git"] + list(args)
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            cwd=cwd or os.getcwd(), encoding='utf-8', errors='replace'
        )
        if result.returncode != 0:
            print(f"Git error: {result.stderr.strip()}", file=sys.stderr)
            return ""
        return result.stdout
    except FileNotFoundError:
        print("Error: git not found in PATH", file=sys.stderr)
        return ""


def get_diff(args: List[str], cwd: Optional[str] = None) -> str:
    """Get git diff output. If first arg is an existing file, read it directly."""
    if not args:
        return run_git("diff", "HEAD", cwd=cwd)
    elif os.path.isfile(args[0]):
        # Treat as a patch/diff file
        with open(args[0], 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    elif args[0] == '--cached':
        return run_git("diff", "--cached", cwd=cwd)
    elif args[0] == '--':
        return run_git("diff", "HEAD", *args[1:], cwd=cwd)
    else:
        # Assume it's a range like HEAD~1 or branch1..branch2
        return run_git("diff", *args, cwd=cwd)


def cmd_diff(args: argparse.Namespace) -> int:
    """Handle 'diff' subcommand - render colored diff."""
    diff_text = get_diff(args.git_args)
    if not diff_text:
        print("No diff output.")
        return 1

    result = parse_diff(diff_text)

    # Get branch info
    branch = run_git("rev-parse", "--abbrev-ref", "HEAD").strip()
    result.branch = branch or None

    renderer = DiffRenderer(
        result,
        use_color=not args.no_color,
        context_lines=args.context,
        compact=args.compact,
        show_line_numbers=not args.no_line_numbers,
    )
    renderer.render()
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    """Handle 'summary' subcommand - compact file summary."""
    diff_text = get_diff(args.git_args)
    if not diff_text:
        print("No diff output.")
        return 1

    result = parse_diff(diff_text)
    renderer = InlineDiffRenderer(result, use_color=not args.no_color)
    
    print(f"\n  📋 Changes: {len(result.files)} files, "
          f"+{result.total_additions} -{result.total_deletions} lines\n")
    print(renderer.render_compact())

    if args.changes:
        print(f"\n  📝 Changed lines:\n")
        print(renderer.render_changes_only(max_lines=args.max_lines))

    print()
    return 0


def cmd_annotate(args: argparse.Namespace) -> int:
    """Handle 'annotate' subcommand - add annotation."""
    store_file = args.store or "review_annotations.json"

    if os.path.exists(store_file):
        store = AnnotationStore.load(store_file)
    else:
        store = AnnotationStore()

    ann = store.add(
        file_path=args.file,
        line=args.line,
        message=args.message,
        severity=args.severity,
        side=args.side,
        suggestion=args.suggestion,
        reviewer=args.reviewer,
        tags=args.tags.split(",") if args.tags else None,
    )
    store.save(store_file)

    c = get_colors()
    sev = Severity.from_str(args.severity)
    print(f"  {sev.icon} Annotation added: {c.BOLD}{args.file}:{args.line}{c.RESET} "
          f"[{args.severity}] {args.message}")
    print(f"    ID: {ann.id}")
    return 0


def cmd_annotations(args: argparse.Namespace) -> int:
    """Handle 'annotations' subcommand - list/manage annotations."""
    store_file = args.store or "review_annotations.json"

    if not os.path.exists(store_file):
        print("  No annotations found.")
        return 0

    store = AnnotationStore.load(store_file)
    formatter = AnnotationFormatter(use_color=not args.no_color)

    if args.action == "list":
        if args.file:
            anns = store.get_by_file(args.file)
        elif args.severity:
            anns = store.get_by_severity(args.severity)
        else:
            anns = store.get_sorted()

        if args.format == "grouped":
            print(formatter.format_grouped_by_file(anns))
        else:
            print(formatter.format_inline(anns))

    elif args.action == "summary":
        print(formatter.format_summary(store))

    elif args.action == "resolve":
        if store.resolve(args.id):
            store.save(store_file)
            print(f"  ✅ Resolved annotation {args.id}")
        else:
            print(f"  ❌ Annotation {args.id} not found")
            return 1

    elif args.action == "remove":
        if store.remove(args.id):
            store.save(store_file)
            print(f"  🗑️ Removed annotation {args.id}")
        else:
            print(f"  ❌ Annotation {args.id} not found")
            return 1

    return 0


def cmd_report(args: argparse.Namespace) -> int:
    """Handle 'report' subcommand - generate reports."""
    diff_text = get_diff(args.git_args)
    if not diff_text:
        print("No diff output.")
        return 1

    result = parse_diff(diff_text)

    # Load annotations if available
    annotations = None
    store_file = args.annotations or "review_annotations.json"
    if os.path.exists(store_file):
        annotations = AnnotationStore.load(store_file)

    # Build metadata
    branch = run_git("rev-parse", "--abbrev-ref", "HEAD").strip()
    base_sha = run_git("rev-parse", "HEAD~1").strip() if not args.base else args.base
    head_sha = run_git("rev-parse", "HEAD").strip()

    metadata = {
        "branch": branch,
        "base_sha": base_sha,
        "head_sha": head_sha,
        "reviewer": args.reviewer or "agent",
        "mode": args.mode or "standard",
    }

    report = ReviewReport(result, annotations, metadata)

    output_dir = args.output_dir or "."
    os.makedirs(output_dir, exist_ok=True)

    if args.json:
        json_path = os.path.join(output_dir, args.json)
        report.save_json(json_path)
        print(f"  📄 JSON report saved: {json_path}")

    if args.html:
        html_path = os.path.join(output_dir, args.html)
        report.save_html(html_path)
        print(f"  🌐 HTML report saved: {html_path}")

    if not args.json and not args.html:
        # Default: print JSON to stdout
        print(report.to_json())

    return 0


def cmd_export(args: argparse.Namespace) -> int:
    """Handle 'export' subcommand - export structured data."""
    diff_text = get_diff(args.git_args)
    if not diff_text:
        print("No diff output.")
        return 1

    result = parse_diff(diff_text)

    if args.format == "json":
        print(result.to_json())
    elif args.format == "stat":
        # git diff --stat style
        for f in result.files:
            total = f.additions + f.deletions
            bar_width = min(total, 50)
            add_width = int((f.additions / max(total, 1)) * bar_width)
            del_width = bar_width - add_width
            bar = "+" * add_width + "-" * del_width
            print(f"  {f.path:<40} | {bar:>50} {f.additions + f.deletions}")
        print(f"\n  {len(result.files)} files changed, "
              f"{result.total_additions} insertions(+), "
              f"{result.total_deletions} deletions(-)")

    return 0


def cmd_serve(args: argparse.Namespace) -> int:
    """Handle 'serve' subcommand - generate HTML and open in canvas."""
    diff_text = get_diff(args.git_args)
    if not diff_text:
        print("No diff output.")
        return 1

    result = parse_diff(diff_text)

    # Load annotations
    annotations = None
    store_file = args.annotations or "review_annotations.json"
    if os.path.exists(store_file):
        annotations = AnnotationStore.load(store_file)

    branch = run_git("rev-parse", "--abbrev-ref", "HEAD").strip()
    head_sha = run_git("rev-parse", "HEAD").strip()

    metadata = {
        "branch": branch,
        "head_sha": head_sha,
        "reviewer": "agent",
    }

    report = ReviewReport(result, annotations, metadata)

    # Save HTML to workspace
    output_path = os.path.join(
        os.environ.get("USERPROFILE", os.path.expanduser("~")),
        "AppData", "Roaming", "mx", "openclaw-home", "yindb2",
        ".openclaw", "workspace", "review_report.html"
    )
    report.save_html(output_path)
    print(f"  🌐 HTML report generated: {output_path}")
    print(f"  Use 'canvas present' to display in browser.")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Visual Code Review System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s diff HEAD~1              Show colored diff
  %(prog)s diff --cached            Show staged changes
  %(prog)s summary HEAD~3           Compact summary of last 3 commits
  %(prog)s annotate src/main.py 42 -s warning -m "Null check needed"
  %(prog)s annotations list         List all annotations
  %(prog)s annotations summary      Show annotation summary
  %(prog)s report --html report.html  Generate HTML report
  %(prog)s export --format json     Export diff as JSON
  %(prog)s serve                    Generate HTML for canvas display
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # diff
    diff_parser = subparsers.add_parser("diff", help="Show colored diff")
    diff_parser.add_argument("git_args", nargs="*", help="Git diff arguments")
    diff_parser.add_argument("--no-color", action="store_true")
    diff_parser.add_argument("--compact", action="store_true", help="Fold long context")
    diff_parser.add_argument("--context", type=int, default=3, help="Context lines")
    diff_parser.add_argument("--no-line-numbers", action="store_true")

    # summary
    summary_parser = subparsers.add_parser("summary", help="Compact file summary")
    summary_parser.add_argument("git_args", nargs="*", help="Git diff arguments")
    summary_parser.add_argument("--no-color", action="store_true")
    summary_parser.add_argument("--changes", action="store_true", help="Show changed lines")
    summary_parser.add_argument("--max-lines", type=int, default=20)

    # annotate
    ann_parser = subparsers.add_parser("annotate", help="Add annotation")
    ann_parser.add_argument("file", help="File path")
    ann_parser.add_argument("line", type=int, help="Line number")
    ann_parser.add_argument("-m", "--message", required=True, help="Annotation message")
    ann_parser.add_argument("-s", "--severity", default="info",
                           choices=["critical", "required", "warning", "info",
                                   "nit", "suggestion", "fyi"])
    ann_parser.add_argument("--side", default="new", choices=["old", "new"])
    ann_parser.add_argument("--suggestion", help="Suggested fix")
    ann_parser.add_argument("--reviewer", default="agent")
    ann_parser.add_argument("--tags", help="Comma-separated tags")
    ann_parser.add_argument("--store", help="Annotation store file")

    # annotations (list/manage)
    anns_parser = subparsers.add_parser("annotations", help="List/manage annotations")
    anns_parser.add_argument("action", choices=["list", "summary", "resolve", "remove"])
    anns_parser.add_argument("--file", help="Filter by file")
    anns_parser.add_argument("--severity", help="Filter by severity")
    anns_parser.add_argument("--format", default="grouped", choices=["inline", "grouped"])
    anns_parser.add_argument("--id", help="Annotation ID (for resolve/remove)")
    anns_parser.add_argument("--store", help="Annotation store file")
    anns_parser.add_argument("--no-color", action="store_true")

    # report
    report_parser = subparsers.add_parser("report", help="Generate reports")
    report_parser.add_argument("git_args", nargs="*", help="Git diff arguments")
    report_parser.add_argument("--json", help="Output JSON filename")
    report_parser.add_argument("--html", help="Output HTML filename")
    report_parser.add_argument("--output-dir", help="Output directory")
    report_parser.add_argument("--annotations", help="Annotations JSON file")
    report_parser.add_argument("--reviewer", help="Reviewer name")
    report_parser.add_argument("--mode", help="Review mode")
    report_parser.add_argument("--base", help="Base SHA")

    # export
    export_parser = subparsers.add_parser("export", help="Export structured data")
    export_parser.add_argument("git_args", nargs="*", help="Git diff arguments")
    export_parser.add_argument("--format", default="json", choices=["json", "stat"])

    # serve
    serve_parser = subparsers.add_parser("serve", help="Generate HTML for canvas")
    serve_parser.add_argument("git_args", nargs="*", help="Git diff arguments")
    serve_parser.add_argument("--annotations", help="Annotations JSON file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "diff": cmd_diff,
        "summary": cmd_summary,
        "annotate": cmd_annotate,
        "annotations": cmd_annotations,
        "report": cmd_report,
        "export": cmd_export,
        "serve": cmd_serve,
    }

    handler = commands.get(args.command)
    if handler:
        return handler(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
