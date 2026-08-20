---
name: "video-content-pipeline"
description: "Faceless video production for YouTube/TikTok/Shorts: Pixar-style images (free via Pollinations), parallax effects, voiceover (Edge TTS), composer — the full pipeline from script to finished video."
---

# Video Content Pipeline 🎬✨

Produktion af faceless videoer — fra script til færdig MP4, uden optagelser.

## Hvad du får

1. **Pixar-style billeder** — gratis via Pollinations.ai (Flux, ingen API-nøgle)
2. **2.5D parallax-effekt** — gør still-billeder levende (PIL/ffmpeg)
3. **Voiceover** — Edge TTS (flere sprog/stemmer) eller Piper (offline)
4. **Kompositor** — billede + tekst + lyd → færdig MP4 (ffmpeg)
5. **Batch-produktion** — hele mappen → alle videoer

## Hurtig start

```bash
# 1) Script → scener
python3 scripts/scene_plan.py script.txt scenes.json

# 2) Generér billeder (gratis)
python3 scripts/generate_images.py scenes.json images/

# 3) Voiceover
python3 scripts/voiceover.py scenes.json audio/

# 4) Saml video
python3 scripts/compositor.py scenes.json images/ audio/ final.mp4
```

## Filer

```
video-content-pipeline/
├── SKILL.md
└── scripts/
    ├── scene_plan.py      # split script → scener med prompts
    ├── generate_images.py # Pollinations (Flux, gratis)
    ├── voiceover.py       # Edge TTS / Piper
    └── compositor.py      # ffmpeg: billeder + tekst + lyd → MP4
```

## Specs (platform)

- YouTube: 1920×1080 · TikTok/Shorts: 1080×1920
- 30-60 sek pr. video · 3-5 sek pr. scene
- Voiceover: 150 ord/min

## Monetisering (niche-ideer)

- Islamisk indhold (FactSage-modellen)
- Historier/fakta · DIY · motiverende citater
- Kombinér med x402-API hvis videoerne bruger live-data
