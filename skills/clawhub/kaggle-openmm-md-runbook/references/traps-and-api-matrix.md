# Traps & API Matrix — Mebendazole / 1LPB MD on Kaggle GPU

Deep reference for the `kaggle-openmm-md-runbook` skill: the hard-won failure modes and API drift
you must internalize before touching `run.py`. Every item below was reproduced in v34..v56 of the
live kernel.

---

## 1. The RECELL Bug — root-caused postmortem

**Symptom sequence (in order of appearance):**
1. **NaN at step ≈251.** First NaN atom is N of NLYS B1; ~182k of ~187k particles NaN by step 278.
   Not one bad atom — systemic.
2. **`max|F|` constant over steps 50→250** (3,719,550,786.8 kJ/mol/nm in v46). A constant force
   during dynamics is a *parameter/static* problem, not an unstable contact.
3. **Restraint force = `2·k·box` on EVERY restrained Cα** (v52): 2·4184·11.9097 ≈ 99,642.2
   kJ/mol/nm. The factor is the box length, not any physical displacement.

**Forensic ladder (v44 → v52):**

| Ver | Test | What it ruled out |
|---|---|---|
| v44 | NaN forensics: first-NaN atom logging | single bad atom |
| v45 | restart from `minimized_state` (not raw) | start-frame / hot-spot |
| v46 | per-50-step TRACE → constant `max\|F\|` | thermal/integration instability |
| v48 | post-min force audit; group-1 argmax on restrained Cα with `\|F\|=2kL` | minimization residue |
| v49 | `AUDIT fc`: `idx_mismatch=0`, `ref_mismatch=0`, refs ≈ raw coords | Python-side restraint wiring |
| v50 | `MIN-DISP`: max restrained displacement P0 vs Pmin = 0.2213 nm | minimization relocation |
| v51 | slot readback of `k/ref/d`: `max(2kd)=0.0` in Python yet physical force ≈ 2kL | Python arithmetic |
| v52 | one force group per force → G5 CustomExternalForce = 2k·box on **every** restrained Cα | everything except frame mismatch |

**v52 QED.** OpenMM's CUDA platform wraps every particle coordinate into `[0, box)³` *before*
evaluating forces. The custom 4-site OPC solvator built its grid centroid-centered on the *raw*
PDB frame (x ∈ [−4.36, 3.22] nm; 2,211/4,130 protein atoms already outside `[0, 11.81]³`), and the
raw-frame positions were written straight into `Modeller.positions`. The restraint force kept
refs in the raw frame. For every out-of-cell Cα, `|x_wrapped − x_ref| = box`, producing
`2·k·box` — a static ~10⁵ kJ/mol/nm force that explodes the system inside 250 steps.

**The fix (v53 — 6 lines in `solvate_opc` + the merge step):**
```python
# in solvate_opc, after computing box / lo / hi / center:
shift  = box/2 - center                      # raw frame -> cell frame
pos    = pos + shift                         # protein xyz
center2 = box/2
grid   = grid[keep] + center2                # build grid in the [0,box) frame
lig_heavy = lig_heavy + shift                # water-avoidance tree in the same frame
# ions pick distances from center2 (not center)
return n_water, shift                        # shift reaches the merge step

# in the ligand merge step (run.py):
lig_pos.append((x/10 + shift[0], y/10 + shift[1], z/10 + shift[2]))
# and when writing positions back into Modeller:
newpos = [Vec3(p.x + shift[0], p.y + shift[1], p.z + shift[2]) for p in modeller.positions]
```

**Validation (v53–v55 logs):** `n_Pmin_outside_box` 137,036 → ~0; TRACE `max(2kd)` 99,642 → ~346;
B1–B5 energies walk −2.438e6 → −2.472e6 kJ/mol; `production ready: 187847 particles`.

---

## 2. OpenMM 8.3.1 ↔ 8.6 API drift

The kernel pins `openmm=8.3.1` because P100 (sm_60) + conda 8.6 + nvrtc 13.3 is a dead end. 8.3
has its own API quirks — **safe patterns**:

| Call | 8.3.1 | 8.6 | Safe pattern |
|---|---|---|---|
| `CustomExternalForce.getParticleParameters(i)` | returns `(idx, params)` | returns `params` | unpack defensively: `r = f.getParticleParameters(i); idx, params = (r if isinstance(r, tuple) else (i, r))` |
| `CustomExternalForce.setParticleParameters(i, ...)` | 3-arg `(i, idx, params)` | 2-arg `(i, params)` | **don't call it** — rebuild the force per equilibration stage (immune to drift) |
| `XmlSerializer.serialize(obj)` | returns `str`, no stream kwarg | accepts optional stream | `open(path, "w").write(XmlSerializer.serialize(obj))` |
| `Context.getState(getKineticEnergy=…)` | **not supported** (`TypeError: unexpected keyword`) | supported | `st = sim.context.getState(getEnergy=True); ke = st.getKineticEnergy(); pe = st.getPotentialEnergy()` |

**Design rule:** for any force whose parameters change between stages (restraints, constraints),
**rebuild the force** rather than `setParticleParameters` — it eliminates an entire class of
version-compat bugs.

---

## 3. GPU / toolchain traps

- **conda OpenMM 8.6 ↔ CUDA 13.3 ↔ P100 (sm_60) is broken.** `nvrtc: invalid value for
  --gpu-architecture` for sm_60/sm_70. Pin `openmm=8.3.1` (CUDA 12, `libnvrtc.so.12`).
- **GPU pinning.** Parse `nvidia-smi --query-gpu=name,compute_cap --format=csv,noheader` →
  `"6.0"` → `"sm_60"`, fallback `"sm_75"`. Export `CUDA_ARCH` before constructing the CUDA
  `Platform` (8.3.1 honors it).
- **`--accelerator: "GPU T4 x2"` does not control the GPU.** Kaggle still assigns a P100.
  Don't waste cycles forcing a T4.
- **Precision.** `{"Precision": "mixed"}` on CUDA → ~240 steps/s; `double` halves throughput for no
  accuracy gain here.
- **Env rebuild is unavoidable.** Kaggle sessions don't persist conda envs; the ~90 s micromamba
  bootstrap is the correct design. Do not "optimize" by assuming `/opt/conda` survives.

---

## 4. Kaggle data & operations traps

- **Mount convention.** Use `/kaggle/input/datasets/<owner>/<slug>`; the bare
  `/kaggle/input/<slug>` 404s. `find_input_dir()` should try both and walk `/kaggle/input` as
  fallback.
- **Dataset propagation lag.** After `kaggle datasets version`, old mounts (and `Bad input file`
  errors) persist for minutes. Poll; do not "fix" code that's actually fine.
- **`kaggle` CLI is not persisted** between sandbox sessions; the key file
  the user's key file is. `pip install -q kaggle`; keep the key file `chmod 600`
- **`code_file` is the file Kaggle executes.** Edit `kernels/run.py` (named in
  `kernel-metadata.json`), never only `run_md.py` (the supervisor's template). Sync with
  `cp run.py run_md.py` before every push. (Cost: v47.)
- **Public kernel + private datasets = no secrets in code.** The kernel is public; don't embed
  API keys.
- **Supervisor lifecycle.** `md_supervisor.py loop` dies with the sandbox. After every reset:
  check `kaggle kernels status`, then start **exactly one** copy. Two loops = double launches.
- **Session cap.** Hardware ≈ 9–12 h, weekly quota ≈ 30 GPU-h/account — the entire reason for
  the 50 ps checkpoint + resume design. Never plan a single-session 100 ns.
- **API backoff.** On `429 Too Many Requests`, raise `INTERVAL` (e.g. 1800). Do not hammer.

---

## 5. False-positive list (do NOT "fix" these)

- **OPC O–M 0.0159 nm "clash".** The 4-site OPC water has O and virtual site M at exactly
  0.0159 nm. Clash reports must **exclude same-residue pairs** (and bonded pairs).
- **DCD writer `dt / AKMA` and `firstStep`.** The hand-rolled `SelDCD`
  (`struct.pack("<i4c9if", 84, b"C",b"O",b"R",b"D", 0, first_step, interval, ...)`,
  `self.dt = dt_ps / 0.04888821`) is **byte-compatible** with `openmm/app/dcdfile.py`.
  An external reviewer flagged both — false positives.
- **Post-min `|F|max ≈ 3,700 kJ/mol/nm` (waters).** Normal for a 2,000-iteration steep descent on a
  ~187k-particle system; the B1–B5 ladder absorbs it. Chasing it to zero wastes GPU-hours.

---

## 6. Debugging toolkit (compact sketches)

**A. Force trace every N steps** (v46 — static vs dynamic discriminator):
```python
sim.step(50)
st = sim.context.getState(getForces=True, getPositions=True)
F = np.asarray(st.getForces(asNumpy=True).value_in_unit(kJmol_nm))
i = int(np.argmax(np.linalg.norm(F, axis=1)))
print(f"step {sim.currentStep} |F|max={np.linalg.norm(F[i]):.1f} on atom {i}")
```

**B. Per-force isolation groups** (v52 — the decisive one):
```python
for i in range(system.getNumForces()):
    system.getForce(i).setForceGroup(i)          # unique group per force
for g, name in enumerate(force_names):
    st = sim.context.getState(getForces=True, groups={g})
    F = np.asarray(st.getForces(asNumpy=True).value_in_unit(kJmol_nm))
    j = int(np.argmax(np.linalg.norm(F, axis=1)))
    print(f"G{g} {name}: max={np.linalg.norm(F[j]):.1f} atom {j}")
# a group max of exactly 2*k*L -> PBC/frame mismatch in that force
```

**C. Restraint slot readback** (v51 — Python-side sanity):
```python
P = np.asarray(sim.context.getState(getPositions=True)
               .getPositions(asNumpy=True).value_in_unit(nanometer))
for s in range(fc.getNumParticles()):
    idx, params = fc.getParticleParameters(s)
    x0, y0, z0, k = params
    d = np.linalg.norm(P[idx] - np.array([x0, y0, z0]))
    print(f"slot {s} idx={idx} d={d:.4f} max(2kd)={2*k*d:.1f}")
# max(2kd)=0 but physical force=2kL -> the kernel's frame differs (the RECELL signature)
```

**D. MIN-DISP** (v50 — rules out minimization relocation):
```python
P0 = np.asarray(modeller.positions.value_in_unit(nanometer))
Pm = np.asarray(sim.context.getState(getPositions=True)
                .getPositions(asNumpy=True).value_in_unit(nanometer))
ds = [np.linalg.norm(Pm[i] - P0[i]) for i in sel["CA"]]
print(f"MIN-DISP max={max(ds):.4f} mean={np.mean(ds):.4f}")
```

**E. Clash report with same-residue exclusion** (so OPC O–M doesn't false-positive):
```python
from scipy.spatial import cKDTree
res_of = np.array([a.residue.index for a in modeller.topology.atoms()])
pairs = cKDTree(P).query_pairs(r=0.05)
real = [(i, j) for i, j in pairs if res_of[i] != res_of[j]]
# also subtract bonded pairs; O-M 0.0159 nm is filtered by the res_of check alone
```

**F. Gold checks (healthy-run gate):** `n_Pmin_outside_box ≈ 0`,
`AUDIT fc idx_mismatch=0 ref_mismatch=0`, `AUDIT start |F|max ≲ 4000`, `G0 asserts passed`,
`system created: 1878xx particles`.

---

*If a new failure matches nothing above, suspect the frame first (RECELL signature: `2·k·box`),
then the OpenMM 8.3.1 API drift, then the dataset mount — in that order.*
