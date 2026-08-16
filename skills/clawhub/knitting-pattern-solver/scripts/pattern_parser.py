#!/usr/bin/env python3
"""
Knitting Pattern Parser & Verifier

Parses standard knitting notation into structured segments, expands repeats,
tracks stitch counts across rows, and flags mismatches.

Usage:
  python pattern_parser.py "k2, p1, *yo, k2tog, rep from * 3 times, k2"
  python pattern_parser.py --verify "CO 100, Row 1: *k2, p2, rep from * to end"
"""

import re
import sys
import argparse
from dataclasses import dataclass, field
from typing import List, Tuple, Optional


# ─── Abbreviation Dictionary ──────────────────────────────────────────────────

STITCH_ABBREVS = {
    # Basic (no change)
    'k': ('knit', 0),
    'p': ('purl', 0),
    'sl': ('slip', 0),
    # Increases
    'yo': ('yarn over', 1),
    'm1': ('make one', 1),
    'm1l': ('make one left', 1),
    'm1r': ('make one right', 1),
    'kfb': ('knit front and back', 1),
    'kf&b': ('knit front and back', 1),
    'pfb': ('purl front and back', 1),
    # Decreases
    'k2tog': ('knit two together', -1),
    'p2tog': ('purl two together', -1),
    'ssk': ('slip slip knit', -1),
    'ssp': ('slip slip purl', -1),
    'k3tog': ('knit three together', -2),
    'sk2po': ('slip 1 knit 2 tog pass over', -2),
    'cdd': ('centered double decrease', -2),
    's2kpo': ('slip 2 knit pass over', -2),
}


@dataclass
class StitchOp:
    """A single stitch operation like 'k2' or 'yo'."""
    abbrev: str
    count: int          # how many times to work it (e.g. k2 = count 2)
    delta: int          # net stitch change
    
    @property
    def description(self) -> str:
        name = STITCH_ABBREVS.get(self.abbrev.lower(), (self.abbrev, 0))[0]
        if self.count > 1:
            return f"{name} ×{self.count}"
        return name
    
    @property
    def total_delta(self) -> int:
        """Total stitch delta for this op.
        For basic stitches (k, p), count doesn't change total stitches.
        For inc/dec, each application changes stitches."""
        # k2 means "knit 2 stitches" — net 0 change
        # yo means "yarn over once" — +1 change
        # k2tog means "knit 2 together once" — -1 change
        # So: for k/p, the count is how many stitches you work (no change)
        # For inc/dec, the count is how many times you do the increase/decrease
        base_delta = STITCH_ABBREVS.get(self.abbrev.lower(), (self.abbrev, 0))[1]
        if base_delta == 0:
            return 0
        return base_delta * self.count


@dataclass
class RepeatSegment:
    """A repeated section, e.g. *k2, p2, rep from * 3 times."""
    ops: List[StitchOp]
    repeat_type: str       # 'count' (N times) or 'to_end' or 'to_last_N'
    repeat_count: int      # for 'count' type, total executions
    remainder: int = 0     # for 'to_last_N' type, stitches remaining after


@dataclass
class Row:
    """A single knitting row instruction."""
    number: int
    raw: str
    ops: List[StitchOp] = field(default_factory=list)
    repeats: List[RepeatSegment] = field(default_factory=list)
    cast_on: Optional[int] = None
    bind_off: Optional[int] = None


@dataclass
class PatternParseResult:
    """Result of parsing a full pattern."""
    rows: List[Row]
    errors: List[str]
    stitch_counts: List[int]  # running count after each row


# ─── Parser ───────────────────────────────────────────────────────────────────

def parse_stitch_token(token: str) -> Optional[StitchOp]:
    """Parse a single stitch token like 'k2', 'yo', 'k2tog', 'p1'."""
    token = token.strip().rstrip(',').strip()
    if not token:
        return None
    
    # Try to match known abbreviations (longest first)
    lower = token.lower()
    for abbrev in sorted(STITCH_ABBREVS.keys(), key=len, reverse=True):
        if lower.startswith(abbrev):
            rest = token[len(abbrev):].strip()
            count = 1
            if rest:
                # Could be a number
                if rest.isdigit():
                    count = int(rest)
                elif rest == '' or rest == '.':
                    count = 1
                else:
                    # Unknown suffix, still parse
                    pass
            delta = STITCH_ABBREVS[abbrev][1]
            return StitchOp(abbrev=abbrev, count=count, delta=delta)
    
    return None


def split_segments(instruction: str) -> List[str]:
    """Split a row instruction into top-level segments.
    Handles comma-separated and repeat notation."""
    # Remove extra whitespace
    instruction = re.sub(r'\s+', ' ', instruction.strip())
    
    # Split on commas first
    parts = re.split(r',\s*', instruction)
    
    # Filter empty
    return [p.strip() for p in parts if p.strip()]


def parse_repeat_segment(text: str) -> Tuple[List[StitchOp], Optional[str], Optional[int]]:
    """Parse a repeat section like '*k2, p2, rep from * 3 times'.
    Returns (ops, repeat_type, repeat_count_or_remainder)."""
    
    # Pattern: *<content> rep from * [to end | N times | to last N sts]
    m = re.match(r'\*(.+?)\s*rep\s+from\s*\*\s*(.*)', text, re.IGNORECASE)
    if not m:
        return [], None, None
    
    content = m.group(1).strip()
    modifier = m.group(2).strip().lower()
    
    # Parse the ops in the repeat
    ops = []
    for part in split_segments(content):
        op = parse_stitch_token(part)
        if op:
            ops.append(op)
    
    # Determine repeat type
    repeat_type = None
    repeat_val = None
    
    if 'to end' in modifier or modifier == '' or modifier == 'to last 0 sts':
        repeat_type = 'to_end'
    elif 'times' in modifier:
        num_match = re.search(r'(\d+)\s*times', modifier)
        if num_match:
            # "3 times" means 3 MORE repetitions (total = 3+1 if counting the first)
            # But conventionally "rep from * 3 times" means do it 3 more times
            # For simplicity, treat as total executions
            repeat_type = 'count'
            repeat_val = int(num_match.group(1))
    elif 'to last' in modifier:
        num_match = re.search(r'to last\s+(\d+)\s*sts?', modifier)
        if num_match:
            repeat_type = 'to_last_N'
            repeat_val = int(num_match.group(1))
    
    return ops, repeat_type, repeat_val


def parse_row(raw_text: str, row_num: int = 0) -> Row:
    """Parse a single row instruction."""
    row = Row(number=row_num, raw=raw_text)
    
    # Check for cast on
    co_match = re.match(r'(?:co|cast on)\s+(\d+)', raw_text, re.IGNORECASE)
    if co_match:
        row.cast_on = int(co_match.group(1))
        return row
    
    # Check for bind off
    bo_match = re.match(r'(?:bo|bind off)\s+(\d+)', raw_text, re.IGNORECASE)
    if bo_match:
        row.bind_off = int(bo_match.group(1))
        return row
    
    # Parse the row
    # First, extract any repeat segments
    repeat_pattern = r'\*.+?rep\s+from\s*\*[^,]*'
    repeats_raw = re.findall(repeat_pattern, raw_text, re.IGNORECASE)
    
    # Remove repeats from the instruction to parse remaining ops
    remaining = re.sub(repeat_pattern, '', raw_text, flags=re.IGNORECASE)
    
    # Parse repeat segments
    for rep_text in repeats_raw:
        ops, rep_type, rep_val = parse_repeat_segment(rep_text)
        if ops and rep_type:
            row.repeats.append(RepeatSegment(
                ops=ops,
                repeat_type=rep_type,
                repeat_count=rep_val or 0,
                remainder=rep_val or 0
            ))
    
    # Parse remaining ops
    for seg in split_segments(remaining):
        op = parse_stitch_token(seg)
        if op:
            row.ops.append(op)
    
    return row


def compute_row_stitch_change(row: Row, current_count: int) -> Tuple[int, List[str]]:
    """Compute stitch change for a row. Returns (new_count, errors)."""
    errors = []
    total_delta = 0
    
    if row.cast_on is not None:
        return row.cast_on, []
    
    if row.bind_off is not None:
        total_delta = -row.bind_off
    else:
        # Simple ops
        for op in row.ops:
            total_delta += op.total_delta
        
        # Repeats
        for rep in row.repeats:
            rep_delta = sum(op.total_delta for op in rep.ops)
            rep_width = sum(op.count if op.total_delta == 0 else 1 for op in rep.ops)
            # Actually repeat width = number of stitches consumed per repeat
            # For k2 = 2 stitches, p1 = 1 stitch, yo = 0 consumed, k2tog = 2 consumed
            
            if rep.repeat_type == 'count':
                total_delta += rep_delta * rep.repeat_count
            elif rep.repeat_type == 'to_end':
                if rep_width > 0 and current_count > 0:
                    num_repeats = current_count // rep_width
                    remainder = current_count % rep_width
                    if remainder != 0:
                        errors.append(
                            f"Row {row.number}: repeat width {rep_width} does not "
                            f"divide evenly into {current_count} stitches "
                            f"(remainder: {remainder})"
                        )
                    total_delta += rep_delta * num_repeats
            elif rep.repeat_type == 'to_last_N':
                available = current_count - rep.remainder
                if rep_width > 0 and available > 0:
                    num_repeats = available // rep_width
                    remainder = available % rep_width
                    if remainder != 0:
                        errors.append(
                            f"Row {row.number}: repeat doesn't divide evenly "
                            f"into available {available} stitches"
                        )
                    total_delta += rep_delta * num_repeats
    
    new_count = current_count + total_delta
    if new_count < 0:
        errors.append(f"Row {row.number}: stitch count goes negative ({new_count})!")
    
    return new_count, errors


def parse_full_pattern(pattern_text: str) -> PatternParseResult:
    """Parse a multi-row pattern and track stitch counts."""
    rows = []
    errors = []
    stitch_counts = []
    
    # Split by rows
    # Handle "CO 100, Row 1: ..., Row 2: ..." or just "Row 1: ..."
    # Also handle plain comma-separated instructions
    
    # Try to split on "Row N:" or "Rnd N:" patterns
    row_splits = re.split(r'(?:Row|Rnd)\s*(\d+)\s*:\s*', pattern_text, flags=re.IGNORECASE)
    
    if len(row_splits) > 1:
        # Structured pattern with Row labels
        idx = 0
        row_num = 0
        for i, part in enumerate(row_splits):
            if i == 0:
                # Text before first "Row" label — could be CO
                pre = part.strip().rstrip(',')
                if pre:
                    row = parse_row(pre, row_num)
                    rows.append(row)
                    row_num += 1
            elif i % 2 == 1:
                # This is the row number
                row_num = int(part)
            else:
                # This is the row content
                content = part.strip().rstrip(',')
                if content:
                    row = parse_row(content, row_num)
                    rows.append(row)
    else:
        # Unstructured — split by commas, treat each as a row or single instruction
        for i, seg in enumerate(split_segments(pattern_text)):
            row = parse_row(seg, i + 1)
            rows.append(row)
    
    # Track stitch counts
    current = 0
    for row in rows:
        if row.cast_on is not None:
            current = row.cast_on
        else:
            current, row_errors = compute_row_stitch_change(row, current)
            errors.extend(row_errors)
        stitch_counts.append(current)
    
    return PatternParseResult(
        rows=rows,
        errors=errors,
        stitch_counts=stitch_counts
    )


def format_row_explanation(row: Row, stitch_count_before: int, stitch_count_after: int) -> str:
    """Format a row as plain English."""
    lines = []
    
    if row.cast_on is not None:
        lines.append(f"Cast on {row.cast_on} stitches.")
        return '\n'.join(lines)
    
    if row.bind_off is not None:
        lines.append(f"Bind off {row.bind_off} stitches. "
                     f"({stitch_count_before} → {stitch_count_after})")
        return '\n'.join(lines)
    
    lines.append(f"Row {row.number}: {row.raw}")
    
    # Explain ops
    for op in row.ops:
        lines.append(f"  • {op.description} (delta: {op.total_delta:+d})")
    
    # Explain repeats
    for rep in row.repeats:
        rep_desc = ', '.join(op.description for op in rep.ops)
        rep_width = sum(op.count if op.total_delta == 0 else (abs(op.delta) if op.delta < 0 else 0) 
                       for op in rep.ops)
        rep_delta = sum(op.total_delta for op in rep.ops)
        
        if rep.repeat_type == 'to_end':
            lines.append(f"  • Repeat: [{rep_desc}] to end of row")
            lines.append(f"    Repeat width: {rep_width} sts, per-repeat delta: {rep_delta:+d}")
            if stitch_count_before > 0 and rep_width > 0:
                n = stitch_count_before // rep_width
                lines.append(f"    {stitch_count_before} ÷ {rep_width} = {n} repeats")
        elif rep.repeat_type == 'count':
            lines.append(f"  • Repeat: [{rep_desc}] {rep.repeat_count} times")
            lines.append(f"    Per-repeat delta: {rep_delta:+d}, "
                        f"total: {rep_delta * rep.repeat_count:+d}")
        elif rep.repeat_type == 'to_last_N':
            lines.append(f"  • Repeat: [{rep_desc}] to last {rep.remainder} stitches")
    
    delta = stitch_count_after - stitch_count_before
    lines.append(f"  → Stitch count: {stitch_count_before} → {stitch_count_after} (net {delta:+d})")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Parse and decode knitting pattern notation'
    )
    parser.add_argument('instruction', nargs='?', 
                       help='Pattern instruction to parse')
    parser.add_argument('--verify', '-v',
                       help='Full pattern to verify stitch counts')
    parser.add_argument('--plain', '-p', action='store_true',
                       help='Output plain English explanation only')
    
    args = parser.parse_args()
    
    if args.verify:
        # Full pattern verification mode
        print("=" * 60)
        print("KNITTING PATTERN VERIFICATION")
        print("=" * 60)
        print()
        
        result = parse_full_pattern(args.verify)
        
        current = 0
        for i, row in enumerate(result.rows):
            before = current
            after = result.stitch_counts[i]
            explanation = format_row_explanation(row, before, after)
            print(explanation)
            print()
            current = after
        
        if result.errors:
            print("⚠️  ERRORS DETECTED:")
            for err in result.errors:
                print(f"  ✗ {err}")
            print()
        else:
            print("✓ All stitch counts verified successfully!")
        
        return
    
    if not args.instruction:
        parser.print_help()
        sys.exit(1)
    
    # Single instruction mode
    print("=" * 60)
    print("PATTERN DECODE")
    print("=" * 60)
    print(f"\nInput: {args.instruction}\n")
    
    row = parse_row(args.instruction, 1)
    
    # For single instruction, assume 100 stitches for repeat calculation
    default_count = row.cast_on if row.cast_on else 100
    
    # Try repeat parsing
    ops, rep_type, rep_val = parse_repeat_segment(args.instruction)
    
    if ops and rep_type:
        # It's a repeat
        rep_width = sum(op.count if op.total_delta == 0 else 1 for op in ops)
        rep_delta = sum(op.total_delta for op in ops)
        
        print("Repeat pattern detected:")
        print(f"  Operations: {', '.join(op.description for op in ops)}")
        print(f"  Repeat width: {rep_width} stitches")
        print(f"  Per-repeat delta: {rep_delta:+d} stitches")
        
        if rep_type == 'to_end':
            print(f"  Repeat type: to end of row")
            if default_count > 0:
                n = default_count // rep_width
                r = default_count % rep_width
                print(f"  At {default_count} stitches: {n} repeats"
                      + (f" (remainder: {r} ⚠️)" if r else " ✓"))
        elif rep_type == 'count':
            print(f"  Repeat type: {rep_val} times")
            print(f"  Total delta: {rep_delta * rep_val:+d} stitches")
        elif rep_type == 'to_last_N':
            print(f"  Repeat type: to last {rep_val} stitches")
        
        # Expanded form
        print(f"\nExpanded sequence (per repeat):")
        for op in ops:
            for _ in range(op.count):
                print(f"  {op.description}")
    else:
        # Simple instruction
        print("Instructions:")
        for op in row.ops:
            print(f"  • {op.description} (delta: {op.total_delta:+d})")
        
        # Show expanded
        print("\nStep-by-step:")
        total = 0
        for op in row.ops:
            for _ in range(op.count):
                total += op.delta
                print(f"  {op.description} → running total delta: {total:+d}")
    
    print()


if __name__ == '__main__':
    main()
