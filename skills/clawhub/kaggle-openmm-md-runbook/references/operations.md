# Operations Quick Reference — Kaggle GPU MD

Part of the `kaggle-openmm-md-runbook` skill. Replace `<owner>` with your Kaggle username and
`<slug>` with your kernel slug (e.g. `mebendazole-md-100ns`).

## Session budget math (P100, mixed precision — measured)

| Quantity | Value |
|---|---|
| Kaggle GPU session wall cap | ~9–12 h (auto-ended by Kaggle; no flag/override exists) |
| Weekly GPU quota | ~30 GPU-h per Kaggle account |
| Measured MD speed (with all diagnostics) | ~240 steps/s @ 2 fs (B1); production pace comparable |
| Steps for 100 ns @ 4 fs | 25,000,000 steps |
| Wall time for 100 ns | ~29 h ≈ **2.5–3 sessions** |
| Equilibration B1–B5 (~1 ns) | ~33 min ≈ 0.55 GPU-h |
| Micromamba bootstrap (openmm=8.3.1 env) | ~90–100 s per fresh session (unavoidable) |

**Rule of thumb:** never plan a single-session 100 ns run. The 50 ps checkpoint + resume-dataset
pattern (RUNBOOK §7.3) is the design; plan for ~3 sessions.

## Supervisor loop pattern

*(Opt-in, user-approved unattended monitoring. Requires the user's own `kaggle.json` and an
explicit human request before starting; run at most one instance; bounded — stops when the run
completes or after 3 consecutive failures.)*

```text
loop forever (INTERVAL = 900 s default):
    status = kaggle kernels status <owner>/<slug>
    if status is terminal (COMPLETE / ERROR):
        # 1. pull /kaggle/working/mdout
        kaggle kernels output <owner>/<slug> -p sessions/<UTC-ts>/
        # 2. read run_state.json -> ns_done, has_state_xml
        # 3. if a VALID state.xml exists:
        #      copy state.xml, system.xml, selection.json, run_state.json -> resume staging
        #      kaggle datasets version -p <staging> -m "resume ns=..."
        # 4. relaunch: kaggle kernels push -p kernels/
    sleep INTERVAL
# stop when status == "done" or after 3 consecutive failures
```

**Invariants:**
- Exactly **one** supervisor process per sandbox — two loops = double launches = wasted quota.
- The supervisor **dies with the sandbox**; after any reset: check `kaggle kernels status` first,
  then restart one copy (`nohup python3 md_supervisor.py loop &`).
- Never resume a session that produced no valid `state.xml` — fix the code first.
- On `429 Too Many Requests`, increase `INTERVAL`; the loop is naturally backoff-tolerant.

## Push / status / output command trio

```bash
kaggle kernels push   -p /path/to/kernels/          # new kernel version
kaggle kernels status <owner>/<slug>                # QUEUED | RUNNING | COMPLETE | ERROR
kaggle kernels output <owner>/<slug> -p /tmp/mdopoll
#   -> /tmp/mdopoll/<slug>.log   (JSON-lines: {"data":"..."} per stdout/stderr line)
#   -> /tmp/mdopoll/mdout/       (session.log, run_state.json, state.xml, checkpoint.chk,
#                                 system.xml, selection.json, eq_*.xml, traj_*.dcd, ...)
```

## Companion dataset commands

```bash
kaggle datasets create  -p /tmp/mbz_inputs --private          # first publish (inputs/resume are private on purpose)
kaggle datasets version -p /tmp/mbz_resume -m "resume ns=0.05"  # every session end
kaggle datasets download <owner>/<dataset-slug> -p /tmp/check --unzip   # verify md5 vs local
```

## Pre-flight (BEFORE any push — saves GPU quota)

```bash
python3 scripts/md_preflight.py --kernel kernels/ --input input/   # 15 static gates, exit 0 = safe to push
bash    scripts/selftest.sh                                        # the skill itself is intact
```
