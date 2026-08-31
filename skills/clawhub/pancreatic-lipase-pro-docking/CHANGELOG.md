# Changelog

## v100.4.1 (2026-08-25) — payload packaging fix

The v100.4.0 payload zip was written WITHOUT the `docking_professional_stack/`
path prefix, so restore_and_run.sh extracted files flat instead of into the
stack directory (its fail-closed check caught this correctly and refused to
run — no silent corruption). v100.4.1 rebuilds the payload with prefixed
entries (62 files, verified extractable). No code changes.

## v100.4.0 (2026-08-25) — MAXIMUM-PRECISION SCIENCE LAYER (multi-model audited)

Deep debug of the whole stack (my own review + parallel AI code audits on
mistral-large-latest / gemini-3.1-flash-lite; every accepted finding fixed,
hallucinated findings rejected with evidence). 41/41 tests, real-docking
validated.

### Fixed — receptor fidelity (largest systematic error)
- 1LPB is a COMPLEX: chain B lipase + chain A colipase + one Ca2+ (HETATM).
  The old cleaner kept only the largest chain: it DELETED colipase and Ca2+
  while advertising a "colipase interface" site. New `--receptor-model
  complex` (default) keeps lipase+colipase+Ca2+ (Ca2+ verified present, typed
  +2, in the production PDBQT); `apo` preserves legacy behavior.
- Oxyanion hole was "+1 and +26 residues after Ser in sequence index" — wrong.
  Now geometric: backbone N within 6 A of Ser152-OG, triad+-2 excluded ->
  Phe77 (5.4 A) + Leu153 (3.3 A), the canonical hPL oxyanion hole, verified
  on the shipped coordinates.
- Colipase interface was the lipase's own C-terminus. Now real <=5 A
  cross-chain contacts (41 residues, chains B|A).
- Catalytic triad Asp geometry now min(OD1,OD2)...His-ND1; catalytic center
  anchored on Ser-OG (0.4 A) instead of a residue-cloud centroid.

### Fixed — ligand chemistry (new chemprep.py)
- pH 7.4 major-microstate protonation (10-case unit-tested): carboxylates -1,
  thiophenolates -1, alkyl phosphonates -2, phosphate esters -1, aliphatic
  amines/guanidines/amidines +1 (biguanide single-cation guard), amides and
  phenols neutral. Old pipeline docked the input SMILES state (fatty-acid
  substrates as neutral acids — wrong by a full ionization state).
- Canonical tautomer (RDKit), undefined-stereocenter enumeration (<=2 centers,
  <=4 isomers; winning isomer reported), ETKDG multi-conformer + MMFF
  lowest-energy start with per-ligand deterministic seed.

### Fixed — bias and validation
- Precision tiers: fast=(ex4,1 seed) / balanced=(ex8,1) / max=(ex24,3 seeds);
  replicate seeds seed+k*7919 (was: single fixed seed 42 everywhere).
- Full Vina mode-table parsing (was: first line matching "1"); NaN/inf guards;
  per-(ligand,site) mean/sd + unstable(sd>0.5) flags; per-variant attribution.
- NEW validate_native.py: re-docking validation gate — co-crystallized MUP
  (altloc A, occupancy 0.67 vs B 0.40), ligand-centered box (canonical
  protocol), obabel ligand prep (meeko/RDKit proximity-bond path mangles
  phosphinates), element-aware Kabsch RMSD, multi-model pose parsing.
  Current: 15/15 atoms, 2.39 A top pose / 2.15 A best-of-modes (WARN band —
  honest; typical for an 11-carbon flexible phosphinate with Vina).
- Aggregate CSV keeps the legacy schema + new consensus columns; checkpoint
  key now (name, site, variant, seed).

### Fixed — code defects (from AI audits + review)
- Lambda in ProcessPoolExecutor (unpicklable — crashed every --workers>1 run);
  sorted(dict) vs items(); altloc B/C atoms in legacy parsers; CSV DictWriter
  restval; collision-safe ligand names; NaN-safe ranking; configurable score
  envelope; /home/user/out/plenv PATH only when present; native-ligand
  double-altloc extraction; digit-H filtering.

### Verified
- 41/41 pytest (24 legacy + 17 new science tests), ~5 s, no docking needed.
- Real anchors reproduce historical calibration through all fixes: ibuprofen
  -7.39..-7.46 (hist. -7.29), caffeine -6.70..-6.81 (hist. -6.78).
- validate_results PASS on all outputs; MUP gate WARN (2.39 A).



## v100.3.10 (2026-08-25) — token-optimization release

SKILL.md input tokens cut 32% (1,494 -> 1,019, o200k_base) with zero behavioral
change — verified by independent multi-model semantic-diff audits; every finding
restored (exception types, --check semantics, Ser152-Asp176-His263 anchors,
vina-log capture, py<=3.11 note, tests path-independence).

### Changed
- Version-history sections (v100.1.4-v100.3.4 narratives, per-file pyflakes
  cleanup lists) removed; behavioral facts kept inline. Registry version list
  retains the history.
- Documented the restore step FIRST: run_pipeline.sh & friends exist only after
  `restore_and_run.sh` unpacks payload_universal_upload.txt ->
  docking_professional_stack/ (flags documented from the script itself).
- Metadata: version aligned with registry (was stale 100.3.4; registry 100.3.9);
  invalid categories (education/science/chemistry) -> [research]; 10 tags ->
  5 valid topics.
- README "Complete Skill Reference" synced to the current SKILL.md.

### Added
- Model-routing note: Vina scoring is deterministic (zero LLM tokens); report
  prose -> cheap model; LLMs never produce or fix scores.
