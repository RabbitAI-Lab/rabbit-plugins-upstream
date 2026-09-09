#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""
Command Display Helper - Formats command execution output with colors and security levels.

Usage:
    python3 cmd_display.py <level> "<command>" "<purpose>" "<result>" [warning] [action]

Levels:
    safe     - 🟢 Read-only information gathering
    low      - 🔵 Project file modifications
    medium   - 🟡 Configuration changes
    high     - 🟠 System-level changes
    critical - 🔴 Potential data loss

Examples:
    python3 cmd_display.py safe "git status" "Check repo state" "$(git status --short)"
    python3 cmd_display.py low "touch file.txt" "Create file" "$(touch file.txt && echo '✓ Created')"
    python3 cmd_display.py medium "npm install" "Install deps" "✓ 42 packages" "May take time"
"""
import sys
import re


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Standard colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_CYAN = '\033[96m'


# Security level configurations
LEVELS = {
    'safe': {
        'emoji': '🟢',
        'color': Colors.GREEN,
        'name': 'SAFE',
        'desc': 'Read-only information gathering'
    },
    'low': {
        'emoji': '🔵',
        'color': Colors.BLUE,
        'name': 'LOW',
        'desc': 'Project file modifications'
    },
    'medium': {
        'emoji': '🟡',
        'color': Colors.YELLOW,
        'name': 'MEDIUM',
        'desc': 'Configuration changes'
    },
    'high': {
        'emoji': '🟠',
        'color': Colors.BRIGHT_YELLOW,
        'name': 'HIGH',
        'desc': 'System-level changes'
    },
    'critical': {
        'emoji': '🔴',
        'color': Colors.RED,
        'name': 'CRITICAL',
        'desc': 'Potential data loss'
    }
}


# ── Untrusted-text hardening ─────────────────────────────────────────────────
# Every argument this script prints — command, purpose, result, warning, action —
# can carry text the agent did not write: the stdout of a command, a filename from
# a cloned repo, an error message from a remote server. Printed raw, a string like
# "\x1b[2K\rSAFE: read-only" repaints the line above and turns a CRITICAL banner
# into a green one. A security display that can be forged by its own input is
# worse than no display, so the input is stripped before any colour is applied.

# ESC ] ... (BEL | ST)  — OSC strings: window title, OSC-8 hyperlinks
_OSC = r'\x1B\][^\x07\x1B]*(?:\x07|\x1B\\)?'
# ESC P/X/^/_ ... ST    — DCS / SOS / PM / APC strings
_DCS = r'\x1B[PX^_][^\x1B]*(?:\x1B\\)?'
# ESC [ ... final byte  — CSI: colour, cursor movement, line erase
_CSI = r'\x1B\[[0-?]*[ -/]*[@-~]'
# Any other two-byte escape, and a bare/truncated trailing ESC
_ESC = r'\x1B[@-Z\\-_]|\x1B'
_ANSI_RE = re.compile('|'.join((_OSC, _DCS, _CSI, _ESC)))

# C0 + DEL + C1. \n is kept only where a caller asks for it (line counting).
_CTRL_ALL = re.compile(r'[\x00-\x1F\x7F-\x9F]')
_CTRL_KEEP_NL = re.compile(r'[\x00-\x09\x0B-\x1F\x7F-\x9F]')


def strip_ansi(text: str) -> str:
    """Remove ANSI/OSC/DCS escape sequences from text."""
    return _ANSI_RE.sub('', text)


def sanitize(text, keep_newlines: bool = False, max_len: int = 800):
    """
    Make attacker-influenced text safe to print inside a coloured report.

    Removes escape sequences and control characters, so the argument cannot
    recolour the report, erase or reposition lines, set the window title, or
    smuggle a hyperlink. Length is capped so a huge argument cannot scroll the
    real banner off the screen.
    """
    if text is None:
        return None
    out = str(text).replace('\t', ' ')
    out = _ANSI_RE.sub('', out)
    out = (_CTRL_KEEP_NL if keep_newlines else _CTRL_ALL).sub('', out)
    if len(out) > max_len:
        out = out[:max_len - 1] + '…'
    return out


def summarize_output(output: str, max_chars: int = 80) -> str:
    """
    Condense multi-line output to a single summary line.
    
    Strategies:
    - Single line: return as-is (truncated if needed)
    - Multiple lines: count and summarize
    - Empty: return placeholder
    """
    if not output or not output.strip():
        return "(no output)"
    
    lines = output.strip().split('\n')
    
    if len(lines) == 1:
        line = lines[0].strip()
        if len(line) > max_chars:
            return line[:max_chars-3] + "..."
        return line
    
    # Multiple lines - create summary
    non_empty = [l for l in lines if l.strip()]
    first_line = non_empty[0].strip() if non_empty else ""
    
    if len(first_line) > 50:
        first_line = first_line[:47] + "..."
    
    return f"{first_line} (+{len(lines)-1} more lines)"


def format_command(
    level: str,
    command: str,
    purpose: str,
    result: str,
    warning: str = None,
    action: str = None
) -> None:
    """
    Format and print a command execution report.
    
    Output format (max 4 lines):
    1. Level + Command
    2. Result (✓/✗)
    3. Purpose
    4. Warning/Action (optional)
    """
    if level not in LEVELS:
        # `level` is argv too — never echo it back unsanitized.
        print(f"Error: Unknown level '{sanitize(level, max_len=40)}'. "
              f"Use: {', '.join(LEVELS.keys())}", file=sys.stderr)
        sys.exit(1)

    config = LEVELS[level]

    # Everything below is printed. Strip escapes and control characters FIRST,
    # so no argument can forge the banner it is displayed inside. Newlines
    # survive in `result` only long enough for summarize_output() to count them.
    command = sanitize(command)
    purpose = sanitize(purpose)
    warning = sanitize(warning)
    action = sanitize(action)
    result = sanitize(result, keep_newlines=True, max_len=20000)

    # Determine result icon and color
    result_clean = result.strip() if result else ""
    if result_clean.startswith('✓') or result_clean.startswith('✔'):
        result_icon = '✓'
        result_color = Colors.BRIGHT_GREEN
        result_text = result_clean.lstrip('✓✔ ')
    elif result_clean.startswith('✗') or result_clean.startswith('✘') or result_clean.startswith('Error'):
        result_icon = '✗'
        result_color = Colors.BRIGHT_RED
        result_text = result_clean.lstrip('✗✘ ')
    else:
        # Auto-detect based on content
        result_icon = '✓'
        result_color = Colors.BRIGHT_GREEN
        result_text = summarize_output(result_clean)

    # Collapse the chosen result line back to a single sanitized line.
    result_text = sanitize(result_text)

    # Line 1: Level + Command
    level_str = f"{config['name']}: {config['desc'].upper()}"
    print(f"{config['color']}{Colors.BOLD}{config['emoji']} {level_str}: {command}{Colors.RESET}")
    
    # Line 2: Result
    print(f"{Colors.BOLD}{result_color}{result_icon}{Colors.RESET}  {result_text}")
    
    # Line 3: Purpose
    print(f"{Colors.CYAN}📋 {purpose}{Colors.RESET}")
    
    # Line 4: Warning or Action (optional, only one shown if both provided)
    if warning:
        print(f"{Colors.BRIGHT_RED}{Colors.BOLD}⚠️  {warning}{Colors.RESET}")
    elif action:
        print(f"{Colors.BRIGHT_YELLOW}👉 {action}{Colors.RESET}")


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        print("\nUsage: cmd_display.py <level> <command> <purpose> <result> [warning] [action]")
        print(f"Levels: {', '.join(LEVELS.keys())}")
        sys.exit(1)

    level = sys.argv[1].lower()
    command = sys.argv[2]
    purpose = sys.argv[3]
    result = sys.argv[4]
    warning = sys.argv[5] if len(sys.argv) > 5 else None
    action = sys.argv[6] if len(sys.argv) > 6 else None

    format_command(level, command, purpose, result, warning, action)


if __name__ == '__main__':
    main()
