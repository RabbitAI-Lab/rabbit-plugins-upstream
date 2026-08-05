#!/usr/bin/env python3
"""add_language.py — Add a new language section to a multilingual markdown template.

Usage:
    python3 add_language.py <file-path> <lang-code> <lang-name> <flag-emoji>

Reads the template, finds each scenario section, and inserts a new language
subsection after the last existing language in each section.

The agent should provide translations for each scenario. This script handles
the structural insertion; translations come from the agent or a translation step.

Example:
    python3 add_language.py common-responses.md ja 日本語 🇯🇵
"""

import re
import sys
from pathlib import Path

def add_language(filepath: str, lang_code: str, lang_name: str, flag: str):
    p = Path(filepath)
    content = p.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Find all "### <flag> <lang>" headers to understand existing languages
    lang_header_re = re.compile(r"^### (.+)$")
    section_re = re.compile(r"^## \d+\.")

    # For each section, find where the last language block ends (before next ## or ---)
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # At section boundaries (## N. Title), after all existing ### blocks,
        # we'll insert the new language placeholder before the next --- or ##
        if section_re.match(line):
            # Scan ahead to find all ### blocks in this section
            j = i + 1
            last_lang_line = i
            while j < len(lines) and not lines[j].startswith("## ") and lines[j].strip() != "---":
                if lang_header_re.match(lines[j]):
                    last_lang_line = j
                j += 1
            # Find the end of the last language block (blank line before --- or next section)
            insert_pos = last_lang_line + 1
            while insert_pos < j and lines[insert_pos].strip() != "":
                insert_pos += 1
            # We'll insert after the section content — actually simpler:
            # just note we need to add. For now, append placeholder at section end.
            pass

        i += 1

    # Simpler approach: just append the new language header+placeholder to each section
    # This is a structural helper; the agent fills in translations
    result = content
    # Find all section headers and insert after last ### in each
    sections = re.split(r"(^## \d+\..*$)", result, flags=re.MULTILINE)

    output = sections[0]  # preamble
    for idx in range(1, len(sections), 2):
        header = sections[idx]
        body = sections[idx + 1] if idx + 1 < len(sections) else ""

        # Check if this language already exists
        if f"### {flag}" in body:
            output += header + body
            continue

        # Insert new language block before the closing --- or end
        # Find the last ### block's end
        new_block = f"\n### {flag} {lang_name}\n\n_TRANSLATE: Add {lang_name} translation here_\n"

        # Insert before the trailing ---
        if "---" in body:
            parts = body.rsplit("---", 1)
            body = parts[0] + new_block + "\n---" + parts[1]
        else:
            body = body + new_block

        output += header + body

    # Update TOC / language list if present
    output = output.replace(
        "支持语言：",
        f"支持语言："
    )

    p.write_text(output, encoding="utf-8")
    print(f"Added {lang_name} ({lang_code}) placeholders to {filepath}")
    print("Fill in translations for each ### block marked _TRANSLATE_")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <file> <lang-code> <lang-name> <flag>")
        sys.exit(1)
    add_language(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
