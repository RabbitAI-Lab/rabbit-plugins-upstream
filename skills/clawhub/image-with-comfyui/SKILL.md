---
name: image-with-comfyui
description: 'Use to generate, edit, or animate images and videos through a user-defined ComfyUI server (COMFYUI_URL env var or comfyui_url in config.json; if no server is reachable the script exits with configuration instructions) — trigger with requests like "make a picture of", "replace the background", "cut out / extract the subject of", "turn this into a video", "edit my photo", or "make a 3D mesh of this character". Not for simple non-generation image tweaks. **Qwen-Image 2.1** is the default model for both text-to-image (T2I) and image editing/multi-image (I2I); it can also **cut out / extract the main subject or any image element into a transparent-background image**. Z-Image / SD3.5 (T2I), Qwen Image Edit (2511, single-image), Wan2.2 (I2V), and Hunyuan 3D v2.1 (I2M, image → 3D GLB mesh) are available on request.'
version: "3.5.0"
license: BSD-3-Clause
compatibility: 'ComfyUI ≥ 0.37.0; requires python3; the endpoint is user-defined (COMFYUI_URL or config.json) — point it at a server you control and trust.'
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

Call a user-defined ComfyUI server to generate or edit images and videos, or turn an image into a 3D mesh. **Qwen-Image 2.1** is the default model for both T2I and I2I; Z-Image / SD3.5 (T2I), Qwen Image Edit 2511 (single-image edit), Wan2.2 (I2V), and Hunyuan 3D v2.1 (I2M, image → 3D GLB) are available on request. If no ComfyUI server is reachable, the script exits with configuration instructions (see [README.md](README.md)).

- **T2I** (Text → Image) → **Qwen-Image 2.1** (default) or Z-Image / SD3.5 Medium
- **I2I** (Image → Image / Edit / Multi-image, up to 16 refs) → **Qwen-Image 2.1** (default) or Qwen Image Edit (2511, single image)
- **I2V** (Image → Video) → Wan2.2 model
- **Cutout** (extract the main subject or any image element) → **Qwen-Image 2.1** — redraws the target on a transparent background, producing a clean, alpha-only image; see [Cutout below](#cutout-extract-the-subject).
- **I2M** (Image → 3D Mesh) → **Hunyuan 3D v2.1** — extracts the main character first (transparent PNG), generates a GLB, scales it ×3000, and zips it for delivery

`config.json` at the skill root holds every default; any value can be overridden by an env var (see the Data & Privacy table there).

## Cutout — Extract the Subject

> **Note:** cutout is a genuine image-generation task, not a simple non-generation tweak — use it when the user wants to isolate the subject or any image element from its surroundings.

**Qwen-Image 2.1** can **cut out / extract** the main subject (or a specified element) from an image and return it on a transparent background. The output is a clean PNG with alpha only — it re-draws the target rather than doing a hard pixel mask, so it works well for organic shapes (people, animals, products, characters) and can target a specific described element (e.g. "extract just the red car", "isolate the vase") via the prompt.

- Use the **`i2i`** subcommand with `--image <path>` and a prompt that names the subject to extract. Keep the prompt focused on *what to keep*, not what to remove.
- The result is transparent (alpha-only). Deliver it as-is — never convert to JPG (which has no alpha channel, so it would flatten transparency onto white).
- This is the same redraw-to-transparent step that I2M runs first (see the i2m rules), but here it is used on its own to produce a standalone cutout image.

## When to Use

- Generate images from text → **t2i**
- Edit one image, or compose 2–16 reference images → **i2i** (`--image` order = slot order = `<image1>`, `<image2>` …)
- Turn an image into a short video → **wan2.2**
- Turn the character in an image into a **3D mesh (GLB)** → **i2m** (Hunyuan 3D v2.1; the main character is extracted first, see below)
- The user sends an image, then within 2 minutes asks to edit or animate it → **image-first mode**, see [references/image-first.md](references/image-first.md)

## Data & Privacy (read before running)

- **What is transmitted:** prompts and the workflow JSON go to the configured endpoint for **every** mode; **I2I, I2V and I2M additionally upload the full source image**.
- **Endpoint** is user-defined (`COMFYUI_URL` env var > `comfyui_url` in `config.json`; bundled default `http://127.0.0.1:8188`). A non-local host prints a data-flow warning on every run; if no server answers, the script exits with configuration instructions instead of a raw timeout.
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
| I2M (Image → 3D Mesh) | Hunyuan 3D v2.1 | `workflows/hunyuan3d-v2.1_i2m_api.json` |

Each workflow is an **adapted** version of a real ComfyUI graph. Original source + exactly what was changed → [references/attribution.md](references/attribution.md).

## CLI Usage

> **⚠️ The prompt is MANDATORY and must be passed via `--prompt` — never as a positional word.**
>
> Every subcommand (`t2i`, `i2i`, `wan2.2`) reads the prompt from `--prompt "..."`. Passing the prompt as a bare positional word fails immediately with exit code 2:
> `python3 image_with_comfyui.py t2i "some description"` → `t2i: error: the following arguments are required: --prompt`
>
> This is a **100%-avoidable failure loop** — the command never reaches ComfyUI, so the model can't help. Always write the prompt through `--prompt` on the **first** attempt.
>
> `i2m` takes no prompt — the character itself is the condition (`--image` is its only required flag).

Full commands and the timeout table → [references/cli-reference.md](references/cli-reference.md)

## Prompt Formatting

Per-model guidance (formulas, rules, example prompts) lives in [references/prompts.md](references/prompts.md). The English prose is there; example prompts keep their bilingual keyword pairs where the original was bilingual (e.g. `blurry 模糊`).

- **Qwen-Image 2.1 (T2I + I2I default):** natural-language prompts. **CFG locked to 1.0** (distilled) — never pass `--cfg`. Optional `--negative` supported in both T2I and I2I (keep it short); I2I prompts stay concise, in the user's language.
- **SD3.5 Medium:** natural language + optional `--negative`; default **1:1 (1024×1024)**, 20 steps, CFG 4.01.
- **Z-Image / Qwen-Image 2.1:** `--aspect` is **optional** — T2I omits it and the output defaults to **1:1 (1024×1024)**; I2I omits it and the output canvas matches the **first reference image's size** (workflow latent switch ON). Pass `--aspect 16:9`, `9:16`, etc. to force a shape — in I2I this flips the latent switch to route the canvas through the ResolutionSelector (reference stays at native size, never stretched).
- **Z-Image:** natural language — **no negative prompts**.
- **Qwen Image Edit (2511):** concise, positive-only, user's exact words.
- **Wan2.2 (I2V):** motion/action prompts; default 81 frames, 4 steps, CFG 4.5.
- **i2m (Hunyuan 3D v2.1, no prompt):** the only input is the character image. Default extraction is **i2i** (Qwen-Image 2.1 redraws the main character centered on a transparent background, saved as PNG — this same redraw-to-transparent cutout is what makes the rest of I2M work; the same Qwen-Image 2.1 I2I call can produce a standalone cutout without any 3D follow-up). Use `--extract rembg` for a non-generative u2net human cutout, or `--extract none` to feed the image straight in (only if it's already a clean cutout). Defaults: resolution 4096, 30 steps, CFG 5.0, delivery scale **×3000** — the raw Hunyuan 3D v2.1 mesh is at a normalized unit scale (character ≈ 2 units, no declared units), so the GLB is scaled in place before zipping (`--scale 1` keeps it unscaled).

## Error Handling

The script auto-detects three categories of server-side problems and reports them with install/source guidance, and `t2i`/`i2i` run through a **runtime fallback chain** when the default model fails. Details → [references/error-handling.md](references/error-handling.md):

1. **Missing nodes** — reports which node, its package, and a pinned GitHub install hint (the script never runs `git clone` itself).
2. **Missing models** — substitutes a compatible model (e.g. SD3.5 medium variants → SD3.5 large).
3. **Non-critical utility nodes** (e.g. `UnloadAllModels`) — bypassed automatically without interrupting generation.
4. **Runtime fallback chain** — `t2i`/`i2i` auto-descend through alternate models (and, for t2i, any available checkpoint) on runtime failures; config problems (missing files/nodes) abort instead of degrading. Disable with `--no-fallback`.

## Output Delivery

**Send the generated file — do not just describe it.** Deliver in the **user's original session**, never raw paths/URLs. Per-channel prefixes and the staging/cleanup routine → [references/delivery.md](references/delivery.md)

**Output format:** generated images default to **JPG** (`config.json` → `image.output_format`). **Routing rule: if the user asks for a PNG image/file, or an RGBA image with transparency/alpha, always pass `--format png` and deliver the PNG file as-is — never convert to JPG** (JPEG has no alpha channel; the conversion would flatten transparency onto white). PNG output passes the server's PNG bytes through unchanged, so transparency is preserved byte-for-byte. Otherwise `--format jpg --jpg-quality N` is available per run; JPG conversion happens client-side (ComfyUI always saves PNG server-side). **i2m delivery rules (3D output):** (1) attach the **extracted character image** from step 1 as an **image** — never just its path (with `--extract none` the step-1 image *is* the user's own input, so there's nothing to send back); (2) send the mesh **packaged as a zip** — the script first **scales the GLB in place by the delivery factor** (default ×3000; the raw mesh is at a normalized unit scale, character ≈ 2 units, no declared units), then zips it (`i2m_<timestamp>.zip`); attach the **zip**, never the raw `.glb`; (3) **never render the mesh** — no GLB → image/video conversion and no 3D-viewer screenshots (a third-party viewer link is fine to share). Format conversion never applies to 3D files.

## Execution Discipline — Fast Path

The **measured GPU sampling time is ~12–20s**. When a task takes minutes, the delay is **not** inference — it's either a model cold-reload or agent-side overhead. Kill the waste:

**i2m exception:** 3D generation is legitimately long (cold checkpoint load + 30 sampling steps + voxel decode ≈ minutes on a 4090). Run it once in the background (`exec` with a generous `timeoutSeconds`), report the queue state, and when it completes deliver the character image + the GLB zip per the i2m delivery rules above — don't spin tool calls around it.

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
