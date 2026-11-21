#!/usr/bin/env python3
"""
report_generator.py - Generate JSON and HTML review reports.

Produces:
1. JSON report: structured review data for other skills to consume
2. HTML report: visual PR-style review page (for canvas display)

Zero external dependencies. HTML is self-contained (inline CSS/JS).
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Optional, Dict, Any

# Import sibling modules
try:
    from diff_parser import DiffResult, FileDiff
    from annotation_store import AnnotationStore, Annotation, Severity
    from diff_renderer import DiffRenderer
except ImportError:
    import importlib.util
    base_dir = os.path.dirname(__file__)
    for mod_name in ["diff_parser", "annotation_store", "diff_renderer"]:
        spec = importlib.util.spec_from_file_location(
            mod_name, os.path.join(base_dir, f"{mod_name}.py")
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules[mod_name] = mod

    from diff_parser import DiffResult, FileDiff
    from annotation_store import AnnotationStore, Annotation, Severity
    from diff_renderer import DiffRenderer


class ReviewReport:
    """
    Complete review report combining diff data and annotations.

    Usage:
        report = ReviewReport(
            diff_result=diff_result,
            annotations=annotation_store,
            metadata={"branch": "feature-x", "reviewer": "agent"}
        )
        report.save_json("review_report.json")
        report.save_html("review_report.html")
    """

    def __init__(self, diff_result: DiffResult,
                 annotations: Optional[AnnotationStore] = None,
                 metadata: Optional[Dict[str, Any]] = None):
        self.diff = diff_result
        self.annotations = annotations or AnnotationStore()
        self.metadata = metadata or {}
        self.generated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to structured dictionary."""
        # Build file-level report data
        files_data = []
        for file_diff in self.diff.files:
            file_annotations = self.annotations.get_by_file(file_diff.path)
            files_data.append({
                "path": file_diff.path,
                "old_path": file_diff.old_path,
                "status": file_diff.status,
                "additions": file_diff.additions,
                "deletions": file_diff.deletions,
                "is_binary": file_diff.is_binary,
                "hunks": [h.to_dict() for h in file_diff.hunks],
                "annotations": [a.to_dict() for a in file_annotations],
                "annotation_count": len(file_annotations),
            })

        return {
            "version": "1.0",
            "generated_at": self.generated_at,
            "metadata": {
                **self.metadata,
                "total_files": len(self.diff.files),
                "total_additions": self.diff.total_additions,
                "total_deletions": self.diff.total_deletions,
            },
            "files": files_data,
            "annotations": self.annotations.to_dict(),
            "summary": {
                "total_files": len(self.diff.files),
                "total_additions": self.diff.total_additions,
                "total_deletions": self.diff.total_deletions,
                "total_annotations": len(self.annotations.annotations),
                "unresolved_annotations": len(self.annotations.get_unresolved()),
                "issues": self._count_issues_by_severity(),
            },
        }

    def _count_issues_by_severity(self) -> Dict[str, int]:
        """Count annotations by severity."""
        counts = {}
        for ann in self.annotations.annotations:
            sev = ann.severity
            counts[sev] = counts.get(sev, 0) + 1
        return counts

    def to_json(self, indent: int = 2) -> str:
        """Export as JSON string."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def save_json(self, filepath: str) -> None:
        """Save JSON report to file."""
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.to_json())

    def save_html(self, filepath: str) -> None:
        """Generate and save HTML report."""
        html = self._generate_html()
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    def _generate_html(self) -> str:
        """Generate self-contained HTML report."""
        data = self.to_dict()
        meta = data["metadata"]
        summary = data["summary"]

        # Build file sections
        file_sections = []
        for file_data in data["files"]:
            file_sections.append(self._render_file_html(file_data))

        files_html = '\n'.join(file_sections)

        # Severity badge counts
        issues = summary.get("issues", {})
        critical_count = issues.get("critical", 0) + issues.get("required", 0)
        warning_count = issues.get("warning", 0)
        info_count = issues.get("info", 0) + issues.get("nit", 0) + issues.get("suggestion", 0) + issues.get("fyi", 0)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Code Review Report</title>
<style>
:root {{
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-tertiary: #21262d;
    --border: #30363d;
    --text-primary: #c9d1d9;
    --text-secondary: #8b949e;
    --text-muted: #6e7681;
    --green: #3fb950;
    --red: #f85149;
    --yellow: #d29922;
    --blue: #58a6ff;
    --purple: #bc8cff;
    --orange: #f0883e;
    --addition-bg: rgba(63, 185, 80, 0.1);
    --deletion-bg: rgba(248, 81, 73, 0.1);
    --annotation-bg: rgba(210, 153, 34, 0.08);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}}

.header {{
    border-bottom: 1px solid var(--border);
    padding-bottom: 16px;
    margin-bottom: 20px;
}}

.header h1 {{
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 8px;
}}

.header .meta {{
    color: var(--text-secondary);
    font-size: 13px;
}}

.summary-bar {{
    display: flex;
    gap: 16px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}}

.summary-item {{
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 12px 16px;
    min-width: 120px;
}}

.summary-item .label {{
    font-size: 12px;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.summary-item .value {{
    font-size: 24px;
    font-weight: 600;
    margin-top: 4px;
}}

.summary-item .value.green {{ color: var(--green); }}
.summary-item .value.red {{ color: var(--red); }}
.summary-item .value.yellow {{ color: var(--yellow); }}
.summary-item .value.blue {{ color: var(--blue); }}

.file-list {{
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    margin-bottom: 20px;
}}

.file-list-header {{
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    font-weight: 600;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.file-item {{
    padding: 8px 16px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    cursor: pointer;
    transition: background 0.1s;
}}

.file-item:hover {{ background: var(--bg-tertiary); }}
.file-item:last-child {{ border-bottom: none; }}

.file-status {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}}

.file-status.added {{ background: var(--green); }}
.file-status.deleted {{ background: var(--red); }}
.file-status.modified {{ background: var(--yellow); }}
.file-status.renamed {{ background: var(--blue); }}

.file-path {{ flex: 1; font-family: monospace; }}
.file-stats {{ color: var(--text-secondary); font-size: 12px; }}
.file-stats .add {{ color: var(--green); }}
.file-stats .del {{ color: var(--red); }}

.file-section {{
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    margin-bottom: 16px;
    overflow: hidden;
}}

.file-header {{
    padding: 10px 16px;
    background: var(--bg-tertiary);
    border-bottom: 1px solid var(--border);
    font-family: monospace;
    font-size: 13px;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.diff-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    font-size: 12px;
    line-height: 20px;
}}

.diff-table tr {{ border-bottom: 1px solid var(--border); }}
.diff-table tr:last-child {{ border-bottom: none; }}

.diff-table td {{
    padding: 0 10px;
    vertical-align: top;
    white-space: pre;
}}

.diff-table .line-num {{
    width: 50px;
    min-width: 50px;
    text-align: right;
    color: var(--text-muted);
    user-select: none;
    padding-right: 10px;
    border-right: 1px solid var(--border);
}}

.diff-table .line-content {{
    padding-left: 10px;
    word-break: break-all;
    white-space: pre-wrap;
}}

.diff-table tr.addition {{ background: var(--addition-bg); }}
.diff-table tr.addition .line-content::before {{ content: "+"; color: var(--green); margin-right: 4px; }}

.diff-table tr.deletion {{ background: var(--deletion-bg); }}
.diff-table tr.deletion .line-content::before {{ content: "-"; color: var(--red); margin-right: 4px; }}

.diff-table tr.context .line-content {{ color: var(--text-secondary); }}

.hunk-header {{
    background: rgba(88, 166, 255, 0.08);
    color: var(--blue);
    padding: 4px 16px;
    font-size: 12px;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}}

.annotation {{
    background: var(--annotation-bg);
    border-left: 3px solid var(--yellow);
    padding: 8px 12px;
    margin: 4px 0;
    border-radius: 0 4px 4px 0;
    font-size: 13px;
}}

.annotation.critical {{ border-left-color: var(--red); background: rgba(248, 81, 73, 0.08); }}
.annotation.warning {{ border-left-color: var(--orange); background: rgba(240, 136, 62, 0.08); }}
.annotation.info {{ border-left-color: var(--blue); background: rgba(88, 166, 255, 0.08); }}
.annotation.nit {{ border-left-color: var(--text-muted); }}
.annotation.suggestion {{ border-left-color: var(--purple); background: rgba(188, 140, 255, 0.08); }}

.annotation .ann-header {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
    font-size: 12px;
}}

.annotation .severity-badge {{
    padding: 1px 6px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
}}

.severity-badge.critical {{ background: rgba(248, 81, 73, 0.2); color: var(--red); }}
.severity-badge.required {{ background: rgba(240, 136, 62, 0.2); color: var(--orange); }}
.severity-badge.warning {{ background: rgba(210, 153, 34, 0.2); color: var(--yellow); }}
.severity-badge.info {{ background: rgba(88, 166, 255, 0.2); color: var(--blue); }}
.severity-badge.nit {{ background: rgba(110, 118, 129, 0.2); color: var(--text-muted); }}
.severity-badge.suggestion {{ background: rgba(188, 140, 255, 0.2); color: var(--purple); }}

.annotation .ann-message {{ margin-top: 4px; }}
.annotation .ann-suggestion {{
    margin-top: 6px;
    padding: 6px 10px;
    background: var(--bg-tertiary);
    border-radius: 4px;
    font-family: monospace;
    font-size: 12px;
    color: var(--green);
}}

.footer {{
    margin-top: 20px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 12px;
    text-align: center;
}}

.badge {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
}}

.badge.critical {{ background: rgba(248, 81, 73, 0.2); color: var(--red); }}
.badge.warning {{ background: rgba(210, 153, 34, 0.2); color: var(--yellow); }}
.badge.pass {{ background: rgba(63, 185, 80, 0.2); color: var(--green); }}

/* Annotation count badge on file items */
.ann-count {{
    background: rgba(210, 153, 34, 0.2);
    color: var(--yellow);
    padding: 1px 6px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
}}

/* Collapsible sections */
.collapsible-header {{
    cursor: pointer;
    user-select: none;
}}
.collapsible-header::before {{
    content: "▼ ";
    display: inline-block;
    transition: transform 0.2s;
}}
.collapsed .collapsible-header::before {{
    transform: rotate(-90deg);
}}
.collapsed .collapsible-content {{
    display: none;
}}
</style>
</head>
<body>

<div class="header">
    <h1>🔍 Code Review Report</h1>
    <div class="meta">
        Generated: {self.generated_at[:19]}
        {f' | Branch: {meta.get("branch", "N/A")}' if meta.get("branch") else ''}
        {f' | Range: {meta.get("base_sha", "")[:8]}..{meta.get("head_sha", "")[:8]}' if meta.get("base_sha") else ''}
        | Reviewer: {meta.get("reviewer", "agent")}
    </div>
</div>

<div class="summary-bar">
    <div class="summary-item">
        <div class="label">Files Changed</div>
        <div class="value">{summary['total_files']}</div>
    </div>
    <div class="summary-item">
        <div class="label">Additions</div>
        <div class="value green">+{summary['total_additions']}</div>
    </div>
    <div class="summary-item">
        <div class="label">Deletions</div>
        <div class="value red">-{summary['total_deletions']}</div>
    </div>
    <div class="summary-item">
        <div class="label">Annotations</div>
        <div class="value {'yellow' if summary['total_annotations'] > 0 else 'blue'}">{summary['total_annotations']}</div>
    </div>
    <div class="summary-item">
        <div class="label">Issues</div>
        <div class="value {'red' if critical_count > 0 else 'yellow' if warning_count > 0 else 'green'}">
            {critical_count + warning_count + info_count}
        </div>
    </div>
</div>

<div class="file-list">
    <div class="file-list-header">
        <span>Changed Files</span>
        <span>{summary['total_files']} files</span>
    </div>
    {self._render_file_list_html(data['files'])}
</div>

{files_html}

<div class="footer">
    Generated by OpenClaw Code Review Visual System v1.0 | {self.generated_at[:19]}
</div>

<script>
// Collapsible file sections
document.querySelectorAll('.file-section').forEach(section => {{
    const header = section.querySelector('.file-header');
    if (header) {{
        header.classList.add('collapsible-header');
        header.addEventListener('click', () => {{
            section.classList.toggle('collapsed');
        }});
    }}
}});

// File list click to scroll
document.querySelectorAll('.file-item').forEach(item => {{
    item.addEventListener('click', () => {{
        const target = document.getElementById(item.dataset.target);
        if (target) {{
            target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}
    }});
}});
</script>

</body>
</html>"""
        return html

    def _render_file_list_html(self, files_data: List[Dict]) -> str:
        """Render the file list section."""
        items = []
        for f in files_data:
            status_class = f["status"]
            ann_badge = ""
            if f["annotation_count"] > 0:
                ann_badge = f'<span class="ann-count">{f["annotation_count"]}</span>'

            items.append(f"""
    <div class="file-item" data-target="file-{self._safe_id(f['path'])}">
        <div class="file-status {status_class}"></div>
        <span class="file-path">{f['path']}</span>
        {ann_badge}
        <span class="file-stats">
            <span class="add">+{f['additions']}</span>
            <span class="del">-{f['deletions']}</span>
        </span>
    </div>""")
        return '\n'.join(items)

    def _render_file_html(self, file_data: Dict) -> str:
        """Render a single file's diff section."""
        path = file_data["path"]
        safe_id = self._safe_id(path)
        status_label = file_data["status"].upper()

        # Build diff rows
        diff_rows = []
        for hunk in file_data.get("hunks", []):
            # Hunk header
            diff_rows.append(f"""
        <tr><td colspan="4" class="hunk-header">{self._escape(hunk['header'])}</td></tr>""")

            for line in hunk.get("lines", []):
                line_type = line["type"]
                old_num = line.get("old_line") or ""
                new_num = line.get("new_line") or ""
                content = self._escape(line["content"])

                diff_rows.append(f"""
        <tr class="{line_type}">
            <td class="line-num">{old_num}</td>
            <td class="line-num">{new_num}</td>
            <td colspan="2" class="line-content">{content}</td>
        </tr>""")

        diff_html = '\n'.join(diff_rows)

        # Build annotations
        annotations_html = ""
        for ann in file_data.get("annotations", []):
            sev = ann["severity"]
            sev_class = sev if sev in ("critical", "required", "warning", "info", "nit", "suggestion") else "info"
            suggestion_html = ""
            if ann.get("suggestion"):
                suggestion_html = f'<div class="ann-suggestion">💡 {self._escape(ann["suggestion"])}</div>'

            annotations_html += f"""
        <div class="annotation {sev_class}">
            <div class="ann-header">
                <span class="severity-badge {sev_class}">{sev}</span>
                <span>L{ann['line']}</span>
                <span style="color: var(--text-muted)">{ann.get('reviewer', '')}</span>
            </div>
            <div class="ann-message">{self._escape(ann['message'])}</div>
            {suggestion_html}
        </div>"""

        return f"""
<div class="file-section" id="file-{safe_id}">
    <div class="file-header">
        <span>📄 {self._escape(path)} <span style="color: var(--text-muted); font-weight: normal">[{status_label}]</span></span>
        <span class="file-stats">
            <span class="add">+{file_data['additions']}</span>
            <span class="del">-{file_data['deletions']}</span>
        </span>
    </div>
    <div class="collapsible-content">
        <table class="diff-table">
            {diff_html}
        </table>
        {annotations_html}
    </div>
</div>"""

    @staticmethod
    def _escape(text: str) -> str:
        """HTML-escape text."""
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))

    @staticmethod
    def _safe_id(path: str) -> str:
        """Convert file path to safe HTML ID."""
        return path.replace("/", "-").replace(".", "-").replace(" ", "-")


# CLI entry point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate review reports")
    parser.add_argument("diff_file", help="Path to diff file")
    parser.add_argument("--annotations", "-a", help="Path to annotations JSON")
    parser.add_argument("--output-json", "-j", help="Output JSON report path")
    parser.add_argument("--output-html", "-o", help="Output HTML report path")
    parser.add_argument("--branch", help="Branch name")
    parser.add_argument("--reviewer", default="agent", help="Reviewer name")

    args = parser.parse_args()

    # Parse diff
    from diff_parser import parse_diff_file
    diff_result = parse_diff_file(args.diff_file)

    # Load annotations if provided
    annotations = None
    if args.annotations and os.path.exists(args.annotations):
        annotations = AnnotationStore.load(args.annotations)

    # Build metadata
    metadata = {
        "reviewer": args.reviewer,
    }
    if args.branch:
        metadata["branch"] = args.branch

    # Generate report
    report = ReviewReport(diff_result, annotations, metadata)

    if args.output_json:
        report.save_json(args.output_json)
        print(f"JSON report saved to: {args.output_json}")

    if args.output_html:
        report.save_html(args.output_html)
        print(f"HTML report saved to: {args.output_html}")

    if not args.output_json and not args.output_html:
        # Default: print JSON to stdout
        print(report.to_json())
