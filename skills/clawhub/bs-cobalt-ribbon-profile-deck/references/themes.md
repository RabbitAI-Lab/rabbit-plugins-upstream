> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Locked theme presets

Use one coordinated preset. The first is the authored light look; examples and delivery start there. Switching presets changes only the content colors; photographs retain their original colors.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Cobalt Ribbon Profile | #182e42 | #ffffff | #093e81 | Default authored cobalt look. |
| Evergreen White | #182e42 | #ffffff | #2f6b62 | A coordinated alternative within the same visual system. |
| Plum White | #182e42 | #ffffff | #735581 | A coordinated alternative within the same visual system. |
| Slate White | #182e42 | #ffffff | #526476 | A coordinated alternative within the same visual system. |

## Fonts (all presets)

Every preset uses the same embedded pair, so switching themes never changes type:

- Display: **Schibsted Grotesk** (variable 400-900; headlines and big numbers at 600, tracking -0.03em, tabular figures).
- Body: **Instrument Sans** (variable 400-700; body text at least 17px, labels 600 uppercase +0.12em).

Both are Latin-subset woff2 files embedded as base64 `@font-face` in the style CSS (about 103 KB together), so the deck stays offline. Keep `--font-display` and `--font-body` pointing at them with Arial only as the last fallback. An exported PPTX shows them only where they are installed; otherwise PowerPoint substitutes a system font.
