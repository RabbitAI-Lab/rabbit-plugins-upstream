#!/usr/bin/env python3
"""Analyze a git diff and output structured metadata as JSON."""

import json
import re
import sys


def classify_type(files, added, removed, diff_text):
    """Classify the change type based on diff content."""
    files_upper = [f.upper() for f in files]
    diff_lower = diff_text.lower()

    # Test files
    test_files = any(
        'test' in f or 'spec' in f or '__' in f or f.endswith('.test.')
        for f in files_upper
    )

    # Docs only
    doc_only = all(
        f.endswith(('.MD', '.RST', '.TXT', '.MDX')) or 'DOCS/' in f
        for f in files_upper
    )

    # Build/CI
    build_files = any(
        f.endswith(('PACKAGE.JSON', 'LOCK', 'TOML', 'YAML', 'YML'))
        and any(k in f for k in ('BUILD', 'CI', 'GITHUB', 'CIRCLECI', 'MAKEFILE'))
        for f in files_upper
    )

    if doc_only:
        return 'docs'
    if build_files and not (added + removed > 50):
        return 'build'
    if test_files and added + removed < 100:
        return 'test'
    if 'revert' in diff_lower[:200]:
        return 'revert'
    if added > removed * 2 and added > 10:
        return 'feat'
    if removed > added * 2:
        return 'refactor'
    if added + removed < 10 and not test_files:
        return 'chore'
    return 'fix'


def extract_scope(files):
    """Extract a likely scope from file paths."""
    if not files:
        return None
    # Take directory name after first src/ or top-level dir
    for f in files:
        parts = f.replace('\\', '/').split('/')
        if 'src' in parts:
            idx = parts.index('src')
            if idx + 1 < len(parts):
                return parts[idx + 1]
        if len(parts) > 1:
            return parts[0]
    return None


def analyze(diff_text):
    """Analyze diff and return metadata dict."""
    lines = diff_text.split('\n')

    # Extract changed files
    files = []
    added = 0
    removed = 0

    for line in lines:
        if line.startswith('diff --git'):
            # diff --git a/path b/path
            parts = line.split()
            if len(parts) >= 4:
                files.append(parts[3][2:])  # strip b/
        elif line.startswith('+') and not line.startswith('+++'):
            added += 1
        elif line.startswith('-') and not line.startswith('---'):
            removed += 1

    change_type = classify_type(files, added, removed, diff_text)
    scope = extract_scope(files)

    return {
        'files': files,
        'added_lines': added,
        'removed_lines': removed,
        'total_changes': added + removed,
        'suggested_type': change_type,
        'suggested_scope': scope,
    }


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            diff_text = f.read()
    else:
        diff_text = sys.stdin.read()

    if not diff_text.strip():
        print(json.dumps({'error': 'empty diff'}, indent=2))
        sys.exit(1)

    result = analyze(diff_text)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
