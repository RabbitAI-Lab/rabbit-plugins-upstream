---
name: image-with-comfyui
description: 'Use to generate, edit, or animate images and videos through a ComfyUI server (loopback by default; remote only via an explicit, trusted COMFYUI_URL) — trigger with requests like "make a picture of", "replace the background", "turn this into a video", or "edit my photo". Not for simple non-generation image tweaks. Uses one universal **Qwen-Image 2.1** model for both text-to-image (T2I) and image editing/multi-image (I2I). Calls a ComfyUI instance (loopback by default) for T2I via Z-Image/SD3.5, I2I via Qwen Image Edit (2511), and I2V via Wan2.2.'
version: "2.3.0"
license: BSD-3-Clause
compatibility: 'ComfyUI ≥ 0.37.0; requires python3; loopback endpoint by default — point COMFYUI_URL at a remote server only if you control and trust it.'
allowed-tools: Read, Write, Edit, Exec
metadata:
  openclaw:
    emoji: "🎨"
    requires:
      anyBins: ["python3"]
    config:
      path: "config.json"
---

# Image with ComfyUI

Call a **loopback-first** ComfyUI server to generate or edit images and videos. One default model does the heavy lifting; Z-Image / SD3.5 / Wan2.2 are available on request.

- **T2I** (Text → Image) → **Qwen-Image 2.1** (default) or Z-Image / SD3.5 Medium
- **I2I** (Image → Image / Edit / Multi-image, up to 16 refs) → **Qwen-Image 2.1** (default) or Qwen Image Edit (2511, single image)
- **I2V** (Image → Video) → Wan2.2 model

`config.json` at the skill root holds every default; any value can be overridden by an env var (see the Data & Privacy table there).

## When to Use

- Generate images from text → **t2i**
- Edit one image, or compose 2–16 reference images → **i2i** (`--image` order = slot order = `<image1>`, `<image2>` …)
- Turn an image into a short video → **wan2.2**
- The user sends an image, then within 2 minutes asks to edit or animate it → **image-first mode**, see [references/image-first.md](references/image-first.md)

## Data & Privacy (read before running)

- **What is transmitted:** prompts and the workflow JSON go to the configured endpoint for **every** mode; **I2I and I2V additionally upload the full source image**.
- **Default endpoint** is loopback-only (`http://127.0.0.1:8188`). Setting `COMFYUI_URL` to a non-loopback host prints a data-flow warning on every run.
- **Written to disk:** generated media is saved under `output_dir` (`config.json` or `COMFYUI_OUTPUT_DIR`). Don't submit sensitive content if the endpoint or disk is a concern.
- **Secrets:** never put credentials in the URL or logs.

## Workflow Files

| Mode | Workflow | File |
|---|---|---|
| T2I (**Qwen-Image 2.1, default**) | Qwen-Image 2.1 dual-mode | `workflows/qwen_image_2.1_api.json` |
| I2I (**Qwen-Image 2.1, default**, incl. multi-image) | same file, switch ON | `workflows/qwen_image_2.1_api.json` |
| T2I (Z-Image) | Z-Image | `workflows/z-image_t2i_api.json` |
| T2I (SD3.5) | SD3.5 Medium | `workflows/sd3.5-med_t2i_api.json` |
| I2I (legacy) | Qwen Image Edit (2511) | `workflows/qwen_image-edit_api.json` |
| I2V | Wan2.2 Image-to-Video | `workflows/wan2.2_i2v_api.json` |

Each workflow is an **adapted** version of a real ComfyUI graph. Original source + exactly what was changed → [references/attribution.md](references/attribution.md).

## CLI Usage

> **⚠️ The prompt is MANDATORY and must be passed via `--prompt` — never as a positional word.**
>
> Every subcommand (`t2i`, `i2i`, `wan2.2`) reads the prompt from `--prompt "..."`. Passing the prompt as a bare positional word fails immediately with exit code 2:
> `python3 image_with_comfyui.py t2i "some description"` → `t2i: error: the following arguments are required: --prompt`
>
> This is a **100%-avoidable failure loop** — the command never reaches ComfyUI, so the model can't help. Always write the prompt through `--prompt` on the **first** attempt.

Full commands and the timeout table → [references/cli-reference.md](references/cli-reference.md)

## Prompt Formatting

Per-model guidance (formulas, rules, example prompts) lives in [references/prompts.md](references/prompts.md). The English prose is there; example prompts keep their bilingual keyword pairs where the original was bilingual (e.g. `blurry 模糊`).

- **Qwen-Image 2.1 (T2I + I2I default):** natural-language prompts. **CFG locked to 1.0** (distilled) — never pass `--cfg`. Optional `--negative` supported in both T2I and I2I (keep it short); I2I prompts stay concise, in the user's language.
- **SD3.5 Medium:** natural language + optional `--negative`; default **1:1 (1024×1024)**, 20 steps, CFG 4.01.
- **Z-Image / Qwen-Image 2.1:** `--aspect` is **optional** — omit it and the output defaults to **1:1 (1024×1024)**. Pass `--aspect 16:9`, `9:16`, etc. for other shapes.
- **Z-Image:** natural language — **no negative prompts**.
- **Qwen Image Edit (2511):** concise, positive-only, user's exact words.
- **Wan2.2 (I2V):** motion/action prompts; default 81 frames, 4 steps, CFG 4.5.

## Error Handling

The script auto-detects three categories of server-side problems and reports them with install/source guidance, and `t2i`/`i2i` run through a **runtime fallback chain** when the default model fails. Details → [references/error-handling.md](references/error-handling.md):

1. **Missing nodes** — reports which node, its package, and a pinned GitHub install hint (the script never runs `git clone` itself).
2. **Missing models** — substitutes a compatible model (e.g. SD3.5 medium variants → SD3.5 large).
3. **Non-critical utility nodes** (e.g. `UnloadAllModels`) — bypassed automatically without interrupting generation.
4. **Runtime fallback chain** — `t2i`/`i2i` auto-descend through alternate models (and, for t2i, any available checkpoint) on runtime failures; config problems (missing files/nodes) abort instead of degrading. Disable with `--no-fallback`.

## Output Delivery

**Send the generated file — do not just describe it.** Deliver in the **user's original session**, never raw paths/URLs. Per-channel prefixes and the staging/cleanup routine → [references/delivery.md](references/delivery.md)

**Output format:** generated images default to **JPG** (`config.json` → `image.output_format`); pass `--format png` for lossless, or `--format jpg --jpg-quality N` per run. Conversion happens client-side (ComfyUI always saves PNG server-side).

## Execution Discipline — Fast Path

The **measured GPU sampling time is ~12–20s**. When a task takes minutes, the delay is **not** inference — it's either a model cold-reload or agent-side overhead. Kill the waste:

1. **Never re-read on repeat.** Don't re-read `SKILL.md`, `config.json`, or the script for a known config / repeat / same-model job. Defaults are baked in; `--aspect` / `--steps` / `--cfg` are in the links above.
2. **At most one pre-check merge.** Gather any needed info in a single batched command, or skip it entirely for trivial repeat jobs.
3. **Run immediately after one check.** Don't inspect, second-guess, or add tool calls between knowing the prompt and running.
4. **Verify only the minimum.** After the run, check only what the user asked (size / seed / file exists).
5. **Golden rule:** sampling is ~12–20s. Anything longer = reload or overhead — never pile on tool calls before the image exists.
6. **Prompt-flag trap:** pass `--prompt "..."` on the first attempt; a positional word wastes a whole turn.

## References (index)

- [references/image-first.md](references/image-first.md) — image-then-edit detection rules + multi-image reference composition
- [references/attribution.md](references/attribution.md) — original source + modifications per workflow
- [references/cli-reference.md](references/cli-reference.md) — full commands + timeout reference
- [references/prompts.md](references/prompts.md) — per-model prompt guidance
- [references/error-handling.md](references/error-handling.md) — auto-handled error categories
- [references/delivery.md](references/delivery.md) — per-channel delivery + staging
