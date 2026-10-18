# CLI Usage Reference (image-with-comfyui)

Full command examples for every subcommand. The SKILL.md procedure only lists the
core rule; open this file for the exact flags.

> **⚠️ The prompt is MANDATORY and must be passed via `--prompt` — never as a positional argument.**
>
> Every subcommand that takes a prompt (`t2i`, `i2i`, `h3_t2v`, `h3_i2v`, `wan2.2`) reads it from `--prompt "..."` (`i2m` has no prompt — see below). Passing the prompt as a bare positional word fails immediately with exit code 2:
> `python3 image_with_comfyui.py t2i "some description"` → `t2i: error: the following arguments are required: --prompt`
>
> This is a **100%-avoidable failure loop** — the model can't help you because the command never reaches ComfyUI. Always write the prompt through the `--prompt` flag on the first attempt.

### T2I (Text → Image)

```bash
# Qwen-Image 2.1 (default model; CFG locked to 1.0 — no --cfg)
# --aspect is OPTIONAL: omit it and the output is 1:1 (1024x1024)
python3 image_with_comfyui.py t2i \
  --prompt "Your detailed image description" \
  --steps 25

# With a negative prompt (Qwen-Image 2.1 supports it)
python3 image_with_comfyui.py t2i \
  --prompt "A detailed image description" \
  --negative "text, watermark, blurry" \
  --steps 25

# Request a specific aspect ratio explicitly (16:9, 9:16, 4:3, ...)
python3 image_with_comfyui.py t2i \
  --prompt "Your detailed image description" \
  --aspect 16:9 \
  --steps 25


# Z-Image
python3 image_with_comfyui.py t2i \
  --model z-image \
  --prompt "Your detailed image description" \
  --aspect 1:1 \
  --steps 9

# SD3.5 Medium (defaults to 1:1)
python3 image_with_comfyui.py t2i \
  --model sd35 \
  --prompt "A beautiful sunset over mountains" \
  --negative "text, watermark, blurry" \
  --steps 20 \
  --cfg 5.5

# Run ONLY the requested model (skip the runtime fallback chain)
python3 image_with_comfyui.py t2i \
  --prompt "..." --model z-image --no-fallback

# JPG output (converted client-side; default from config.json image.output_format)
python3 image_with_comfyui.py t2i \
  --prompt "..." --format jpg --jpg-quality 90
```

### I2I (Edit Image)

```bash
# Qwen-Image 2.1 (default I2I)
python3 image_with_comfyui.py i2i \
  --prompt "Change background to a beach" \
  --image /path/to/source.jpg \
  --steps 25

# Explicit aspect ratio: routes the I2I latent canvas through the
# ResolutionSelector (workflow latent switch OFF) instead of matching the
# first reference image's size, so a portrait photo CAN become 16:9 landscape.
# The reference is uploaded at native size, never stretched. Without --aspect,
# the output follows the first reference image's own size (no 1:1 forcing).
python3 image_with_comfyui.py i2i \
  --prompt "Extend the scene into a wide landscape" \
  --image /path/to/portrait.jpg \
  --aspect 16:9

# Multi-image reference (up to 16): --image order = slot order
python3 image_with_comfyui.py i2i \
  --prompt "put the shirt from <image2> on the person in <image1>" \
  --image /path/to/base.jpg /path/to/reference.jpg

# Legacy single-image edit
python3 image_with_comfyui.py i2i \
  --model qwen_imageedit \
  --prompt "put on a red jacket" \
  --image /path/to/source.jpg \
  --steps 4

# Qwen-Image 2.1 edit with a negative prompt
python3 image_with_comfyui.py i2i \
  --prompt "replace the background with a night city" \
  --negative "text, watermark" \
  --image /path/to/source.jpg

# Run ONLY the requested model (skip the runtime fallback chain)
python3 image_with_comfyui.py i2i \
  --prompt "..." --image /path/to/source.jpg --no-fallback

# JPG output (see t2i example)
python3 image_with_comfyui.py i2i \
  --prompt "..." --image /path/to/source.jpg --format jpg
```

### I2V (Image → Video) — **MiniMax H3** (`h3_i2v`, default) / Wan2.2 (legacy)

```bash
# MiniMax H3 I2V (default video model): reference image -> video
python3 image_with_comfyui.py h3_i2v \
  --prompt "the person walks forward and smiles" \
  --image /path/to/source.jpg \
  --length 10            # default 10 s; --seed optional
```

### T2V (Text → Video) — **MiniMax H3** (`h3_t2v`)

```bash
python3 image_with_comfyui.py h3_t2v \
  --prompt "a mountain lake at dawn, gentle wind over the water" \
  --length 15            # default 15 s; --aspect optional; --seed optional
```

### I2V (Image → Video) — Wan2.2 (legacy)

```bash
python3 image_with_comfyui.py wan2.2 \
  --prompt "the person walks forward and smiles" \
  --image /path/to/source.jpg \
  --length 81 --steps 4
```


### pi2m (Image → 3D Mesh, Pixal3D / Trellis2 → GLB) — default I2M

```bash
# Feed the source image straight in: the trellis2 graph removes its own
# background internally (birefnet), so no client-side extraction is done.
python3 image_with_comfyui.py pi2m --image /path/to/character.jpg

# Higher-detail / more-iterative generation
python3 image_with_comfyui.py pi2m --image /path/to/character.jpg \
  --steps 15 --cfg 7.5

# Delivery scale: the Trellis2 mesh carries its own real-world units, so the
# default is ×1 (no upscale). Override with --scale N if you want a different
# delivery size.
python3 image_with_comfyui.py pi2m --image /path/to/character.jpg --scale 1
```

- Output: a **GLB file** under `output_dir/meshes/` (prefix `pi2m_<timestamp>`),
  kept at its **natural units** (delivery scale defaults to ×1 — the Trellis2
  mesh is NOT at a normalized unit scale like Hunyuan, so no in-place ×3000
  upscale is applied) and **automatically packaged as `<same-stem>.zip`** — the
  result block prints both paths plus the delivery hints.
- **Delivery (i2m rules):** send the **zip** (the mesh) as an attachment, never
  the raw `.glb`. (2) **Never render the mesh** — no GLB → image/video
  conversion, no 3D-viewer screenshots (a third-party viewer *link* is fine).
- The source image is the only condition: `pi2m` takes **no prompt**, the
  character image is the condition (`--image` is its only required flag).
- Requires the Pixal3D / Trellis2 custom nodes and their checkpoint files
  (`trellis_2_int8_convrot.safetensors`, the Trellis2 VAEs, `moge_2_vitl_normal_fp16.safetensors`,
  `birefnet.safetensors`, `pixal3d_int8_convrot.safetensors`) installed on the
  ComfyUI server.
- This mode is the slow one by design: expect minutes, not ~20 s (see SKILL.md
  "i2m exception"). Run it in the background and deliver the zip on completion.

### hyi2m (Image → 3D Mesh, Hunyuan 3D v2.1 → GLB)

```bash
# Default: extract the main character first (Qwen-Image 2.1 i2i redraw on a
# transparent background, PNG), then generate the mesh.
python3 image_with_comfyui.py hyi2m --image /path/to/character.jpg

# Non-generative extraction: u2net human cutout (pixel-precise, no redraw)
python3 image_with_comfyui.py i2m --image /path/to/character.jpg --extract rembg

# Image is already a clean cutout — skip extraction entirely
python3 image_with_comfyui.py hyi2m --image /path/to/cutout.png --extract none

# Higher-detail / more-iterative generation
python3 image_with_comfyui.py hyi2m --image /path/to/character.jpg \
  --resolution 8192 --steps 35 --cfg 6.0 --seed 42

# Custom delivery scale (default: x3000; 1 = keep the normalized units)
python3 image_with_comfyui.py hyi2m --image /path/to/character.jpg --scale 1
```

- Output: a **GLB file** under `output_dir/meshes/` (prefix `hyi2m_<timestamp>`),
  **scaled in place by the delivery factor** (default ×3000 — the raw Hunyuan
  3D v2.1 mesh is at a normalized unit scale, character ≈ 2 units, no declared
  units; `--scale 1` keeps it unscaled) and **automatically packaged as
  `<same-stem>.zip`** — the result block prints both paths plus the delivery hints.
- **Delivery (i2m rules):** (1) send the extracted **character image** (the
  step-1 PNG; the script prints it as `CHARACTER IMAGE`) **as an image** — with
  `--extract none` there is no new image to send back. (2) send the **zip** (the
  scaled GLB) as an attachment, never the raw `.glb`. (3) **Never render the
  mesh** — no
  GLB → image/video conversion, no 3D-viewer screenshots (a third-party
  viewer *link* is fine).
- Requires `hunyuan_3d_v2.1.safetensors` in the server's `models/checkpoints/`
  and ComfyUI **≥ 0.37.0** (all Hunyuan 3D v2.1 nodes are core — no custom
  packages).
- This mode is the slow one by design: expect minutes, not ~20 s (see SKILL.md
  "i2m exception"). Run it in the background and deliver on completion.

### Health Check

```bash
python3 image_with_comfyui.py test
```

### Output Format (t2i / i2i)

ComfyUI's `SaveImage` node always writes PNG server-side. `--format jpg` converts the
**downloaded** image client-side (Pillow) to JPEG — alpha channels are composited
onto white, and conversion failures fall back to PNG automatically. `--format png`
passes the server's PNG bytes through **unchanged** (no conversion), so RGBA
transparency survives intact. Defaults come from `config.json` → `image.output_format`
(default `"jpg"`) and `image.jpg_quality` (default 89). Videos (wan2.2) are always
MP4 and are not affected.

**Routing rule:** the user's wording decides the format —

- "PNG image/file", "PNG format", "keep the alpha channel", or **"RGBA image with transparency"** → always `--format png`, and **deliver the PNG file directly without any JPG/JPEG conversion** (never flatten transparency onto a background).
- No format mentioned → use the config default (JPG).

---

## Timeout Reference

| Model | Timeout |
|---|---|
| T2I (Qwen-Image 2.1) | 600s |
| T2I (Z-Image) | 100s |
| SD3.5 Medium | 100s |
| I2I (Qwen 2.1) | 600s |
| I2I (Qwen Image Edit 2511) | 600s |
| I2V (MiniMax H3) | 2400s |
| T2V (MiniMax H3) | 2400s |
| I2V (Wan2.2) | 1000s |
| I2M (Hunyuan 3D v2.1) | 900s |
