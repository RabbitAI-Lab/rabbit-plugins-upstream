# Running hPL docking on Kaggle

Kaggle gives free Linux VMs with **4 vCPU / ~30 GB RAM**, a **12 h** per-session
ceiling and **~20 GB** of working disk. CPU notebooks have **no weekly quota**,
which is what makes them a good fit for Vina.

**Use CPU, not GPU.** AutoDock Vina has no CUDA path — a GPU kernel docks no
faster, and GPU time is capped at ~30 h/week. `--gpu` exists only for users who
bolt on their own GPU rescoring step.

Everything below was executed against the live Kaggle API; the failure modes in
§5 are ones this runner actually hit, not hypotheticals.

---

## 1. Get an API token

1. Sign in at kaggle.com → click your avatar → **Settings**.
2. Scroll to **API** → **Create New API Token**.
3. A `kaggle.json` downloads: `{"username":"<user>","key":"<32-hex>"}`.
4. Install it:

```bash
mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json      # the CLI warns loudly if this is world-readable
pip install kaggle
```

Alternatives (either works, no file needed):

```bash
export KAGGLE_USERNAME=<user> KAGGLE_KEY=<32-hex>
# or point at a JSON holding several accounts:
#   {"providers":{"kaggle":{"username":..., "api_key":..., "accounts":[{...}]}}}
python scripts/kaggle_dock.py check --creds secrets.json --account 0
```

**Account must be phone-verified** or kernels cannot use internet, and the
toolchain install inside the kernel will fail.

---

## 2. Verify before you spend a run

```bash
python scripts/kaggle_dock.py check
# {"ok": true, "cmd": "check", "exit": 0, "username": "...", "kernels_visible": 5, ...}
```

Exit `3` means the credentials are wrong — fix that before anything else.

---

## 3. One-shot run

`run` = push + poll + fetch. The runner embeds the whole docking stack and your
ligand CSV into the kernel script as base64, so the kernel needs **no dataset
and no GitHub access** — only internet for the conda install.

```bash
python scripts/kaggle_dock.py run \
  --stack docking_professional_stack \
  --ligands ligands.csv \
  --precision balanced \
  --workers 4 \
  --title "hPL screen batch 1" \
  --out kaggle_out \
  --timeout 3600
```

Last stdout line is JSON:

```json
{"ok": true, "cmd": "run", "exit": 0,
 "kernel": "<user>/hpl-screen-batch-1",
 "url": "https://www.kaggle.com/code/<user>/hpl-screen-batch-1",
 "out": "kaggle_out",
 "summary": {"ok": true, "returncode": 0, "elapsed_s": 116.2, "n_rows": 10}}
```

Results land in `kaggle_out/dock_results/results_all_sites.csv` — same schema as
a local run, so downstream tooling is unchanged.

Measured: 2 ligands × 5 sites, `--precision fast`, **~116 s wall** including the
micromamba install (~70 s of that is the install, paid once per kernel).

### Step-by-step (if you prefer the phases separate)

```bash
python scripts/kaggle_dock.py push   --ligands ligands.csv --title "hPL screen batch 1"
python scripts/kaggle_dock.py status --slug hpl-screen-batch-1     # exit 0 = COMPLETE
python scripts/kaggle_dock.py fetch  --slug hpl-screen-batch-1 --out kaggle_out
```

`status` exits `5` while still running, `0` on COMPLETE, `4` on error.

### Raw CLI equivalent

```bash
kaggle kernels push   -p kernel_dir/          # needs script.py + kernel-metadata.json
kaggle kernels status <user>/<slug>
kaggle kernels output <user>/<slug> -p ./out
```

`kernel-metadata.json` must set `"enable_internet": true` or the install step
dies with no network.

---

## 4. Sizing a run

12 h ceiling, 4 vCPU. Rough per-ligand cost across all 5 sites:

| Precision | ~per ligand | Ligands in 11 h (safety margin) |
|---|---|---|
| `fast` | ~15 s | ~2,600 |
| `balanced` | ~30 s | ~1,300 |
| `max` | ~200 s | ~200 |

Split anything larger into batches of ≤1,000 and push them as separate kernels.
A kernel killed at 12 h loses everything not already written to
`/kaggle/working`, so prefer several short kernels over one long one.

---

## 5. Debugging problems inside kaggle.com

### The slug trap (most common, looks like an auth error)

Kaggle derives the kernel slug from the **title**, not from the `id` in
`kernel-metadata.json`. Pushing `id: user/hpl-dock-verify-v101` with
`title: "hPL docking verify v101"` creates the kernel at
**`user/hpl-docking-verify-v101`**. Polling the id you asked for then returns:

```
Cannot access kernel 'user/hpl-dock-verify-v101'
(Permission 'kernels.get' was denied)
```

That message says *permission*, but the cause is the slug. `kaggle_dock.py`
derives the slug from the title so the two always agree. If you push by hand:
list your kernels and use the real slug —

```bash
kaggle kernels list --user <your-username>
```

### Reading logs when a kernel fails

The kernel's stdout is downloaded with the output as `<slug>.log`:

```bash
kaggle kernels output <user>/<slug> -p ./out
cat ./out/<slug>.log
```

Or open `https://www.kaggle.com/code/<user>/<slug>` → **Logs** tab. The kernel
script prints each shell command it runs, so the failing step is greppable:

```bash
grep -n '^\$ ' out/<slug>.log        # every command
grep -n 'FATAL' out/<slug>.log       # our own hard stops
```

### Symptom table

| Symptom | Cause | Fix |
|---|---|---|
| `401 Unauthorized` | bad/rotated key, or `{"api_key":...}` instead of `{"key":...}` | regenerate token; `kaggle.json` needs exactly `username` + `key` |
| `Permission 'kernels.get' was denied` | slug ≠ id (see above) | use the title-derived slug |
| `FATAL: micromamba download failed` | internet disabled or account not phone-verified | set `enable_internet: true`; verify phone |
| Kernel status `error`, log ends in the install step | conda solve failed / transient mirror | re-run; pin `python=3.11` (meeko+vina are not 3.12-clean) |
| `RESULT: FAIL` from `--check` | env built but a tool is missing | read which line lacks `✓`; usually `vina` |
| Status stuck `running` past your timeout | kernel is queued, not hung | Kaggle queues under load; poll with `status`, don't re-push |
| Output missing `results_all_sites.csv` | docking failed before writing | read the log; `n_rows: 0` in the summary confirms it |
| `429` / quota message | too many concurrent kernels | Kaggle allows a limited number of concurrent runs; wait or use another account |

### Rules that keep runs cheap

- **Never re-push to poll.** Each push starts a new run and burns a slot.
- **One kernel per account at a time.** Concurrent runs on one account queue
  behind each other and can be killed.
- `is_private: true` (the default here) keeps ligand structures off the public
  internet. Set `--public` only for data you may disclose.
- Kernels are ephemeral: anything not in `/kaggle/working` at exit is gone. The
  runner deletes the conda env and the unpacked stack before finishing so
  `fetch` returns results, not 100+ files of scaffolding.

### Rotating multiple accounts

With a `--creds` pool, `--account N` picks a slot. Keep **one project per
account at a time** and record which account ran what — nothing in this skill
tracks that for you.

```bash
python scripts/kaggle_dock.py run --creds secrets.json --account 2 --ligands batch3.csv --title "hPL batch 3"
```
