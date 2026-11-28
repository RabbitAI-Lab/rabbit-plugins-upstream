# Icon library

Every pictorial mark on a green pharmacy page is an **inline SVG**. Never
emoji, Unicode dingbats (text check marks, stars, arrows, bullets) or icon
fonts. The validator greps for them and fails the build.

## Sprite pattern

The engine defines every glyph once in a hidden sprite at the top of
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

<svg class="ic" viewBox="0 0 24 24" width="16" height="16"><use href="#i-arrow-right"/></svg>
```

- Lucide grammar: 24 viewBox, `stroke="currentColor"`, stroke-width 2
  (2.4 for the tiny plus, minus and check), round caps and joins.
- Colour always inherits; size via `width`/`height`.
- Decorative icons sit inside `aria-hidden` wrappers; icon-only buttons and
  links carry an `aria-label`.
- The star is the one filled glyph (`fill="currentColor"`) so ratings read at
  12px.

## Sprite ids used by this style

| Sprite id | Glyph | Where it appears |
| --- | --- | --- |
| `i-cross` | rounded medical cross | brand mark, footer band, health card |
| `i-arrow-right` | arrow-right | every CTA, "See all" links, promo tiles |
| `i-chevron-right` / `i-chevron-down` | chevrons | breadcrumbs; FAQ toggles |
| `i-menu` / `i-x` | menu / x | mobile hamburger |
| `i-plus` / `i-minus` | plus / minus | add-to-cart pills, quantity steppers |
| `i-check` | check | benefit rows, side-card lists, form confirmations, toast |
| `i-star` | star (filled) | ratings, testimonial rows |
| `i-search` | search | header search, phone mockup |
| `i-map-pin` | map-pin | delivery location, contact card, app feature |
| `i-shopping-bag` | shopping-bag | cart button, add-to-cart on detail pages |
| `i-user` | user | sign in |
| `i-tag` | tag | Offers button, Deals filter chip |
| `i-stethoscope` | stethoscope | pharmacy services pill, phone tiles |
| `i-file-text` / `i-file-check` | file icons | upload-prescription card, service card, app feature |
| `i-upload` | upload | prescription upload zone and icon button |
| `i-truck` / `i-clock` / `i-rotate-ccw` | delivery facts | hero badge, product perks, delivery chip, opening hours |
| `i-shield-check` / `i-badge-check` | verified marks | hero badge, brand line, about values |
| `i-heart-pulse` / `i-pill` / `i-leaf` | health glyphs | phone tiles, feature-banner facts, about values |
| `i-video` / `i-message-circle` / `i-phone` / `i-mail` | contact formats | consultation format pills, contact cards, footer social |
| `i-smartphone` / `i-bell` / `i-calendar` / `i-credit-card` / `i-sparkles` | UI marks | store chips, phone status bar, membership chip |
| `i-trash` | trash | remove line in cart |
| `i-globe` / `i-at-sign` / `i-rss` | generic social | footer social row |

## Adding an icon

Copy the path data from the Lucide set, wrap it in a `<g id="i-name">` with
the same attributes as its neighbours, and reference it with `<use>`. Keep
the id prefix `i-`.

## Vendor marks

Use LobeHub-style monochrome marks only for real AI-integration contexts
with a visible text label. This storefront has none; app-store chips are
plain text ("Download for iOS / Android") with the smartphone glyph, and
brand tiles are two-letter monograms of fictional brands.
