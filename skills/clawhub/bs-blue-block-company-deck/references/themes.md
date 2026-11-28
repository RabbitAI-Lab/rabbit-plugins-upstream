> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Locked theme presets

Use one coordinated preset. The first is the authored light look; examples and delivery start there. The style kit maps accent colors while photographs retain their original colors.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Blue Block Company | #222a30 | #ffffff | #204f82 | Default authored look. |
| Evergreen White | #222a30 | #ffffff | #2f6b62 | A coordinated alternative within the same visual system. |
| Plum White | #222a30 | #ffffff | #735581 | A coordinated alternative within the same visual system. |
| Slate White | #222a30 | #ffffff | #526476 | A coordinated alternative within the same visual system. |

## Fonts (all presets)

Every preset uses the same two embedded families, stored as base64 `@font-face` data URIs inside the style kit's `contentCSS` so the deck works offline (about 103 KB of font data):

- `--font-display`: **Newsreader** (variable, weight 500 for headlines and big numbers, tabular lining figures).
- `--font-body`: **Inter Tight** (variable, 400 body, 500–600 labels and names).

Change fonts only by swapping both the `@font-face` data and these two tokens; keep the total under 250 KB and add the licence to `third-party-notices.md`.
