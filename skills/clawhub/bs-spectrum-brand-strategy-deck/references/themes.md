> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Theme presets

Use these named sets only. The ink, paper and accent tokens are locked. The authored preset uses light paper as its neutral reference; dark layout treatments are intentional and retain light text.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Authored | #121613 | #f5f3e8 | #2eaaeb | Default reference grammar |
| Teal | #121613 | #f5f3e8 | #258b83 | Calm planning and teaching |
| Clay | #121613 | #f5f3e8 | #ca6d45 | Warm workshops and reviews |

The neutral canvas and dark panels are layout decisions. Keep sufficient contrast in every preset. Images retain their authored colors.

## Fonts (all presets)

Every preset uses the same embedded fonts: **Bricolage Grotesque** (variable, weight 600 for headings) as `--font-display` and **Figtree** (variable) as `--font-body`. Both are inlined as base64 `@font-face` data URIs (about 61 KB of woff2, about 82 KB as base64), so the deck stays offline. Do not swap in Arial or a system-only stack; PowerPoint export substitutes portable fonts unless `--fonts keep` is chosen.
