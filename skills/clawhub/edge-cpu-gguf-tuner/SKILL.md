---
name: edge-cpu-gguf-tuner
description: Tune llama.cpp GGUF inference on CPU-only / edge boxes (1-4 cores, low RAM) for maximum tokens/sec. Complements GPU-oriented tuners. Contains measured, counterintuitive CPU-specific findings — flash attention helps even at short contexts, KV-cache quantization HURTS on CPU, batch size is a no-op, newer-arch Q4 beats older smaller Q5. Use when a model runs without a GPU, on a VPS, container, SBC, or sandbox.
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