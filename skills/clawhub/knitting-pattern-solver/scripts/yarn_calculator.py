#!/usr/bin/env python3
"""
Knitting Yarn Calculator

Calculate total yarn requirements for a knitting project based on a gauge swatch.

Usage:
  python yarn_calculator.py --gauge-stitches 20 --gauge-rows 28 --swatch-yards 18 \
    --project-stitches 200 --project-rows 300
"""

import argparse
import sys
import math


# Common skein sizes (yards per 100g skein)
SKEIN_SIZES = {
    'fingering': 400,
    'sock': 440,
    'sport': 300,
    'dk': 220,
    'worsted': 200,
    'aran': 180,
    'bulky': 130,
    'super_bulky': 90,
}

# Dye-lot matching recommendation: always buy enough from the same lot
DYELOT_BUFFER = 0.15  # 15%


def calculate_yarn(
    gauge_stitches: float,
    gauge_rows: float,
    swatch_yards: float,
    project_stitches: int,
    project_rows: int,
    buffer: float = DYELOT_BUFFER,
) -> dict:
    """Calculate yarn requirements from gauge swatch data.
    
    Args:
        gauge_stitches: stitches per 4-inch swatch
        gauge_rows: rows per 4-inch swatch
        swatch_yards: yards consumed by the 4x4 swatch
        project_stitches: total stitches across project width
        project_rows: total rows in project
        buffer: safety buffer multiplier (0.15 = 15%)
    
    Returns:
        dict with calculation details
    """
    swatch_units = gauge_stitches * gauge_rows
    project_units = project_stitches * project_rows
    
    if swatch_units == 0:
        raise ValueError("Gauge stitches × rows cannot be zero")
    
    area_ratio = project_units / swatch_units
    estimated_yards = swatch_yards * area_ratio
    recommended_yards = estimated_yards * (1 + buffer)
    
    # Calculate for different yarn weights
    skein_estimates = {}
    for weight, yds_per_skein in SKEIN_SIZES.items():
        skeins_needed = math.ceil(recommended_yards / yds_per_skein)
        skein_estimates[weight] = {
            'yards_per_skein': yds_per_skein,
            'skeins': skeins_needed,
            'total_yards': skeins_needed * yds_per_skein,
        }
    
    # Calculate dimensions
    width_inches = (project_stitches / gauge_stitches) * 4
    length_inches = (project_rows / gauge_rows) * 4
    
    return {
        'swatch_units': swatch_units,
        'project_units': int(project_units),
        'area_ratio': area_ratio,
        'estimated_yards': round(estimated_yards, 1),
        'recommended_yards': round(recommended_yards, 1),
        'buffer_pct': buffer * 100,
        'width_inches': round(width_inches, 1),
        'length_inches': round(length_inches, 1),
        'width_cm': round(width_inches * 2.54, 1),
        'length_cm': round(length_inches * 2.54, 1),
        'skein_estimates': skein_estimates,
    }


def format_output(result: dict) -> str:
    """Format the calculation result for display."""
    lines = [
        "=" * 55,
        "🧶 YARN CALCULATION RESULTS",
        "=" * 55,
        "",
        f"Gauge swatch: {result['swatch_units']:.0f} stitch-units",
        f"Project:      {result['project_units']:,} stitch-units",
        f"Area ratio:   {result['area_ratio']:.2f}×",
        "",
        "📐 Estimated project dimensions:",
        f"   Width:  {result['width_inches']}\" ({result['width_cm']} cm)",
        f"   Length: {result['length_inches']}\" ({result['length_cm']} cm)",
        "",
        "🧶 Yarn needed:",
        f"   Base estimate:    {result['estimated_yards']:.0f} yards "
        f"({result['estimated_yards'] * 0.9144:.0f} m)",
        f"   With {result['buffer_pct']:.0f}% buffer: {result['recommended_yards']:.0f} yards "
        f"({result['recommended_yards'] * 0.9144:.0f} m)",
        "",
        "📦 Skein recommendations (buy from same dye lot!):",
    ]
    
    for weight, info in result['skein_estimates'].items():
        lines.append(
            f"   {weight:15s}: {info['skeins']} skeins × "
            f"{info['yards_per_skein']} yd = {info['total_yards']} yd"
        )
    
    lines.extend([
        "",
        "💡 Tip: Always buy all skeins from the same dye lot.",
        "    If substituting yarn, knit a new swatch and recalculate.",
    ])
    
    return '\n'.join(lines)


def main():
    p = argparse.ArgumentParser(
        description='Calculate knitting yarn requirements from gauge swatch'
    )
    p.add_argument('--gauge-stitches', type=float, required=True,
                  help='Stitches per 4-inch swatch')
    p.add_argument('--gauge-rows', type=float, required=True,
                  help='Rows per 4-inch swatch')
    p.add_argument('--swatch-yards', type=float, required=True,
                  help='Yards consumed by the swatch')
    p.add_argument('--project-stitches', type=int, required=True,
                  help='Total stitches across project width')
    p.add_argument('--project-rows', type=int, required=True,
                  help='Total rows in project')
    p.add_argument('--buffer', type=float, default=DYELOT_BUFFER,
                  help=f'Safety buffer (default: {DYELOT_BUFFER})')
    p.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = p.parse_args()
    
    try:
        result = calculate_yarn(
            gauge_stitches=args.gauge_stitches,
            gauge_rows=args.gauge_rows,
            swatch_yards=args.swatch_yards,
            project_stitches=args.project_stitches,
            project_rows=args.project_rows,
            buffer=args.buffer,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    if args.json:
        import json
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == '__main__':
    main()
