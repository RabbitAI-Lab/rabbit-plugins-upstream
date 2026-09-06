# Phosor AI — Agent Skill

**Skill version 1.1.0** · API v1.0.0 · updated 2026-09-03

Two version numbers, on purpose: the skill version tracks this package
(commands, docs, the bundled client), the API version tracks the gateway
contract. A skill release that only rewords docs or fixes the client does not
move the API version, and a gateway change does not force a skill release.

Verify what you installed: `python3 scripts/phosor_client.py --version`

## Quick Start

```bash
export PHOSOR_API_KEY="your-key"

# Text-to-Video
python3 scripts/phosor_client.py submit "A cat walking on a beach" --width 854 --height 480

# Image-to-Video (two-step: upload then submit)
python3 scripts/phosor_client.py upload-image photo.jpg
python3 scripts/phosor_client.py submit "The scene comes alive" --image-url "images/img-xxx.jpg"

# Check status / get result
python3 scripts/phosor_client.py status <request_id>
python3 scripts/phosor_client.py result <request_id>

# LoRA Upload (custom pre-trained)
python3 scripts/phosor_client.py upload-lora high_noise.safetensors low_noise.safetensors

python3 scripts/phosor_client.py save-lora <lora_id>

# Image Studio: AI product photography (separate product surface, same API key)
python3 scripts/phosor_client.py upload-image product.jpg
python3 scripts/phosor_client.py studio-suite --image-url "<s3_url from upload>" \
  --layout-types "white_background,lifestyle_scene" --count-per-type 2
python3 scripts/phosor_client.py studio-status <job_id>
```

See [SKILL.md](SKILL.md#image-studio-product--model-photography) for the full Image Studio quick start (clothing/model suite, one-off edits like remove-bg/inpaint/translate).

## Requirements

- Python 3.7+ (stdlib only, no pip install needed)
- `PHOSOR_API_KEY` environment variable

## Commands

Run `python3 scripts/phosor_client.py --help` for all 31 commands (23 video/LoRA + 8 Image Studio).

## Links

- [Phosor AI](https://phosor.ai)
- [API Documentation](https://docs.phosor.ai)
