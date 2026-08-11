# Codex GPT-5.6-Sol + Claude — Hardware/Embedded Review

Validated pairing for adversarial review of firmware/embedded projects.

## Roles

| Role | Model | Command |
|------|-------|---------|
| Architect | Codex GPT-5.6-Sol (reasoning=medium; bump to high if shallow) | `codex exec -C <project_dir> --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox -c model='gpt-5.6-sol' -c model_reasoning_effort='medium'` |
| Inspector | Claude Fable 5 (tmux) | `python3 /path/to/claude-tmux.py --yolo --model best --timeout 600 --hard-timeout 1200` |
| Cross-review | Claude Fable 5 (same cmd) | Same as Inspector |
| Synthesis | Claude Fable 5 | Same as Inspector |

## Approaches

### Approach A: `codex exec -C <dir>` (recommended for large projects)

For Codex as the reviewer, **do NOT use `adversarial_review.py --project-dir`** when the project has many files. The script concatenates ALL source into stdin, which:

- Exceeds Codex's 1 MB input limit for projects > ~85 files
- Floods the model with irrelevant test/build files
- Prevents Codex from exploring files selectively

Instead, pass a focused prompt via inline argument and let Codex explore with `cat`/`rg`/`sed`.
**Prefer inline prompt over pipe** to avoid PTY buffer/deadlock issues:

```bash
codex exec \
  -C /path/to/project \
  --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox \
  -c model='gpt-5.6-sol' -c model_reasoning_effort='medium' \
  'Review the project. Explore src/ and lib/ files yourself via cat/rg/sed.
   Focus on algorithmic correctness and hardware realism.
   Output JSON findings with id/severity/file/line/summary/evidence and verdict.'
```

The inline prompt (~200 chars) is kept intentionally short — Codex reads the
task from the prompt and explores files on its own. If the prompt contains
apostrophes or complex quoting that break single-quote shell syntax, write it
to a file and use `"$(< /tmp/prompt.txt)"`:

```bash
codex exec ... "$(< /tmp/prompt.txt)" 'short fallback instruction'
```

The prompt should include: task description, hardware context, JSON output format,
and a directive to `cat`/`rg` files from `src/` and `lib/`. The `-C` flag sets the
context directory so `exec` shell commands run there.

### Approach B: `adversarial_review.py --project-dir` (for small projects)

For projects with <50 source files and no build artifacts:

```bash
python3 scripts/adversarial_review.py --project-dir /path --a-cmd "codex ..."
```

Before launch, verify `_SKIP_DIRS` excludes `.pio`, `build`, `target`, `test`, `unity` and `_SKIP_DIR_PREFIX` covers `.adversarial-*` and project-specific dot-dirs. Check input size < 700K chars using the script's own `_list_tree`:

```bash
python3 -c "exec(open('scripts/adversarial_review.py').read().split('if __name__')[0]); import os; f=_list_tree('.'); print(f'{len(f)} files, {sum(os.path.getsize(p) for p in f):,} chars')"
```

## Strengths

- **Codex (GPT-5.6-Sol)** excels at algorithmic correctness analysis: DSP math (Goertzel, Kalman, FFT), lock-free concurrency patterns, signal-processing pipeline design, and hardware/physics realism of detection thresholds.
- **Claude (Fable 5)** excels at edge-case hunting, error recovery, and hardware physical limits (RSSI quantization, settling times, noise floors, SPI bus timing).

## When to use

- Embedded firmware with DSP/sensing algorithms (ESP32, CC1101, BLE)
- Projects where hardware physics limits matter (RF sensing, radar-like processing)
- Dual-core concurrency review (lock-free, SPSC, atomic memory ordering)

## Pitfalls

- **`_SKIP_DIRS` must exclude `.pio`, `build`, `target`, `test`, `unity`** for PlatformIO projects. Without these, `_list_tree()` descends into compiled library directories (383 MB+) and lists only build artifacts — the model never sees the source code. Run the file-count check above before launch.
- **`_SKIP_DIR_PREFIX`** filters dot-prefixed dirs (`.adversarial-*`, `.omnisense-*`). These are not caught by the plain `_SKIP_DIRS` set.
- **Dot-prefixed files at the project root** (`.omnisense-*.md` specs, `.adversarial-*.json`) must be filtered by `name.startswith(".")` — they live in non-skipped directories.
- **The `_fail_phase` private-method bug:** older `adversarial_review.py` called `runner._fail_phase()` but `runner.py` exports `fail_phase()` (no underscore). If you see `module 'adversarial_common.runner' has no attribute '_fail_phase'`, replace `runner._fail_phase(` with `runner.fail_phase(` in line 271.
- **Codex uses stdin as prompt** in Approach B. No inline `exec "..."` argument is passed; the persona + file listing are piped via `communicate(input=...)`. Ensure the persona starts with a clear instruction.
- **`--project-dir` includes ALL non-skipped files.** For large projects, always verify the `_list_tree` output before assuming the model received relevant files.
- **Timeouts:** GPT-5.6-Sol reasoning=high can take 2-10 min per response. Start with reasoning=medium (near-instant thinking, still thorough). Bump to high or xhigh only if the findings are shallow.
- **GPT-5.6-Sol reasoning=high may appear hung** for 4+ minutes with no output — the model is silently reasoning before the next action. The process is not hung if the PID is still alive (check `process(action='poll')`). With reasoning=medium, the model produces intermediate tool calls (cat, rg) within seconds.

## Hardware context to include in persona

When reviewing RF sensing firmware (433 MHz CC1101, 2.4 GHz WiFi CSI, BLE spectral scan):

- CC1101 RSSI: ~6-bit quantization, -110 dBm noise floor, +10 dBm TX max
- ESP32-S3: dual-core, single-precision FPU only, SPI bus shared with SD card
- 433 MHz through walls: 3-10 dB attenuation per wall, multipath complex
- WiFi CSI: requires sustained traffic (>10 pps), gain lock via undocumented Espressif PHY symbols
- BLE spectral scan: 40 channels vs 3-channel fallback (HCI controller dependency)
