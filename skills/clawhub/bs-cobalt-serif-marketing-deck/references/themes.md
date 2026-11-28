> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Theme presets

Use these named sets only. The ink, paper and accent tokens are locked. The authored preset uses light paper as its neutral reference; dark layout treatments are intentional and retain light text.

| Preset | Ink | Paper | Accent | Use |
| --- | --- | --- | --- | --- |
| Authored | #141719 | #f4f2ec | #5362ff | Default reference grammar |
| Teal | #141719 | #f4f2ec | #258b83 | Calm planning and teaching |
| Clay | #141719 | #f4f2ec | #ca6d45 | Warm workshops and reviews |

The neutral canvas and dark panels are layout decisions. Keep sufficient contrast in every preset. Images retain their authored colors.

## Fonts (all presets)

Every preset uses the same embedded pair: **Newsreader** (variable serif, weight 500 for headlines, tabular lining figures for numbers) as `--font-display`, and **Geist** (variable sans) as `--font-body`. Both are embedded in the style CSS as base64 woff2 `@font-face` rules (about 87 KB together), so delivered decks stay offline. Do not swap in Arial, Georgia or system fonts; keep the `--font-display` / `--font-body` variables so the editor and export keep working. Licences are in `third-party-notices.md`.
