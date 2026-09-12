---
name: kaggle-openmm-md-runbook
description: OpenMM 8.3.1 molecular dynamics runbook for Kaggle free GPU (P100 sm_60): 100 ns checkpoint/resume across ~12 h sessions, fact registry (24 traps / 20 rules / 23 errors, stable IDs) + query CLI for token-efficient grounding, 22-gate static preflight checker (incl. enable_gpu + CPU fail-fast), literature-verified calibration protocol (CAL-01..12, orlistat/1LPB positive control), append-only lesson log. Use when planning, executing, debugging, calibrating, or handing off an OpenMM MD run on Kaggle.
version: 1.2.3
categories: [research, knowledge]
topics: [molecular-dynamics, openmm, kaggle, drug-discovery, computational-chemistry]
metadata:
  openclaw:
    emoji: "🧬"
    requires:
      bins: [bash, python3]
    optional:
      bins: [kaggle]
---

# 🧬 Kaggle OpenMM MD Runbook

Distilled, hard-won operating manual for running multi-day OpenMM molecular dynamics on Kaggle's
free GPU. It compresses 22 kernel versions (v34→v56) of debug history of a real 100 ns run
(mebendazole ↔ 1LPB pancreatic lipase–colipase) into the rules, traps, and exact commands another
agent needs to (a) launch the run, (b) debug it when it explodes, or (c) hand it off cleanly —
plus a static preflight checker (`scripts/md_preflight.py`) that catches the recurring footguns
before you burn GPU quota.

## Use when

- Planning or executing OpenMM MD on Kaggle free GPU (Tesla P100, sm_60).
- Resuming an MD run across Kaggle's ~12 h session cap (30 GPU-h weekly quota).
- Debugging NaN explosions, constant huge forces, or "Python-side data is perfect but the
  force kernel disagrees".
- Rebuilding a broken ligand SDF before solvation (bond/coordinate mismatch).
- Handing the run to another agent / fresh sandbox.
- Choosing OpenMM 8.3.1 vs 8.6 on a P100, or hitting 8.3↔8.6 API drift.

## Non-negotiable rules

1. **[R01] Edit `run.py` only** — Kaggle executes `code_file` from `kernel-metadata.json`; `run_md.py`
   is the supervisor's template. Keep them identical: `cp run.py run_md.py` before every push. (v47)
2. **[R02] Pin `openmm=8.3.1`** in the micromamba env. 8.6 links nvrtc 13.3, which rejects
   `--gpu-architecture=sm_60/sm_70` → P100 sessions die at import. (v38–v40)
3. **[R03] `--accelerator` does not choose the GPU.** Kaggle assigns the P100 regardless of
   `"GPU T4 x2"`. Design around the GPU you get, not the one you request.
4. **[R04] Reinstall the pinned `kaggle` CLI every fresh sandbox** (`pip install -q kaggle==2.2.4`); the API key file
   persists in the workspace, the package does not.
5. **[R05] Use `/kaggle/input/datasets/<owner>/<slug>`** — the bare `/kaggle/input/<slug>` 404s.
6. **[R06] Dataset re-uploads propagate lazily.** Old mounts (and `Bad input file` errors) persist for
   minutes — poll; do not "fix" code that is actually fine.
7. **[R07] Never `setParticleParameters` on OpenMM 8.3 without a shim** — better: rebuild the
   `CustomExternalForce` per equilibration stage. (v41)
8. **[R08] Re-center the whole complex into `[0, box)^3` before solvation** (the RECELL fix). CUDA wraps
   coordinates; raw PDB-frame positions give every out-of-cell restrained atom a static
   `2·k·box` force → NaN by step ~251. Apply the shift to protein, grid, ligand AND ions. (v34→v53)
9. **[R09] Restrain to MINIMIZED coordinates**, never raw input coordinates. (v50–v52)
10. **[R10] Rebuild the restraint force each stage** (`system.removeForce(prev)` first) — stacked
    restraints silently double. (v53–v54)
11. **[R11] Use `getState(..., getEnergy=True)` then `.getKineticEnergy()`/`.getPotentialEnergy()`** —
    the `getKineticEnergy=`/`getPotentialEnergy=` kwargs do not exist in 8.3. (v55)
12. **[R12] Rebuild the ligand via VF2 heavy-atom graph match + `AddHs(addCoords=True)`** — never
    `EmbedMolecule`+`AlignMol` (gave 1.56 Å RMSD and wrong H placement). Verify identity by
    InChIKey vs PubChem. 
13. **[R13] Don't chase post-min `|F|max ≈ 3,700 kJ/mol/nm`** (waters, 2,000-iter min) to zero —
    equilibration absorbs it.
14. **[R14] The OPC `O↔M 0.0159 nm` pair is not a clash** — it's the 4-site water's virtual site inside
    one residue. Clash reports must exclude same-residue (and bonded) pairs.
15. **[R15] Plan for ≥3 sessions**: 100 ns at 4 fs = 25,000,000 steps ≈ 29 h vs ~12 h session caps —
    checkpoint every 50 ps and resume. Never plan a single-session 100 ns.
16. **[R16] Run exactly ONE supervisor loop, and only when the human asked for it** — it pulls mdout,
    versions the resume dataset, and relaunches, with explicit stop conditions (done / 3 failures).
    After a sandbox reset: check status first, then restart one copy.
17. **[R17] `"enable_gpu": true` in kernel-metadata.json, and verify `platform CUDA` in the first
    log lines** — the kaggle CLI defaults enable_gpu to FALSE; a missing flag means a CPU-only
    session (~10–100× slower — minimize ~10×, dynamics ~100×; 0 GPU-h burned, TRAP-22).
    Contrast R03: the `accelerator` field chooses WHICH GPU you are assigned; `enable_gpu`
    decides WHETHER you get one at all. Preflight G21 checks it statically.
18. **[R18] Production kernels fail fast when CUDA is unavailable** (CPU allowed only in `MBZ_DRY`
    smoke mode) and log steps/s every checkpoint vs the ~240 steps/s P100 baseline, so a
    slow-burn CPU session is caught at the first 50 ps checkpoint (TRAP-23).
19. **[R19] Calibration-before-production** — a 5 ns positive-control run (orlistat in 1LPB,
    dt 2 fs, no HMR) must pass ALL 12 literature gates CAL-01..CAL-12
    (`registry/calibration.json`) before production runs are trusted on a new pipeline.
20. **[R20] Ledger hygiene** — every Kaggle usage-log START gets an END entry, even on cancel or
    failure, with gpu_minutes taken from `kaggle quota` (TRAP-24).

## 🧭 Grounding contract (anti-hallucination — for every consuming model)

1. Answer from this skill by **fetching facts, not recalling them**: use
   `scripts/skill_query.py` (below) and cite entry IDs in your answer (e.g. `[R08]`, `[TRAP-03]`,
   `[ERR-009]`). Every registry claim carries its evidence (kernel version/log line).
2. If a fact is NOT in the registry or docs, say **UNKNOWN** and propose how to verify —
   never invent parameters, versions, paths, forces, or log values. If a query is ambiguous,
   ask for clarification or give the candidate interpretations with their registry IDs.
3. Do not "fix" the documented false positives ([TRAP-14] O–M pair, [TRAP-15] DCD constants,
   [TRAP-16] post-min |F|max).

## 🗂 Machine-readable registry + query CLI (token-efficient grounding)

`registry/` holds the skill's facts as JSON with stable IDs: `traps.json` (TRAP-01..21),
`rules.json` (R01..R20), `errors.json` (ERR-001..023: error-text → cause → one-line fix),
`calibration.json` (CAL-01..12 literature-verified gates + citations),
`params.json` (exact simulation parameters + budget math), `lessons.jsonl` (+schema).
Query surgically instead of reading prose:

```bash
python3 scripts/skill_query.py list traps            # one line per trap (ID | title)
python3 scripts/skill_query.py trap TRAP-03          # full entry (symptom/cause/fix/evidence)
python3 scripts/skill_query.py error "nvrtc"         # error lookup -> ERR-001 + one-line fix
python3 scripts/skill_query.py param production      # exact production parameters
python3 scripts/skill_query.py essence               # ~45-line ultra-compact briefing (small-context models)
python3 scripts/skill_query.py essence --json        # same, machine-readable
```

`md_preflight.py` gained `--explain Gxx` (one-line fix per gate), `--version`, parameter
gates (G16 HMR · G17 OPC water · G18 removeCMMotion · G19 checkpoint writes ·
G20 accelerator-advisory), and — after the 2026-09-08 silent-CPU-session incident —
**G21 `enable_gpu` in kernel-metadata.json (blocker)** and **G22 CPU fail-fast guard in
run.py** — 22 gates total.

## 🔁 Self-improvement loop (safe, human-in-the-loop)

Found a NEW failure not in `errors.json`? After solving it, record the lesson — the skill
learns append-only, but cannot rewrite itself:

```bash
python3 scripts/learn.py add --symptom "..." --fix "..." --cause "..." --confidence observed --source "<model-or-human>"
python3 scripts/learn.py verify      # schema-validate the log
python3 scripts/learn.py export      # promotion-ready JSON for human review
```

* confidence starts at `hypothesis|observed`; `verified` requires `--human-approved`.
* Entries are promoted into `traps.json`/`errors.json` (with stable IDs) only by a human at
  publish time — this is how another agent benefits from your debugging.

## 🧪 Calibration protocol (positive control before production)

A short 5 ns / 2 fs (no HMR) simulation of the **orlistat–1LPB** complex must reproduce
published pancreatic-lipase MD observables before any production run is trusted on a new
pipeline (**R19**). Orlistat is the reference inhibitor (IC50 0.14–0.48 µM across verified
assays); a pipeline that cannot reproduce its literature behaviour is not ready for
production science.

| Gate | Metric | Band | Literature anchor |
|---|---|---|---|
| CAL-01 | protein RMSD plateau | 1.0–3.0 Å, drift <0.5 Å / 2 ns | V2015: 1.25–2.5 Å; Mughal 2025: 2.0–2.5 Å |
| CAL-02 | ligand RMSD (final 2 ns) | ≤5.0 Å, no ejection | V2015: 1.2–4.8 Å |
| CAL-03 | d(Ser152 Oγ–ligand) min | <6.0 Å (ejected: 8–15 Å) | V2015 lead 2.05 Å vs 8.47/15.35 Å ejected |
| CAL-04 | Ser152 H-bond occupancy | ≥0.50 | V2015: 64% |
| CAL-05 | Phe77 H-bond occupancy | ≥0.30 (His263 informative) | V2015: 77% / 30% |
| CAL-06 | triad RMSF (Ser152/Asp176/His263) | <1.0 Å | Life 2026: triad stable |
| CAL-07 | global max RMSF | <3.0 Å | V2015: <3.0 Å |
| CAL-08 | Rg σ (final 2 ns) | <0.5 Å | Life 2026: stable Rg ~1.97 nm |
| CAL-09 | PE relative drift | <0.01 | V2015: energy stable −450 kcal/mol from 8 ns |
| CAL-10 | density | 0.985–1.02 g/cm³ | NPT 1 bar / 310 K health |
| CAL-11 | mean temperature | 307–313 K | 310 K setpoint |
| CAL-12 | any protein–ligand H-bond | ≥0.50 frames | V2015: sustained network |

Why 5 ns is enough (verified): the V2015 lead complex shows consistent RMSD from 2.5 ns and
stable energy from 8 ns of a 10 ns run; its 50 ns extension held conclusions (Ser152 →98%);
catechin equilibrates in ~5 ns; Life-2026 complexes equilibrate within 20 ns; and V2015's
10 ns window already discriminates binders (orlistat keeps Phe77+Ser152) from ejected hits
(all contacts lost). Machine-readable gates + full citations: `registry/calibration.json`
(`python3 scripts/skill_query.py list calibration`).

```bash
# run it (calibration mode): TARGET_NS=5, dt 2 fs, no HMR, orlistat inputs
# -> calibration_report.json: ALL 12 PASS = pipeline VALIDATED; any FAIL = debug first
```

## Safety boundaries (read before any command)

This skill is **documentation plus a read-only static checker (`md_preflight.py` / `skill_query.py`)
and one explicitly-invoked, append-only logger (`learn.py`)** — no component acts on its own:

1. **Credentials stay with the human.** The commands below use the *user's own* Kaggle account.
   An agent must never print, copy, relocate, or read the contents of the user's Kaggle
   credentials; it may only note whether the standard CLI key file exists (and keep it `chmod 600`).
2. **Remote mutations are user-directed.** `kaggle kernels push`, `kaggle datasets version/create`,
   and publishing anything are performed **only on explicit human instruction**, never autonomously.
3. **The supervisor loop is opt-in and user-visible.** Start it only on an EXPLICIT user
   instruction to operate unattended — words like "run the supervisor", "keep it running
   overnight", "monitor and relaunch" in the user's own message. A mere mention of Kaggle,
   kernels, or MD in a task NEVER qualifies. Run exactly one instance; stop on
   `status == "done"` or after 3 consecutive failures (bounded operation — it is a polling
   monitor, not a self-replicating daemon). Prefer your platform's supervised-process
   mechanism (e.g. `start_process`/`stop_process`) over `nohup … &`; the nohup form is the
   bare-VM fallback only.
4. **All executables are local and bounded.** `scripts/md_preflight.py` is a static checker: it reads
   the two dirs you pass it — no network, no credentials, no system state. `scripts/skill_query.py`
   only reads this skill's own `registry/*.json` files. `scripts/learn.py` is an append-only logger
   that writes ONLY to this skill's own `registry/lessons.jsonl`, ONLY when a human or agent
   deliberately runs it (never edits existing lines; never invoked by any other component).
   Everything else is markdown.
5. **Account & supply-chain guarantees (with disclosure).** Every `kaggle kernels` command shown acts
   only on YOUR OWN kernel slug under your own account (push/status/output — never other users'
   resources). The workflow fetches packages from exactly two official sources: the `micro.mamba.pm`
   micromamba binary (**pinned release 1.5.10 + SHA-256-verified before extraction** — the hardened
   bootstrap in RUNBOOK.md; the historical mutable `latest` variant is retired), and the conda-forge channel
   (openmm=8.3.1 hard-pinned as safety-critical; helper packages float — locked-spec reproducibility
   instructions also in that note). No other network fetches, installers, or third-party sources exist
   anywhere in this skill.

## Fast path (run with the user's own Kaggle credentials, on their instruction)

```bash
# 0. one-time per fresh sandbox: the CLI is ephemeral, the key file persists
#    (if the user has not placed kaggle.json, STOP and ask them — do not create keys)
pip install -q kaggle==2.2.4 && chmod 600 ~/.kaggle/kaggle.json   # pinned CLI; user-provided key; standard hygiene

# 1. check the remote run
kaggle kernels status <owner>/<kernel-slug>          # QUEUED/RUNNING/COMPLETE/ERROR

# 2. if it ended, pull the log + /kaggle/working/mdout
kaggle kernels output <owner>/<kernel-slug> -p /tmp/mdopoll

# 3. edit THE kernel Kaggle executes (run.py — never only run_md.py), then sync + push
#    ⚠️ R17/TRAP-22: kernel-metadata.json MUST contain "enable_gpu": true (the CLI defaults
#    it to false -> CPU-only session, ~100x slower). Preflight G21 checks it BEFORE the push.
cd /path/to/md_run/kernels
python3 -m py_compile run.py && cp run.py run_md.py && kaggle kernels push -p .
#    after push: verify 'platform CUDA (...)' appears in the log within the first minutes —
#    a 'platform CPU' line means STOP and fix the metadata (ERR-021).

# 4. restart the background supervisor (dies with the sandbox; start exactly one)
cd /path/to/md_run && INTERVAL=900 KAGGLE_ACCOUNT=<owner> \
  nohup python3 md_supervisor.py loop >/dev/null 2>&1 &   # user-started, self-stopping; dies with the sandbox

# 5. before ANY push: static preflight (this skill) + local CPU dry run (kernel's MBZ_DRY)
python3 SKILL_DIR/scripts/md_preflight.py --kernel kernels/ --input input/
MBZ_DRY=1 MBZ_INP=/path/to/input python3 kernels/run_md.py --engine   # writes dry_ok.json
```

## The three fatal traps

### (a) P100 (sm_60) + the OpenMM pin — TRAP-01 / ERR-001
Kaggle assigns **Tesla P100-PCIE-16GB (sm_60)**. conda OpenMM 8.6 links `cuda-nvrtc` 13.3,
which **rejects sm_60/sm_70** at JIT; OpenMM 8.3.1 (CUDA 12) supports sm_60. Pin
`openmm=8.3.1`; export `CUDA_ARCH` from `nvidia-smi` before constructing the CUDA platform.
Rebuild the ~90 s micromamba env every session — Kaggle never persists it.

### (b) `--accelerator` does not control the GPU — TRAP-02
Kaggle assigns the GPU regardless of `kernel-metadata.json`'s `"accelerator"` value; there is
no override. Design for sm_60. (Simulation-side, inject an `--accelerator` advisory — see G20.)

### (c) The RECELL PBC bug — TRAP-03 / R08 — root cause of the v34–v52 NaN explosions
OpenMM/CUDA wraps every coordinate into `[0, box)^3` silently. The custom 4-site OPC solvator built
its grid **centroid-centered on the raw PDB frame** and never re-centered the complex → ~137k
particles outside the cell → every restrained Cα carried a static force of exactly `2·k·box`
(v52 measured 2·4184·11.9097 ≈ 99,642 kJ/mol/nm). Forensic signature: `max|F|` **constant**
across steps 50→250, then NaN at step ~251. Diagnosis: one `setForceGroup` per force; the
offending group's max is exactly `2·k·L`.

The 6-line fix inside `solvate_opc`:
```python
shift  = box/2 - center        # raw frame -> cell frame
pos    = pos + shift           # protein atoms
center2 = box/2
grid   = grid[keep] + center2  # build the water grid in the cell frame
lig_heavy = lig_heavy + shift  # ligand must sit in the SAME frame
return n_water, shift          # pass shift to the merge step
```
...plus apply `shift` to the ligand xyz at the merge step and when writing positions back into
`modeller.positions`. Validation: `n_Pmin_outside_box` 137,036 → ~0; B1–B5 energies walk
−2.438e6 → −2.472e6 kJ/mol (healthy, reproducible).

## Equilibration ladder

| Stage | length | dt | ensemble | restraint k (kcal/mol/Å²): Cα / ligand | barostat |
|---|---|---|---|---|---|
| B1 | 100 ps | 2 fs | NVT | 10.0 / 10.0 | – |
| B2 | 250 ps | 2 fs | NPT | 5.0 / 5.0 | 1 bar, 310 K, every 25 steps |
| B3 | 250 ps | 2 fs | NPT | 2.0 / 3.0 | same |
| B4 | 250 ps | 2 fs | NPT | 0.5 / 1.0 | same |
| B5 | 150 ps | 4 fs | NPT | 0.0 / 0.0 (restraint removed) | same |

k in kJ/mol/nm² = kcal/mol/Å² × 418.4. Per stage: fresh `Simulation`, `setState(prev_state)`
(B1 ← `minimized_state`), `sim.step(nsteps)`, `saveState(eq_<stage>.xml)`. P100 measured:
B1 ≈ 3.5 min → ≈240 steps/s at 2 fs with full diagnostics. References = minimized coords;
remove the previous stage's force before adding the new one.

## Production + checkpointing

- Integrator: `LangevinMiddleIntegrator(310 K, 1/ps, 4 fs)`, HMR (`hydrogenMass=4 amu`),
  PME 1.0 nm, `ewaldErrorTolerance=5e-4`, dispersion correction on, `removeCMMotion=False`.
- DCD: selected atoms (all protein heavy + ligand ≈ 8,130) every 2,500 steps (10 ps/frame) via a
  byte-compatible `SelDCD` writer — the `dt/AKMA` and `firstStep` constants are CORRECT;
  external reviewers flagging them were wrong (false positive).
- Checkpoint every 12,500 steps (50 ps): `state.xml` + `checkpoint.chk` + `run_state.json`
  (ns, step, T̄, PĒ, density, ns/day from a sliding 300 s window).
- Total 25,000,000 steps ≈ 29 h ≈ 2.5–3 sessions. Budget: ~0.55 GPU-h equilibration,
  ~13 min fresh boot + ~33 min B1–B5 on fresh builds only (resume skips straight to production).
- Resume: kernel detects `state.xml` + `system.xml` in the resume dataset → deserialize
  (`XmlSerializer.deserialize(open(...).read())` — string arg in 8.3) → `production_loop`.

## Debugging toolkit

- **A. Force trace every N steps** — constant `max|F|` across steps ⇒ static/parameter cause.
- **B. Per-force isolation** — unique `setForceGroup(i)` per force, then per-group
  `getState(getForces=True, groups={g})`; a group max of exactly `2·k·L` = PBC/frame mismatch.
- **C. Restraint slot readback** — Python computes `max(2kd)=0` but the physical force is
  `2·k·box` ⇒ the kernel sees different coordinates (the RECELL signature).
- **D. MIN-DISP** — tiny P0-vs-Pmin displacements rule out minimization relocation.
- **E. Clash report** — `cKDTree.query_pairs(0.05 nm)` minus bonded AND same-residue pairs.
- **F. Gold checks** — `n_Pmin_outside_box ≈ 0`, `AUDIT fc idx_mismatch=0`, start `|F|max ≲ 4000`,
  `G0 asserts passed`, `n_particles ≈ 187,8xx`.
- **G. Local CPU dry-run** — `MBZ_DRY=1` builds + minimizes + 100 steps; cheap pre-flight.

## OpenMM 8.3.1 vs 8.6 API matrix

| Call | 8.3.1 | 8.6 |
|---|---|---|
| `CustomExternalForce.getParticleParameters(i)` | `(particle_index, params)` | bare `params` |
| `CustomExternalForce.setParticleParameters(i, idx, params)` | 3-arg | 2-arg |
| `XmlSerializer.serialize(obj, stream?)` | returns `str`, no stream arg | accepts stream |
| `Context.getState(getKineticEnergy=/getPotentialEnergy=)` | **not supported** → `getEnergy=True` + `.getKineticEnergy()` | supported |

## Env vars honored by the kernel

| var | default | meaning |
|---|---|---|
| `TARGET_NS` | 100 | production target |
| `MBZ_PAD` | 1.2 | solvation padding (nm) |
| `MBZ_SALT` | 0.15 | NaCl molarity |
| `MBZ_MINITER` | 2000 | minimizer iterations |
| `MBZ_WORK` | /kaggle/working/mdout | output dir |
| `MBZ_INP` / `MBZ_RES` | auto | override input / resume dirs |
| `MBZ_DRY` | '' | =1 → local CPU smoke: minimize, clash report, 100 steps, `dry_ok.json` |
| `MBZ_DRY_FORCE` | '' | =1 → dump top-12 force atoms + contacts (DRY mode) |
| `MBZ_DRY_STEPS` | 100 | DRY step count |

## Included in this skill

- `RUNBOOK.md` — the complete original field manual (v34→v56 chronology, every command, every log
  line, ops appendices). Start there for the full story.
- `references/traps-and-api-matrix.md` — RECELL postmortem, full 8.3.1↔8.6 drift table, GPU/Kaggle
  traps, false-positive list, toolkit code sketches.
- `references/operations.md` — session budget math, supervisor-loop pattern, push/status/output
  and dataset commands.
- `registry/calibration.json` — the 12 literature-verified calibration gates (CAL-01..12) with
  per-gate sources, the verified citation table (L1–L7), the short-run validity argument, and
  the corrections log from the 2026-09-09 verification pass.
- `scripts/md_preflight.py` — stdlib-only static checker (22 gates G01–G22) to run before pushes.
- `scripts/selftest.sh` — proves the skill + checker are intact (`md_preflight.py --selftest`).
