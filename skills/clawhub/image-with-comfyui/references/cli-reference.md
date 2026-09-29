# CLI Usage Reference (image-with-comfyui)

Full command examples for every subcommand. The SKILL.md procedure only lists the
core rule; open this file for the exact flags.

> **⚠️ The prompt is MANDATORY and must be passed via `--prompt` — never as a positional argument.**
>
> Every subcommand (`t2i`, `i2i`, `wan2.2`) reads the prompt from `--prompt "..."`. Passing the prompt as a bare positional word fails immediately with exit code 2:
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

### I2V (Image → Video)

```bash
python3 image_with_comfyui.py wan2.2 \
  --prompt "the person walks forward and smiles" \
  --image /path/to/source.jpg \
  --length 81 --steps 4
```

### Health Check

```bash
python3 image_with_comfyui.py test
```

### Output Format (t2i / i2i)

ComfyUI's `SaveImage` node always writes PNG server-side. `--format jpg` converts the
**downloaded** image client-side (Pillow) to JPEG — alpha channels are composited
onto white, and conversion failures fall back to PNG automatically. Defaults come
from `config.json` → `image.output_format` (default `"jpg"`) and `image.jpg_quality` (default 89).
Videos (wan2.2) are always MP4 and are not affected.

---

## Timeout Reference

| Model | Timeout |
|---|---|
| T2I (Qwen-Image 2.1) | 600s |
| T2I (Z-Image) | 100s |
| SD3.5 Medium | 100s |
| I2I (Qwen 2.1) | 600s |
| I2I (Qwen Image Edit 2511) | 600s |
| I2V (Wan2.2) | 1000s |
