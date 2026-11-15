#!/usr/bin/env python3
"""
annotation_store.py - Line-level annotation management for code review.

Supports:
- Adding/removing annotations on specific file:line positions
- Severity levels (critical, warning, info, nit, suggestion)
- Export annotations as JSON for other skills to consume
- Import annotations from external sources
- Merge annotations from multiple reviewers

Zero external dependencies. Pure Python 3.7+ implementation.
"""

import json
import uuid
import os
import sys
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Tuple
from enum import Enum


class Severity(Enum):
    """Annotation severity levels."""
    CRITICAL = "critical"      # Blocks merge
    REQUIRED = "required"      # Must fix before merge
    WARNING = "warning"        # Should fix
    INFO = "info"              # Informational
    NIT = "nit"                # Minor, optional
    SUGGESTION = "suggestion"  # Consider this
    FYI = "fyi"                # For reference only

    @classmethod
    def from_str(cls, s: str) -> 'Severity':
        """Parse severity from string (case-insensitive)."""
        s = s.lower().strip()
        mapping = {
            "critical": cls.CRITICAL,
            "blocker": cls.CRITICAL,
            "required": cls.REQUIRED,
            "must fix": cls.REQUIRED,
            "warning": cls.WARNING,
            "warn": cls.WARNING,
            "info": cls.INFO,
            "informational": cls.INFO,
            "nit": cls.NIT,
            "nitpick": cls.NIT,
            "minor": cls.NIT,
            "suggestion": cls.SUGGESTION,
            "consider": cls.SUGGESTION,
            "optional": cls.SUGGESTION,
            "fyi": cls.FYI,
        }
        return mapping.get(s, cls.INFO)

    @property
    def icon(self) -> str:
        """Get emoji icon for this severity."""
        icons = {
            "critical": "🔴",
            "required": "🟠",
            "warning": "🟡",
            "info": "🔵",
            "nit": "⚪",
            "suggestion": "💡",
            "fyi": "ℹ️",
        }
        return icons.get(self.value, "❓")

    @property
    def sort_order(self) -> int:
        """Sort order (lower = more severe)."""
        orders = {
            "critical": 0,
            "required": 1,
            "warning": 2,
            "info": 3,
            "nit": 4,
            "suggestion": 5,
            "fyi": 6,
        }
        return orders.get(self.value, 99)


@dataclass
class Annotation:
    """A single annotation/comment on a code line."""
    id: str
    file_path: str
    line: int
    side: str = "new"  # "old" or "new"
    severity: str = "info"
    message: str = ""
    suggestion: Optional[str] = None  # Suggested code replacement
    reviewer: str = "agent"
    created_at: str = ""
    resolved: bool = False
    thread_id: Optional[str] = None  # For grouping related annotations
    tags: List[str] = field(default_factory=list)  # e.g., ["security", "performance"]

    def __post_init__(self):
        if not self.id:
            self.id = f"ann-{uuid.uuid4().hex[:8]}"
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "file_path": self.file_path,
            "line": self.line,
            "side": self.side,
            "severity": self.severity,
            "message": self.message,
            "suggestion": self.suggestion,
            "reviewer": self.reviewer,
            "created_at": self.created_at,
            "resolved": self.resolved,
            "thread_id": self.thread_id,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Annotation':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class AnnotationStore:
    """
    Store and manage annotations for a code review session.

    Usage:
        store = AnnotationStore()
        store.add("src/main.py", 42, "Potential null pointer", severity="warning")
        store.add("src/main.py", 55, "Consider using a dict comprehension", severity="suggestion")
        
        # Export
        json_str = store.to_json()
        store.save("review_annotations.json")
        
        # Query
        warnings = store.get_by_severity("warning")
        file_anns = store.get_by_file("src/main.py")
    """

    annotations: List[Annotation] = field(default_factory=list)
    session_id: str = ""
    created_at: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.session_id:
            self.session_id = f"review-{uuid.uuid4().hex[:8]}"
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def add(self, file_path: str, line: int, message: str,
            severity: str = "info", side: str = "new",
            suggestion: Optional[str] = None,
            reviewer: str = "agent",
            tags: Optional[List[str]] = None,
            thread_id: Optional[str] = None) -> Annotation:
        """Add a new annotation."""
        ann = Annotation(
            id="",  # Will be auto-generated
            file_path=file_path,
            line=line,
            side=side,
            severity=severity,
            message=message,
            suggestion=suggestion,
            reviewer=reviewer,
            tags=tags or [],
            thread_id=thread_id,
        )
        self.annotations.append(ann)
        return ann

    def remove(self, annotation_id: str) -> bool:
        """Remove an annotation by ID."""
        before = len(self.annotations)
        self.annotations = [a for a in self.annotations if a.id != annotation_id]
        return len(self.annotations) < before

    def resolve(self, annotation_id: str) -> bool:
        """Mark an annotation as resolved."""
        for ann in self.annotations:
            if ann.id == annotation_id:
                ann.resolved = True
                return True
        return False

    def get_by_file(self, file_path: str) -> List[Annotation]:
        """Get all annotations for a specific file."""
        return sorted(
            [a for a in self.annotations if a.file_path == file_path],
            key=lambda a: (a.line, Severity.from_str(a.severity).sort_order)
        )

    def get_by_severity(self, severity: str) -> List[Annotation]:
        """Get all annotations of a specific severity."""
        return [a for a in self.annotations if a.severity == severity]

    def get_by_reviewer(self, reviewer: str) -> List[Annotation]:
        """Get all annotations from a specific reviewer."""
        return [a for a in self.annotations if a.reviewer == reviewer]

    def get_unresolved(self) -> List[Annotation]:
        """Get all unresolved annotations."""
        return [a for a in self.annotations if not a.resolved]

    def get_sorted(self) -> List[Annotation]:
        """Get all annotations sorted by severity then file then line."""
        return sorted(
            self.annotations,
            key=lambda a: (
                Severity.from_str(a.severity).sort_order,
                a.file_path,
                a.line,
            )
        )

    def get_summary(self) -> Dict[str, Any]:
        """Get annotation summary statistics."""
        severity_counts = {}
        for ann in self.annotations:
            sev = ann.severity
            severity_counts[sev] = severity_counts.get(sev, 0) + 1

        file_counts = {}
        for ann in self.annotations:
            fp = ann.file_path
            file_counts[fp] = file_counts.get(fp, 0) + 1

        return {
            "total": len(self.annotations),
            "unresolved": len(self.get_unresolved()),
            "by_severity": severity_counts,
            "by_file": file_counts,
            "reviewers": list(set(a.reviewer for a in self.annotations)),
        }

    def merge(self, other: 'AnnotationStore') -> None:
        """Merge annotations from another store (e.g., from another reviewer)."""
        existing_ids = {a.id for a in self.annotations}
        for ann in other.annotations:
            if ann.id not in existing_ids:
                self.annotations.append(ann)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "version": "1.0",
            "session_id": self.session_id,
            "created_at": self.created_at,
            "metadata": self.metadata,
            "annotations": [a.to_dict() for a in self.annotations],
            "summary": self.get_summary(),
        }

    def to_json(self, indent: int = 2) -> str:
        """Export as JSON string."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def save(self, filepath: str) -> None:
        """Save annotations to a JSON file."""
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.to_json())

    @classmethod
    def load(cls, filepath: str) -> 'AnnotationStore':
        """Load annotations from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        store = cls(
            session_id=data.get("session_id", ""),
            created_at=data.get("created_at", ""),
            metadata=data.get("metadata", {}),
        )
        for ann_data in data.get("annotations", []):
            store.annotations.append(Annotation.from_dict(ann_data))
        return store

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AnnotationStore':
        """Create from dictionary."""
        store = cls(
            session_id=data.get("session_id", ""),
            created_at=data.get("created_at", ""),
            metadata=data.get("metadata", {}),
        )
        for ann_data in data.get("annotations", []):
            store.annotations.append(Annotation.from_dict(ann_data))
        return store


class AnnotationFormatter:
    """Format annotations for terminal display."""

    def __init__(self, use_color: bool = True):
        self.use_color = use_color

    def format_inline(self, annotations: List[Annotation]) -> str:
        """Format annotations as inline text (for chat/terminal)."""
        if not annotations:
            return "  ✅ No issues found."

        lines = []
        for ann in sorted(annotations, key=lambda a: (a.file_path, a.line)):
            sev = Severity.from_str(ann.severity)
            icon = sev.icon if self.use_color else f"[{ann.severity.upper()}]"
            loc = f"{ann.file_path}:{ann.line}"
            resolved = " ✅" if ann.resolved else ""

            line = f"  {icon} {loc} — {ann.message}{resolved}"
            if ann.suggestion:
                line += f"\n     💡 Suggestion: {ann.suggestion}"
            lines.append(line)

        return '\n'.join(lines)

    def format_grouped_by_file(self, annotations: List[Annotation]) -> str:
        """Format annotations grouped by file."""
        if not annotations:
            return "  ✅ No issues found."

        # Group by file
        by_file: Dict[str, List[Annotation]] = {}
        for ann in annotations:
            by_file.setdefault(ann.file_path, []).append(ann)

        lines = []
        for filepath, file_anns in sorted(by_file.items()):
            lines.append(f"\n  📄 {filepath}")
            lines.append(f"  {'─' * (len(filepath) + 4)}")

            for ann in sorted(file_anns, key=lambda a: a.line):
                sev = Severity.from_str(ann.severity)
                icon = sev.icon if self.use_color else f"[{ann.severity.upper()}]"
                resolved = " ✅" if ann.resolved else ""
                lines.append(f"    {icon} L{ann.line}: {ann.message}{resolved}")
                if ann.suggestion:
                    lines.append(f"       💡 {ann.suggestion}")

        return '\n'.join(lines)

    def format_summary(self, store: AnnotationStore) -> str:
        """Format a summary of all annotations."""
        summary = store.get_summary()
        lines = [
            f"\n  📊 Review Summary",
            f"  {'─' * 30}",
            f"  Total annotations: {summary['total']}",
            f"  Unresolved: {summary['unresolved']}",
        ]

        if summary['by_severity']:
            lines.append("  By severity:")
            for sev, count in sorted(summary['by_severity'].items(),
                                     key=lambda x: Severity.from_str(x[0]).sort_order):
                icon = Severity.from_str(sev).icon
                lines.append(f"    {icon} {sev}: {count}")

        if summary['by_file']:
            lines.append("  By file:")
            for fp, count in sorted(summary['by_file'].items()):
                lines.append(f"    📄 {fp}: {count}")

        return '\n'.join(lines)


# CLI entry point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Annotation store CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add annotation
    add_parser = subparsers.add_parser("add", help="Add an annotation")
    add_parser.add_argument("file", help="File path")
    add_parser.add_argument("line", type=int, help="Line number")
    add_parser.add_argument("message", help="Annotation message")
    add_parser.add_argument("--severity", "-s", default="info",
                           choices=["critical", "required", "warning", "info", "nit", "suggestion", "fyi"])
    add_parser.add_argument("--suggestion", help="Suggested fix")
    add_parser.add_argument("--store-file", default="review_annotations.json",
                           help="Store file path")

    # List annotations
    list_parser = subparsers.add_parser("list", help="List annotations")
    list_parser.add_argument("--store-file", default="review_annotations.json")
    list_parser.add_argument("--file", help="Filter by file")
    list_parser.add_argument("--severity", help="Filter by severity")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show summary")
    summary_parser.add_argument("--store-file", default="review_annotations.json")

    # Export
    export_parser = subparsers.add_parser("export", help="Export as JSON")
    export_parser.add_argument("--store-file", default="review_annotations.json")
    export_parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    if args.command == "add":
        store_file = args.store_file
        if os.path.exists(store_file):
            store = AnnotationStore.load(store_file)
        else:
            store = AnnotationStore()

        ann = store.add(
            file_path=args.file,
            line=args.line,
            message=args.message,
            severity=args.severity,
            suggestion=args.suggestion,
        )
        store.save(store_file)
        print(f"Added annotation {ann.id}: {args.file}:{args.line} [{args.severity}] {args.message}")

    elif args.command == "list":
        if not os.path.exists(args.store_file):
            print("No annotations found.")
            sys.exit(0)
        store = AnnotationStore.load(args.store_file)
        formatter = AnnotationFormatter()

        if args.file:
            anns = store.get_by_file(args.file)
        elif args.severity:
            anns = store.get_by_severity(args.severity)
        else:
            anns = store.get_sorted()

        print(formatter.format_grouped_by_file(anns))

    elif args.command == "summary":
        if not os.path.exists(args.store_file):
            print("No annotations found.")
            sys.exit(0)
        store = AnnotationStore.load(args.store_file)
        formatter = AnnotationFormatter()
        print(formatter.format_summary(store))

    elif args.command == "export":
        if not os.path.exists(args.store_file):
            print("No annotations found.")
            sys.exit(0)
        store = AnnotationStore.load(args.store_file)
        json_str = store.to_json()
        if args.output:
            with open(args.output, 'w') as f:
                f.write(json_str)
            print(f"Exported to {args.output}")
        else:
            print(json_str)

    else:
        parser.print_help()
