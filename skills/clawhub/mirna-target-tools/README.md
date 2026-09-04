# mirna-target-tools

A streamlined bioinformatics toolkit for **miRNA target prediction, functional annotation, conservation analysis, and regulatory network construction** — from raw miRNA sequences to a Cytoscape-ready network in one pipeline.

## What it does

- **Target prediction** — run TargetScan and miRanda to predict miRNA target genes
- **Result merging** — intersect multiple predictors to obtain high-confidence targets
- **Target annotation & enrichment** — annotate genes (symbol → Entrez/Ensembl ID + description) and run GO (BP/CC/MF) + KEGG enrichment via g:Profiler
- **Conservation analysis** — extract multi-species homologous miRNA sequences from miRBase (or supply your own FASTA), align them with free-end-gap global alignment, and quantify per-position conservation (Shannon bits + identity) with seed-region highlighting and publication-ready sequence logo + alignment plots
- **Enrichment plots** — publication-style bubble plots (300 dpi)
- **Network visualization** — generate Cytoscape-ready `.sif` network files

## Species support

Human, mouse, rat, **sheep (Ovis aries)**, **goat (Capra hircus)**, cow.

## Quick start

```bash
# 1. Check environment
python3 scripts/check_env.py

# 2. Predict targets
python3 scripts/targetscan_predict.py --input mirna_list.txt --output targetscan.txt
python3 scripts/miranda_predict.py --mirna mirna.fa --mrna 3utr.fa --output miranda.txt

# 3. Merge (intersection = high confidence)
python3 scripts/merge_targets.py --targetscan targetscan.txt --miranda miranda.txt --output merged.txt

# 4. Annotate + enrich target genes
python3 scripts/annotate_targets.py --input merged.txt --gene-col TargetGene \
    --species goat --output-dir results/annotation

# 5. Plot enrichment
python3 scripts/plot_enrichment.py --input results/annotation/merged_enrichment_all.tsv \
    --output enrichment_bubble.png

# 6. Build Cytoscape network
python3 scripts/format_cytoscape.py --input merged.txt --output network.sif

# 7. Conservation analysis (multi-species homologous miRNAs)
python3 scripts/conservation_analysis.py --mirna miR-504-5p \
    --reference-species chi --outdir results/conservation --prefix miR-504
```

## Conservation analysis (detail)

Two input modes, one pipeline:

```bash
# Mode 1 — auto-extract homologs from miRBase (exact miRBase-ID match, no miR-5046 false hits)
python3 scripts/conservation_analysis.py --mirna miR-504-5p \
    --reference-species chi --outdir results/conservation --prefix miR-504

# Mode 2 — supply your own multi-species FASTA
python3 scripts/conservation_analysis.py --input-fa homologs.fa \
    --reference-species chi --outdir results/conservation --prefix miR-504

# Optional: species whitelist + custom seed region
python3 scripts/conservation_analysis.py --mirna miR-504-5p \
    --species hsa,chi,bta,mmu,oar --seed-start 2 --seed-end 8
```

Key options:

| Option | Description | Default |
|--------|-------------|---------|
| `--mirna` | Target miRNA ID (e.g. `miR-504-5p`), auto-extract homologs from miRBase | — |
| `--input-fa` | User-provided multi-sequence FASTA (alternative to `--mirna`) | — |
| `--mature-fa` | Local `mature.fa` path (otherwise downloaded & cached to `~/.cache/mirna-target-tools/`) | auto-download |
| `--reference-species` | Alignment anchor species prefix (e.g. `chi`, `hsa`) | first sequence |
| `--species` | Comma-separated species whitelist (e.g. `hsa,chi,bta`) | all |
| `--seed-start` / `--seed-end` | Seed region nt range (highlighted + separately scored) | `2` / `8` |
| `--no-plot` | Skip plots, output TSV only | off |

Outputs (all prefixed with `--prefix`):

- `{prefix}_aligned.fa` — multiple sequence alignment (with gaps)
- `{prefix}_conservation.tsv` — per-position conservation (identity %, Shannon bits, base counts, coverage)
- `{prefix}_summary.tsv` — seed/core-region stats, mean pairwise identity
- `{prefix}_sequence_logo.png/.svg` — information-content sequence logo (WebLogo colors)
- `{prefix}_alignment.png/.svg` — MSA figure (300 dpi)

> Alignment uses free-end-gap global alignment (Needleman–Wunsch variant, pure stdlib): gaps concentrate at the 5'/3' termini (isomiR variation) while the seed region stays strictly aligned.

## Dependencies

- **Required:** `pandas`, `numpy`
- **Optional:** `mygene` (gene annotation), `matplotlib` (conservation & enrichment plots)

> Conservation analysis core (FASTA/MSA/conservation scoring) is pure standard library — zero third-party deps; it downloads miRBase `mature.fa` on first run (cached) or accepts a local file via `--mature-fa`. Enrichment (GO/KEGG via g:Profiler REST API) is also stdlib-only; `mygene` is only needed for gene-symbol annotation.

See `references/workflow.md` for the full walkthrough.

## Author

**DestinQu**

## License

MIT
