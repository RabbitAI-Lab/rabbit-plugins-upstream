# Icon library

All icons are inline SVG referenced from one hidden sprite:

```html
<svg class="i"><use href="#i-arrow-right"/></svg>   <!-- Lucide, stroke -->
<svg class="b"><use href="#b-shopify"/></svg>       <!-- brand mark, fill -->
```

Never emoji, Unicode arrows/ticks/stars or icon fonts — the validator fails
on them.

## Lucide (ISC)

24 viewBox, `fill="none"`, `stroke="currentColor"`, stroke-width 2, round
caps and joins. Size with CSS (14–17px in UI, 15px in the app sidebar).
Colour inherits: ink for neutral UI, mint inside `.icon-tile`, checks and
active states.

| Id | Where |
| --- | --- |
| `i-arrow-right` | ghost CTAs, "N articles" links, Register, Contact |
| `i-arrow-up-right` | popular-article rows |
| `i-download` | primary "Download" CTA (replaces any platform logo) |
| `i-check` | plan includes, compare table, release check lists |
| `i-plus` / `i-minus` | FAQ accordion |
| `i-search` | resources search |
| `i-play` | replay thumbnails |
| `i-rss` | changelog RSS link |
| `i-plug`, `i-trending-up`, `i-clock` | feature cards |
| `i-activity`, `i-box`, `i-plug`, `i-calendar-clock`, `i-shield-check`, `i-credit-card` | resource categories |
| `i-square-pen`, `i-bot`, `i-puzzle`, `i-calendar`, `i-radio` | app window sidebar |
| `i-twitter`, `i-github`, `i-linkedin`, `i-youtube`, `i-instagram`, `i-message-circle`, `i-mail` | footer socials |
| `i-menu` / `i-x` | mobile menu |
| `i-circle-check` | toast |

## Brand marks (Simple Icons, CC0)

Monochrome `fill="currentColor"` marks for the product's real integrations
only (commerce platforms, payments, CRM, mail, sheets, chat). Always beside
a visible name or inside an "integrations" grid; never recoloured to brand
colours, never decorative, never used as the product's own logo. For AI
model names in a model picker, use text chips; if a mark is wanted, use the
LobeHub monochrome set (`@lobehub/icons`) with the same rules.

The product logo is a simple original geometric mark drawn in SVG.
