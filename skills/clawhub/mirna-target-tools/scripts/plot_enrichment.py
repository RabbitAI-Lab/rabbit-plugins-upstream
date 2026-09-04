#!/usr/bin/env python3
"""
Plot functional enrichment results as a publication-style bubble plot.

Input: enrichment TSV produced by annotate_targets.py (g:Profiler output).

Usage:
  python plot_enrichment.py --input merged_enrichment_all.tsv \
      --output enrichment_bubble.png [--source GO:BP] [--top 15]

Dependencies:
  pip install pandas numpy matplotlib
"""

import argparse
import sys
import os

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(
        description='Plot enrichment results as a bubble plot')
    parser.add_argument('--input', required=True, help='Enrichment TSV from annotate_targets.py')
    parser.add_argument('--output', required=True, help='Output PNG file')
    parser.add_argument('--source', default=None,
                        help='Restrict to one source (GO:BP/GO:CC/GO:MF/KEGG); default: all sources')
    parser.add_argument('--top', type=int, default=15,
                        help='Show top N terms by p-value (default: 15)')
    parser.add_argument('--figsize', default='9,6',
                        help='Figure size width,height in inches (default: 9,6)')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: input file '{args.input}' not found!")
        sys.exit(1)

    df = pd.read_csv(args.input, sep='\t')

    # Required columns (g:Profiler / gseapy output)
    if 'name' not in df.columns or 'p_value' not in df.columns:
        print("Error: input must have 'name' and 'p_value' columns.")
        print(f"Found columns: {list(df.columns)}")
        sys.exit(1)

    if args.source:
        if 'source' not in df.columns:
            print("Error: --source requested but input has no 'source' column.")
            sys.exit(1)
        df = df[df['source'] == args.source]
        if len(df) == 0:
            print(f"No terms for source '{args.source}'.")
            sys.exit(1)

    # Size column: number of queried genes in the term
    size_col = None
    for c in ('intersection_size', 'query_size', 'term_size'):
        if c in df.columns:
            size_col = c
            break
    if size_col is None:
        df['_size'] = 20
        size_col = '_size'

    df = df.sort_values('p_value').head(args.top).copy()
    df['neg_log10_p'] = df['p_value'].apply(
        lambda p: -np.log10(p) if p > 0 else float('inf'))

    # Truncate long term names for readability
    df['label'] = df['name'].apply(lambda s: s if len(str(s)) <= 60 else str(s)[:57] + '...')

    w, h = [float(x) for x in args.figsize.split(',')]
    fig, ax = plt.subplots(figsize=(w, h))

    sc = ax.scatter(
        df['neg_log10_p'],
        range(len(df))[::-1],
        s=df[size_col] * 12,
        c=df['p_value'],
        cmap='viridis_r',
        edgecolors='black',
        linewidths=0.4,
        alpha=0.9,
    )

    ax.set_yticks(range(len(df))[::-1])
    ax.set_yticklabels(df['label'], fontsize=9)
    ax.set_xlabel('-log10(p-value)', fontsize=11)
    ax.set_ylabel('')
    title = f'Enrichment analysis'
    if args.source:
        title += f' ({args.source})'
    ax.set_title(title, fontsize=13, fontweight='bold')

    cbar = fig.colorbar(sc, ax=ax, pad=0.01)
    cbar.set_label('p-value', fontsize=10)

    ax.grid(axis='x', linestyle='--', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(args.output, dpi=300, bbox_inches='tight')
    print(f"Bubble plot written to {args.output} ({len(df)} terms)")
    print("Done!")


if __name__ == '__main__':
    main()
