> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Locked theme presets

Use one coordinated preset. The first is the authored light look; examples and delivery start there. Presets change the content accent colors while photographs retain their original colors.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Steel Curve Profile | #192c38 | #ffffff | #456b83 | Default authored look. |
| Evergreen White | #192c38 | #ffffff | #2f6b62 | A coordinated alternative within the same visual system. |
| Plum White | #192c38 | #ffffff | #735581 | A coordinated alternative within the same visual system. |
| Slate White | #192c38 | #ffffff | #526476 | A coordinated alternative within the same visual system. |

## Fonts (all presets)

Every preset uses the same two embedded fonts, inlined as base64 woff2 in the style kit's `contentCSS` so the deck stays offline (about 60 KB together): **Manrope** (variable 200–800) for headlines and numbers via `--font-display`, and **Hanken Grotesk** (variable 100–900) for body text via `--font-body`. Presets change colour only; do not switch the deck back to Arial or a system stack.
