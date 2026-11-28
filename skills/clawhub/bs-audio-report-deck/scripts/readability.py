#!/usr/bin/env python3
"""Raise slide text that renders too small for the content language.

Many styles are designed around English editorial type, where 10px body copy
still reads; Chinese, Japanese and Korean copy at that size does not. After
measuring in the browser (see references/readability.md), raise only what is
below the floor:

    python3 scripts/readability.py --project project.json \
        --rule 'p=13.5/1.75' --rule '.content-label=10.5' --rule '#cover-m-cover-11=14'

A rule is SELECTOR=SIZE[/LINE-HEIGHT] in px. `#<node-id>` targets one node by its
project ID; any other selector is scoped to the slide content. The rules are kept
in one marked block of the project's `contentCSS`, replaced on every run, so the
command can be re-run after each compose. `--clear` removes the block.
Standard library only.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

START = "/* narrated-readability:start */"
END = "/* narrated-readability:end */"
SELECTOR = re.compile(r"^[#.\w\s\-\[\]=\"':>*,()]+$")


def parse_rule(raw):
    if "=" not in raw:
        raise ValueError(f"Rule {raw!r} needs SELECTOR=SIZE.")
    selector, value = raw.rsplit("=", 1)
    selector = selector.strip()
    if not selector or not SELECTOR.match(selector) or "{" in selector or "}" in selector:
        raise ValueError(f"Unsupported selector {selector!r}.")
    size, _, line = value.partition("/")
    size = float(size)
    if not 6 <= size <= 72:
        raise ValueError(f"Size {size} is outside 6-72px.")
    declarations = [f"font-size:{size:g}px!important"]
    if line:
        height = float(line)
        if not 1 <= height <= 3:
            raise ValueError(f"Line height {height} is outside 1-3.")
        declarations.append(f"line-height:{height:g}!important")
    if selector.startswith("#") and re.fullmatch(r"#[\w\-]+", selector):
        target = f'.slide[data-imported] [data-node="{selector[1:]}"]'
    else:
        target = ", ".join(f".slide[data-imported] {part.strip()}" for part in selector.split(","))
    return f"{target}{{{';'.join(declarations)}}}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--rule", action="append", default=[])
    parser.add_argument("--clear", action="store_true")
    args = parser.parse_args()
    if not args.rule and not args.clear:
        parser.error("give at least one --rule, or --clear")

    payload = json.loads(args.project.read_text(encoding="utf-8"))
    project = payload.get("project", payload)
    css = project.get("contentCSS", "") or ""
    css = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", css, flags=re.S).rstrip()
    rules = [] if args.clear else [parse_rule(raw) for raw in args.rule]
    if rules:
        css = f"{css}\n{START}\n" + "\n".join(rules) + f"\n{END}\n"
    project["contentCSS"] = css
    args.project.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"ok": True, "rules": len(rules), "project": str(args.project.resolve())}))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"readability.py: {error}", file=sys.stderr)
        sys.exit(1)
