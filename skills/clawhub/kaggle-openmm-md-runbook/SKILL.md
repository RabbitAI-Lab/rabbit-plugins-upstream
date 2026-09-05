---
name: kaggle-openmm-md-runbook
description: Battle-tested runbook for running long (100 ns) OpenMM molecular dynamics on Kaggle's free GPU (P100 sm_60) — covers the mandatory OpenMM 8.3.1 pin, checkpoint/resume across the ~12 h session cap, Kaggle-specific pitfalls (kaggle CLI not persisted, /kaggle/input/datasets/<owner>/<slug> mount path, dataset propagation lag, --accelerator not choosing the GPU), the root-caused PBC coordinate-frame (RECELL) bug that NaN-explodes the system, ligand SDF rebuild via VF2 graph match, the B1–B5 equilibration ladder, and the agentic supervisor loop that auto-pulls mdout and relaunches. Use when planning, executing, debugging, or handing off an OpenMM MD run on Kaggle.
version: 1.0.2
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

1. **Edit `run.py` only** — Kaggle executes `code_file` from `kernel-metadata.json`; `run_md.py`
   is the supervisor's template. Keep them identical: `cp run.py run_md.py` before every push. (v47)
2. **Pin `openmm=8.3.1`** in the micromamba env. 8.6 links nvrtc 13.3, which rejects
   `--gpu-architecture=sm_60/sm_70` → P100 sessions die at import. (v38–v40)
3. **`--accelerator` does not choose the GPU.** Kaggle assigns the P100 regardless of
   `"GPU T4 x2"`. Design around the GPU you get, not the one you request.
4. **Reinstall the `kaggle` CLI every fresh sandbox** (`pip install -q kaggle`); the API key file
   persists in the workspace, the package does not.
5. **Use `/kaggle/input/datasets/<owner>/<slug>`** — the bare `/kaggle/input/<slug>` 404s.
6. **Dataset re-uploads propagate lazily.** Old mounts (and `Bad input file` errors) persist for
   minutes — poll; do not "fix" code that is actually fine.
7. **Never `setParticleParameters` on OpenMM 8.3 without a shim** — better: rebuild the
   `CustomExternalForce` per equilibration stage. (v41)
8. **Re-center the whole complex into `[0, box)³` before solvation** (the RECELL fix). CUDA wraps
   coordinates; raw PDB-frame positions give every out-of-cell restrained atom a static
   `2·k·box` force → NaN by step ~251. Apply the shift to protein, grid, ligand AND ions. (v34→v53)
9. **Restrain to MINIMIZED coordinates**, never raw input coordinates. (v50–v52)
10. **Rebuild the restraint force each stage** (`system.removeForce(prev)` first) — stacked
    restraints silently double. (v53–v54)
11. **Use `getState(..., getEnergy=True)` then `.getKineticEnergy()`/`.getPotentialEnergy()`** —
    the `getKineticEnergy=`/`getPotentialEnergy=` kwargs do not exist in 8.3. (v55)
12. **Rebuild the ligand via VF2 heavy-atom graph match + `AddHs(addCoords=True)`** — never
    `EmbedMolecule`+`AlignMol` (gave 1.56 Å RMSD and wrong H placement). Verify identity by
    InChIKey vs PubChem. 
13. **Don't chase post-min `|F|max ≈ 3,700 kJ/mol/nm`** (waters, 2,000-iter min) to zero —
    equilibration absorbs it.
14. **The OPC `O↔M 0.0159 nm` pair is not a clash** — it's the 4-site water's virtual site inside
    one residue. Clash reports must exclude same-residue (and bonded) pairs.
15. **Plan for ≥3 sessions**: 100 ns at 4 fs = 25,000,000 steps ≈ 29 h vs ~12 h session caps —
    checkpoint every 50 ps and resume. Never plan a single-session 100 ns.
16. **Run exactly ONE supervisor loop, and only when the human asked for it** — it pulls mdout,
    versions the resume dataset, and relaunches, with explicit stop conditions (done / 3 failures).
    After a sandbox reset: check status first, then restart one copy.

## Safety boundaries (read before any command)

This skill is **documentation plus a read-only static checker** — it never acts on its own:

1. **Credentials stay with the human.** The commands below use the *user's own* Kaggle account.
   An agent must never print, copy, relocate, or read the contents of the user's Kaggle
   credentials; it may only note whether the standard CLI key file exists (and keep it `chmod 600`).
2. **Remote mutations are user-directed.** `kaggle kernels push`, `kaggle datasets version/create`,
   and publishing anything are performed **only on explicit human instruction**, never autonomously.
3. **The supervisor loop is opt-in.** Start it only when the human asks for unattended operation;
   run exactly one instance; stop on `status == "done"` or after 3 consecutive failures (bounded
   operation — it is a polling monitor, not a self-replicating daemon).
4. **The only executable here is static.** `scripts/md_preflight.py` reads the two dirs you pass
   it, touches no network, no credentials, no system state. Everything else is markdown.

## Fast path (run with the user's own Kaggle credentials, on their instruction)

```bash
# 0. one-time per fresh sandbox: the CLI is ephemeral, the key file persists
#    (if the user has not placed kaggle.json, STOP and ask them — do not create keys)
pip install -q kaggle && chmod 600 ~/.kaggle/kaggle.json   # user-provided key; standard hygiene

# 1. check the remote run
kaggle kernels status <owner>/<kernel-slug>          # QUEUED/RUNNING/COMPLETE/ERROR

# 2. if it ended, pull the log + /kaggle/working/mdout
kaggle kernels output <owner>/<kernel-slug> -p /tmp/mdopoll

# 3. edit THE kernel Kaggle executes (run.py — never only run_md.py), then sync + push
cd /path/to/md_run/kernels
python3 -m py_compile run.py && cp run.py run_md.py && kaggle kernels push -p .

# 4. restart the background supervisor (dies with the sandbox; start exactly one)
cd /path/to/md_run && INTERVAL=900 KAGGLE_ACCOUNT=<owner> \
  nohup python3 md_supervisor.py loop >/dev/null 2>&1 &

# 5. before ANY push: static preflight (this skill) + local CPU dry run (kernel's MBZ_DRY)
python3 SKILL_DIR/scripts/md_preflight.py --kernel kernels/ --input input/
MBZ_DRY=1 MBZ_INP=/path/to/input python3 kernels/run_md.py --engine   # writes dry_ok.json
```

## The three fatal traps

### (a) P100 (sm_60) + the OpenMM pin
Kaggle sessions got **Tesla P100-PCIE-16GB (sm_60)**. conda OpenMM 8.6 links `cuda-nvrtc` 13.3,
which **rejects sm_60/sm_70** at JIT. OpenMM 8.3.1 (CUDA 12, `libnvrtc.so.12`) supports
sm_60/sm_75+. Pin `openmm=8.3.1` in the bootstrap and export `CUDA_ARCH` parsed from
`nvidia-smi --query-gpu=name,compute_cap` before constructing the CUDA platform
(`{"Precision": "mixed"}`). The ~90 s micromamba bootstrap runs every session — Kaggle never
persists conda envs; keep it, it's cheap.

### (b) `--accelerator` does not control the GPU
`"accelerator": "GPU T4 x2"` in `kernel-metadata.json` did not stop Kaggle from assigning a P100.
GPU type/count/memory are platform-assigned; there is no override. Accept and design for sm_60.

### (c) The RECELL PBC bug — root cause of the v34–v52 NaN explosions
OpenMM/CUDA wraps every coordinate into `[0, box)³` silently. The custom 4-site OPC solvator built
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
- `scripts/md_preflight.py` — stdlib-only static checker (15 gates G01–G15) to run before pushes.
- `scripts/selftest.sh` — proves the skill + checker are intact (`md_preflight.py --selftest`).
