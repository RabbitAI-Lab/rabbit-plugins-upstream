#!/usr/bin/env python3
"""Check an edit plan against a word-timed transcript before rendering.

Verifies that no content word is clipped by a cut, reports how much speech the plan
removes, and compares content characters against the edited transcript so a lost
syllable or a dropped phrase shows up as a number rather than a listening test.
"""
import argparse
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

FILLERS = {'阿','嗯', '呃', '啊', '噢', '哦', '唔', '额', '唉'}
PUNCTUATION = '，。？！、：；,.?!:;﹑—… ()（）”””'
_EN_FILLER = re.compile(r'^(?:umm*|uhh*|ermm*|hmm+)$', re.I)


def content(text):
    return ''.join(c for c in text if c not in PUNCTUATION)


def is_filler(text):
    stripped = content(text)
    if not stripped:
        return False
    return all(c in FILLERS for c in stripped) or bool(_EN_FILLER.match(stripped))


def read_words(path):
    words = json.loads(Path(path).read_text(encoding='utf-8'))['words']
    return [dict(text=w['text'], start=float(w['start']), end=float(w['end'])) for w in words]


def read_plan(path, end):
    """Read the kept intervals and the ranges dropped on purpose.

    An interval ending in null runs to end, in seconds."""
    spec = json.loads(Path(path).read_text(encoding='utf-8'))
    fps = Fraction(str(spec['fps']))

    def intervals(key):
        spans = []
        for left, right in spec.get(key, []):
            if right is None and isinstance(left, int):
                right = max(left+1, math.ceil(end*fps))
            if not isinstance(left, int) or not isinstance(right, int) or left >= right or left < 0:
                raise ValueError(f'Each {key} interval needs two ordered nonnegative frame indices.')
            spans.append((left, right))
        return spans

    return fps, intervals('keep'), intervals('drop')


def coverage(spans, fps, end):
    """Kept and removed seconds, plus the removed ranges in source order."""
    kept = sum(right-left for left, right in spans)/float(fps)
    holes, cursor = [], 0
    for left, right in sorted(spans):
        if left > cursor:
            holes.append((cursor/float(fps), left/float(fps)))
        cursor = max(cursor, right)
    if cursor/float(fps) < end:
        holes.append((cursor/float(fps), end))
    return kept, holes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('words', type=Path, help='Word-timed transcript of the source')
    parser.add_argument('plan', type=Path, help='Edit plan in source frames')
    parser.add_argument('--edited', type=Path, help='Word-timed transcript of the rendered cut')
    parser.add_argument('--tolerance', type=float, default=0.05,
                        help='Seconds a cut may overlap a word before it counts as damage')
    parser.add_argument('--limit', type=int, default=12, help='Damaged words to list')
    args = parser.parse_args()

    source = read_words(args.words)
    if not source:
        parser.error('The transcript has no words.')
    speech_end = max(w['end'] for w in source) + .5
    fps, spans, drops = read_plan(args.plan, speech_end)
    kept, holes = coverage(spans, fps, speech_end)
    ordered = sorted(spans)

    print(f'plan      {float(fps):g} fps, {len(ordered)} kept intervals, '
          f'{len(holes)} cuts, keeps {kept:.2f}s of {speech_end:.2f}s')

    status = 0
    if any(ordered[i][0] < ordered[i-1][1] for i in range(1, len(ordered))):
        status = 1
        print('FAIL      kept intervals overlap in source coordinates')
    if any(a < right and left < b for a, b in drops for left, right in spans):
        status = 1
        print('FAIL      a drop range overlaps kept footage')

    # Speech the user asked to remove, by trimming or for a highlight, is listed under
    # drop. Words wholly inside it are left out of both checks; one that straddles its
    # edge is still damage, since the boundary belongs in the gap between two words.
    margin = args.tolerance
    dropped = [(a/float(fps)-margin, b/float(fps)+margin) for a, b in drops]

    def chosen(word):
        return any(a <= word['start'] and word['end'] <= b for a, b in dropped)

    damaged, borderline, removed = [], 0, 0
    for word in source:
        if not content(word['text']) or is_filler(word['text']):
            continue
        if chosen(word):
            removed += len(content(word['text']))
            continue
        worst = 0.0
        for left, right in holes:
            overlap = min(right, word['end'])-max(left, word['start'])
            worst = max(worst, overlap)
        # A cut inside the word loses its onset or tail. Cutting the gap between two
        # words overlaps neither, so this stays quiet on a well-placed edit.
        if worst > args.tolerance:
            damaged.append((worst, word))
        elif worst > args.tolerance/2:
            borderline += 1

    total = sum(len(content(w['text'])) for w in source
                if content(w['text']) and not is_filler(w['text']))
    print(f'source    {len(source)} tokens, {total} content characters')
    if drops:
        print(f'drop      {removed} content characters removed on purpose')
        total -= removed
    if damaged:
        status = 1
        damaged.sort(key=lambda item: -item[0])
        print(f'FAIL      {len(damaged)} content words straddle a cut')
        for worst, word in damaged[:args.limit]:
            print(f'          -{worst:.3f}s  {word["start"]:.2f}-{word["end"]:.2f}  {word["text"]}')
    else:
        print('OK        every cut falls between words')
    if borderline:
        print(f'          {borderline} more cuts overlap a word by under {args.tolerance:.2f}s')

    if args.edited:
        edited = read_words(args.edited)
        count = sum(len(content(w['text'])) for w in edited
                    if content(w['text']) and not is_filler(w['text']))
        delta = count-total
        print(f'edited    {len(edited)} tokens, {count} content characters ({delta:+d})')
        if delta:
            status = 1
            print('FAIL      the cut lost or invented speech; compare both transcripts')
        else:
            print('OK        the cut removed only fillers and pauses'+(' besides the drops' if drops else ''))

    print('PASS' if status == 0 else 'REVIEW BEFORE RENDERING')
    return status


if __name__ == '__main__':
    sys.exit(main())
