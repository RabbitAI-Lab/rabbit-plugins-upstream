# Icon library

Every pictorial mark on a mono page is an **inline SVG**. Never emoji,
Unicode dingbat characters (text check marks, stars, arrows, bullets) or
icon fonts; the validator scans for them and fails.

## Sprite pattern

The engine defines each glyph once in a hidden sprite at the top of
`<body>` and references it everywhere:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <g id="i-arrow-right" fill="none" stroke="currentColor" stroke-width="2"
       stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>
    </g>
  </defs>
</svg>

<svg class="ic" viewBox="0 0 24 24"><use href="#i-arrow-right"/></svg>
```

- Lucide grammar: 24 viewBox, `stroke="currentColor"`, stroke-width 2,
  round caps and joins.
- Size through the `.ic` class or a parent rule; colour always inherits,
  so icons are ink on ground and white inside dark surfaces.
- Decorative icons sit inside `aria-hidden` wrappers; icon-only buttons
  carry an `aria-label`.

## Sprite ids used by this style

| Sprite id | Glyph | Where it appears |
| --- | --- | --- |
| `i-menu` / `i-x` | menu / x | mobile toggle (swapped by `aria-expanded`) |
| `i-arrow-right` | arrow-right | primary buttons, service rows, detail "Next" |
| `i-arrow-left` | arrow-left | detail "Previous" |
| `i-arrow-up-right` | arrow-up-right | poster hover badge, text links |
| `i-arrow-up` | arrow-up | footer back-to-top |
| `i-plus` | plus | accordion toggles (rotates 45 degrees when open) |
| `i-check` | check | includes lists, deliverables, "How I work", form confirmation |
| `i-send` | send | contact form submit |
| `i-mail`, `i-phone`, `i-map-pin`, `i-calendar` | mail, phone, map-pin, calendar | contact card rows |
| `i-pen-tool`, `i-printer`, `i-clock` | pen-tool, printer, clock | About principles |
| `i-layers`, `i-image`, `i-sparkles`, `i-palette`, `i-message` | spare glyphs | available for extra principles or services |

## Tool tiles are text, not icons

The toolkit shows two-letter abbreviations (`Rs`, `Vc`, `Ly`, `Mo`, `Ty`,
`Pr`) on dark rounded squares with a category label beneath. Never place
vendor logos or product marks here.

## AI marks

If a page genuinely describes an AI integration, LobeHub monochrome marks
may be used at the same size as the Lucide glyphs, always with a visible
text label. The demo does not need any.

## Adding a glyph

Copy the path data from the Lucide set into a new `<g id="i-name">` inside
the sprite with the same stroke attributes, then reference it with
`<use href="#i-name"/>`. Keep ids in the `i-` namespace so the validator
and the style checks can find them.
