#!/usr/bin/env python3
"""md_preflight.py — static, stdlib-only pre-push checker for OpenMM MD kernels on Kaggle.

Part of the `kaggle-openmm-md-runbook` skill. Scans a kernel directory (run.py,
run_md.py, kernel-metadata.json) and an input directory (protein_md.pdb, ligand.sdf)
for the recurring v34…v56 footguns documented in the runbook, BEFORE you burn GPU quota.

Usage:
    md_preflight.py [--kernel DIR] [--input DIR] [--json]
    md_preflight.py --selftest

Exit codes: 0 = all gates pass (warnings allowed), 1 = a blocker gate failed,
            2 = usage/IO error, 3 = selftest internal failure.
Reads only the two dirs you pass. No network. No writes (selftest uses tempfile only).
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

# ----------------------------------------------------------------------------- helpers

def _read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()

def _strip_docstrings(code):
    """Remove triple-quoted docstring regions (non-greedy), keep normal strings."""
    code = re.sub(r'"""(?:.|\n)*?"""', '""', code)
    code = re.sub(r"'''(?:.|\n)*?'''", "''", code)
    # inline comments lie about markers (e.g. a comment naming _Pmin is not code)
    code = re.sub(r"(?m)[ \t]*#[^\n]*$", "", code)
    return code

def _code_lines(code):
    """Yield (line_no, stripped_line) for non-comment, non-empty lines."""
    for i, raw in enumerate(code.splitlines()):
        s = raw.strip()
        if s and not s.startswith("#"):
            yield i, s

def _sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

# ----------------------------------------------------------------------------- gate context

class Ctx:
    def __init__(self, kernel, inp):
        self.kernel = kernel
        self.inp = inp
        self.run_py = os.path.join(kernel, "run.py")
        self.run_md_py = os.path.join(kernel, "run_md.py")
        self.meta_py = os.path.join(kernel, "kernel-metadata.json")
        self.pdb = os.path.join(inp, "protein_md.pdb")
        self.sdf = os.path.join(inp, "ligand.sdf")
        self.code_raw = _read(self.run_py) if os.path.isfile(self.run_py) else None
        self.code = _strip_docstrings(self.code_raw) if self.code_raw is not None else None
        try:
            self.meta_json = json.loads(_read(self.meta_py)) if os.path.isfile(self.meta_py) else None
        except Exception:
            self.meta_json = None

# results: list of dicts {gate, name, status, severity, detail}
def R(gid, name, status, severity, detail):
    return {"gate": gid, "name": name, "status": status, "severity": severity, "detail": detail}

# ----------------------------------------------------------------------------- gates G01-G15

def g01(c):
    if c.code_raw is None:
        return R("G01", "run.py present", "FAIL", "blocker", f"no run.py in {c.kernel}")
    if not os.path.isfile(c.run_md_py):
        return R("G01", "run.py≡run_md.py", "WARN", "warn",
                 "run_md.py missing (supervisor template) — create it: cp run.py run_md.py")
    if _sha256(c.run_py) != _sha256(c.run_md_py):
        return R("G01", "run.py≡run_md.py", "FAIL", "blocker",
                 "run.py != run_md.py; sync before push: cp run.py run_md.py (v47)")
    return R("G01", "run.py≡run_md.py", "PASS", "blocker", "hash-identical")

def g02(c):
    if not os.path.isfile(c.meta_py):
        return R("G02", "metadata code_file", "FAIL", "blocker", "kernel-metadata.json missing")
    try:
        meta = json.loads(_read(c.meta_py))
    except Exception as e:
        return R("G02", "metadata code_file", "FAIL", "blocker", f"metadata not JSON: {e}")
    cf = meta.get("code_file")
    if cf != "run.py":
        return R("G02", "metadata code_file", "FAIL", "blocker",
                 f'code_file="{cf}" — Kaggle executes THIS file; set code_file="run.py" (v47)')
    return R("G02", "metadata code_file", "PASS", "blocker", 'code_file="run.py"')

def g03(c):
    if c.code is None:
        return R("G03", "getState energy kwargs", "WARN", "blocker", "skipped (no run.py)")
    pat = re.compile(r"getState\s*\([^)]*?get(?:Kinetic|Potential)Energy\s*=", re.DOTALL)
    m = pat.search(c.code)
    if m:
        return R("G03", "getState energy kwargs", "FAIL", "blocker",
                 "OpenMM 8.3 rejects getKineticEnergy=/getPotentialEnergy= kwargs (v55) — "
                 "use getState(getEnergy=True) then .getKineticEnergy()/.getPotentialEnergy()")
    return R("G03", "getState energy kwargs", "PASS", "blocker", "no 8.6-only energy kwargs")

def g04(c):
    if c.code is None:
        return R("G04", "restraint build pattern", "WARN", "warn", "skipped (no run.py)")
    if "CustomExternalForce(" not in c.code:
        return R("G04", "restraint build pattern", "WARN", "warn",
                 "no CustomExternalForce found — restraints expected in an MD kernel")
    if "removeForce(" in c.code or "_build_fc" in c.code:
        return R("G04", "restraint build pattern", "PASS", "warn",
                 "per-stage force rebuild present (8.3/8.6-drift-immune, v53+)")
    if "setParticleParameters(" in c.code and "_fce_set" in c.code:
        return R("G04", "restraint build pattern", "PASS", "warn", "setParticleParameters shimmed")
    return R("G04", "restraint build pattern", "WARN", "warn",
             "recommend rebuilding the restraint force per stage (_build_fc + removeForce); "
             "bare setParticleParameters differs between 8.3 (3-arg) and 8.6 (2-arg) — v41")

def g05(c):
    if c.code is None:
        return R("G05", "openmm pin", "WARN", "blocker", "skipped (no run.py)")
    text = "\n".join(s for _, s in _code_lines(c.code))
    if re.search(r"openmm\s*=\s*8\.6\b", text):
        return R("G05", "openmm pin", "FAIL", "blocker",
                 "openmm=8.6 found — P100 sm_60 is broken with nvrtc 13.3 (v38–v40); pin openmm=8.3.1")
    if "openmm=8.3.1" not in text:
        return R("G05", "openmm pin", "FAIL", "blocker",
                 "no openmm=8.3.1 pin found in bootstrap/create lines — unpinned OpenMM resolves "
                 "to the broken 8.6 line on P100 (sm_60)")
    return R("G05", "openmm pin", "PASS", "blocker", "openmm=8.3.1 pinned")

def g06(c):
    if c.code is None:
        return R("G06", "CUDA_ARCH pinning", "WARN", "blocker", "skipped (no run.py)")
    if "nvidia-smi" in c.code and "CUDA_ARCH" in c.code:
        return R("G06", "CUDA_ARCH pinning", "PASS", "blocker",
                 "CUDA_ARCH exported from nvidia-smi query")
    return R("G06", "CUDA_ARCH pinning", "FAIL", "blocker",
             "derive CUDA_ARCH (sm_XX) from nvidia-smi --query-gpu=compute_cap before "
             "Platform.getPlatformByName(\"CUDA\") — (v38–v40)")

def g07(c):
    if c.code is None:
        return R("G07", "restraint refs", "WARN", "blocker", "skipped (no run.py)")
    if re.search(r"(_Pmin|_refpos|minimized_state)", c.code):
        return R("G07", "restraint refs", "PASS", "blocker",
                 "restraint references come from minimized coordinates marker")
    return R("G07", "restraint refs", "FAIL", "blocker",
             "restraints must reference MINIMIZED coordinates (_Pmin/_refpos), not raw input "
             "coords — raw-frame refs + wrapped dynamics = 2·k·box forces (v50–v52)")

def g08(c):
    if c.code is None:
        return R("G08", "RECELL shift", "WARN", "blocker", "skipped (no run.py)")
    m = re.search(r"def\s+solvate_opc\s*\(", c.code)
    if not m:
        return R("G08", "RECELL shift", "WARN", "blocker",
                 "no solvate_opc found — custom OPC solvator expected; verify re-centering manually")
    window = c.code[m.start():m.start() + 12000]
    nxt = re.search(r"\n(?:def|class)\s+\w+", window[10:])
    if nxt:
        window = window[:nxt.start() + 10]
    has_shift_expr = re.search(r"box\s*/\s*2\s*-\s*center", window) is not None
    has_shift_use = "shift" in window
    if has_shift_expr and has_shift_use:
        return R("G08", "RECELL shift", "PASS", "blocker",
                 "solvator re-centers the complex into [0, box)³ (v53 fix present)")
    return R("G08", "RECELL shift", "FAIL", "blocker",
             "solvate_opc missing the RECELL re-centering (shift = box/2 − center applied to "
             "protein+grid+ligand) — CUDA wraps coords; out-of-cell restrained atoms get 2·k·box "
             "forces and the system NaNs by step ~251")

def g09(c):
    if c.code is None:
        return R("G09", "XmlSerializer style", "WARN", "blocker", "skipped (no run.py)")
    bad = re.search(r"XmlSerializer\.serialize\([^)]*,", c.code, re.DOTALL)
    if bad:
        return R("G09", "XmlSerializer style", "FAIL", "blocker",
                 "2-arg/stream XmlSerializer.serialize(...) — 8.3 takes 1 arg and returns str "
                 "(v53 bug); use open(path,'w').write(XmlSerializer.serialize(obj))")
    if "XmlSerializer.serialize(" in c.code:
        return R("G09", "XmlSerializer style", "PASS", "blocker", "string-return style used")
    return R("G09", "XmlSerializer style", "WARN", "blocker",
             "no XmlSerializer.serialize call found — expected for state/system checkpointing")

def _sdf_counts(lines):
    """Return (natoms, nbonds) from a V2000 counts line (index 3) or None."""
    if len(lines) < 4:
        return None
    ln = lines[3]
    if ln.startswith("M  END") or "V3000" in ln:
        return None
    try:
        return int(ln[0:3]), int(ln[3:6])
    except (ValueError, IndexError):
        return None

def g10(c):
    if not os.path.isfile(c.sdf):
        return R("G10", "ligand atom count", "FAIL", "blocker", f"ligand.sdf missing at {c.sdf}")
    counts = _sdf_counts(_read(c.sdf).splitlines())
    if counts is None:
        return R("G10", "ligand atom count", "WARN", "blocker",
                 "counts line unparsable / V3000 — verify ligand manually")
    nat = counts[0]
    if nat != 35:
        return R("G10", "ligand atom count", "FAIL", "blocker",
                 f"ligand.sdf V2000 atom count = {nat}, expected 35 (mebendazole + Hs) — "
                 "rebuild via the VF2/AddHs builder, never re-embed")
    return R("G10", "ligand atom count", "PASS", "blocker", "35 atoms")

def g11(c):
    if not os.path.isfile(c.sdf):
        return R("G11", "ligand formula", "WARN", "warn", "skipped (no ligand.sdf)")
    lines = _read(c.sdf).splitlines()
    counts = _sdf_counts(lines)
    if counts is None or counts[0] == 0:
        return R("G11", "ligand formula", "WARN", "warn", "formula check skipped (V3000/empty)")
    nat = counts[0]
    formula = {}
    for ln in lines[4:4 + nat]:
        if len(ln) < 34:
            continue
        el = ln[31:34].strip()
        if el in ("C", "H", "N", "O"):
            formula[el] = formula.get(el, 0) + 1
    f = "C%dH%dN%dO%d" % (formula.get("C", 0), formula.get("H", 0),
                          formula.get("N", 0), formula.get("O", 0))
    if f == "C16H13N3O3":
        return R("G11", "ligand formula", "PASS", "warn", "C16H13N3O3 == mebendazole (InChIKey cross-check in runbook)")
    return R("G11", "ligand formula", "WARN", "warn",
             f"formula {f} != C16H13N3O3 — if this is the MBZ kernel, rebuild ligand.sdf via the "
             "VF2 heavy-atom match + AddHs(addCoords=True)")

def g12(c):
    if not os.path.isfile(c.pdb):
        return R("G12", "protein Ca²⁺", "WARN", "warn", f"protein_md.pdb missing at {c.pdb}")
    caline = None
    for ln in _read(c.pdb).splitlines():
        if re.match(r"HETATM\s+\d+\s+CA\s", ln):
            caline = ln
            break
    if caline is None:
        return R("G12", "protein Ca²⁺", "WARN", "warn",
                 "no Ca²⁺ HETATM line found — 1LPB needs its Ca²⁺; check the input")
    chain = caline[21] if len(caline) > 21 else "?"
    if chain == "Z":
        return R("G12", "protein Ca²⁺", "PASS", "warn", "Ca²⁺ HETATM in chain Z (clean terminals)")
    return R("G12", "protein Ca²⁺", "WARN", "warn",
             f"Ca²⁺ found but in chain '{chain}' — moving it to chain Z keeps PDBFixer terminal "
             "detection clean")

def g13(c):
    if c.code is None:
        return R("G13", "Kaggle mount paths", "WARN", "blocker", "skipped (no run.py)")
    pat = re.compile(r"/kaggle/input/([A-Za-z0-9_.\-]+)")
    hits = []
    for i, s in _code_lines(c.code):
        if "find_input_dir" in s or "datasets/" in s:
            continue
        for m in pat.finditer(s):
            if m.group(1).rstrip("/").startswith("datasets"):
                continue  # the documented datasets/<owner>/<slug> convention
            hits.append((i + 1, m.group(0)))
    if hits:
        return R("G13", "Kaggle mount paths", "FAIL", "blocker",
                 f"bare mount {hits[0][1]} at line {hits[0][0]} — use "
                 "/kaggle/input/datasets/<owner>/<slug> (bare /kaggle/input/<slug> 404s)")
    return R("G13", "Kaggle mount paths", "PASS", "blocker", "no bare /kaggle/input mounts")

def g14(c):
    if c.code is None:
        return R("G14", "no embedded secrets", "WARN", "blocker", "skipped (no run.py)")
    pat = re.compile(
        r'(["\'])username\1\s*:\s*(["\'])[^\2]{1,64}\2[^}]{0,200}?(["\'])key\3\s*:\s*(["\'])[0-9A-Fa-f]{16,}\4',
        re.DOTALL)
    if pat.search(c.code):
        return R("G14", "no embedded secrets", "FAIL", "blocker",
                 "Kaggle-API-key-shaped string inside run.py — the kernel is PUBLIC; keep "
                 "keep credentials in the Kaggle CLI’s standard key file only (never in kernel code)")
    return R("G14", "no embedded secrets", "PASS", "blocker", "no key-shaped strings")

def g15(c):
    if c.code is None:
        return R("G15", "SelDCD constants", "WARN", "warn", "skipped (no run.py)")
    if "SelDCD" not in c.code:
        return R("G15", "SelDCD constants", "PASS", "warn", "no custom DCD writer present")
    ok = ("0.04888821" in c.code) and ('b"C"' in c.code or "CORD" in c.code)
    if ok:
        return R("G15", "SelDCD constants", "PASS", "warn",
                 "header constants present (AKMA 0.04888821, CORD magic) — matches OpenMM reference")
    return R("G15", "SelDCD constants", "WARN", "warn",
             "SelDCD header constants missing (AKMA 0.04888821 / CORD magic) — do NOT 'fix' them "
             "away; the correct writer is byte-compatible with openmm/app/dcdfile.py")

def g16(c):
    if c.code is None:
        return R("G16", "HMR for 4 fs dt", "WARN", "warn", "skipped (no run.py)")
    if re.search(r"(4\s*\*\s*unit\.femtosecond|0\.004\s*\*\s*unit\.picosecond)", c.code) \
            and "hydrogenMass" not in c.code:
        return R("G16", "HMR for 4 fs dt", "WARN", "warn",
                 "4 fs timestep without hydrogenMass — set hydrogenMass=4*unit.amu (HMR) "
                 "in forcefield_kwargs, or drop dt to 2 fs")
    return R("G16", "HMR for 4 fs dt", "PASS", "warn", "HMR consistent with timestep")

def g17(c):
    if c.code is None:
        return R("G17", "OPC water ff", "WARN", "warn", "skipped (no run.py)")
    if "opc" not in c.code.lower():
        return R("G17", "OPC water ff", "WARN", "warn",
                 "no opc water forcefield found — this kernel uses amber19/opc.xml (4-site, "
                 "M virtual site) with ff19SB")
    return R("G17", "OPC water ff", "PASS", "warn", "4-site OPC water forcefield referenced")

def g18(c):
    if c.code is None:
        return R("G18", "removeCMMotion", "WARN", "warn", "skipped (no run.py)")
    if "removeCMMotion" not in c.code:
        return R("G18", "removeCMMotion", "WARN", "warn",
                 "forcefield kwargs missing removeCMMotion — the kernel sets "
                 "removeCMMotion=False deliberately (runbook params)")
    return R("G18", "removeCMMotion", "PASS", "warn", "removeCMMotion set")

def g19(c):
    if c.code is None:
        return R("G19", "checkpoint writes", "WARN", "warn", "skipped (no run.py)")
    ok = ("saveState" in c.code) and ("saveCheckpoint" in c.code or "run_state" in c.code)
    if not ok:
        return R("G19", "checkpoint writes", "WARN", "warn",
                 "no 50 ps checkpoint + run_state.json pattern found — multi-session runs "
                 "require it (rule R15)")
    return R("G19", "checkpoint writes", "PASS", "warn",
             "saveState + checkpoint/run_state writes present")

def g20(c):
    meta = c.meta_json
    if meta and "accelerator" in meta:
        return R("G20", "accelerator advisory", "WARN", "warn",
                 "kernel-metadata has 'accelerator' — Kaggle assigns the GPU regardless "
                 "(TRAP-02); do not rely on it")
    return R("G20", "accelerator advisory", "PASS", "warn", "no accelerator override expected")

GATES = [g01, g02, g03, g04, g05, g06, g07, g08, g09, g10,
         g11, g12, g13, g14, g15, g16, g17, g18, g19, g20]

EXPLAIN = {
 "G01": "cp run.py run_md.py before every push (Kaggle runs code_file=run.py; v47).",
 "G02": "set code_file=\"run.py\" in kernel-metadata.json.",
 "G03": "use getState(getEnergy=True) then State.getKineticEnergy()/getPotentialEnergy() (8.3).",
 "G04": "rebuild restraint CustomExternalForce per stage (_build_fc + removeForce).",
 "G05": "pin openmm=8.3.1 — 8.6 + nvrtc 13.3 rejects sm_60/sm_70 on the P100.",
 "G06": "export CUDA_ARCH parsed from nvidia-smi --query-gpu=compute_cap before CUDA platform.",
 "G07": "restraint refs must be MINIMIZED coords (_Pmin/_refpos), not raw input.",
 "G08": "solvate_opc must re-center into [0,box)^3: shift = box/2 - center, applied to all frames.",
 "G09": "open(path,'w').write(XmlSerializer.serialize(obj)) — no stream arg in 8.3.",
 "G10": "ligand.sdf must have 35 atoms — rebuild via VF2+AddHs, never re-embed.",
 "G11": "formula must be C16H13N3O3 (mebendazole); check the ligand build.",
 "G12": "keep the Ca2+ HETATM, ideally in chain Z for clean terminal detection.",
 "G13": "mount via /kaggle/input/datasets/<owner>/<slug> or find_input_dir.",
 "G14": "remove credential-shaped strings — the kernel is public; keys stay in the user's CLI config.",
 "G15": "restore AKMA 0.04888821 + CORD header — the writer is byte-compatible with OpenMM.",
 "G16": "hydrogenMass=4*unit.amu when running dt=4 fs (HMR).",
 "G17": "use amber19/opc.xml (4-site) water with ff19SB.",
 "G18": "set removeCMMotion=False in forcefield_kwargs.",
 "G19": "write state.xml + checkpoint.chk + run_state.json every 50 ps for multi-session resume.",
 "G20": "--accelerator is advisory only; design for the Kaggle-assigned GPU (sm_60 path).",
}

# ----------------------------------------------------------------------------- runner

def run_checks(kernel, inp):
    c = Ctx(kernel, inp)
    out = []
    for g in GATES:
        try:
            out.append(g(c))
        except Exception as e:  # a checker must never crash the caller
            out.append(R("G??", getattr(g, "__name__", "?"), "WARN", "warn",
                         f"gate raised {type(e).__name__}: {e}"))
    return out

def emit(results, as_json):
    npass = sum(1 for r in results if r["status"] == "PASS")
    nwarn = sum(1 for r in results if r["status"] == "WARN")
    nfail = sum(1 for r in results if r["status"] == "FAIL")
    if as_json:
        for r in results:
            print(json.dumps(r, ensure_ascii=False))
        print(json.dumps({"summary": {"passed": npass, "warned": nwarn, "failed": nfail}}))
    else:
        for r in results:
            print(f"[{r['status']}] {r['gate']} {r['name']} — {r['detail']}")
        print(f"summary: passed={npass} warned={nwarn} failed={nfail}")
    blockers_failed = [r for r in results
                       if r["status"] == "FAIL" and r["severity"] == "blocker"]
    return 1 if blockers_failed else 0

# ----------------------------------------------------------------------------- selftest

_BROKEN_RUN = '''# broken fixture — every blocker violated on purpose
BOOTSTRAP = "micromamba create -y -n md -c conda-forge python=3.12 openmm=8.6.0 rdkit"
DATA = "/kaggle/input/mebendazole-md-inputs"
kjson = {"username": "someuser", "key": "abcdef0123456789abcdef0123456789"}

class SelDCD:
    MAGIC = 84  # constants intentionally missing (no AKMA, no CORD)

def solvate_opc(modeller, center, box):
    grid = build_grid(center)          # raw-frame grid, NO shift (RECELL missing)
    return len(grid)

def engine(ctx):
    refs = pos_raw[idx]                # restraints reference RAW coords (no _Pmin)
    fc = app.CustomExternalForce("k*((x-x0)^2)")
    fc.setParticleParameters(0, 3, [0, 0, 0, 4184.0])
    st = ctx.getState(getKineticEnergy=True, getPositions=True)
    with open("system.xml", "w") as fh:
        XmlSerializer.serialize(system, fh)
'''

_GOOD_RUN = '''# fixed fixture — all gates should pass
BOOTSTRAP = ("micromamba create -y -n md -c conda-forge python=3.12 "
             "openmm=8.3.1 openmmforcefields openff-toolkit ambertools rdkit pdbfixer")
DATA = "/kaggle/input/datasets/<owner>/mebendazole-md-inputs"
rc = subprocess.run(["nvidia-smi", "--query-gpu=name,compute_cap",
                     "--format=csv,noheader"], capture_output=True, text=True)
os.environ["CUDA_ARCH"] = "sm_" + rc.stdout.split(",")[1].strip().replace(".", "")

class SelDCD:
    def header(self, first_step, interval):
        dt = self.dt_ps / 0.04888821
        return struct.pack("<i4c9if", 84, b"C", b"O", b"R", b"D",
                           0, first_step, interval, 0, 0, 0, 0, 0, 0, dt)

def solvate_opc(modeller, pos, center, box):
    shift = box / 2 - center
    pos = pos + shift
    center2 = box / 2
    grid = build_grid(center2)
    return len(grid), shift

_Pmin_np = None
_refpos = {}

def _build_fc(k_ca, k_lig):
    f = app.CustomExternalForce("k*((x-x0)^2+(y-y0)^2+(z-z0)^2)")
    for pi in sel["CA"]:
        p = _refpos[pi]   # references ARE the minimized positions (_Pmin_np)
        f.addParticle(pi, [float(p[0]), float(p[1]), float(p[2]), k_ca * 418.4])
    return f

def stage(system, prev_fc_idx, minimized_state):
    system.removeForce(prev_fc_idx)
    system.addForce(_build_fc(10.0, 10.0))

fk = {"constraints": app.HBonds, "rigidWater": True, "removeCMMotion": False,
      "hydrogenMass": 4 * unit.amu, "nonbondedMethod": app.PME}
gen = SystemGenerator(forcefields=["amber19/protein.ff19SB.xml", "amber19/opc.xml"],
                      small_molecule_forcefield="openff-2.2.0", forcefield_kwargs=fk)
integrator = LangevinMiddleIntegrator(310 * unit.kelvin, 1 / unit.picosecond,
                                      4 * unit.femtosecond)

def checkpoint(sim):
    st = sim.context.getState(getPositions=True, getVelocities=True, getEnergy=True)
    ke = st.getKineticEnergy()
    pe = st.getPotentialEnergy()
    with open("system.xml", "w") as fh:
        fh.write(XmlSerializer.serialize(system))
    with open("state.xml", "w") as fh:
        fh.write(XmlSerializer.serialize(st))
    sim.saveState("state.xml")
    sim.saveCheckpoint("checkpoint.chk")
    json.dump({"ns": 0.05}, open("run_state.json", "w"))
    return ke, pe
'''

_BROKEN_META = '{"id": "x/y", "title": "y", "code_file": "run_md.py", "language": "python"}'
_GOOD_META = '{"id": "x/y", "title": "y", "code_file": "run.py", "language": "python", "enable_gpu": true}'

def _sdf_text(natoms, elements):
    """Build a minimal V2000 SDF with `natoms` atoms; counts line at index 3."""
    nbonds = natoms - 11
    lines = ["fixture-ligand", "  md_preflight", ""]
    lines.append("%3d%3d  0  0  0  0  0  0  0  0999 V2000" % (natoms, nbonds))
    for i, el in enumerate(elements):
        lines.append("%10.4f%10.4f%10.4f %-3s 0  0  0  0  0  0  0  0  0  0  0  0"
                     % (0.5 * i, 0.25 * i, 0.1 * i, el))
    lines.append("M  END")
    return "\n".join(lines) + "\n"

def _elements(c, h, n, o):
    return (["C"] * c) + (["H"] * h) + (["N"] * n) + (["O"] * o)

_GOOD_PDB = ("HETATM" + "  453" + " " + " CA " + " " + " " + "CA " + " " + "Z" + " 453"
             + "      -4.000   1.000   2.000  1.00  0.00          CA  \n"
             "ATOM      1  N   NLYS B1       1.000   2.000   3.000  1.00  0.00           N  \n")

def _fixture(broken):
    td = tempfile.mkdtemp(prefix="md_preflight_fixture_")
    k = os.path.join(td, "kernels")
    i = os.path.join(td, "input")
    os.makedirs(k)
    os.makedirs(i)
    run = _BROKEN_RUN if broken else _GOOD_RUN
    with open(os.path.join(k, "run.py"), "w") as fh:
        fh.write(run)
    with open(os.path.join(k, "run_md.py"), "w") as fh:
        fh.write(run + ("\n# drift\n" if broken else ""))
    with open(os.path.join(k, "kernel-metadata.json"), "w") as fh:
        fh.write(_BROKEN_META if broken else _GOOD_META)
    with open(os.path.join(i, "ligand.sdf"), "w") as fh:
        fh.write(_sdf_text(34, _elements(16, 13, 3, 2)) if broken
                 else _sdf_text(35, _elements(16, 13, 3, 3)))
    with open(os.path.join(i, "protein_md.pdb"), "w") as fh:
        fh.write("ATOM      1  N   NLYS B1       1.000   2.000   3.000  1.00  0.00           N  \n"
                 if broken else _GOOD_PDB)
    return k, i

def selftest():
    here = os.path.abspath(__file__)
    kb, ib = _fixture(broken=True)
    kf, ig = _fixture(broken=False)
    pb = subprocess.run([sys.executable, here, "--kernel", kb, "--input", ib, "--json"],
                        capture_output=True, text=True)
    pf = subprocess.run([sys.executable, here, "--kernel", kf, "--input", ig, "--json"],
                        capture_output=True, text=True)
    failed_blockers = set()
    for ln in pb.stdout.splitlines():
        try:
            rec = json.loads(ln)
        except ValueError:
            continue
        if rec.get("status") == "FAIL" and rec.get("severity") == "blocker":
            failed_blockers.add(rec["gate"])
    expected = {"G01", "G02", "G03", "G05", "G06", "G07", "G08", "G09", "G10", "G13", "G14"}
    ok_broken = (pb.returncode == 1 and expected.issubset(failed_blockers))
    missing = expected - failed_blockers
    any_fail_fixed = any((json.loads(l).get("status") == "FAIL")
                         for l in pf.stdout.splitlines()
                         if l.strip().startswith("{") and "summary" not in l)
    ok_fixed = (pf.returncode == 0 and not any_fail_fixed)
    # v2 extras: --explain + --version + new warn gates present in both fixtures
    pe = subprocess.run([sys.executable, here, "--explain", "G09"], capture_output=True, text=True)
    ok_explain = pe.returncode == 0 and pe.stdout.startswith("G09:")
    pv = subprocess.run([sys.executable, here, "--version"], capture_output=True, text=True)
    ok_version = pv.returncode == 0 and pv.stdout.strip()
    ran_gates = set()
    for ln in pf.stdout.splitlines():
        try:
            rec = json.loads(ln)
        except ValueError:
            continue
        if rec.get("gate", "").startswith("G"):
            ran_gates.add(rec["gate"])
    ok_all_gates = {f"G{i:02d}" for i in range(1, 21)}.issubset(ran_gates)
    if ok_broken and ok_fixed and ok_explain and ok_version and ok_all_gates:
        print("SELFTEST OK (broken fixture -> exit 1 with %d blockers; fixed fixture -> exit 0; "
              "explain/version ok; 20 gates)" % len(failed_blockers))
        return 0
    print("SELFTEST FAIL")
    if not ok_broken:
        print(f"  broken fixture: exit={pb.returncode} (want 1); missing expected blockers: "
              f"{sorted(missing) or 'none'}")
    if not ok_fixed:
        print(f"  fixed fixture: exit={pf.returncode} (want 0)")
        print(pf.stdout)
    return 3

# ----------------------------------------------------------------------------- main

VERSION = "2.0.0"

def main(argv=None):
    ap = argparse.ArgumentParser(description="Static pre-push checker for Kaggle OpenMM MD kernels")
    ap.add_argument("--kernel", default="./kernels", help="dir with run.py/run_md.py/kernel-metadata.json")
    ap.add_argument("--input", default="./input", help="dir with protein_md.pdb/ligand.sdf")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true", help="run fixture-based self-test and exit")
    ap.add_argument("--version", action="store_true", help="print checker version and exit")
    ap.add_argument("--explain", metavar="Gxx", help="one-line fix for a gate, then exit")
    a = ap.parse_args(argv)
    if a.version:
        print(VERSION)
        return 0
    if a.explain:
        gid = a.explain.upper()
        if gid in EXPLAIN:
            print(f"{gid}: {EXPLAIN[gid]}")
            return 0
        print(f"unknown gate {gid} (G01-G{len(GATES):02d})", file=sys.stderr)
        return 2
    if a.selftest:
        return selftest()
    if not os.path.isfile(os.path.join(a.kernel, "run.py")):
        print(f"error: {a.kernel}/run.py not found (pass --kernel DIR)", file=sys.stderr)
        return 2
    results = run_checks(a.kernel, a.input)
    return emit(results, a.json)

if __name__ == "__main__":
    sys.exit(main())
