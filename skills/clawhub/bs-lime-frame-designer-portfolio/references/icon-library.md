# Icon library

Every pictorial mark is an **inline SVG**. Never emoji, Unicode dingbats
(text check marks, stars, arrows, bullets) or icon fonts; the validator
greps for them and fails the build.

## Sprite pattern

The sprite is defined once at the top of `<body>` and referenced
everywhere:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <g id="i-arrow-right" fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></g>
</defs></svg>

<svg class="ic" viewBox="0 0 24 24"><use href="#i-arrow-right"/></svg>
```

- Lucide grammar: 24 viewBox, `stroke="currentColor"`, stroke-width 2
  (2.5 for the small wordmark glyphs), round caps and joins.
- Size with `width`/`height` or the `.ic` class; colour always inherits.
- Decorative icons sit inside `aria-hidden` wrappers; icon-only links and
  buttons carry an `aria-label`.

## Sprite ids used by this style

| Sprite id | Glyph | Where it appears |
| --- | --- | --- |
| `i-arrow-right` | arrow-right | nav CTA disc, "Learn more" links, next-project disc |
| `i-arrow-up-right` | arrow-up-right | primary pill discs, work card discs, section links |
| `i-arrow-left` | arrow-left | the not-found "Back to home" disc |
| `i-menu` / `i-x` | menu / x | mobile hamburger |
| `i-chevron-right` | chevron-right | breadcrumb separators |
| `i-plus` | plus | accordion disc (rotates to a cross when open) |
| `i-check` | check | lime check discs in includes and deliverables, form confirmation |
| `i-phone`, `i-mail`, `i-map-pin`, `i-clock` | contact | collaboration split, FAQ aside, contact card |
| `i-globe`, `i-at-sign`, `i-message-circle`, `i-rss` | generic social | portrait social column, footer bar |
| `i-star` | star (stroked, lime fill) | testimonial ratings |
| `i-play` | play (filled) | stats band thumbnail disc |
| `i-pen-tool`, `i-layout`, `i-smartphone`, `i-rocket` | services | the four service icon discs |
| `i-circle`, `i-square`, `i-triangle`, `i-hexagon` | outline shapes | wordmark glyphs and the brand disc |
| `i-quote`, `i-sparkles`, `i-shapes`, `i-zap` | spare | available for new sections |

## Rules

- UI icons are Lucide-grammar strokes only. If you need a glyph that is
  not in the sprite, add it to `<defs>` in the same grammar rather than
  inlining a full SVG in the page body.
- Brand or tool marks: use LobeHub monochrome marks only for a real AI
  integration and only with a visible text label beside the mark. Never
  use logos of design tools, social networks or clients; the wordmark
  marquee is text plus an outline shape.
- Social buttons are generic (globe, at-sign, message, feed) and point at
  the contact page, never at external networks.
