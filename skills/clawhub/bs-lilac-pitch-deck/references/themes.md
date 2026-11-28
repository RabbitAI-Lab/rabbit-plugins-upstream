> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Theme presets

Apply one named preset. The authored palette uses light paper; individual dark section canvases are deliberate page treatments. Do not replace the deck with unrelated styling. Original raster illustrations and photographs keep their own colors.

| Preset | Ink | Paper | Accent | Use |
|---|---|---|---|---|
| Lilac Glass | #140b2d | #f2eff6 | #7050dc | Authored style and default delivery |
| Ocean Glass | #140b2d | #f2eff6 | #2468ab | A coordinated alternate accent |
| Rose Glass | #140b2d | #f2eff6 | #bd4c79 | A coordinated alternate accent |
| Moss Glass | #140b2d | #f2eff6 | #558260 | A coordinated alternate accent |

## Fonts (all presets)

Every preset uses the same embedded type: **Geist** for headlines and body (weight 500 headlines, tracking −0.035em) and **Geist Mono** for labels, axes and small numbers. Both are variable Latin woff2 files embedded as base64 `@font-face` data URIs (about 70 KB together) so the deck stays offline. Do not switch back to Arial; if a font must change, keep it to two families and update `--font-display` / `--font-body` / `--font-mono` and `third-party-notices.md`.
