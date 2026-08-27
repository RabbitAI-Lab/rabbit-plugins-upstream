# Story and shot design

## Episode architecture

For a 45–90 second serial motion comic, use:

1. **0–3 s — Hook:** an impossible question, alarming image, or contradiction.
2. **3–20 s — Situation:** identify the character, need, and immediate constraint.
3. **20–40 s — Rule or price:** reveal what the character must risk.
4. **40–65 s — Consequence:** show the choice changing reality.
5. **Final 10–20 s — Double turn:** resolve the episode's emotional question, then reveal a larger series mystery.

The hook must be understandable without prior episodes. The final beat must add information rather than merely saying “未完待续”.

## Shot selection

Create a new keyframe only when at least one changes:

- story location;
- speaker or point of view;
- emotional state;
- decisive prop state;
- revealed information;
- time.

Do not create a new image because a fixed number of seconds elapsed.

Typical 60–80 second episode:

- 8–10 keyframes;
- 4–9 seconds per keyframe;
- 1–3 characters per frame;
- no more than two main locations.

## Writing constraints

- Write dialogue for speech, not prose.
- Put exposition in short narration sentences.
- Give different characters different sentence rhythm.
- Avoid explaining what the frame already proves.
- Keep character names and key terms pronunciation-friendly.
- Reserve silence after a reversal; do not fill every second with speech.

## Shot table fields

Record:

| Field | Purpose |
|---|---|
| `shot` | Stable shot number |
| `story beat` | What changes |
| `visual` | Subject, action, framing, light |
| `spoken lines` | IDs from TTS manifest |
| `motion` | hold, push, pull, pan-left, pan-right |
| `SFX` | Event and intended timestamp |
| `caption safe area` | Top, lower third, or custom |

Write the complete spoken script and shot table before starting image generation.

