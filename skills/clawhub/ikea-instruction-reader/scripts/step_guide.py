#!/usr/bin/env python3
"""
Assembly Step Guide

Provides text guidance for common furniture assembly step types,
generates tool checklists, and warns about common mistakes.

Usage:
  python step_guide.py --type cam_lock
  python step_guide.py --type back_panel
  python step_guide.py --tools --project shelf
  python step_guide.py --warnings --step-type drawer_slide
"""

import argparse
import sys
import json


# Tool requirements by project type
PROJECT_TOOLS = {
    'shelf': [
        ('Allen key (4mm)', 'Included', 'For most cam locks and bolts'),
        ('Phillips screwdriver (#2)', 'Required', 'For screws and cam locks'),
        ('Hammer', 'Required', 'For back panel nails'),
        ('Level', 'Recommended', 'For wall anchoring'),
    ],
    'drawer_chest': [
        ('Allen key (4mm)', 'Included', 'For cam locks'),
        ('Phillips screwdriver (#2)', 'Required', 'For all screws'),
        ('Hammer', 'Required', 'For back panel and dowels'),
        ('Rubber mallet', 'Recommended', 'For tight drawer slide joints'),
        ('Level', 'Required', 'For wall anchoring (critical for dressers!)'),
    ],
    'table': [
        ('Allen key (4mm or 5mm)', 'Included', 'For leg attachment'),
        ('Phillips screwdriver (#2)', 'Required', 'For brackets'),
        ('Wrench (10mm)', 'Sometimes', 'For bolt-on legs'),
    ],
    'bed_frame': [
        ('Allen key (5mm)', 'Included', 'For center beam and corners'),
        ('Phillips screwdriver (#2)', 'Required', 'For slat holders'),
        ('Rubber mallet', 'Recommended', 'For wooden dowel joints'),
        ('Measuring tape', 'Recommended', 'To verify mattress fit'),
    ],
    'chair': [
        ('Allen key (4mm or 5mm)', 'Included', 'For seat-to-back bolts'),
        ('Phillips screwdriver (#2)', 'Required', 'For leg screws'),
        ('Wrench (10mm)', 'Sometimes', 'For bolted legs'),
    ],
}

# Step type guidance
STEP_GUIDES = {
    'cam_lock': {
        'title': 'Cam Lock Joint Assembly',
        'steps': [
            'Insert the wood dowel into the pre-drilled hole on the panel edge (the narrow side).',
            'Align the adjacent panel so the cam lock hole (larger round hole) faces you.',
            'Insert the cam lock into the round hole with the ARROW pointing toward the dowel.',
            'Turn the cam lock clockwise with a screwdriver until it tightens (about 180° turn).',
            'The joint should pull together snugly. If there\'s a gap, check that the dowel is fully inserted.',
        ],
        'common_mistakes': [
            'Arrow pointing AWAY from dowel → cam lock won\'t grab. Flip it.',
            'Forgetting to insert the dowel first → nothing for the cam lock to grab.',
            'Overtightening → can strip the cam lock. Stop when snug.',
            'Using cam lock without dowel → they work as a pair, always.',
        ],
    },
    'back_panel': {
        'title': 'Back Panel Installation',
        'steps': [
            'Lay the frame face-down on a flat, clean surface.',
            'Place the back panel onto the frame, unfinished side facing UP (toward you).',
            'Align all edges with the frame. The panel should fit exactly within the recessed lip.',
            'Verify the frame is SQUARE: measure both diagonals — they must be equal.',
            'Nail the panel starting from the CENTER of each edge, working outward.',
            'Place a nail every 6 inches (15cm) along all four edges.',
        ],
        'common_mistakes': [
            'Nailing corners first → panel buckles in the middle. Start from center.',
            'Frame not square before nailing → permanently crooked furniture.',
            'Finished side of panel facing up → visible nails from the front.',
            'Too few nails → back panel rattles, furniture is wobbly.',
        ],
    },
    'drawer_slide': {
        'title': 'Drawer Slide Installation',
        'steps': [
            'Identify the FRAME-SIDE tracks (usually wider, with a locking bracket).',
            'Identify the DRAWER-SIDE tracks (usually narrower, with wheels).',
            'Install frame-side tracks on the cabinet interior, screws in the elongated holes first.',
            'Install drawer-side tracks on the drawer sides.',
            'Test: slide the drawer in. It should click into place and slide smoothly.',
            'Adjust: if sticking, loosen screws slightly and reposition.',
        ],
        'common_mistakes': [
            'Mixing up frame-side and drawer-side tracks → drawer won\'t fit.',
            'Installing left/right slides on wrong sides → drawer slides out by itself.',
            'Tightening all screws before testing → can\'t adjust.',
            'Installing slides at wrong height → drawer doesn\'t align with face frame.',
        ],
    },
    'shelf_pin': {
        'title': 'Adjustable Shelf Placement',
        'steps': [
            'Count the shelf support pins (usually 4 per shelf).',
            'Insert pins into the pre-drilled holes at your desired shelf height.',
            'All 4 pins must be at the SAME height — use a measuring tape to verify.',
            'Ensure the flat side of the pin faces UP to support the shelf.',
            'Lower the shelf onto the pins. It should rest evenly.',
        ],
        'common_mistakes': [
            'Uneven pin heights → shelf wobbles.',
            'Pins upside down → shelf falls through.',
            'Using fewer than 4 pins → shelf sags under weight.',
        ],
    },
    'wall_anchor': {
        'title': 'Wall Anchoring (CRITICAL SAFETY STEP)',
        'steps': [
            'Position the furniture in its final location against the wall.',
            'Mark the wall through the anchor bracket holes.',
            'Drill pilot holes at the marks (use wall-appropriate anchors).',
            'Screw the bracket to the wall. Test by pulling — it must hold firm.',
            'Attach the furniture to the bracket per the included hardware.',
        ],
        'common_mistakes': [
            'Skipping this step → furniture can tip and cause serious injury or death.',
            'Using drywall without anchors → bracket pulls out easily.',
            'Anchoring to baseboard instead of wall stud → weak anchor.',
            'Not testing the anchor → false sense of security.',
        ],
    },
}


def show_step_guide(step_type: str):
    """Show guidance for a specific step type."""
    if step_type not in STEP_GUIDES:
        print(f"Unknown step type: {step_type}")
        print(f"Available types: {', '.join(STEP_GUIDES.keys())}")
        sys.exit(1)
    
    guide = STEP_GUIDES[step_type]
    print("=" * 55)
    print(f"🔧 {guide['title']}")
    print("=" * 55)
    print()
    print("STEPS:")
    for i, step in enumerate(guide['steps'], 1):
        print(f"  {i}. {step}")
    print()
    print("⚠️  COMMON MISTAKES:")
    for mistake in guide['common_mistakes']:
        print(f"  • {mistake}")
    print()


def show_tools(project_type: str):
    """Show required tools for a project type."""
    if project_type not in PROJECT_TOOLS:
        print(f"Unknown project type: {project_type}")
        print(f"Available types: {', '.join(PROJECT_TOOLS.keys())}")
        sys.exit(1)
    
    tools = PROJECT_TOOLS[project_type]
    print("=" * 55)
    print(f"🛠️  TOOL CHECKLIST: {project_type.replace('_', ' ').title()}")
    print("=" * 55)
    print()
    for tool, status, notes in tools:
        icon = '✅' if status == 'Required' else ('📦' if status == 'Included' else '💡')
        print(f"  {icon} {tool}")
        print(f"     Status: {status}")
        print(f"     Notes:  {notes}")
        print()


def show_warnings(step_type: str):
    """Show only warnings for a step type."""
    if step_type not in STEP_GUIDES:
        print(f"Unknown step type: {step_type}")
        sys.exit(1)
    
    guide = STEP_GUIDES[step_type]
    print(f"⚠️  WARNINGS for {guide['title']}:")
    for mistake in guide['common_mistakes']:
        print(f"  • {mistake}")


def main():
    parser = argparse.ArgumentParser(
        description='Furniture assembly step guide and tool checklist'
    )
    parser.add_argument('--type', help='Step type to show guidance for')
    parser.add_argument('--tools', action='store_true', help='Show tool checklist')
    parser.add_argument('--project', default='shelf', help='Project type for tools')
    parser.add_argument('--warnings', action='store_true', help='Show warnings only')
    parser.add_argument('--step-type', help='Step type for warnings')
    parser.add_argument('--list-types', action='store_true', help='List all step types')
    
    args = parser.parse_args()
    
    if args.list_types:
        print("Available step types:")
        for stype, guide in STEP_GUIDES.items():
            print(f"  {stype}: {guide['title']}")
        return
    
    if args.tools:
        show_tools(args.project)
    elif args.warnings and args.step_type:
        show_warnings(args.step_type)
    elif args.type:
        show_step_guide(args.type)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
