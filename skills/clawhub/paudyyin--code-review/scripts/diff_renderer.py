#!/usr/bin/env python3
"""
diff_renderer.py - Terminal colored diff rendering.

Renders parsed diff data as PR-style colored terminal output.
Supports:
- GitHub-style diff rendering with +/- prefixes
- Side-by-side mode (narrow terminals)
- Compact mode (fewer context lines)
- File-level summary bars
- Line numbering

Zero external dependencies. Uses ANSI escape codes for colors.
Falls back to plain text on non-TTY outputs.
"""

import sys
import os
from typing import List, Optional, Dict, Any, TextIO

# Try to import diff_parser from same directory
try:
    from diff_parser import DiffResult, FileDiff, Hunk, DiffLine
except ImportError:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "diff_parser",
        os.path.join(os.path.dirname(__file__), "diff_parser.py")
    )
    diff_parser = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(diff_parser)
    DiffResult = diff_parser.DiffResult
    FileDiff = diff_parser.FileDiff
    Hunk = diff_parser.Hunk
    DiffLine = diff_parser.DiffLine


# ANSI color codes
class Colors:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Standard colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_CYAN = "\033[96m"

    # Background colors (for diff lines)
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"

    # Combined styles for diff
    ADD_LINE = "\033[32m"       # Green text for additions
    DEL_LINE = "\033[31m"       # Red text for deletions
    HUNK_HEADER = "\033[36m"    # Cyan for @@ headers
    FILE_HEADER = "\033[1;34m"  # Bold blue for file names
    LINE_NUM = "\033[33m"       # Yellow for line numbers
    CONTEXT = "\033[90m"        # Dim/gray for context


class PlainColors:
    """No-op color codes for non-TTY output."""
    def __getattr__(self, name):
        return ""


def get_colors(use_color: Optional[bool] = None) -> Any:
    """Get color codes based on terminal capability."""
    if use_color is None:
        use_color = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return Colors() if use_color else PlainColors()


class DiffRenderer:
    """
    Render parsed diff data to terminal with colors and formatting.

    Usage:
        renderer = DiffRenderer(diff_result)
        renderer.render()                    # Full render to stdout
        renderer.render_to_string()          # Return as string
        renderer.render_file("src/main.py")  # Render single file
    """

    def __init__(self, diff_result: DiffResult, use_color: Optional[bool] = None,
                 context_lines: int = 3, max_width: int = 120,
                 show_line_numbers: bool = True, compact: bool = False):
        self.diff = diff_result
        self.c = get_colors(use_color)
        self.context_lines = context_lines
        self.max_width = max_width
        self.show_line_numbers = show_line_numbers
        self.compact = compact
        self._output: List[str] = []

    def render(self, file: TextIO = None) -> None:
        """Render the full diff to output."""
        output = file or sys.stdout
        text = self.render_to_string()
        output.write(text)

    def render_to_string(self) -> str:
        """Render the full diff and return as string."""
        self._output = []
        self._render_header()
        self._render_summary_bar()

        for file_diff in self.diff.files:
            self._render_file(file_diff)

        self._render_footer()
        return '\n'.join(self._output)

    def render_file(self, filepath: str) -> str:
        """Render a single file's diff."""
        self._output = []
        for file_diff in self.diff.files:
            if file_diff.path == filepath or file_diff.old_path == filepath:
                self._render_file(file_diff)
                break
        return '\n'.join(self._output)

    def render_file_list(self) -> str:
        """Render just the file list summary."""
        self._output = []
        self._render_summary_bar()
        return '\n'.join(self._output)

    def _emit(self, text: str = "") -> None:
        """Add a line to output."""
        self._output.append(text)

    def _render_header(self) -> None:
        """Render the diff header."""
        c = self.c
        width = min(self.max_width, 80)

        self._emit()
        self._emit(f"{c.BOLD}{'═' * width}{c.RESET}")
        self._emit(f"{c.BOLD}  📋 Code Review — Diff Summary{c.RESET}")
        self._emit(f"{c.BOLD}{'═' * width}{c.RESET}")

        if self.diff.branch:
            self._emit(f"  Branch: {c.CYAN}{self.diff.branch}{c.RESET}")
        if self.diff.base_sha and self.diff.head_sha:
            self._emit(f"  Range:  {c.DIM}{self.diff.base_sha[:8]}..{self.diff.head_sha[:8]}{c.RESET}")

        self._emit()

    def _render_summary_bar(self) -> None:
        """Render the file change summary bar."""
        c = self.c
        total_files = len(self.diff.files)
        total_add = self.diff.total_additions
        total_del = self.diff.total_deletions

        self._emit(f"  {c.BOLD}{total_files}{c.RESET} file(s) changed, "
                   f"{c.GREEN}+{total_add}{c.RESET} additions, "
                   f"{c.RED}-{total_del}{c.RESET} deletions")

        # Visual bar
        total = total_add + total_del
        if total > 0:
            bar_width = 40
            add_width = int((total_add / total) * bar_width)
            del_width = bar_width - add_width
            bar = f"{c.GREEN}{'█' * add_width}{c.RED}{'█' * del_width}{c.RESET}"
            self._emit(f"  [{bar}]")
            self._emit()

        # File list
        for f in self.diff.files:
            status_icon = {
                "added": f"{c.GREEN}●{c.RESET}",
                "deleted": f"{c.RED}●{c.RESET}",
                "modified": f"{c.YELLOW}●{c.RESET}",
                "renamed": f"{c.CYAN}●{c.RESET}",
                "binary": f"{c.DIM}●{c.RESET}",
            }.get(f.status, f"{c.DIM}?{c.RESET}")

            add_str = f"{c.GREEN}+{f.additions}{c.RESET}" if f.additions else ""
            del_str = f"{c.RED}-{f.deletions}{c.RESET}" if f.deletions else ""
            changes = f"{add_str}{del_str}".strip()

            self._emit(f"    {status_icon} {f.path}  {c.DIM}{changes}{c.RESET}")

        self._emit()
        self._emit(f"  {c.DIM}{'─' * min(self.max_width - 4, 76)}{c.RESET}")
        self._emit()

    def _render_file(self, file_diff: FileDiff) -> None:
        """Render a single file's diff."""
        c = self.c

        # File header
        status_label = {
            "added": "NEW FILE",
            "deleted": "DELETED",
            "modified": "MODIFIED",
            "renamed": "RENAMED",
            "binary": "BINARY",
        }.get(file_diff.status, "CHANGED")

        self._emit(f"  {c.FILE_HEADER}{'─' * 3} {file_diff.path} {c.RESET} "
                   f"{c.DIM}[{status_label}]{c.RESET}")

        if file_diff.old_path and file_diff.status == "renamed":
            self._emit(f"    {c.DIM}renamed from: {file_diff.old_path}{c.RESET}")

        if file_diff.is_binary:
            self._emit(f"    {c.DIM}(binary file){c.RESET}")
            self._emit()
            return

        # Render each hunk
        for hunk in file_diff.hunks:
            self._render_hunk(hunk, file_diff)

        self._emit()

    def _render_hunk(self, hunk: Hunk, file_diff: FileDiff) -> None:
        """Render a single hunk."""
        c = self.c

        # Hunk header
        if hunk.section_heading:
            self._emit(f"    {c.HUNK_HEADER}{hunk.header}{c.RESET} "
                       f"{c.DIM}{hunk.section_heading}{c.RESET}")
        else:
            self._emit(f"    {c.HUNK_HEADER}{hunk.header}{c.RESET}")

        # Determine which lines to show (context folding)
        visible_lines = self._get_visible_lines(hunk)

        # Render lines
        line_num_width = max(
            len(str(hunk.old_start + hunk.old_lines)),
            len(str(hunk.new_start + hunk.new_lines)),
            3
        )

        for diff_line, is_folded in visible_lines:
            if is_folded:
                self._emit(f"    {c.DIM}{'⋮':^{line_num_width * 2 + 3}}{c.RESET}")
                continue

            self._render_diff_line(diff_line, line_num_width)

    def _get_visible_lines(self, hunk: Hunk):
        """
        Determine which lines to show, with context folding.
        Returns list of (DiffLine, is_folded_marker).
        """
        if not self.compact:
            return [(line, False) for line in hunk.lines]

        # Compact mode: fold long context runs
        result = []
        context_run = 0
        fold_threshold = self.context_lines * 2 + 2

        for line in hunk.lines:
            if line.type == "context":
                context_run += 1
                if context_run <= self.context_lines:
                    result.append((line, False))
                elif context_run == fold_threshold:
                    result.append((line, True))  # Fold marker
                # else: skip
            else:
                if context_run > 0:
                    # Show trailing context
                    for i in range(max(0, context_run - self.context_lines), context_run):
                        idx = len(result) - context_run + i
                        if idx >= 0 and idx < len(result):
                            pass  # Already added
                context_run = 0
                result.append((line, False))

        # Handle trailing context
        return result

    def _render_diff_line(self, line: DiffLine, num_width: int) -> None:
        """Render a single diff line with colors and line numbers."""
        c = self.c

        # Prefix and color based on type
        if line.type == "addition":
            prefix = "+"
            color = c.ADD_LINE
        elif line.type == "deletion":
            prefix = "-"
            color = c.DEL_LINE
        else:
            prefix = " "
            color = ""

        # Line numbers
        if self.show_line_numbers:
            old_num = str(line.old_line or "").rjust(num_width)
            new_num = str(line.new_line or "").rjust(num_width)
            num_str = f"{c.LINE_NUM}{old_num} {new_num}{c.RESET}"
        else:
            num_str = ""

        # Content (truncate if too long)
        content = line.content
        max_content = self.max_width - (num_width * 2 + 6)
        if len(content) > max_content:
            content = content[:max_content - 3] + "..."

        self._emit(f"  {num_str} {color}{prefix} {content}{c.RESET}")

    def _render_footer(self) -> None:
        """Render the diff footer."""
        c = self.c
        width = min(self.max_width, 80)
        self._emit(f"{c.BOLD}{'═' * width}{c.RESET}")
        self._emit()


class InlineDiffRenderer:
    """
    Render compact inline diff for conversation/terminal output.
    More compact than DiffRenderer, suitable for embedding in chat.
    """

    def __init__(self, diff_result: DiffResult, use_color: Optional[bool] = None):
        self.diff = diff_result
        self.c = get_colors(use_color)

    def render_compact(self) -> str:
        """Render a compact single-line summary per file."""
        c = self.c
        lines = []

        for f in self.diff.files:
            status = {"added": "🟢", "deleted": "🔴", "modified": "🟡",
                      "renamed": "📝"}.get(f.status, "❓")
            lines.append(f"  {status} {f.path}  "
                        f"{c.GREEN}+{f.additions}{c.RESET} "
                        f"{c.RED}-{f.deletions}{c.RESET}")

        return '\n'.join(lines)

    def render_changes_only(self, max_lines: int = 20) -> str:
        """Render only changed lines (no context), limited count."""
        c = self.c
        lines = []
        count = 0

        for f in self.diff.files:
            if f.is_binary:
                continue
            for hunk in f.hunks:
                for line in hunk.lines:
                    if line.type in ("addition", "deletion"):
                        if count >= max_lines:
                            remaining = sum(
                                sum(1 for l in h.lines if l.type in ("addition", "deletion"))
                                for ff in self.diff.files for h in ff.hunks
                            ) - count
                            lines.append(f"  {c.DIM}... and {remaining} more changes{c.RESET}")
                            return '\n'.join(lines)

                        prefix = f"{c.GREEN}+{c.RESET}" if line.type == "addition" else f"{c.RED}-{c.RESET}"
                        loc = f"{f.path}:{line.new_line or line.old_line}"
                        lines.append(f"  {prefix} {c.DIM}{loc}{c.RESET} {line.content[:80]}")
                        count += 1

        return '\n'.join(lines)


# CLI entry point
if __name__ == "__main__":
    from diff_parser import parse_diff, parse_diff_file

    if len(sys.argv) < 2:
        print("Usage: diff_renderer.py <diff_file> [--compact] [--no-color] [--context N]")
        sys.exit(1)

    filepath = sys.argv[1]
    compact = '--compact' in sys.argv
    no_color = '--no-color' in sys.argv
    context = 3
    if '--context' in sys.argv:
        idx = sys.argv.index('--context')
        if idx + 1 < len(sys.argv):
            context = int(sys.argv[idx + 1])

    if filepath == '-':
        result = parse_diff(sys.stdin.read())
    else:
        result = parse_diff_file(filepath)

    use_color = not no_color
    renderer = DiffRenderer(result, use_color=use_color, context_lines=context, compact=compact)
    renderer.render()
