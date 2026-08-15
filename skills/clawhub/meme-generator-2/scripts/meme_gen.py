#!/usr/bin/env python3
"""
Meme Generator — SVG-based meme creation tool.
Pure Python stdlib. No external dependencies.

Usage:
  python meme_gen.py make 'Unit tests?' 'No tests.' --template drake --output meme.svg
  python meme_gen.py batch 'Coffee is debug code' --all-templates --output-dir memes/
  python meme_gen.py quote --category programming --count 5
  echo 'When it works on production' | python meme_gen.py --template this_is_fine

Author: Denis Voronin
License: MIT
Version: 1.0.0
"""

import argparse
import html
import os
import sys
import textwrap

VERSION = "1.0.0"

# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────

WIDTH = 800
HEIGHT = 800

# ──────────────────────────────────────────────
# Quote Packs
# ──────────────────────────────────────────────

QUOTES = {
    "programming": [
        ("COMMITTING TO MAIN", "WORKS ON MY MACHINE"),
        ("WRITING UNIT TESTS", "COPY-PASTING FROM STACK OVERFLOW"),
        ("IT WORKED ONCE", "I'LL TOUCH IT AGAIN"),
        ("CLEAN CODE", "IF ELSE IF ELSE IF ELSE"),
        ("CODE REVIEW", "LGTM 🚀"),
        ("SENIOR DEV", "GOOGLE THE SAME THING"),
        ("DEBUGGING FOR 3 HOURS", "MISSING SEMICOLON"),
        ("DEPLOYING ON FRIDAY", "WHAT COULD GO WRONG"),
        ("REFACTORING", "MAKING IT WORSE"),
        ("DOCUMENTATION", "// TODO: WRITE DOCS"),
        ("PRODUCTION", "NOBODY KNOWS HOW"),
        ("TECHNICAL DEBT", "BANKRUPTCY"),
        ("IMMUTABLE STATE", "MUTABLE STATE"),
        ("FUNCTIONAL PROGRAMMING", "SIDE EFFECTS EVERYWHERE"),
        ("TYPE SAFETY", "ANY"),
        ("MICROSERVICES", "DISTRIBUTED MONOLITH"),
        ("AGILE", "MEETINGS"),
        ("CI/CD", "MANUAL DEPLOY"),
        ("CODE OWNER", "BLAME EVERYONE"),
        ("LEGACY CODE", "I WROTE IT 6 MONTHS AGO"),
    ],
    "startup": [
        ("RAISING SEED ROUND", "HAVING A PRODUCT"),
        ("DISRUPT", "COPY EXISTING IDEA"),
        ("AI-POWERED", "TWO IF STATEMENTS"),
        ("PIVOT", "WE FAILED"),
        ("RUNWAY", "6 MONTHS"),
        ("BURN RATE", "ASTRONOMICAL"),
        ("SERIES A", "MORE POWERPOINT"),
        ("HOCKEY STICK", "FLAT LINE"),
        ("10X ENGINEER", "CHARGES 10X"),
        ("UNITY", "EXCEL SPREADSHEET"),
        ("MVP", "BARELY WORKS"),
        ("PRODUCT-MARKET FIT", "ONE CUSTOMER"),
        ("GROWTH HACKING", "SPAMMING"),
        ("THOUGHT LEADER", "LINKEDIN POSTS"),
        ("EXIT STRATEGY", "GET ACQUIRED"),
    ],
    "productivity": [
        ("TODAY'S TO-DO LIST", "SCROLLING SOCIAL MEDIA"),
        ("DEEP WORK", "DEEP DISTRACTION"),
        ("POMODORO", "BREAK FOREVER"),
        ("PLANNER", "NEVER OPENED IT"),
        ("WAKE UP AT 5AM", "SNOOZE TO 9"),
        ("JUGGLING PRIORITIES", "ONE PRIORITY: DOING NOTHING"),
        ("AUTOMATE EVERYTHING", "MANUALLY CLICKING"),
        ("ZERO INBOX", "5000 UNREAD"),
        ("HABIT TRACKER", "GAVE UP DAY 2"),
        ("MONK MODE", "PHONE ADDICTION"),
        ("TIME BLOCKING", "BLOCKING ON THE COUCH"),
        ("KANBAN", "EVERYTHING IN BACKLOG"),
        ("OKRS", "WE TRIED"),
        ("SECOND BRAIN", "FORGOT PASSWORD"),
        ("EAT THE FROG", "ORDER PIZZA"),
    ],
    "student": [
        ("STUDYING", "REDDIT IN A NEW TAB"),
        ("DUE TOMORROW", "DOING IT AT 3AM"),
        ("GROUP PROJECT", "DOING IT ALL ALONE"),
        ("TEXTBOOK", "NEVER OPENED"),
        ("LECTURE", "ASLEEP"),
        ("EXAM TOMORROW", "NETFLIX TONIGHT"),
        ("OFFICE HOURS", "TOO EMBARRASSED"),
        ("WEEKLY READING", "SUMMARY WEBSITE"),
        ("NOTE-TAKING", "DOODLING"),
        ("DISSERTATION", "CHANGE EVERYTHING"),
        ("FINAL YEAR", "STILL UNDECIDED"),
        ("SCHOLARSHIP", "PARTY"),
        ("FREE PERIOD", "SLEEP"),
        ("GRADE CURVE", "ALMOST PASSED"),
        ("CONCENTRATION", "PHONE IN HAND"),
    ],
}

# ──────────────────────────────────────────────
# Text helpers
# ──────────────────────────────────────────────

def escape(text: str) -> str:
    """Escape text for XML/SVG."""
    return html.escape(str(text), quote=True)


def wrap_text(text: str, max_chars: int = 22) -> list:
    """Word-wrap text into lines, each at most max_chars wide."""
    text = text.strip()
    if not text:
        return [""]
    lines = []
    for raw_paragraph in text.split("\n"):
        words = raw_paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for w in words[1:]:
            if len(current) + 1 + len(w) <= max_chars:
                current += " " + w
            else:
                lines.append(current)
                current = w
        lines.append(current)
    return lines


def estimate_char_width(font_size: float) -> float:
    """Approximate avg character width for Impact-like font."""
    return font_size * 0.52


def optimal_font_size(lines: list, max_width_ratio: float = 0.92,
                      base_size: float = 60, min_size: float = 22) -> float:
    """Find a font size that makes the longest line fit within max_width_ratio."""
    longest = max((len(l) for l in lines), default=1)
    while base_size > min_size:
        cw = estimate_char_width(base_size)
        if longest * cw <= WIDTH * max_width_ratio:
            return base_size
        base_size -= 2
    return min_size


# ──────────────────────────────────────────────
# SVG Building Blocks
# ──────────────────────────────────────────────

def svg_text_block(lines, x, y, font_size, fill="white", stroke="black",
                   stroke_width=None, anchor="middle", animate=False,
                   extra=""):
    """Generate SVG text with Impact-like styling + outline."""
    if stroke_width is None:
        stroke_width = max(2, font_size * 0.07)
    sw = stroke_width
    parts = []
    lh = font_size * 1.05
    for i, line in enumerate(lines):
        ly = y + i * lh
        animate_tag = ""
        if animate:
            delay = i * 0.2
            animate_tag = (
                f'<animate attributeName="opacity" values="0;1" '
                f'dur="0.4s" begin="{delay}s" fill="freeze" />'
            )
        # Paint order: stroke (outline) first, then fill
        parts.append(
            f'<text x="{x}" y="{ly}" '
            f'font-family="Impact, \'Arial Black\', Haettenschweiler, sans-serif" '
            f'font-size="{font_size:.1f}" font-weight="bold" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw:.1f}" '
            f'stroke-linejoin="round" stroke-linecap="round" '
            f'paint-order="stroke fill" '
            f'text-anchor="{anchor}" letter-spacing="1.5" {extra}>'
            f'{escape(line)}{animate_tag}</text>'
        )
    return "\n".join(parts)


def bottom_text_svg(text, y_start=None, animate=False):
    """Bottom-centered impact text block."""
    lines = wrap_text(text)
    fs = optimal_font_size(lines)
    if y_start is None:
        total_h = len(lines) * fs * 1.05
        y_start = HEIGHT - total_h - 25
    return svg_text_block(lines, WIDTH / 2, y_start + fs, fs, animate=animate)


def top_text_svg(text, y_start=65, animate=False):
    """Top-centered impact text block."""
    lines = wrap_text(text)
    fs = optimal_font_size(lines)
    return svg_text_block(lines, WIDTH / 2, y_start, fs, animate=animate)


def center_text_svg(text, y_start=None, animate=False, fs_override=None):
    """Center-anchored text."""
    lines = wrap_text(text, max_chars=18)
    fs = fs_override or optimal_font_size(lines, max_width_ratio=0.85)
    if y_start is None:
        total_h = len(lines) * fs * 1.05
        y_start = (HEIGHT - total_h) / 2 + fs
    return svg_text_block(lines, WIDTH / 2, y_start, fs, animate=animate)


# ──────────────────────────────────────────────
# Template Definitions
# Each returns SVG content (defs, background, shapes).
# The caller adds text blocks on top.
# ──────────────────────────────────────────────

def _gradient(id, c1, c2):
    return (
        f'<linearGradient id="{id}" x1="0%" y1="0%" x2="0%" y2="100%">'
        f'<stop offset="0%" stop-color="{c1}"/>'
        f'<stop offset="100%" stop-color="{c2}"/>'
        f'</linearGradient>'
    )


def tpl_drake(top_text, bottom_text):
    """Two-panel reject/approve layout (Drake-style)."""
    defs = _gradient("bg_drake", "#5c4a8a", "#3a2e5c")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_drake)"/>'
    # Top panel: reject
    panels = (
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT//2}" fill="#2a2a3a"/>'
        f'<line x1="0" y1="{HEIGHT//2}" x2="{WIDTH}" y2="{HEIGHT//2}" '
        f'stroke="#555" stroke-width="4"/>'
    )
    # Stylized figure (simplified)
    figure = f'''
    <g transform="translate(180, 120) scale(2.2)">
      <circle cx="0" cy="-30" r="22" fill="#e8b87a"/>
      <path d="M -18 -40 Q -22 -52 0 -54 Q 22 -52 18 -40" fill="#3a2a1a"/>
      <rect x="-20" y="-8" width="44" height="50" rx="6" fill="#d4534c"/>
      <path d="M -28 -8 L 28 -8 L 28 -18 L -28 -18 Z" fill="#b5403a"/>
      <path d="M -12 42 Q -14 60 -18 75 M 12 42 Q 14 60 18 75" stroke="#1a1a2a" stroke-width="6" fill="none"/>
      <rect x="-22" y="-8" width="6" height="30" fill="#d4534c" transform="rotate(-40, -22, -8)"/>
    </g>
    <g transform="translate(180, 520) scale(2.2)">
      <circle cx="0" cy="-30" r="22" fill="#e8b87a"/>
      <path d="M -18 -40 Q -22 -52 0 -54 Q 22 -52 18 -40" fill="#3a2a1a"/>
      <rect x="-20" y="-8" width="44" height="50" rx="6" fill="#4ca84c"/>
      <path d="M -12 42 Q -10 60 -8 75 M 12 42 Q 10 60 8 75" stroke="#1a1a2a" stroke-width="6" fill="none"/>
      <rect x="14" y="-5" width="20" height="6" fill="#888" transform="rotate(-20, 14, -5)"/>
    </g>
    '''
    shapes = defs + bg + panels + figure
    # Text goes on the right side of each panel
    top_lines = wrap_text(top_text, max_chars=18)
    bot_lines = wrap_text(bottom_text, max_chars=18)
    fs = optimal_font_size(top_lines, max_width_ratio=0.45)
    fs2 = optimal_font_size(bot_lines, max_width_ratio=0.45)
    top = svg_text_block(top_lines, WIDTH * 0.72, HEIGHT // 2 - 60 + fs, fs, anchor="middle")
    bot = svg_text_block(bot_lines, WIDTH * 0.72, HEIGHT - 70 + fs2, fs2, anchor="middle")
    return shapes, top, bot


def tpl_distracted_boyfriend(top_text, bottom_text):
    """Three-character distracted boyfriend layout."""
    defs = _gradient("bg_db", "#8ab4d8", "#5a8aba")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_db)"/>'
    scene = '''
    <g transform="translate(0, 180)">
      <!-- Boyfriend (center, turning) -->
      <circle cx="340" cy="100" r="35" fill="#e8b87a"/>
      <rect x="310" y="135" width="60" height="90" rx="8" fill="#3b6ca8"/>
      <path d="M 320 70 Q 320 50 350 45 Q 380 50 380 70" fill="#4a3a2a"/>
      <path d="M 365 110 Q 400 100 430 95" stroke="#d4534c" stroke-width="4" fill="none"/>
      <!-- Girlfriend (left, angry) -->
      <circle cx="150" cy="105" r="32" fill="#e8b87a"/>
      <rect x="122" y="137" width="56" height="85" rx="8" fill="#c44d5e"/>
      <path d="M 130 75 Q 130 55 152 52 Q 175 55 175 75" fill="#8a4a3a"/>
      <!-- Distraction (right) -->
      <circle cx="550" cy="95" r="30" fill="#e8b87a"/>
      <rect x="524" y="125" width="52" height="80" rx="8" fill="#e8d44e"/>
      <path d="M 530 65 Q 530 45 550 42 Q 572 45 572 65" fill="#5a4a3a"/>
    </g>
    '''
    shapes = defs + bg + scene
    top = center_text_svg(top_text, y_start=50, fs_override=42)
    bottom_lines = wrap_text(bottom_text, max_chars=15)
    labels = (
        svg_text_block(wrap_text(top_text, max_chars=12), 150, 400, 28, anchor="middle")
        + "\n"
        + svg_text_block(wrap_text(bottom_text, max_chars=12), 550, 390, 28, anchor="middle")
        + "\n"
        + svg_text_block(["ME"], 340, 420, 28, anchor="middle")
    )
    return shapes, top, labels


def tpl_two_buttons(top_text, bottom_text):
    """Two-button dilemma."""
    defs = _gradient("bg_btn", "#3a3a4a", "#1a1a2a")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_btn)"/>'
    scene = '''
    <g transform="translate(0, 140)">
      <!-- Hand -->
      <circle cx="400" cy="380" r="30" fill="#e8b87a"/>
      <rect x="375" y="395" width="50" height="120" rx="8" fill="#d4534c"/>
      <path d="M 380 380 L 360 370 L 365 390" stroke="#e8b87a" stroke-width="14" fill="#e8b87a" stroke-linejoin="round"/>
      <!-- Buttons -->
      <rect x="180" y="60" width="180" height="200" rx="12" fill="#5566aa" stroke="#888" stroke-width="3"/>
      <rect x="440" y="60" width="180" height="200" rx="12" fill="#aa5566" stroke="#888" stroke-width="3"/>
      <!-- Sweat drop -->
      <path d="M 350 350 Q 345 370 352 375 Q 360 370 358 350 Z" fill="#7ec8e3" opacity="0.8"/>
    </g>
    '''
    shapes = defs + bg + scene
    top_lines = wrap_text(top_text, max_chars=14)
    bot_lines = wrap_text(bottom_text, max_chars=14)
    top = svg_text_block(top_lines, 270, 260, 30, anchor="middle")
    bot = svg_text_block(bot_lines, 530, 260, 30, anchor="middle")
    return shapes, top, bot


def tpl_change_my_mind(top_text, bottom_text):
    """Change My Mind — guy at table with sign."""
    defs = _gradient("bg_cmm", "#c8a878", "#a88858")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_cmm)"/>'
    scene = '''
    <g transform="translate(100, 280)">
      <!-- Table -->
      <rect x="0" y="200" width="600" height="30" fill="#8a6a3a"/>
      <rect x="40" y="230" width="20" height="120" fill="#8a6a3a"/>
      <rect x="540" y="230" width="20" height="120" fill="#8a6a3a"/>
      <!-- Sign on table -->
      <rect x="150" y="140" width="300" height="70" fill="white" stroke="#333" stroke-width="3"/>
      <!-- Person -->
      <circle cx="300" cy="80" r="40" fill="#e8b87a"/>
      <path d="M 270 50 Q 270 20 310 15 Q 350 20 335 50" fill="#5a4a3a"/>
      <rect x="260" y="120" width="80" height="90" rx="8" fill="#c44d4d"/>
      <path d="M 300 120 L 300 165 M 280 150 L 320 150" stroke="white" stroke-width="4"/>
    </g>
    '''
    shapes = defs + bg + scene
    top = top_text_svg(top_text, y_start=55, animate=False)
    sign_lines = wrap_text(top_text, max_chars=24)
    sign = svg_text_block(sign_lines, WIDTH / 2, 455, 28, anchor="middle")
    return shapes, top, sign


def tpl_galaxy_brain(top_text, bottom_text):
    """Galaxy Brain — ascending brain levels."""
    defs = _gradient("bg_gb", "#0a0a2a", "#000010")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_gb)"/>'
    # Stars
    import random
    rng = random.Random(42)
    stars = "".join(
        f'<circle cx="{rng.randint(0, WIDTH)}" cy="{rng.randint(0, HEIGHT)}" '
        f'r="{rng.choice([0.5, 1, 1, 1.5, 2])}" fill="white" opacity="{rng.uniform(0.3, 1):.1f}"/>'
        for _ in range(100)
    )
    brains = ''
    colors = ["#8a6a4a", "#aa6a8a", "#6a8aaa", "#6aaaba", "#ffffff"]
    y_positions = [100, 260, 420, 580, 700]
    for i, (c, y) in enumerate(zip(colors, y_positions)):
        scale = 1.0 + i * 0.1
        brains += f'''
        <g transform="translate(180, {y}) scale({scale})">
          <path d="M -30 -15 Q -40 -25 -25 -30 Q -10 -35 0 -28 Q 10 -35 25 -30 Q 40 -25 30 -15
                   Q 40 -5 25 0 Q 40 5 30 15 Q 35 25 15 28 Q 0 25 -15 28 Q -35 25 -30 15
                   Q -40 5 -25 0 Q -40 -5 -30 -15 Z" fill="{c}" opacity="0.9"/>
          <path d="M -5 -25 L -8 25 M 5 -20 L 10 22 M 15 -10 L 20 15" stroke="{c}" stroke-width="2" opacity="0.5"/>
        </g>
        '''
    shapes = defs + bg + stars + brains
    # We'll use top_text and bottom_text as first and last labels
    top = svg_text_block(wrap_text(top_text, max_chars=16), WIDTH * 0.7, 130, 30, anchor="middle")
    bot = svg_text_block(wrap_text(bottom_text, max_chars=16), WIDTH * 0.7, 720, 30, anchor="middle")
    return shapes, top, bot


def tpl_stonks(top_text, bottom_text):
    """Stonks — upward arrow with suit guy."""
    defs = _gradient("bg_st", "#1a2a4a", "#0a1a3a")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_st)"/>'
    scene = '''
    <g transform="translate(0, 100)">
      <!-- Suit guy -->
      <circle cx="180" cy="120" r="45" fill="#e8b87a"/>
      <path d="M 145 90 Q 145 55 185 50 Q 225 55 220 90" fill="#5a4a3a"/>
      <rect x="140" y="165" width="80" height="120" rx="6" fill="#2a2a3a"/>
      <path d="M 180 165 L 180 200 L 165 200 L 180 240 L 195 200 L 180 200" fill="white"/>
      <rect x="175" y="200" width="10" height="10" fill="#c44d4d"/>
      <!-- Arms -->
      <rect x="95" y="165" width="20" height="80" rx="4" fill="#2a2a3a" transform="rotate(-30, 105, 165)"/>
      <rect x="245" y="165" width="20" height="80" rx="4" fill="#2a2a3a" transform="rotate(30, 255, 165)"/>
      <!-- Stonks arrow -->
      <path d="M 350 500 L 450 400 L 500 430 L 650 200 L 750 150"
            stroke="#4caf50" stroke-width="10" fill="none" stroke-linejoin="round"/>
      <path d="M 750 150 L 720 160 L 735 185 Z" fill="#4caf50"/>
      <!-- Grid lines -->
      <line x1="350" y1="500" x2="750" y2="500" stroke="#333" stroke-width="2"/>
      <line x1="350" y1="500" x2="350" y2="150" stroke="#333" stroke-width="2"/>
    </g>
    <text x="600" y="100" font-family="'Arial Black', sans-serif" font-size="72"
          fill="#4caf50" font-weight="bold" transform="rotate(-8, 600, 80)">STONKS</text>
    '''
    shapes = defs + bg + scene
    top = top_text_svg(top_text, y_start=50, animate=False)
    bot = bottom_text_svg(bottom_text)
    return shapes, top, bot


def tpl_this_is_fine(top_text, bottom_text):
    """This is Fine — dog in burning room."""
    defs = _gradient("bg_tf", "#cc5522", "#882200")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_tf)"/>'
    scene = '''
    <g transform="translate(0, 0)">
      <!-- Flames -->
      <path d="M 0 500 Q 50 350 100 450 Q 150 300 200 480 Q 300 350 350 500 Q 500 320 550 490
               Q 650 380 700 500 Q 750 350 800 520 L 800 800 L 0 800 Z"
            fill="#ff6600" opacity="0.7"/>
      <path d="M 0 600 Q 80 500 150 580 Q 250 450 350 600 Q 450 480 550 580 Q 650 500 800 620
               L 800 800 L 0 800 Z"
            fill="#ffaa00" opacity="0.6"/>
      <!-- Dog -->
      <g transform="translate(280, 320)">
        <ellipse cx="120" cy="80" rx="100" ry="70" fill="#e8c890"/>
        <circle cx="220" cy="50" r="45" fill="#e8c890"/>
        <path d="M 190 15 L 175 -10 L 205 5 Z" fill="#e8c890"/>
        <path d="M 240 15 L 255 -10 L 225 5 Z" fill="#e8c890"/>
        <circle cx="210" cy="45" r="4" fill="#333"/>
        <circle cx="232" cy="45" r="4" fill="#333"/>
        <ellipse cx="222" cy="62" rx="6" ry="4" fill="#333"/>
        <path d="M 218 65 Q 222 72 226 65" stroke="#333" stroke-width="2" fill="none"/>
        <!-- Coffee mug -->
        <rect x="40" y="50" width="30" height="35" rx="3" fill="#d4534c"/>
        <path d="M 70 55 Q 80 60 80 70 Q 80 78 70 80" stroke="#d4534c" stroke-width="4" fill="none"/>
        <!-- Ears -->
        <ellipse cx="185" cy="20" rx="12" ry="20" fill="#c8a878" transform="rotate(-20, 185, 20)"/>
        <ellipse cx="255" cy="20" rx="12" ry="20" fill="#c8a878" transform="rotate(20, 255, 20)"/>
      </g>
    </g>
    '''
    shapes = defs + bg + scene
    top = top_text_svg(top_text)
    bot = bottom_text_svg(bottom_text)
    return shapes, top, bot


def tpl_doge(top_text, bottom_text):
    """Doge — shiba inu with colorful text."""
    defs = _gradient("bg_doge", "#f0e8d0", "#d8d0b8")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_doge)"/>'
    scene = '''
    <g transform="translate(150, 180)">
      <!-- Shiba body -->
      <ellipse cx="250" cy="280" rx="180" ry="120" fill="#e8a850"/>
      <!-- Head -->
      <ellipse cx="250" cy="120" rx="110" ry="100" fill="#e8a850"/>
      <!-- Snout -->
      <ellipse cx="250" cy="150" rx="60" ry="50" fill="#f8e8c8"/>
      <!-- Ears -->
      <path d="M 160 50 L 140 10 L 200 40 Z" fill="#c88838"/>
      <path d="M 340 50 L 360 10 L 300 40 Z" fill="#c88838"/>
      <!-- Eyes -->
      <ellipse cx="205" cy="110" rx="12" ry="15" fill="#222"/>
      <ellipse cx="295" cy="110" rx="12" ry="15" fill="#222"/>
      <!-- Nose -->
      <ellipse cx="250" cy="130" rx="14" ry="10" fill="#222"/>
      <!-- Mouth -->
      <path d="M 230 165 Q 250 185 270 165" stroke="#222" stroke-width="3" fill="none"/>
      <!-- Legs -->
      <rect x="130" y="350" width="40" height="80" rx="8" fill="#e8a850"/>
      <rect x="330" y="350" width="40" height="80" rx="8" fill="#e8a850"/>
    </g>
    '''
    shapes = defs + bg + scene
    # Doge-style colorful labels
    doge_words = ["WOW", "SUCH", "VERY", "MUCH", "SO"]
    import random
    rng = random.Random(7)
    colors = ["#4488ff", "#ff44aa", "#44dd44", "#ffaa00", "#aa44ff"]
    doge_labels = []
    for i, word in enumerate(doge_words):
        x = rng.randint(60, WIDTH - 200)
        y = rng.randint(60, HEIGHT - 100)
        rot = rng.randint(-15, 15)
        c = colors[i % len(colors)]
        combined = f"{word} {top_text.upper()}" if i == 0 else word
        doge_labels.append(
            f'<text x="{x}" y="{y}" font-family="Comic Sans MS, Impact, sans-serif" '
            f'font-size="32" fill="{c}" font-weight="bold" '
            f'transform="rotate({rot}, {x}, {y})">{escape(combined)}</text>'
        )
    top = "\n".join(doge_labels)
    bot = bottom_text_svg(bottom_text)
    return shapes, top, bot


def tpl_expanding_brain(top_text, bottom_text):
    """Expanding Brain — four stages with increasing glow."""
    defs = _gradient("bg_eb", "#1a1a2a", "#0a0a1a")
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg_eb)"/>'
    import math
    brains = ''
    glows = ["#555566", "#6666aa", "#8888dd", "#aaddff", "#ffffff"]
    y_pos = [40, 180, 320, 460, 600]
    for i, (c, y) in enumerate(zip(glows, y_pos)):
        brightness = 0.3 + i * 0.17
        brains += f'''
        <g transform="translate(160, {y + 60}) scale({0.8 + i * 0.08})" opacity="{brightness:.2f}">
          <path d="M -25 -12 Q -35 -20 -20 -25 Q -8 -28 0 -22 Q 8 -28 20 -25 Q 35 -20 25 -12
                   Q 35 -4 20 0 Q 35 4 25 12 Q 30 20 12 22 Q 0 20 -12 22 Q -30 20 -25 12
                   Q -35 4 -20 0 Q -35 -4 -25 -12 Z" fill="{c}"/>
        </g>
        '''
        brains += f'<line x1="0" y1="{y + 120}" x2="{WIDTH}" y2="{y + 120}" stroke="#333" stroke-width="2"/>'
    shapes = defs + bg + brains
    # Text labels for each stage
    top = svg_text_block(wrap_text(top_text, max_chars=16), WIDTH * 0.7, 100, 28, anchor="middle")
    bot = svg_text_block(wrap_text(bottom_text, max_chars=16), WIDTH * 0.7, 660, 28, anchor="middle")
    return shapes, top, bot


def tpl_panik_kalm(top_text, bottom_text):
    """Panik / Kalm / Panik — three-panel."""
    defs = ''
    bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#2a2a3a"/>'
    panels = (
        f'<rect x="0" y="0" width="{WIDTH//3}" height="{HEIGHT}" fill="#6a2a2a"/>'
        f'<rect x="{WIDTH//3}" y="0" width="{WIDTH//3}" height="{HEIGHT}" fill="#2a4a6a"/>'
        f'<rect x="{2*WIDTH//3}" y="0" width="{WIDTH//3}" height="{HEIGHT}" fill="#6a2a2a"/>'
        f'<line x1="{WIDTH//3}" y1="0" x2="{WIDTH//3}" y2="{HEIGHT}" stroke="#555" stroke-width="4"/>'
        f'<line x1="{2*WIDTH//3}" y1="0" x2="{2*WIDTH//3}" y2="{HEIGHT}" stroke="#555" stroke-width="4"/>'
    )
    # Panic waves
    waves = ''
    for cx in [WIDTH // 6, 5 * WIDTH // 6]:
        waves += f'''
        <g transform="translate({cx}, {HEIGHT // 2})">
          <circle cx="0" cy="0" r="40" fill="none" stroke="#ff4444" stroke-width="3" opacity="0.5">
            <animate attributeName="r" values="40;80;40" dur="1.5s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.5;0;0.5" dur="1.5s" repeatCount="indefinite"/>
          </circle>
          <circle cx="0" cy="0" r="30" fill="none" stroke="#ff4444" stroke-width="3" opacity="0.7">
            <animate attributeName="r" values="30;60;30" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.7;0;0.7" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
          </circle>
        </g>
        '''
    # Kalm face
    kalm = f'''
    <g transform="translate({WIDTH // 2}, {HEIGHT // 2})">
      <circle cx="0" cy="0" r="50" fill="#88cc88"/>
      <path d="M -20 -10 L -10 -10 M 10 -10 L 20 -10" stroke="#222" stroke-width="3"/>
      <path d="M -12 15 Q 0 22 12 15" stroke="#222" stroke-width="3" fill="none"/>
    </g>
    '''
    shapes = defs + bg + panels + waves + kalm
    labels = (
        f'<text x="{WIDTH//6}" y="{HEIGHT - 40}" font-family="Impact, sans-serif" font-size="36" '
        f'fill="white" stroke="black" stroke-width="2" paint-order="stroke fill" '
        f'text-anchor="middle" font-weight="bold">PANIK</text>'
        f'<text x="{WIDTH//2}" y="{HEIGHT - 40}" font-family="Impact, sans-serif" font-size="36" '
        f'fill="white" stroke="black" stroke-width="2" paint-order="stroke fill" '
        f'text-anchor="middle" font-weight="bold">KALM</text>'
        f'<text x="{5*WIDTH//6}" y="{HEIGHT - 40}" font-family="Impact, sans-serif" font-size="36" '
        f'fill="white" stroke="black" stroke-width="2" paint-order="stroke fill" '
        f'text-anchor="middle" font-weight="bold">PANIK</text>'
    )
    # Custom text blocks
    top_lines = wrap_text(top_text, max_chars=12)
    bot_lines = wrap_text(bottom_text, max_chars=12)
    top = svg_text_block(top_lines, WIDTH // 6, 60, 28, anchor="middle")
    bot = svg_text_block(bot_lines, 5 * WIDTH // 6, 60, 28, anchor="middle")
    mid = svg_text_block(wrap_text("(realization)", max_chars=12), WIDTH // 2, 60, 28, anchor="middle")
    return shapes, top, mid + "\n" + bot + "\n" + labels


# ──────────────────────────────────────────────
# Template Registry
# ──────────────────────────────────────────────

TEMPLATES = {
    "drake": tpl_drake,
    "distracted_boyfriend": tpl_distracted_boyfriend,
    "two_buttons": tpl_two_buttons,
    "change_my_mind": tpl_change_my_mind,
    "galaxy_brain": tpl_galaxy_brain,
    "stonks": tpl_stonks,
    "this_is_fine": tpl_this_is_fine,
    "doge": tpl_doge,
    "expanding_brain": tpl_expanding_brain,
    "panik_kalm": tpl_panik_kalm,
}

TEMPLATE_ALIASES = {
    "drake": "drake",
    "distracted": "distracted_boyfriend",
    "boyfriend": "distracted_boyfriend",
    "buttons": "two_buttons",
    "two_buttons": "two_buttons",
    "change_my_mind": "change_my_mind",
    "cmm": "change_my_mind",
    "galaxy_brain": "galaxy_brain",
    "galaxy": "galaxy_brain",
    "stonks": "stonks",
    "stocks": "stonks",
    "this_is_fine": "this_is_fine",
    "fine": "this_is_fine",
    "doge": "doge",
    "expanding_brain": "expanding_brain",
    "brain": "expanding_brain",
    "panik_kalm": "panik_kalm",
    "panik": "panik_kalm",
    "kalm": "panik_kalm",
}


def resolve_template(name: str):
    key = name.lower().strip()
    key = TEMPLATE_ALIASES.get(key, key)
    return TEMPLATES.get(key)


# ──────────────────────────────────────────────
# SVG Assembly
# ──────────────────────────────────────────────

def build_svg(template_fn, top_text, bottom_text, animate=False):
    """Assemble full SVG document."""
    shapes, top, bottom = template_fn(top_text, bottom_text)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <style>
      @media (prefers-reduced-motion: reduce) {{
        animate {{ display: none; }}
      }}
    </style>
  </defs>
  {shapes}
  {top}
  {bottom}
</svg>'''
    return svg


def svg_to_html(svg_content: str, title: str = "Meme") -> str:
    """Wrap SVG in a standalone HTML file for easy viewing."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<style>
  body {{ margin: 0; padding: 0; display: flex; justify-content: center;
         align-items: center; min-height: 100vh; background: #1a1a2a; }}
  svg {{ max-width: 100%; height: auto; }}
</style>
</head>
<body>
{svg_content}
</body>
</html>'''


def custom_template(top_text, bottom_text, template_path: str):
    """Load a custom SVG template from file.

    The template file should be a complete SVG. Text placeholders
    {{TOP}} and {{BOTTOM}} will be replaced.
    """
    with open(template_path, "r") as f:
        tpl = f.read()
    # Replace placeholders
    top_lines = wrap_text(top_text)
    bot_lines = wrap_text(bottom_text)
    fs = optimal_font_size(top_lines)
    top_svg = svg_text_block(top_lines, WIDTH / 2, 65, fs)
    fs2 = optimal_font_size(bot_lines)
    bot_svg = svg_text_block(bot_lines, WIDTH / 2, HEIGHT - 40, fs2)
    tpl = tpl.replace("{{TOP}}", top_svg)
    tpl = tpl.replace("{{BOTTOM}}", bot_svg)
    return tpl, "", ""


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

def cmd_make(args):
    """Generate a single meme."""
    template_fn = resolve_template(args.template)
    if not template_fn:
        print(f"Error: Unknown template '{args.template}'", file=sys.stderr)
        print(f"Available: {', '.join(sorted(TEMPLATES.keys()))}", file=sys.stderr)
        sys.exit(1)

    top = args.top.upper() if args.top else ""
    bottom = args.bottom.upper() if args.bottom else ""

    svg = build_svg(template_fn, top, bottom, animate=args.animate)

    output = args.output or "meme.svg"
    with open(output, "w") as f:
        f.write(svg)
    print(f"✓ Meme saved to {output}")

    if args.html:
        html_out = output.rsplit(".", 1)[0] + ".html"
        with open(html_out, "w") as f:
            f.write(svg_to_html(svg, title=f"{top} {bottom}"))
        print(f"✓ HTML version saved to {html_out}")


def cmd_batch(args):
    """Generate memes across all templates."""
    top = args.top.upper() if args.top else ""
    bottom = args.bottom.upper() if args.bottom else ""

    output_dir = args.output_dir or "memes"
    os.makedirs(output_dir, exist_ok=True)

    templates = TEMPLATES
    if not args.all_templates and args.templates:
        templates = {}
        for t in args.templates:
            fn = resolve_template(t)
            if fn:
                templates[t] = fn
            else:
                print(f"Warning: Unknown template '{t}', skipping", file=sys.stderr)

    count = 0
    for name, fn in templates.items():
        svg = build_svg(fn, top, bottom, animate=args.animate)
        outpath = os.path.join(output_dir, f"{name}.svg")
        with open(outpath, "w") as f:
            f.write(svg)
        count += 1
        print(f"  ✓ {name}.svg")

    print(f"\n✓ Generated {count} memes in {output_dir}/")

    if args.html:
        for name in templates:
            svg_path = os.path.join(output_dir, f"{name}.svg")
            html_path = os.path.join(output_dir, f"{name}.html")
            with open(svg_path) as f:
                svg = f.read()
            with open(html_path, "w") as f:
                f.write(svg_to_html(svg, title=name))
        print(f"✓ HTML versions saved to {output_dir}/")


def cmd_quote(args):
    """Print quotes from a category."""
    import random
    category = args.category
    if category not in QUOTES:
        print(f"Error: Unknown category '{category}'", file=sys.stderr)
        print(f"Available: {', '.join(sorted(QUOTES.keys()))}", file=sys.stderr)
        sys.exit(1)

    quotes = QUOTES[category]
    count = min(args.count, len(quotes))
    selected = random.sample(quotes, count) if count < len(quotes) else quotes

    for i, (top, bottom) in enumerate(selected, 1):
        print(f"{i}. {top} / {bottom}")

    if args.generate:
        # Generate memes from selected quotes
        output_dir = args.output_dir or f"quotes_{category}"
        os.makedirs(output_dir, exist_ok=True)
        template_fn = resolve_template(args.template or "drake")
        if not template_fn:
            template_fn = TEMPLATES["drake"]
        for i, (top, bottom) in enumerate(selected, 1):
            svg = build_svg(template_fn, top, bottom)
            outpath = os.path.join(output_dir, f"meme_{i}.svg")
            with open(outpath, "w") as f:
                f.write(svg)
        print(f"\n✓ Generated {count} memes in {output_dir}/")


def cmd_list(args):
    """List available templates and quote categories."""
    print("TEMPLATES:")
    for name in sorted(TEMPLATES.keys()):
        print(f"  • {name}")
    print(f"\nQUOTE CATEGORIES:")
    for cat in sorted(QUOTES.keys()):
        print(f"  • {cat} ({len(QUOTES[cat])} quotes)")


def cmd_custom(args):
    """Generate meme with custom SVG template."""
    if not os.path.exists(args.template_file):
        print(f"Error: Template file not found: {args.template_file}", file=sys.stderr)
        sys.exit(1)
    top = args.top.upper() if args.top else ""
    bottom = args.bottom.upper() if args.bottom else ""
    svg, _, _ = custom_template(top, bottom, args.template_file)
    output = args.output or "custom_meme.svg"
    with open(output, "w") as f:
        f.write(svg)
    print(f"✓ Custom meme saved to {output}")


def read_stdin():
    """Read from stdin if available."""
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return None


def main():
    parser = argparse.ArgumentParser(
        prog="meme_gen",
        description="SVG Meme Generator — create crisp, shareable memes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s make 'Unit tests?' 'No tests.' --template drake --output meme.svg
  %(prog)s batch 'Coffee is debug code' --all-templates --output-dir memes/
  %(prog)s quote --category programming --count 5
  echo 'When it works on production' | %(prog)s --template this_is_fine
  %(prog)s list
  %(prog)s custom 'Hello' 'World' --template-file my_template.svg
        """
    )
    parser.add_argument("--version", action="version", version=f"meme_gen {VERSION}")
    # Global --template for pipe mode (echo 'text' | meme_gen.py --template X)
    parser.add_argument("-t", "--template", default=None, help="Template (for pipe mode)")
    parser.add_argument("-o", "--output", default=None, help="Output file (for pipe mode)")

    sub = parser.add_subparsers(dest="command")

    # make
    p_make = sub.add_parser("make", help="Generate a single meme")
    p_make.add_argument("top", help="Top text")
    p_make.add_argument("bottom", nargs="?", default="", help="Bottom text")
    p_make.add_argument("-t", "--template", default="drake", help="Template name")
    p_make.add_argument("-o", "--output", default="meme.svg", help="Output file")
    p_make.add_argument("--html", action="store_true", help="Also generate HTML")
    p_make.add_argument("--animate", action="store_true", help="Animated text effects")
    p_make.set_defaults(func=cmd_make)

    # batch
    p_batch = sub.add_parser("batch", help="Generate memes across multiple templates")
    p_batch.add_argument("top", help="Top text")
    p_batch.add_argument("bottom", nargs="?", default="", help="Bottom text")
    p_batch.add_argument("-a", "--all-templates", action="store_true", help="Use all templates")
    p_batch.add_argument("--templates", nargs="*", help="Specific templates")
    p_batch.add_argument("-o", "--output-dir", default="memes", help="Output directory")
    p_batch.add_argument("--html", action="store_true", help="Also generate HTML")
    p_batch.add_argument("--animate", action="store_true", help="Animated text effects")
    p_batch.set_defaults(func=cmd_batch)

    # quote
    p_quote = sub.add_parser("quote", help="Get quotes from a category")
    p_quote.add_argument("-c", "--category", default="programming", help="Quote category")
    p_quote.add_argument("-n", "--count", type=int, default=5, help="Number of quotes")
    p_quote.add_argument("-g", "--generate", action="store_true", help="Generate memes from quotes")
    p_quote.add_argument("-t", "--template", default="drake", help="Template for generated memes")
    p_quote.add_argument("-o", "--output-dir", default=None, help="Output directory")
    p_quote.set_defaults(func=cmd_quote)

    # list
    p_list = sub.add_parser("list", help="List available templates and categories")
    p_list.set_defaults(func=cmd_list)

    # custom
    p_custom = sub.add_parser("custom", help="Generate meme with custom SVG template")
    p_custom.add_argument("top", help="Top text")
    p_custom.add_argument("bottom", nargs="?", default="", help="Bottom text")
    p_custom.add_argument("template_file", help="Path to custom SVG template")
    p_custom.add_argument("-o", "--output", default="custom_meme.svg", help="Output file")
    p_custom.set_defaults(func=cmd_custom)

    args = parser.parse_args()

    # Handle stdin piped input
    stdin_text = read_stdin()
    if stdin_text and not args.command:
        # Pipe mode: use stdin as top text
        template_fn = resolve_template(
            getattr(args, "template", None) or "this_is_fine"
        )
        if not template_fn:
            template_fn = TEMPLATES["this_is_fine"]
        svg = build_svg(template_fn, stdin_text.upper(), "")
        print(svg)
        return

    if not args.command:
        # If template is given via global but no subcommand
        if hasattr(args, "template") and args.template:
            stdin_text = stdin_text or "PLACEHOLDER"
            template_fn = resolve_template(args.template) or TEMPLATES["this_is_fine"]
            svg = build_svg(template_fn, stdin_text.upper(), "")
            with open("meme.svg", "w") as f:
                f.write(svg)
            print("✓ Meme saved to meme.svg")
            return
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
