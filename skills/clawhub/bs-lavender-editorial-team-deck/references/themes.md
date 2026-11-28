> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Theme presets

Apply one named preset. The authored palette uses light paper; individual dark section canvases are deliberate page treatments. Do not replace the deck with unrelated styling. Original raster illustrations and photographs keep their own colors.

| Preset | Ink | Paper | Accent | Use |
|---|---|---|---|---|
| Violet Editorial | #111111 | #e8e8e8 | #6518e9 | Authored style and default delivery |
| Cobalt Editorial | #111111 | #e8e8e8 | #2459e6 | A coordinated alternate accent |
| Forest Editorial | #111111 | #e8e8e8 | #26775b | A coordinated alternate accent |
| Brick Editorial | #111111 | #e8e8e8 | #a94339 | A coordinated alternate accent |

## Fonts (all presets)

Every preset uses the same embedded fonts, embedded as base64 `@font-face` in the style (`style-source.css`, carried in the kit's `contentCSS`; about 95 KB, OFL 1.1, see `third-party-notices.md`):

- `--font-display`: **Schibsted Grotesk** (variable 400–900) — uppercase headings at weight 600, labels, numbers with tabular figures.
- `--font-body`: **Inter** (variable 100–900) — body lines and ledes.

Do not switch the deck to Arial or a system stack, and do not add a third family. Presets change only the accent colour.
