> These named palettes configure presentation content during generation. The common editor remains black/white/gray and has no theme chooser; users can still edit individual content colors.

# Theme presets

Choose a complete named preset. Preserve the visual identity across all pages rather than accepting arbitrary user hex colors. The authored default is Mint Paper; use it for the initial example and delivered deck unless the user selects another preset.

| Preset | Paper | Ink | Accent | Use |
| --- | --- | --- | --- | --- |
| Mint Paper | `#f1f0ec` | `#171918` | `#3eaf9d` | Workshops, shared ideas, and project introductions. |
| Clay Paper | `#f1f0ec` | `#171918` | `#c96b50` | Practical craft projects and warmer community stories. |
| Cobalt Paper | `#f1f0ec` | `#171918` | `#426cbd` | Structured updates, goals, and clear milestone narratives. |
| Plum Paper | `#f1f0ec` | `#171918` | `#946a9e` | Creative proposals and reflective workshop material. |

The three theme tokens are `--paper`, `--ink`, and `--accent`. Keep neutral paper and dark ink constant. Accent pages use dark ink; light pages use accent display titles and dark body text. Keep tiny or long body copy dark rather than accent-colored. Photographs retain their original color.

Mint Paper keeps the authored colors. Other presets map `#3eaf9d` to their accent color when the deck is generated; saturated tints and shades follow that change. Keep authored colors in the stylesheet so preset remapping can find them. Do not bake accent colors into photography or SVG raster data.

Use two to four accent-filled pages per ten slides as a pacing guide, not a mandatory quota. On paper pages, an accent headline, a number, or one prop in an illustration can provide emphasis. Preserve empty paper around the message.

## Fonts

All four presets share the same embedded fonts: Bricolage Grotesque (display, weight 700, uppercase) and Figtree (body). They live as base64 `@font-face` data URIs in the style (`style-source.css`, carried in the kit's `contentCSS`), so the deck stays offline. Presets change only the accent color, never the fonts.
