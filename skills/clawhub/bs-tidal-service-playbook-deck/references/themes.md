> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Locked theme presets

Use one coordinated preset. The first is the authored light look; examples and delivery start there. Presets change the content accent colors while photographs retain their original colors.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Tidal Service Playbook | #122f46 | #def3fa | #244d67 | Default ice-blue and navy look. |
| Evergreen White | #122f46 | #def3fa | #2f6b62 | A coordinated alternative within the same visual system. |
| Plum White | #122f46 | #def3fa | #735581 | A coordinated alternative within the same visual system. |
| Slate White | #122f46 | #def3fa | #526476 | A coordinated alternative within the same visual system. |

## Type (all presets)

Every preset uses the same embedded font: **Manrope** (variable 200–800, Latin subset, ~25 KB, SIL OFL 1.1), set through `--font-display` and `--font-body` in the style kit's `contentCSS` as a base64 `@font-face`, so the deck stays offline. Headlines weight 500 with −0.035em tracking; body 400; labels 700 uppercase with +0.14em tracking. Presets change colour only, never the font. PowerPoint export substitutes a portable system font unless `--fonts keep` is passed.
