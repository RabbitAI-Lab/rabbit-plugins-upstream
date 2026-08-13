# ⚙️ edge-cpu-gguf-tuner

**Categories:** automation, productivity, research  
**Public tags:** #automation, #llama-cpp, #gguf, #cpu-inference, #performance

## ✨ Functionalities

Tunes llama.cpp GGUF inference on CPU-only / edge machines (1-4 cores, low RAM) for maximum tokens/sec, with measured CPU-specific findings for flash attention, KV-cache quantization, batch size, and quant choices.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/edge-cpu-gguf-tuner
```

Benchmark one llama.cpp parameter at a time on the target CPU, compare repeated measurements, validate output quality, and deploy only the measured winner.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Runs llama.cpp binaries locally
• Loads GGUF model files (read)
• No network calls except optional model downloads
• Requires: cmake/g++ if building llama.cpp

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Runs local inference only; your prompts stay on-machine.
- Model files are loaded locally; nothing is sent to the cloud.
- No secrets are involved.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `7a75c69ab795b0033ffe3acc6109dffa7d936d5e3167b37340cc26e5b7cc9c87`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# edge-cpu-gguf-tuner 🧮⚡

**Max tokens/sec for llama.cpp on CPU-only / constrained machines** (VPS, containers, sandboxes, Raspberry Pi).
GPU tuning guides (e.g. `llama-params-optimizer`) actively mislead on CPU — this skill is the measured CPU counterpart.

## TL;DR — measured results (2 vCPU / 2 GB RAM, llama.cpp build 1a064ab, CPU build, r=3–5)

| Param | Best on CPU | Why (measured) |
|---|---|---|
| `--threads` | **= physical cores** | 1→2 threads: tg 16.9→30.7 t/s (+82%, perfect 1.9× scaling) |
| `--flash-attn` | **on** | pp2048 +9%, tg128 +11% even at short ctx; **bit-identical output** (temp 0.1, FA on/off) |
| `--cache-type-k/v` | **f16 (default)** | q8_0: **pp −11…19%** — dequant overhead > bandwidth win at short ctx 🌀 |
| `-b/--batch-size` | default 2048, don't bother | 512/1024/2048 spread = ±2.4% — pure noise on CPU+small models |
| quant choice | newer-arch **Q4_K_M** > older smaller **Q5_K_M** | Qwen3-0.6B Q4_K_M beat Qwen2.5-0.5B Q5_K_M everywhere (pp 152 vs 77 t/s, tg 33 vs 30) |
| mmap | keep default (on) | lets page cache absorb models > free RAM (1.1 GB model ran fine in 1.4 GB available) |

## Workflow (30 min, control-variable)

1. **Build bench tool** (~2 min cached): `cd llama.cpp && cmake --build build --config Release --target llama-bench llama-completion -j $(nproc)`
2. **Baseline** (root of all truth): `llama-bench -m model.gguf -p 512,1024,2048 -n 128,256 -t <cores> -o md`
3. **Sweep ONE variable per invocation** — never chain: `-t 1,2` / `-b 512,1024,2048` / `-fa off,on` / `-ctk f16,q8_0 -ctv f16,q8_0` (bench cross-multiplies), `-r 3` is enough during sweep.
4. **Validate winner** head-to-head on every model baseline vs tuned).
5. **Quality gate**: same prompt, `llama-completion --temp 0.1`, FA on vs off — outputs must be identical.
6. **E2E**: real generation, read `common_perf_print` tokens/s; expect within ±5–8% of bench (shared-box noise).

## Counterintuitive log (the valuable part) 🌀

1. **KV q8_0 slows CPU** (−11…19% pp, −1…2% tg). The GPU rule *inverts*: at ≤4K ctx the KV fits caches anyway, dequant math is pure overhead. Only quantize KV when RAM-starved.
2. **FA helps even at short ctx on ≤0.7B models**; neutral on 1.5B — never hurts → default ON on CPU.
3. **Bigger+newer-arch Q4 beats smaller-older Q5.** Architecture generation ≺ quant type for CPU speed; don't pick models by param count alone.
4. **Batch size is a no-op** for CPU prompt processing of small models — ignore the GPU-era +67% claims.
5. **No memory sweet-spot cliff on CPU** (that's a VRAM-bank artifact). Just keep model+KV+compute inside available RAM; 90–95% rules don't apply.

## Pitfalls
- llama-bench default `-r 5` — long runs; pass `-r 3` for sweeps.
- New llama.cpp renamed the CLI: monolithic `llama` needs server libs (fails with `LLAMA_BUILD_SERVER=OFF`); use **`llama-completion`** — full common-params (`-fa`, `-ctk`, templated chat, non-interactive stdin-EOF exit).
- Classic `llama-simple` accepts ONLY `-m -n prompt` — no tuning flags reach it.
- Rerun after any environment wipe; binary targets: `llama-bench llama-completion` (+optional `llama-simple`).

## Deploy the tuned answer

---

*README-only documentation remediation. No functional artifact file was changed.*
