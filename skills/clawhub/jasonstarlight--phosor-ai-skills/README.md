# Phosor AI — Agent Skill

**Skill version 1.3.8** · API v1.2.4 · updated 2026-11-04

Two version numbers, on purpose: the skill version tracks this package
(commands, docs, the bundled client), the API version tracks the gateway
contract. A skill release that only rewords docs or fixes the client does not
move the API version, and a gateway change does not force a skill release.

Verify what you installed: `python3 scripts/phosor_client.py --version`

## Quick Start

```bash
export PHOSOR_API_KEY="your-key"

# MiniMax H3 Standard — Text-to-Video
python3 scripts/phosor_client.py submit "A cat walking on a beach" \
  --model minimax/h3/text-to-video --resolution-tier 480p --aspect 16:9 --duration 5

# MiniMax H3 Turbo — same input shape, faster variant
python3 scripts/phosor_client.py submit "A cat walking on a beach" \
  --model minimax/h3/text-to-video/turbo --resolution-tier 480p --aspect 16:9 --duration 5

# MiniMax H3 Image-to-Video (two-step: upload then submit)
python3 scripts/phosor_client.py upload-image photo.jpg
python3 scripts/phosor_client.py submit "The scene comes alive" \
  --model minimax/h3/image-to-video --image-url "images/img-xxx.jpg" \
  --resolution-tier 480p --aspect 16:9 --duration 5

# Choose Turbo for the same image-to-video mode
python3 scripts/phosor_client.py submit "The scene comes alive" \
  --model minimax/h3/image-to-video/turbo --image-url "images/img-xxx.jpg" \
  --resolution-tier 480p --aspect 16:9 --duration 5

# Check status / get result
python3 scripts/phosor_client.py status <request_id>
python3 scripts/phosor_client.py result <request_id>

# LoRA Upload (custom pre-trained)
python3 scripts/phosor_client.py upload-lora high_noise.safetensors low_noise.safetensors

python3 scripts/phosor_client.py save-lora <lora_id>

# Image Studio: AI product photography (secondary product surface, same API key)
python3 scripts/phosor_client.py upload-image product.jpg
python3 scripts/phosor_client.py studio-suite --image-url "<s3_url from upload>" \
  --layout-types "white_background,lifestyle_scene" --count-per-type 2
python3 scripts/phosor_client.py studio-status <job_id>
```

See [SKILL.md](SKILL.md#image-studio-product--model-photography) for the full Image Studio quick start (clothing/model suite, one-off edits like remove-bg/inpaint/translate).

For reference-to-video, use `minimax/h3/reference-to-video` or
`minimax/h3/reference-to-video/turbo` with one or more reference image/video inputs;
the full H3 mode table and limits are in [SKILL.md](SKILL.md#h3-model-map).

## Requirements

- Python 3.7+ (stdlib only, no pip install needed)
- `PHOSOR_API_KEY` environment variable

## Commands

Run `python3 scripts/phosor_client.py --help` for all 31 commands (23 video/LoRA + 8 Image Studio).

## Links

- [Phosor AI](https://phosor.ai)
- [API Documentation](https://docs.phosor.ai)


## Price and model coverage (1.3.8 preparation)

The package includes GPT Image 2 pricing and LTX 2.3 discovery/submit guidance.
See `SKILL.md` and `references/api.md` for units and tier qualifications.
Model API, Image Studio and Drama have separate availability and billing contracts.
A configured rate is not a promise that the corresponding model is open.
Version 1.3.8 is prepared locally and has not been published to a registry.
