# v101.0.5 — NO SILENT ENVIRONMENT CHANGES (2026-09-06)

Closes the audit's last behavioural finding: *"some helper paths can
persistently install or upgrade software in your user account despite the main
instructions saying they will not."* That was accurate.

- **`arena_auto_run.py` no longer auto-installs.** Reached via
  `restore_and_run.sh`, it ran `pip install --user --upgrade` over 8 packages
  (rdkit, meeko, vina, gemmi, pandas, numpy, scipy, scikit-learn) whenever a
  dependency was missing — mutating account-wide site-packages and potentially
  upgrading unrelated installs, with no prompt. It now prints the missing
  dependencies, recommends the isolated `micromamba -p plenv` route, and exits.
  The old behaviour requires an explicit `HPL_ALLOW_PIP_BOOTSTRAP=1`.
- **Optional installers disclosed** in the SKILL.md capability table, including
  that `setup_mamba.sh` writes micromamba into `$HOME/micromamba`.

# v101.0.4 — PAYLOAD INTEGRITY (2026-09-06)

Closes the audit's "unauthenticated self-extracting code path" finding.

- **`restore_and_run.sh` now verifies the payload before extracting it.** It
  previously printed the sha256 and extracted regardless. The expected digest
  ships in `EXPECTED_SHA256`; a mismatch aborts with a clear message and writes
  nothing. Verified both ways: valid payload extracts 66 files, a tampered
  digest refuses and leaves no directory behind.
- **Zip-slip guard.** Members with absolute paths or `..` components are
  rejected before anything touches disk.
- **Environment disclosure sharpened** in SKILL.md: `plenv/` is ~2 GB and
  persists, conda-forge packages are not hash-pinned, and the Kaggle kernel
  downloads its toolchain at run time.

# v101.0.3 — COMMAND-INJECTION FIX (2026-09-06)

Closes the last finding from the ClawHub security audit: *"a Kaggle
command-injection risk that users should review before installing."* The risk
was real and is reproduced in the test suite.

- **The Kaggle kernel no longer builds its docking command through a shell.**
  `--extra` was interpolated into an f-string passed to `subprocess.run(...,
  shell=True)`, so `--extra "; rm -rf / #"` would have executed inside the
  kernel. The command is now an argument list run with `shell=False`, which
  makes shell metacharacters inert.
- **`--extra` is allow-listed at the CLI boundary** (second layer):
  `parse_extra_flags()` tokenises with `shlex`, accepts only known
  `multi_site_docking.py` flags, and rejects `;`, `|`, `&`, backticks, `$`,
  redirects and newlines in values. Rejection is loud (exit 2), never silent.
- **9 new regression tests** covering six injection payloads, five legitimate
  flag strings, and an assertion that `EXTRA_FLAGS` is never interpolated into
  a shell string. Suite: **60 -> 72**.
- **Environment disclosure sharpened** in SKILL.md: the `plenv/` prefix is ~2 GB
  and persists, conda-forge packages are not hash-pinned, and the Kaggle kernel
  downloads its toolchain at run time.

Re-verified end-to-end on a live Kaggle kernel after hardening: 103 s, exit 0,
10 result rows, `--extra "--seed 7"` accepted, output cleanup working
(38 files fetched instead of 102). Kaggle vs local agreement: max delta
0.120 kcal/mol, well inside Vina's 0.5 band.

# v101.0.2 — SCANNER HARDENING (2026-09-06)

- **Removed dynamic code execution from the test suite.** `tests/test_v101.py`
  loaded helper scripts with `spec_from_file_location` + `exec_module`, which a
  static scanner cannot distinguish from arbitrary code execution
  (`suspicious.dynamic_code_execution`). Replaced with a plain
  `sys.path` + `importlib.import_module`. Same 60 tests, same behaviour.
- **skill-card.md refreshed** (was still describing v100.4.1 as purely local).
  Now declares the Kaggle upload path, the PubChem lookup, that scoring never
  involves an LLM, and that writes stay inside the working directory.

# v101.0.1 — SECURITY-AUDIT RESPONSE (2026-09-06)

Addresses findings from the ClawHub/NVIDIA SkillSpector audit of the previous
release. No functional change to docking.

- **Capability disclosure added to SKILL.md.** The audit's central complaint was
  that a self-extracting archive installs packages and runs code "without clear
  top-level disclosure". SKILL.md now carries a table stating exactly what is
  extracted, what is installed and where, which binaries execute, and every
  network destination — including that `kaggle_dock.py` **uploads your ligand
  CSV** to your Kaggle account, and that everything else is local with no LLM
  calls.
- **Scope creep removed.** `executive_dashboard_demo.html` (a 14 KB demo
  artifact) and `run_uploaded_molecules.sh` (a generic upload launcher) were
  flagged as capabilities beyond the manifest. Both deleted.
  `generate_executive_dashboard.py` is kept — it backs the documented
  `--executive-dashboard` flag — and is now covered by the disclosure table.
- **Description/behaviour mismatch fixed.** The old README claimed it reproduced
  SKILL.md "verbatim" while the bundle documented an undisclosed AI provider
  hook. The rewritten README makes no such claim and the network boundary is
  stated explicitly.

# v101.0.0 — RELIABILITY + CLOUD LAYER (2026-09-06)

Every fix below was found by execution or by adversarial model review and then
verified by running the code. Nothing in this entry is aspirational.

## Bugs fixed (all reproduced before the fix, re-tested after)

1. **Test suite hard-failed without RDKit.** `bash run_tests.sh` on a clean box
   produced **12 errors**, which reads as "this skill is broken" — the failures
   were only missing chemistry deps. `test_v1004.py` had a `requires_1lpb`
   guard but no `requires_rdkit` guard.
   → now **29 passed / 12 skipped** bare, **41 passed** with RDKit.

2. **`time_s` was always empty in `results_all_sites.csv`.** Per-job wall times
   were collected into `runs_detail.csv` and then dropped by the aggregator,
   which wrote a literal `""`. Every downstream consumer (report, dashboard,
   cost estimates) saw a blank column.
   → replicate times are summed per (ligand, site) and written.

3. **Kaggle status never resolved (v101 cloud layer).** The SDK returns the enum
   `KernelWorkerStatus.COMPLETE`, whose `str()` is `"KernelWorkerStatus.COMPLETE"`,
   so `status.lower() == "complete"` was False. A *finished* kernel was reported
   as `running: true` and `run` polled until timeout.
   → `_normalize_status()` takes the token after the last dot. Regression-tested
   against both the dict and enum shapes.

4. **Kaggle slug/id mismatch.** Kaggle derives the kernel slug from the **title**,
   not the `id` in `kernel-metadata.json`. Pushing `id=…/hpl-dock-verify-v101`
   with `title="hPL docking verify v101"` created `…/hpl-docking-verify-v101`;
   polling the requested id then returned `Permission 'kernels.get' was denied`
   — a *permission* message for what is really a slug bug.
   → the runner derives the slug from the title so the two always agree, and
   `references/kaggle.md` documents the trap.

5. **`fetch` downloaded the entire stack** (102 files) alongside the results,
   because the kernel left the unpacked stack in `/kaggle/working`.
   → kernel now cleans the env, the stack and `__pycache__` before exiting.

6. **Credential precedence contradicted its own docstring** (`--creds` is checked
   before `~/.kaggle/kaggle.json`, docs claimed the reverse).
   → docstring corrected to match the code; explicit input beats ambient files.

7. **`selfcheck` env fingerprint reported `vina: unavailable`** on a working
   stack, because it searched `PATH` rather than the interpreter's own env —
   defeating the purpose of recording the fingerprint.
   → resolves `vina` next to `--python` first; now records `AutoDock Vina f458505-mod`.

## New features

- **`scripts/kaggle_dock.py`** — run the full 5-site pipeline on free Kaggle CPU
  kernels. `check | push | status | fetch | run`. The stack and ligands are
  embedded in the kernel as base64, so no dataset or GitHub access is needed.
  Stable exit codes (0/2/3/4/5/6) and a single JSON line on stdout per command.
  **Verified end-to-end against the live API**: 2 ligands × 5 sites in ~116 s,
  10 result rows, scores matching local runs within Vina's noise band
  (ibuprofen −7.39 on Kaggle vs −7.35…−7.45 locally).
- **`scripts/selfcheck.py`** — the self-improvement layer. Docks a fixed
  reference pair, compares against `calibration/baseline.json`, appends every
  run to `calibration/history.jsonl`, and **exits 1 on drift > 0.5 kcal/mol**
  (Vina's own reproducibility band). Records a full env fingerprint so a future
  drift can be explained rather than guessed at. Verified in both directions:
  clean run exits 0; a tampered baseline is caught with Δ 2.715.
- **`tests/test_v101.py`** — 19 regression tests covering every defect above.
  Suite total **41 → 60**. Mutation-tested: reverting fix #3 makes 3 tests fail.

## Token efficiency (progressive disclosure)

SKILL.md was a single flat document. It is now a router: the body carries the
decision table, the run commands, the anti-hallucination rules and the
calibration anchors; everything else moved into `references/` and loads only
when the agent needs it.

- SKILL.md body: **~1440 → ~1150 tokens**, while *adding* Kaggle, drift
  detection and honesty rules.
- Deep material (`kaggle.md`, `debugging.md`, `reference.md`, `workflows.md`)
  costs **zero tokens** until read.

## Anti-hallucination

- **Rule 0** at the top of SKILL.md: report only scores present in a generated
  CSV; if a tool did not run, say so.
- `references/reference.md` documents the **complete** CLI surface, read from
  the argument parsers, so an agent never has to guess a flag.
- Explicit gates: `validate_native.py` >3 Å is now a stated **FAIL/stop**, not
  an unspecified case; `selfcheck.py` exit 1 blocks publication.
- Explicit statistics guidance: differences below ~0.5 kcal/mol are noise, and
  `unstable(sd>0.5)` rows must not be ranked.
- Stated limitation: Vina does not model covalent chemistry at the Ser152
  nucleophile.

## Compatibility

- Skill layout follows the Agent Skills open standard (`SKILL.md` + `scripts/`
  + `references/`), so it loads on any conforming runtime, not just one vendor.
- Frontmatter is spec-legal: name ≤64 chars, description ≤1024 (465), body
  under 500 lines — asserted by `test_skill_md_frontmatter_limits`.
- Description now states **when** to use the skill (trigger terms: pancreatic
  lipase, PNLIP, hPL, anti-obesity screening) so smaller models route to it.
- Tools emit one machine-readable JSON line and stable exit codes, so weaker
  models can act on results without parsing prose.
- Python ≤3.11 pinned (meeko/vina are not 3.12-clean); tests degrade to skips
  rather than errors when optional deps are absent.


---

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
