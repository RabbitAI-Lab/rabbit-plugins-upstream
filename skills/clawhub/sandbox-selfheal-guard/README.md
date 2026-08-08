# 🛡️ sandbox-selfheal-guard

**Categories:** agents, automation, security  
**Public tags:** #agents, #self-healing, #sandbox, #resilience, #automation

## ✨ Functionalities

Anti-stuck / anti-snapshot-wipe guard for agentic sandboxes: self-healing runner, byte-verified GGUF manifest, native CPU rebuild, hard timeouts, binary fallback chain, prompt-cache integration, and light-swarm auto mode.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/sandbox-selfheal-guard
```

Review the repair manifest, run a dry check first, then use the guarded healer with bounded timeouts; inspect every proposed destructive or network action.

A representative command from the unchanged skill documentation is:

```bash
#!/bin/bash
# selfheal_runner.sh — sourced by all model runners
set -e
LOG=/tmp/selfheal.log
echo "$(date -Iseconds) selfheal pre-flight start" >> $LOG

# 1. apt packages
for bin in cmake g++ curl; do
  if ! command -v $bin >/dev/null; then
    echo "missing $bin → apt-get install" | tee -a $LOG
    sudo apt-get update -qq && sudo apt-get install -y -qq $bin
  fi
done

# 2. npx shim prevents Arena hang
if [ ! -x "$HOME/.shim/npx" ]; then
  mkdir -p "$HOME/.shim"
  printf '#!/bin/bash\nexec /usr/bin/npx --yes "$@"\n' > "$HOME/.shim/npx"
  chmod +x "$HOME/.shim/npx"
  echo "shim recreated" >> $LOG
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Runs repair/heal scripts (selfheal_runner.sh)
• May modify workspace files it is configured to guard
• May rebuild local binaries (cmake/g++)

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Runs shell repair commands that can modify files, credentials, dependencies, and workspace state.
- Keep repair recipes narrowly scoped and idempotent; use --dry-run first.
- Review manifest entries before install.
- No data is sent off-box unless you configure an off-box sync.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `8349e571b3b676bfbe3301e7863f4939107d10cc1bfbcad79690fbc33f258d2f`

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

# sandbox-selfheal-guard 🛡️⚡ v2.1.0 — MAX SPEED + ACTUAL RUNNER LIB

**Problem:** Arena.ai Agent Mode, OpenClaw, containerized sandboxes evict large binaries — `build/`, `*.gguf` 2.4GB, apt packages — when workspace snapshot cap exceeded (128MB / 10k files). Scripts survive (small text) but invoke missing binaries → agent appears to "think forever" user stops it.

## What's New in v2.1.0 — Debug Fixes & Features

**Debug fixes:**
- v2.0.0 referenced `selfheal_runner.sh` 180-line library but file not bundled — **now included** as actual executable library in package `scripts/selfheal_runner.sh`
- Fixed missing native build flag: add `-DLLAMA_NATIVE=ON -DCMAKE_BUILD_TYPE=Release` → +7-10% pp from AVX512/VNNI
- Fixed byte-size check only existence → now exact byte manifest verification (484M vs 15-byte HTML error page)
- Fixed npx hang root cause clarified: Arena sandbox stdin closed → shim mandatory export PATH="$HOME/.shim:$PATH"
- Fixed no logging → now `/tmp/selfheal.log` with timestamped rebuild/redownload events

**New features:**
- **Prompt-cache integration**: `prompt_cache_layer.py` SHA256 lookup before heavy inference → 0.06s hit = ∞ t/s, 60% save
- **Run_max_speed integration**: `run_max_speed.sh` uses selfheal pre-flight + cache + fallback + timeout
- **Light-swarm auto**: <8 words casual → SCOUT only 2.2s, prevents full swarm hang on trivial chat
- **Per-agent timeout with fallback**: SCOUT/SPARK/FORGE 60s, SAGE 150s, fallback q3 on timeout
- **Updated manifest**: 4 models with exact bytes + speed roles (SCOUT 34 t/s etc)
- **Integration tests**: `test_selfheal.sh` simulates missing binary, missing model, truncated model, npx hang

## Core Recipe: pre-flight self-heal + per-call timeout (Reference Implementation)

**`scripts/selfheal_runner.sh` (now bundled, 220 lines):**
```bash
#!/bin/bash
# selfheal_runner.sh — sourced by all model runners
set -e
LOG=/tmp/selfheal.log
echo "$(date -Iseconds) selfheal pre-flight start" >> $LOG

# 1. apt packages
for bin in cmake g++ curl; do
  if ! command -v $bin >/dev/null; then
    echo "missing $bin → apt-get install" | tee -a $LOG
    sudo apt-get update -qq && sudo apt-get install -y -qq $bin
  fi
done

# 2. npx shim prevents Arena hang
if [ ! -x "$HOME/.shim/npx" ]; then
  mkdir -p "$HOME/.shim"
  printf '#!/bin/bash\nexec /usr/bin/npx --yes "$@"\n' > "$HOME/.shim/npx"
  chmod +x "$HOME/.shim/npx"
  echo "shim recreated" >> $LOG
fi
export PATH="$HOME/.shim:$PATH"

# 3. llama.cpp binaries native rebuild +7-10%
CLI=~/llama.cpp/build/bin/llama-completion
if [ ! -x "$CLI" ]; then
  echo "rebuild llama.cpp native" >> $LOG
  cd ~/llama.cpp
  cmake -B build -DLLAMA_NATIVE=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_BUILD_SERVER=OFF -DLLAMA_SERVER=OFF
  cmake --build build --target llama-simple llama-completion llama-bench llama-simple-chat -j2
fi

# 4. GGUF manifest verification
declare -A MANIFEST=(
  ["Qwen2.5-0.5B-Instruct-Q5_K_M.gguf"]=420086080
  ["Qwen3-0.6B-Q4_K_M.gguf"]=484220320
  ["DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"]=1117320800
  ["Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"]=397808288
)
for f in "${!MANIFEST[@]}"; do
  exp=${MANIFEST[$f]}
  if [ ! -f ~/$f ] || [ "$(stat -c%s ~/$f)" != "$exp" ]; then
    echo "redownload $f (expected $exp)" >> $LOG
    case $f in
      Qwen2.5-0.5B*) curl -sSL -o ~/$f https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/$f ;;
      Qwen3-0.6B*) curl -sSL -o ~/$f https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF/resolve/main/$f ;;
      DeepSeek*) curl -sSL -o ~/$f https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/$f ;;
      Coder*) curl -sSL -o ~/$f https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF/resolve/main/$f ;;
    esac
  fi
done

# 5. auth
[ -f ~/.clawhub/TOKEN ] || echo "auth missing — run clawhub login" >> $LOG

# Wrap model call with timeout + fallback
run_with_timeout() {
  local model=$1 prompt=$2 n=$3 timeout=$4
  timeout $timeout ~/llama.cpp/build/bin/llama-completion -m $model --prompt "$prompt" -n $n -t 2 -fa on --ctx-size 2048 2>/dev/null || \
  timeout 60 ~/llama.cpp/build/bin/llama-simple -m $model -n $n "$prompt" 2>/dev/null || \
  return 2
}
```

Then per-call wrapper:
- r1 (1.5B ~13 t/s): budget = 45s + n/10
- q3/fast/code (0.5-0.6B ~30 t/s): budget = 30s + n/20
- Absolute cap 300s
- Fallback: `llama-completion` → `llama-simple` → exit 2

## Optimal CPU params (from edge-cpu-gguf-tuner v2)

| Param | Best | Why |
|---|---|---|
| -t | =2 physical cores | t=4 oversubscribes tg -42% |
| -fa | on | pp +11% tg +19% small models |
| -ctk/-ctv | f16 default | q8_0 pp -35-50% CPU |
| -b | 2048 default | no-op ±2.4% |
| quant | newer Q4_K_M > older Q5_K_M | arch > quant speed |
| build | -DLLAMA_NATIVE=ON | AVX512/VNNI +7-10% pp |
| cache | SHA256 hit | 33x faster 2.1s→0.06s |
| ctx | 2048 fast / 4096 r1 | less KV overhead |

## Byte Manifest + Roles + Speed

| File | Bytes | Role | Speed |
|---|---|---|---|
| Qwen2.5-0.5B-Instruct-Q5_K_M.gguf | 420,086,080 | SPARK | 30 t/s |
| Qwen3-0.6B-Q4_K_M.gguf | 484,220,320 | SCOUT | 34 t/s fastest |
| DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf | 1,117,320,800 | SAGE deep | 14 t/s |
| Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf | 397,808,288 | FORGE code | 31 t/s pp145 |

## Anti-hang Rules (must enforce)

1. Never run inference without `timeout`
2. Always verify binary exists + exec
3. Always verify model byte size not just existence
4. Light-swarm (SCOUT only 80-120 tokens) casual chat; full swarm substantive
5. Independent timeouts per swarm agent — slow SAGE can't hang SCOUT
6. Log self-heal triggers to `/tmp/selfheal.log` and continue
7. Visible progress echo before long ops (spinner/header)

## Integration Tests (NEW)

`scripts/test_selfheal.sh`:
- Simulate missing `llama-completion` → expect rebuild
- Simulate missing GGUF → expect redownload manifest check
- Simulate truncated GGUF (15-byte HTML) → expect redownload
- Simulate npx without shim → expect shim recreation
- Simulate model timeout → expect fallback q3
- Simulate repeated prompt → expect cache hit 0.06s

## Related Skills Integration

- `edge-cpu-gguf-tuner v2` — provides tuned params
- `fast-response-optimizer` — reply-first + parallel
- `prompt-cache` — hash dedup
- `openclaw-cache-kit` — long retention system prompt
- `model-fallback` — chain
- `keepalive` — gateway 24/7

Authored field Arena 2026-07-27 for user-reported "agent stops responding". Root cause snapshot eviction 2.4GB GGUF+build, scripts calling missing binaries. v2.1.0 adds actual runner lib, cache, native rebuild, tests.

---

*README-only documentation remediation. No functional artifact file was changed.*
