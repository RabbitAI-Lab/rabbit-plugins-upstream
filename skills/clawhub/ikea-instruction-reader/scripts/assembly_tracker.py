#!/usr/bin/env python3
"""
Furniture Assembly Tracker

Tracks parts inventory, step completion, and provides status reports
for flat-pack furniture assembly.

Usage:
  python assembly_tracker.py init --name "KALLAX" --parts-json '{"dowel": 48, "cam_lock": 48}'
  python assembly_tracker.py use --step 3 --parts "dowel:8,cam_lock:8"
  python assembly_tracker.py status
  python assembly_tracker.py verify
"""

import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


STATE_DIR = Path.home() / ".assembly_tracker"
STATE_FILE = STATE_DIR / "current_project.json"


def load_state() -> dict:
    """Load current project state."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict):
    """Save project state."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def cmd_init(args):
    """Initialize a new assembly project."""
    parts = {}
    if args.parts_json:
        parts = json.loads(args.parts_json)
    elif args.parts:
        for item in args.parts.split(','):
            name, qty = item.split(':')
            parts[name.strip()] = int(qty)
    
    steps = {}
    if args.total_steps:
        steps = {str(i): {'completed': False, 'parts_used': {}} for i in range(1, args.total_steps + 1)}
    
    state = {
        'name': args.name,
        'created': datetime.now().isoformat(),
        'total_parts': dict(parts),
        'used_parts': {},
        'remaining_parts': dict(parts),
        'steps': steps,
        'total_steps': args.total_steps or 0,
        'current_step': 1,
        'completed_steps': 0,
        'log': [],
    }
    save_state(state)
    print(f"✓ Project '{args.name}' initialized!")
    print(f"  Parts: {sum(parts.values())} total items across {len(parts)} types")
    if steps:
        print(f"  Steps: {args.total_steps}")
    print(f"  State saved to: {STATE_FILE}")


def cmd_use(args):
    """Mark parts as used in a step."""
    state = load_state()
    if not state:
        print("✗ No active project. Run 'init' first.", file=sys.stderr)
        sys.exit(1)
    
    parts_used = {}
    for item in args.parts.split(','):
        name, qty = item.split(':')
        parts_used[name.strip()] = int(qty)
    
    step_key = str(args.step)
    if step_key not in state.get('steps', {}):
        state.setdefault('steps', {})[step_key] = {'completed': False, 'parts_used': {}}
    
    # Deduct parts
    for name, qty in parts_used.items():
        remaining = state['remaining_parts'].get(name, 0)
        if remaining < qty:
            print(f"⚠️  WARNING: Using {qty}× {name} but only {remaining} remaining!")
        state['remaining_parts'][name] = remaining - qty
        state['used_parts'][name] = state['used_parts'].get(name, 0) + qty
        state['steps'][step_key]['parts_used'][name] = \
            state['steps'][step_key]['parts_used'].get(name, 0) + qty
    
    state['log'].append({
        'timestamp': datetime.now().isoformat(),
        'action': 'use',
        'step': args.step,
        'parts': parts_used,
    })
    save_state(state)
    
    print(f"✓ Step {args.step}: Marked {len(parts_used)} part types as used")
    for name, qty in parts_used.items():
        remaining = state['remaining_parts'].get(name, 0)
        print(f"  {name}: used {qty}, {remaining} remaining")


def cmd_complete(args):
    """Mark a step as complete."""
    state = load_state()
    if not state:
        print("✗ No active project.", file=sys.stderr)
        sys.exit(1)
    
    step_key = str(args.step)
    if step_key in state.get('steps', {}):
        if not state['steps'][step_key]['completed']:
            state['steps'][step_key]['completed'] = True
            state['completed_steps'] += 1
        state['current_step'] = args.step + 1
        state['log'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'complete',
            'step': args.step,
        })
        save_state(state)
        total = state.get('total_steps', 0)
        pct = (state['completed_steps'] / total * 100) if total else 0
        print(f"✓ Step {args.step} marked complete!")
        print(f"  Progress: {state['completed_steps']}/{total} steps ({pct:.0f}%)")
        print(f"  Next: Step {args.step + 1}")
    else:
        print(f"✗ Step {args.step} not found.", file=sys.stderr)


def cmd_status(args):
    """Show current assembly status."""
    state = load_state()
    if not state:
        print("✗ No active project.", file=sys.stderr)
        sys.exit(1)
    
    total_parts = sum(state.get('total_parts', {}).values())
    used_parts = sum(state.get('used_parts', {}).values())
    total_steps = state.get('total_steps', 0)
    completed = state.get('completed_steps', 0)
    current = state.get('current_step', 1)
    
    print()
    print("╔" + "═" * 50 + "╗")
    name_label = f"  {state['name']}"
    print(f"║{name_label:<50s}║")
    print("╠" + "═" * 50 + "╣")
    steps_label = f"  Steps: {completed}/{total_steps} ({completed/total_steps*100:.0f}%)" if total_steps else "  Steps: N/A"
    print(f"║{steps_label:<50s}║")
    if total_parts:
        parts_label = f"  Parts: {used_parts}/{total_parts} ({used_parts/total_parts*100:.0f}%)"
    else:
        parts_label = "  Parts: N/A"
    print(f"║{parts_label:<50s}║")
    print("╠" + "═" * 50 + "╣")
    
    # Steps
    for step_num in sorted(state.get('steps', {}).keys(), key=int):
        step = state['steps'][step_num]
        step_int = int(step_num)
        if step['completed']:
            label = f"  ✓ Step {step_int}"
            print(f"║{label:<50s}║")
        elif step_int == current:
            label = f"  → Step {step_int} (NEXT)"
            print(f"║{label:<50s}║")
        else:
            label = f"    Step {step_int}"
            print(f"║{label:<50s}║")
    
    # Remaining parts summary
    print("╠" + "═" * 50 + "╣")
    remaining = {k: v for k, v in state.get('remaining_parts', {}).items() if v > 0}
    if remaining:
        label = "  Remaining parts:"
        print(f"║{label:<50s}║")
        for name, qty in sorted(remaining.items()):
            line = f"    {name}: {qty}"
            print(f"║{line:<50s}║")
    
    # Warnings
    neg_parts = {k: v for k, v in state.get('remaining_parts', {}).items() if v < 0}
    if neg_parts:
        print("╠" + "═" * 50 + "╣")
        for name, qty in neg_parts.items():
            line = f"  ⚠ OVERUSED {name} by {abs(qty)}!"
            print(f"║{line:<50s}║")
    
    print("╚" + "═" * 50 + "╝")
    print()


def cmd_verify(args):
    """Verify remaining parts are non-negative and check for anomalies."""
    state = load_state()
    if not state:
        print("✗ No active project.", file=sys.stderr)
        sys.exit(1)
    
    issues = []
    
    # Check for overused parts
    for name, remaining in state.get('remaining_parts', {}).items():
        if remaining < 0:
            issues.append(f"OVERUSED: {name} used {abs(remaining)} more than available!")
    
    # Check for unused parts
    total_remaining = sum(state.get('remaining_parts', {}).values())
    total = sum(state.get('total_parts', {}).values())
    if total > 0 and state.get('completed_steps', 0) == state.get('total_steps', 0):
        unused = {k: v for k, v in state.get('remaining_parts', {}).items() if v > 0}
        if unused:
            issues.append("Assembly complete but parts remain:")
            for name, qty in unused.items():
                issues.append(f"  Leftover: {qty}× {name}")
    
    # Check step parts
    for step_num, step in state.get('steps', {}).items():
        if step['parts_used'] and not step['completed']:
            issues.append(f"Step {step_num} has parts used but not marked complete")
    
    if issues:
        print("⚠️  ISSUES FOUND:")
        for issue in issues:
            print(f"  • {issue}")
    else:
        print("✓ All checks passed! No issues detected.")
    
    return issues


def main():
    parser = argparse.ArgumentParser(
        description='Flat-pack furniture assembly tracker'
    )
    sub = parser.add_subparsers(dest='command')
    
    # init
    p_init = sub.add_parser('init', help='Initialize a new assembly project')
    p_init.add_argument('--name', required=True, help='Project name')
    p_init.add_argument('--parts', help='Parts as name:qty,name:qty')
    p_init.add_argument('--parts-json', help='Parts as JSON')
    p_init.add_argument('--total-steps', type=int, help='Total number of steps')
    
    # use
    p_use = sub.add_parser('use', help='Mark parts as used in a step')
    p_use.add_argument('--step', type=int, required=True)
    p_use.add_argument('--parts', required=True, help='Parts as name:qty,name:qty')
    
    # complete
    p_complete = sub.add_parser('complete', help='Mark a step as complete')
    p_complete.add_argument('--step', type=int, required=True)
    
    # status
    sub.add_parser('status', help='Show current assembly status')
    
    # verify
    sub.add_parser('verify', help='Verify parts and check for issues')
    
    args = parser.parse_args()
    
    if args.command == 'init':
        cmd_init(args)
    elif args.command == 'use':
        cmd_use(args)
    elif args.command == 'complete':
        cmd_complete(args)
    elif args.command == 'status':
        cmd_status(args)
    elif args.command == 'verify':
        cmd_verify(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
