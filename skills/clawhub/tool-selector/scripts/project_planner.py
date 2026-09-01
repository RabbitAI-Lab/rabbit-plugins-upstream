#!/usr/bin/env python3
"""
DIY Project Planner

Generates complete project plans including tools, materials, costs,
and step-by-step instructions for common DIY projects.

Usage:
  python project_planner.py plan "raised garden bed"
  python project_planner.py plan "shelf" --have "drill,screwdriver"
  python project_planner.py list
  python project_planner.py cost "picture frame"
"""

import argparse
import sys
import json


# ─── Project Database ─────────────────────────────────────────────────────────

PROJECTS = {
    'raised garden bed': {
        'category': 'Outdoor',
        'difficulty': 'Beginner',
        'time': '2-3 hours',
        'tools': {
            'required': [
                ('Cordless drill', 40, 'Driving screws'),
                ('Circular saw or hand saw', 40, 'Cutting boards to length'),
                ('Measuring tape', 10, 'Measuring cuts'),
            ],
            'recommended': [
                ('Speed square', 8, 'Marking straight cuts'),
                ('Phillips bit set', 12, 'For driving deck screws'),
                ('Safety glasses', 8, 'Eye protection'),
            ],
        },
        'materials': [
            ('Cedar 2×6 board, 8ft', 4, 12, 'Side and end panels'),
            ('Cedar 2×4 board, 8ft', 2, 7, 'Corner posts'),
            ('Exterior deck screws, 3" (box of 100)', 1, 8, 'Assembly'),
            ('Landscape fabric, 4×8ft', 1, 5, 'Weed barrier'),
            ('Potting soil (cubic feet)', 12, 2.5, 'Fill the bed'),
        ],
        'steps': [
            'Measure and mark cut lines on all boards.',
            'Cut side boards to desired length (typically 4ft sides, 8ft ends).',
            'Cut 4 corner posts from 2×4, 12" each.',
            'Pre-drill holes to prevent cedar from splitting.',
            'Attach side boards to corner posts with 3" deck screws, staggering joints.',
            'Place bed in final location, level if needed.',
            'Line bottom with landscape fabric.',
            'Fill with potting soil and plant.',
        ],
        'safety': ['Safety glasses', 'Work gloves'],
        'notes': 'Use cedar or redwood for edible gardens. Avoid pressure-treated lumber for food crops.',
    },
    'floating shelf': {
        'category': 'Hanging & Mounting',
        'difficulty': 'Beginner',
        'time': '1-2 hours',
        'tools': {
            'required': [
                ('Stud finder', 15, 'Locating wall studs'),
                ('Cordless drill', 40, 'Drilling pilot holes'),
                ('Level (24")', 10, 'Ensuring shelf is straight'),
                ('Measuring tape', 10, 'Spacing brackets'),
            ],
            'recommended': [
                ('Phillips screwdriver', 8, 'Manual tightening'),
                ('Pencil', 1, 'Marking drill points'),
                ('Safety glasses', 8, 'Eye protection'),
            ],
        },
        'materials': [
            ('Floating shelf bracket (heavy-duty)', 2, 8, 'Support'),
            ('Wood screws 2.5" (for studs)', 4, 0.25, 'Mounting brackets'),
            ('Drywall anchors (if no stud)', 4, 1, 'Alternative mounting'),
            ('Shelf board', 1, 20, 'The actual shelf'),
        ],
        'steps': [
            'Use stud finder to locate wall studs in desired location.',
            'Mark stud locations with pencil at shelf height.',
            'Hold level against wall and mark bracket positions.',
            'Drill pilot holes at marks (into studs if possible).',
            'Install first bracket with 2.5" wood screws into stud.',
            'Install second bracket, checking level.',
            'If no stud available, use heavy-duty drywall anchors (50lb+ rated).',
            'Place shelf on brackets and secure per bracket instructions.',
        ],
        'safety': ['Safety glasses'],
        'notes': 'For shelves holding books, always anchor into studs. Drywall anchors alone may fail.',
    },
    'picture frame': {
        'category': 'Woodworking',
        'difficulty': 'Beginner',
        'time': '1 hour',
        'tools': {
            'required': [
                ('Miter saw or miter box', 15, '45° angle cuts'),
                ('Measuring tape', 10, 'Measuring frame pieces'),
                ('Bar clamps (2)', 12, 'Holding frame during glue-up'),
            ],
            'recommended': [
                ('Corner clamps', 10, 'Keeping corners square'),
                ('Sandpaper (120 and 220 grit)', 3, 'Smoothing edges'),
                ('Wood glue brush', 2, 'Applying glue evenly'),
            ],
        },
        'materials': [
            ('Picture frame moulding', 1, 15, 'Frame material'),
            ('Wood glue', 1, 5, 'Bonding corners'),
            ('Finishing nails (1")', 20, 2, 'Reinforcing joints'),
            ('Picture hanging hardware', 1, 3, 'Sawtooth hanger'),
            ('Glass/acrylic pane', 1, 8, 'Protecting artwork'),
            ('Mat board (optional)', 1, 5, 'Decorative border'),
        ],
        'steps': [
            'Measure artwork and calculate frame dimensions (add 1/4" overlap per side).',
            'Cut 4 pieces of moulding with 45° miter cuts using miter saw.',
            'Dry-fit pieces to verify corners meet cleanly.',
            'Apply wood glue to all mitered edges.',
            'Assemble frame and clamp with bar clamps and corner clamps.',
            'Wipe excess glue with damp cloth.',
            'Let glue dry for 1 hour minimum.',
            'Reinforce corners with 1" finishing nails (pre-drill first).',
            'Sand all surfaces smooth, starting with 120 grit then 220 grit.',
            'Insert glass, mat, artwork, and backing. Attach hanging hardware.',
        ],
        'safety': ['Safety glasses', 'Dust mask (when sanding)'],
        'notes': 'For precise miter joints, cut slightly long and trim to exact length.',
    },
    'tv wall mount': {
        'category': 'Hanging & Mounting',
        'difficulty': 'Intermediate',
        'time': '1-2 hours',
        'tools': {
            'required': [
                ('Stud finder', 15, 'Critical: locate studs for TV weight'),
                ('Cordless drill', 40, 'Drilling into studs'),
                ('Level (24")', 10, 'Level mount plate'),
                ('Socket set (metric)', 15, 'Bolting TV to mount'),
                ('Measuring tape', 10, 'Positioning'),
            ],
            'recommended': [
                ('Pencil', 1, 'Marking'),
                ('Safety glasses', 8, 'Drilling protection'),
                ('Drywall saw', 8, 'For in-wall cable routing'),
            ],
        },
        'materials': [
            ('TV wall mount bracket (VESA-compatible)', 1, 30, 'Mounting hardware'),
            ('Lag bolts 3/8" × 3" (usually included)', 4, 1, 'Mounting to studs'),
            ('In-wall cable management kit (optional)', 1, 15, 'Hiding cables'),
        ],
        'steps': [
            'Determine TV height (center of screen at eye level when seated).',
            'Use stud finder to locate 2 studs at bracket spacing.',
            'Mark stud centers and bracket holes with pencil.',
            'Verify marks are level using the level.',
            'Drill pilot holes for lag bolts (slightly smaller than bolt).',
            'Bolt wall plate to studs with lag bolts — TIGHTEN FIRMLY.',
            'Attach mounting arms to back of TV per manufacturer instructions.',
            'Lift TV and hook onto wall plate (get help for large TVs!).',
            'Route cables through wall or cable management kit.',
            'Secure safety lock if mount has one.',
        ],
        'safety': ['Safety glasses', 'Get a second person to help lift'],
        'notes': 'ALWAYS mount into studs. A 50lb TV on drywall anchors is dangerous. Verify VESA pattern matches your TV.',
    },
    'leaky faucet repair': {
        'category': 'Plumbing',
        'difficulty': 'Beginner-Intermediate',
        'time': '30-60 min',
        'tools': {
            'required': [
                ('Adjustable wrench', 10, 'Removing faucet parts'),
                ('Phillips and flathead screwdriver', 8, 'Handle screws'),
                ('Basin wrench', 12, 'Hard-to-reach supply nuts'),
                ('Slip-joint pliers', 10, 'Gripping parts'),
            ],
            'recommended': [
                ('Replacement O-rings/washers kit', 5, 'Most common fix'),
                ('Plumber\'s grease', 4, 'Lubricating O-rings'),
                ('Towel', 0, 'Catching water'),
                'Flashlight', 5, 'Seeing under sink',
            ],
        },
        'materials': [
            ('Faucet repair kit (brand-specific)', 1, 10, 'New washers/O-rings/cartridge'),
            ('Plumber\'s tape (Teflon)', 1, 2, 'Thread sealing'),
        ],
        'steps': [
            'TURN OFF WATER SUPPLY (valves under sink).',
            'Open faucet to drain remaining water.',
            'Remove decorative cap on handle and unscrew handle.',
            'Remove the cartridge or stem (take photo first for reference).',
            'Inspect O-rings and washers for wear.',
            'Replace worn parts with exact matches from repair kit.',
            'Apply plumber\'s grease to new O-rings.',
            'Reassemble in reverse order.',
            'Turn water supply back on and test for leaks.',
        ],
        'safety': ['Towel to catch water'],
        'notes': 'Take a photo before disassembling. Bring old parts to the store for exact matching. If the faucet is old, replacing it may be cheaper than repairing.',
    },
    'ceiling fan install': {
        'category': 'Electrical',
        'difficulty': 'Intermediate',
        'time': '2-3 hours',
        'tools': {
            'required': [
                ('Cordless drill', 40, 'Mounting bracket screws'),
                ('Voltage tester', 10, 'CRITICAL: verify power is off'),
                ('Wire strippers', 10, 'Preparing wires'),
                ('Adjustable wrench', 10, 'Motor housing bolts'),
                ('Screwdriver set', 8, 'Various assembly screws'),
            ],
            'recommended': [
                ('Circuit finder', 15, 'Identifying breaker'),
                ('Stepladder', 30, 'Reaching ceiling'),
            ],
        },
        'materials': [
            ('Ceiling fan (with light kit)', 1, 80, 'The fan unit'),
            ('Fan-rated ceiling box', 1, 8, 'MUST support fan weight'),
            ('Wire nuts (assorted)', 1, 3, 'Connecting wires'),
        ],
        'steps': [
            'TURN OFF BREAKER for the circuit. Verify with voltage tester!',
            'Remove existing light fixture.',
            'Verify the ceiling box is fan-rated. If not, replace it (critical safety).',
            'Install fan mounting bracket to ceiling box.',
            'Assemble fan motor housing per instructions.',
            'Hang motor on mounting bracket (use the temporary support hook).',
            'Connect wires: black-to-black, white-to-white, ground-to-ground.',
            'Secure wire nuts and tuck wires into box.',
            'Attach fan blades.',
            'Attach light kit if included.',
            'Install remote receiver if applicable.',
            'Turn breaker on and test all functions.',
        ],
        'safety': ['Voltage tester (non-negotiable)', 'Stepladder', 'Safety glasses'],
        'notes': 'Standard ceiling boxes do NOT support fan weight. You MUST use a fan-rated box. If unsure, hire an electrician.',
    },
}


def normalize_query(query: str) -> str:
    """Normalize a project query to match database keys."""
    q = query.lower().strip()
    for key in PROJECTS:
        if key in q or q in key:
            return key
    return q


def find_project(query: str) -> dict:
    """Find a project by fuzzy matching."""
    q = query.lower().strip()
    # Exact match
    if q in PROJECTS:
        return PROJECTS[q]
    # Partial match
    for key, proj in PROJECTS.items():
        if q in key or key in q:
            return proj
        # Check category
        if q in proj.get('category', '').lower():
            return proj
    return None


def calculate_cost(project: dict) -> tuple:
    """Calculate total material cost range."""
    total_low = 0
    for item in project['materials']:
        qty = item[1]
        unit_cost = item[2]
        total_low += qty * unit_cost
    return total_low


def plan_project(query: str, have_tools: str = ''):
    """Generate a project plan."""
    project = find_project(query)
    if not project:
        print(f"Project not found: '{query}'")
        print(f"\nAvailable projects:")
        list_projects()
        return
    
    have = set(t.strip().lower() for t in have_tools.split(',') if t.strip())
    
    cost = calculate_cost(project)
    
    print()
    print("═" * 55)
    print(f"  📊 PROJECT: {query.title()}")
    print(f"  ⏱️  Time: {project['time']} | 🎯 Difficulty: {project['difficulty']}")
    print("═" * 55)
    print()
    
    # Tools
    print("TOOLS NEEDED:")
    all_tools = project['tools']['required'] + project['tools']['recommended']
    for tool_info in all_tools:
        name, price, purpose = tool_info[0], tool_info[1], tool_info[2]
        is_req = tool_info in project['tools']['required']
        tag = "required" if is_req else "recommended"
        
        # Check if user has this tool
        have_match = any(h in name.lower() or name.lower() in h for h in have)
        icon = "✅" if have_match else ("⬜" if is_req else "💡")
        
        print(f"  {icon} {name}")
        print(f"     ~${price} ({tag}) — {purpose}")
    
    print()
    
    # Materials
    print("MATERIALS:")
    for mat in project['materials']:
        name, qty, unit, purpose = mat
        line_cost = qty * unit
        print(f"  • {name}")
        print(f"    Qty: {qty} × ${unit} = ~${line_cost}")
        print(f"    Use: {purpose}")
    
    # Add waste buffer
    buffer = int(cost * 0.15)
    print(f"\n  💰 MATERIALS TOTAL: ~${cost}")
    print(f"  + 15% waste buffer: +${buffer}")
    print(f"  📌 RECOMMENDED BUDGET: ~${cost + buffer}")
    
    print()
    
    # Safety
    print("⚠️  SAFETY GEAR:")
    for item in project['safety']:
        print(f"  • {item}")
    
    print()
    
    # Steps
    print("📋 STEPS:")
    for i, step in enumerate(project['steps'], 1):
        print(f"  {i}. {step}")
    
    print()
    
    # Notes
    if project.get('notes'):
        print(f"📝 NOTES: {project['notes']}")
        print()


def list_projects():
    """List all available projects."""
    print("\n📋 AVAILABLE PROJECTS:")
    print()
    
    categories = {}
    for name, proj in PROJECTS.items():
        cat = proj.get('category', 'Other')
        categories.setdefault(cat, []).append((name, proj))
    
    for cat in sorted(categories.keys()):
        print(f"  {cat}:")
        for name, proj in categories[cat]:
            print(f"    • {name} ({proj['difficulty']}, {proj['time']})")
        print()


def cost_estimate(query: str):
    """Just show cost estimate."""
    project = find_project(query)
    if not project:
        print(f"Project not found: '{query}'")
        return
    
    cost = calculate_cost(project)
    buffer = int(cost * 0.15)
    
    print(f"\n💰 COST ESTIMATE: {query.title()}")
    print(f"  Materials base: ${cost}")
    print(f"  + 15% buffer:   ${buffer}")
    print(f"  Total:          ~${cost + buffer}")
    print(f"\n  Cost breakdown:")
    for mat in project['materials']:
        name, qty, unit, purpose = mat
        print(f"    {name}: {qty} × ${unit} = ${qty * unit}")


def main():
    parser = argparse.ArgumentParser(
        description='DIY Project Planner — tools, materials, costs, steps'
    )
    sub = parser.add_subparsers(dest='command')
    
    # plan
    p_plan = sub.add_parser('plan', help='Generate a project plan')
    p_plan.add_argument('project', help='Project name or description')
    p_plan.add_argument('--have', default='', help='Comma-separated tools you already own')
    
    # list
    sub.add_parser('list', help='List all available projects')
    
    # cost
    p_cost = sub.add_parser('cost', help='Show cost estimate for a project')
    p_cost.add_argument('project', help='Project name')
    
    args = parser.parse_args()
    
    if args.command == 'plan':
        plan_project(args.project, args.have)
    elif args.command == 'list':
        list_projects()
    elif args.command == 'cost':
        cost_estimate(args.project)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
