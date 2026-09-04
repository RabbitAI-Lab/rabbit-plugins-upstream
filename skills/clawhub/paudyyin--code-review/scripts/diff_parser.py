#!/usr/bin/env python3
"""
diff_parser.py - Parse git diff output into structured data.

Zero external dependencies. Pure Python 3.7+ implementation.
Parses unified diff format (git diff output) into a structured representation
suitable for rendering, annotation, and report generation.
"""

import re
import json
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum


class LineType(Enum):
    CONTEXT = "context"
    ADDITION = "addition"
    DELETION = "deletion"
    HUNK_HEADER = "hunk_header"
    FILE_HEADER = "file_header"
    INDEX_LINE = "index"
    BINARY = "binary"


class FileStatus(Enum):
    ADDED = "added"
    DELETED = "deleted"
    MODIFIED = "modified"
    RENAMED = "renamed"
    COPIED = "copied"
    BINARY = "binary"


@dataclass
class DiffLine:
    """A single line in a diff hunk."""
    type: str  # "context", "addition", "deletion"
    content: str
    old_line: Optional[int] = None
    new_line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "content": self.content,
            "old_line": self.old_line,
            "new_line": self.new_line,
        }


@dataclass
class Hunk:
    """A hunk (@@ ... @@) in a diff."""
    old_start: int
    old_lines: int
    new_start: int
    new_lines: int
    header: str  # The @@ line text
    section_heading: Optional[str] = None  # Text after @@ ... @@ on same line
    lines: List[DiffLine] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "old_start": self.old_start,
            "old_lines": self.old_lines,
            "new_start": self.new_start,
            "new_lines": self.new_lines,
            "header": self.header,
            "section_heading": self.section_heading,
            "lines": [line.to_dict() for line in self.lines],
        }


@dataclass
class FileDiff:
    """Diff for a single file."""
    path: str
    old_path: Optional[str] = None  # For renames
    status: str = "modified"  # added, deleted, modified, renamed
    additions: int = 0
    deletions: int = 0
    hunks: List[Hunk] = field(default_factory=list)
    is_binary: bool = False
    old_mode: Optional[str] = None
    new_mode: Optional[str] = None
    similarity: Optional[int] = None  # For renames (rename from/to)

    @property
    def effective_path(self) -> str:
        """Path to use for display (new path for renames)."""
        return self.path

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "old_path": self.old_path,
            "status": self.status,
            "additions": self.additions,
            "deletions": self.deletions,
            "hunks": [h.to_dict() for h in self.hunks],
            "is_binary": self.is_binary,
        }


@dataclass
class DiffResult:
    """Complete parsed diff result."""
    files: List[FileDiff] = field(default_factory=list)
    base_sha: Optional[str] = None
    head_sha: Optional[str] = None
    branch: Optional[str] = None
    total_additions: int = 0
    total_deletions: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "files": [f.to_dict() for f in self.files],
            "base_sha": self.base_sha,
            "head_sha": self.head_sha,
            "branch": self.branch,
            "total_additions": self.total_additions,
            "total_deletions": self.total_deletions,
            "total_files": len(self.files),
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


class DiffParser:
    """
    Parse unified diff format (git diff output) into structured data.

    Usage:
        parser = DiffParser()
        result = parser.parse(diff_text)
        # or
        result = parser.parse_file("path/to/diff.patch")
    """

    # Regex patterns
    RE_DIFF_HEADER = re.compile(r'^diff --git a/(.+?) b/(.+)$')
    RE_INDEX_LINE = re.compile(r'^index ([a-f0-9]+)\.\.([a-f0-9]+)')
    RE_HUNK_HEADER = re.compile(
        r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(.*)'
    )
    RE_OLD_FILE = re.compile(r'^--- (?:a/(.+)|/dev/null)')
    RE_NEW_FILE = re.compile(r'^\+\+\+ (?:b/(.+)|/dev/null)')
    RE_RENAME_FROM = re.compile(r'^rename from (.+)')
    RE_RENAME_TO = re.compile(r'^rename to (.+)')
    RE_NEW_FILE_MODE = re.compile(r'^new file mode (\d+)')
    RE_DELETED_FILE = re.compile(r'^deleted file mode (\d+)')
    RE_SIMILARITY = re.compile(r'^similarity index (\d+)%')
    RE_BINARY = re.compile(r'^Binary files')

    def __init__(self):
        self._result = DiffResult()
        self._current_file: Optional[FileDiff] = None
        self._current_hunk: Optional[Hunk] = None
        self._pending_rename_from: Optional[str] = None

    def parse(self, diff_text: str) -> DiffResult:
        """Parse a unified diff text string."""
        self._result = DiffResult()
        self._current_file = None
        self._current_hunk = None
        self._pending_rename_from = None

        lines = diff_text.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]
            self._process_line(line, lines, i)
            i += 1

        # Finalize last file/hunk
        self._finalize_hunk()
        self._finalize_file()

        # Calculate totals
        for f in self._result.files:
            self._result.total_additions += f.additions
            self._result.total_deletions += f.deletions

        return self._result

    def parse_file(self, filepath: str) -> DiffResult:
        """Parse a diff from a file."""
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            return self.parse(f.read())

    def _process_line(self, line: str, all_lines: List[str], idx: int):
        """Process a single line of diff output."""
        # diff --git header
        m = self.RE_DIFF_HEADER.match(line)
        if m:
            self._finalize_hunk()
            self._finalize_file()
            self._start_file(m.group(1), m.group(2))
            return

        if self._current_file is None:
            return

        # Index line
        m = self.RE_INDEX_LINE.match(line)
        if m:
            return

        # New file mode
        m = self.RE_NEW_FILE_MODE.match(line)
        if m:
            self._current_file.status = "added"
            return

        # Deleted file mode
        m = self.RE_DELETED_FILE.match(line)
        if m:
            self._current_file.status = "deleted"
            return

        # Similarity index (rename)
        m = self.RE_SIMILARITY.match(line)
        if m:
            self._current_file.similarity = int(m.group(1))
            self._current_file.status = "renamed"
            return

        # Rename from/to
        m = self.RE_RENAME_FROM.match(line)
        if m:
            self._pending_rename_from = m.group(1)
            return

        m = self.RE_RENAME_TO.match(line)
        if m:
            if self._pending_rename_from:
                self._current_file.old_path = self._pending_rename_from
                self._current_file.path = m.group(1)
                self._current_file.status = "renamed"
            self._pending_rename_from = None
            return

        # Binary files
        if self.RE_BINARY.match(line):
            self._current_file.is_binary = True
            self._current_file.status = "binary"
            return

        # --- line
        m = self.RE_OLD_FILE.match(line)
        if m:
            if m.group(1) is None:  # /dev/null
                self._current_file.status = "added"
            return

        # +++ line
        m = self.RE_NEW_FILE.match(line)
        if m:
            if m.group(1) is None:  # /dev/null
                self._current_file.status = "deleted"
            return

        # Hunk header
        m = self.RE_HUNK_HEADER.match(line)
        if m:
            self._finalize_hunk()
            self._start_hunk(
                int(m.group(1)),
                int(m.group(2)) if m.group(2) else 1,
                int(m.group(3)),
                int(m.group(4)) if m.group(4) else 1,
                line,
                m.group(5).strip() if m.group(5) else None,
            )
            return

        # Diff content lines
        if self._current_hunk is not None:
            if line.startswith('+'):
                self._add_diff_line("addition", line[1:])
            elif line.startswith('-'):
                self._add_diff_line("deletion", line[1:])
            elif line.startswith(' ') or line == '':
                # Context line (space prefix) or empty context line
                content = line[1:] if line.startswith(' ') else line
                self._add_diff_line("context", content)
            elif line.startswith('\\'):
                # "\ No newline at end of file"
                pass

    def _start_file(self, old_path: str, new_path: str):
        """Start a new file diff."""
        self._current_file = FileDiff(
            path=new_path,
            old_path=old_path if old_path != new_path else None,
        )

    def _finalize_file(self):
        """Finalize the current file."""
        if self._current_file is not None:
            self._result.files.append(self._current_file)
            self._current_file = None

    def _start_hunk(self, old_start: int, old_lines: int,
                    new_start: int, new_lines: int,
                    header: str, section_heading: Optional[str] = None):
        """Start a new hunk."""
        self._current_hunk = Hunk(
            old_start=old_start,
            old_lines=old_lines,
            new_start=new_start,
            new_lines=new_lines,
            header=header,
            section_heading=section_heading,
        )

    def _finalize_hunk(self):
        """Finalize the current hunk."""
        if self._current_hunk is not None and self._current_file is not None:
            self._current_file.hunks.append(self._current_hunk)
            self._current_hunk = None

    def _add_diff_line(self, line_type: str, content: str):
        """Add a line to the current hunk."""
        if self._current_hunk is None or self._current_file is None:
            return

        diff_line = DiffLine(type=line_type, content=content)

        if line_type == "context":
            diff_line.old_line = self._current_hunk.old_start + sum(
                1 for l in self._current_hunk.lines if l.type in ("context", "deletion")
            )
            diff_line.new_line = self._current_hunk.new_start + sum(
                1 for l in self._current_hunk.lines if l.type in ("context", "addition")
            )
        elif line_type == "addition":
            diff_line.new_line = self._current_hunk.new_start + sum(
                1 for l in self._current_hunk.lines if l.type in ("context", "addition")
            )
            self._current_file.additions += 1
        elif line_type == "deletion":
            diff_line.old_line = self._current_hunk.old_start + sum(
                1 for l in self._current_hunk.lines if l.type in ("context", "deletion")
            )
            self._current_file.deletions += 1

        self._current_hunk.lines.append(diff_line)


def parse_diff(diff_text: str) -> DiffResult:
    """Convenience function to parse diff text."""
    parser = DiffParser()
    return parser.parse(diff_text)


def parse_diff_file(filepath: str) -> DiffResult:
    """Convenience function to parse a diff file."""
    parser = DiffParser()
    return parser.parse_file(filepath)


# CLI entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: diff_parser.py <diff_file> [--json]")
        print("       echo 'diff text' | python diff_parser.py -")
        sys.exit(1)

    if sys.argv[1] == '-':
        diff_text = sys.stdin.read()
        result = parse_diff(diff_text)
    else:
        result = parse_diff_file(sys.argv[1])

    output_json = '--json' in sys.argv
    if output_json:
        print(result.to_json())
    else:
        # Summary output
        print(f"Files changed: {len(result.files)}")
        print(f"Additions: +{result.total_additions}")
        print(f"Deletions: -{result.total_deletions}")
        print()
        for f in result.files:
            status_icon = {
                "added": "🟢", "deleted": "🔴", "modified": "🟡",
                "renamed": "📝", "binary": "📦"
            }.get(f.status, "❓")
            print(f"  {status_icon} {f.path} (+{f.additions}/-{f.deletions})")
