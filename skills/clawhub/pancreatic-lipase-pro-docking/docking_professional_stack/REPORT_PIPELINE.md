# Report Pipeline (v100.2.0)

End-to-end workflow added in v100.2.0, distilled from a full 338-molecule x 5-site
virtual screen (2026-08-03) that produced an executive report with parallel
multi-provider AI analysis.

## Pipeline
```
molecule names (txt)          -> resolve_names.py   -> molecules_resolved.csv (SMILES via PubChem)
molecules_resolved.csv        -> multi_site_docking.py -> dock_results/results_all_sites.csv
                                (5 sites, checkpointed, parallel, memory-guarded)
results_all_sites.csv         -> redock_high.py     -> dock_results_ex16/ + comparison CSV
results (+ optional analysis) -> build_report.py    -> REPORT.md
```
Or run everything: `bash run_pipeline.sh molecules.txt --redock 10 --workers 2`

## The 5 positions (auto-detected from the receptor structure)
| Site | Detection |
|---|---|
| catalytic_triad | Ser(OG) + Asp(OD1,OD2) + His(ND1,NE2) clustered ≤15 Å |
| oxyanion_hole | backbone amides at catalytic-Ser+1 and +26 |
| lid | sequence window +87..+107 after catalytic Ser |
| hydrophobic_pocket | hydrophobic residues ≤8 Å of Ser-OG |
| colipase_cterm | last 45 residues of the catalytic chain |

Detection is by atom composition (not motif text) — robust to PDB numbering
offsets (1LPB uses PDB numbering shifted −2 vs UniProt P16233).

## AI multi-provider analysis (optional, no keys in the skill)
The skill never embeds credentials. To reproduce the 4-provider distribution:
split molecules_resolved.csv into N shards, send one shard per provider
(router/orchestrator of your choice, ~6000 tokens), save each reply to
`analysis/<provider>.md`, then run:
`python3 build_report.py --results dock_results/results_all_sites.csv --analysis-dir analysis`

## Debug log (2026-08-03 session)
- vina 1.2.x removed `--log` -> capture stdout as vina.log (fixed in v100.1.4)
- PEP-701 nested f-string broke dashboard on Python ≤3.11 (fixed in v100.1.4)
- PubChem batch POST 404s; per-name GET works; JSON key is `ConnectivitySMILES`
- unicode names (β, ′) need ASCII-ification before PubChem lookup
- catalytic residue identification by motif GHSLG was off-by-one vs PDB numbering;
  atom-composition detection is definitive
- ligand PDBQT prep was repeated 5x (once per site) -> shared cache: 2x speedup
- parallel vina on a 2 GB box: 2 workers x --cpu 1, sequential ligand prep
- 32-rotatable-bond ligands (orlistat) OOM vina at any exhaustiveness ->
  --max-rotb 20 default guard; covalent inhibitors are outside rigid-docking scope
- shallow screen (ex=2) reliably ranks strong binders; ex=16 deepens poses
  (mean Δ −0.40 kcal/mol over 50 pairs) and fixes false positives
