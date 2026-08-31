#!/usr/bin/env python3
"""
Tool Substitution Finder

Find alternative tools when you don't have the exact one needed.

Usage:
  python tool_substitution.py "miter saw"
  python tool_substitution.py "pipe wrench"
"""

import argparse
import sys


SUBSTITUTIONS = {
    'miter saw': [
        ('Circular saw + speed square', 'Good', 'For straight cuts. Clamp a speed square as a guide.'),
        ('Circular saw + miter guide', 'Good', 'For angle cuts up to 45°. Less precise than miter saw.'),
        ('Hand saw + miter box', 'Workable', 'Slower but accurate for small projects. Great for trim.'),
        ('Table saw with miter gauge', 'Good', 'For wider material. Limited angle range.'),
    ],
    'circular saw': [
        ('Hand saw', 'Workable', 'Much slower. Good for small cuts.'),
        ('Jigsaw with long blade', 'Last Resort', 'Not ideal for straight cuts in thick wood.'),
        ('Table saw', 'Good', 'If material size allows, better precision.'),
        ('Track saw', 'Exact Match', 'Premium alternative with guide rail.'),
    ],
    'cordless drill': [
        ('Corded drill', 'Exact Match', 'Just need an outlet. Equal power.'),
        ('Hand drill (eggbeater)', 'Last Resort', 'Manual. Only for small holes.'),
        ('Impact driver', 'Good', 'Better for driving screws. Can drill with adapter.'),
        ('Rotary tool (Dremel)', 'Last Resort', 'Only for tiny holes.'),
    ],
    'pipe wrench': [
        ('Adjustable pliers (Channel-lock)', 'Good', 'For small pipes (up to 1").'),
        ('Strap wrench', 'Good', 'Won\'t scratch chrome/surface finishes.'),
        ('Basin wrench', 'Last Resort', 'Only for tight spaces under sinks.'),
        ('Adjustable crescent wrench', 'Workable', 'For hex fittings and small pipes.'),
    ],
    'stud finder': [
        ('Magnet on string', 'Good', 'Find drywall screws/nails. Free DIY method.'),
        ('Tapping/knocking', 'Workable', 'Listen for solid sound vs hollow. Less reliable.'),
        ('Measuring from outlet', 'Good', 'Outlets attach to studs. Measure 16" from outlet.'),
        ('Finish nail probe', 'Last Resort', 'Tiny hole to locate stud. Patch after.'),
    ],
    'level': [
        ('Smartphone level app', 'Good', 'Surprisingly accurate for basic tasks.'),
        ('Water level (hose + water)', 'Good', 'DIY: clear hose filled with water. Very accurate over distance.'),
        ('Marble test', 'Workable', 'Place round object, see if it rolls. Rough check only.'),
        ('Framing square + plumb bob', 'Workable', 'Traditional method. Takes practice.'),
    ],
    'orbital sander': [
        ('Sandpaper + sanding block', 'Good', 'Slower but effective. Use a cork or rubber block.'),
        ('Hand sanding', 'Workable', 'Very slow for large surfaces. Fine for small projects.'),
        ('Mouse sander', 'Good', 'Similar function, different shape for corners.'),
        ('Belt sander', 'Last Resort', 'Too aggressive for finishing. Will remove too much material.'),
    ],
    'jigsaw': [
        ('Coping saw', 'Workable', 'Manual version. Good for thin material.'),
        ('Reciprocating saw', 'Last Resort', 'Rougher cuts. Better for demolition.'),
        ('Scroll saw', 'Good', 'For very fine/intricate work in thin material.'),
        ('Router with circle jig', 'Workable', 'For specific curved cuts only.'),
    ],
    'wire strippers': [
        ('Utility knife', 'Workable', 'Score insulation and pull. Risky for delicate wire.'),
        ('Pliers + scissors', 'Workable', 'Use pliers to grip, scissors to score insulation.'),
        ('Diagonal cutters', 'Last Resort', 'Can strip but risks cutting the wire.'),
        ('Teeth', 'Last Resort', 'Only for thick insulation on large wire. Don\'t do this.'),
    ],
    'torque wrench': [
        ('Regular wrench + scale', 'Workable', 'Estimate force. Not precise. Risky for critical applications.'),
        ('Factory spec + feel', 'Last Resort', 'Tighten until "snug plus 1/4 turn." NOT recommended.'),
        ('Beam-type torque wrench', 'Good', 'Cheaper alternative. Less convenient but accurate.'),
    ],
    'clamp': [
        ('Heavy books/weights', 'Workable', 'For glue-ups on flat surfaces.'),
        ('Bungee cords/ratchet straps', 'Good', 'For irregular shapes or large pieces.'),
        ('Vise grips (locking pliers)', 'Good', 'For small parts. Can damage wood without pads.'),
        ('String/rope tourniquet', 'Workable', 'Old technique: loop rope around and twist a stick.'),
    ],
}


ICONS = {
    'Exact Match': '⭐',
    'Good': '✅',
    'Workable': '⚠️',
    'Last Resort': '❌',
}


def find_substitution(tool: str):
    """Find alternatives for a given tool."""
    tool_lower = tool.lower().strip()
    
    # Direct match
    if tool_lower in SUBSTITUTIONS:
        return SUBSTITUTIONS[tool_lower]
    
    # Partial match
    for key, subs in SUBSTITUTIONS.items():
        if tool_lower in key or key in tool_lower:
            return subs
    
    return None


def show_substitutions(tool: str):
    """Display substitutions for a tool."""
    subs = find_substitution(tool)
    
    if not subs:
        print(f"\nNo specific substitution data for '{tool}'.")
        print("General principle: look for tools with similar function —")
        print("  cutting → different saws, knives, or abrasive tools")
        print("  gripping → pliers, clamps, vise grips, straps")
        print("  measuring → different measuring devices or reference points")
        return
    
    print(f"\n🔧 ALTERNATIVES FOR: {tool.upper()}")
    print("=" * 55)
    print()
    
    # Sort by quality
    quality_order = {'Exact Match': 0, 'Good': 1, 'Workable': 2, 'Last Resort': 3}
    sorted_subs = sorted(subs, key=lambda x: quality_order.get(x[1], 4))
    
    for alt, quality, notes in sorted_subs:
        icon = ICONS.get(quality, '•')
        print(f"  {icon} {alt}")
        print(f"     Quality: {quality}")
        print(f"     Notes: {notes}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description='Find alternative tools when you don\'t have the exact one'
    )
    parser.add_argument('tool', help='The tool you need an alternative for')
    parser.add_argument('--list', action='store_true', help='List all tools with substitution data')
    
    args = parser.parse_args()
    
    if args.list:
        print("Tools with substitution data:")
        for tool in sorted(SUBSTITUTIONS.keys()):
            print(f"  • {tool}")
        return
    
    show_substitutions(args.tool)


if __name__ == '__main__':
    main()
