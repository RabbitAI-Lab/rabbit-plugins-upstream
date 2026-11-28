# Style guide — Mint Noir

## Palette (CSS custom properties)

| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `#07090a` | page ground |
| `--bg-2` | `#0a0e0f` | app sidebar, inset panels |
| `--surface` | `#0e1213` | app window body |
| `--ink` | `#edf1f0` | primary text |
| `--ink-85/80/72/68/65/62/58/50/45/40/38` | ink at that opacity | body, nav, captions, labels |
| `--ink-06` | ink at 6 % | footer wordmark |
| `--mint` | `#6ee7c8` | the only accent |
| `--mint-06/10/22` | mint at 6/10/22 % | tinted fills, tag fills, accent borders |
| `--red` | `#ff7a7a` | negative deltas, LIVE and FIX tags |
| `--amber` | `#f5b867` | challenge / performance / advanced tags |
| `--sky` | `#7cc4f5` | intermediate / improved tags |
| `--line` … `--line-4` | white at 6 / 8 / 10 / 14 % | hairline borders |
| `--fill` … `--fill-3` | white at 3 / 4 / 7 % | card and control fills |

Never introduce purple or violet. Never add a second saturated brand colour.

## Type

- Sans: **Geist** (400 body, 500 buttons/labels, 600 headings).
- Mono: **Geist Mono** 500 for eyebrows (11px, +8 % tracking, uppercase),
  tags (9.5–11px), numbers in tables, dates and deltas.
- Serif accent: **Instrument Serif** italic 400, mint, one word or short
  phrase per headline, sized about 1.16× the surrounding headline, tracking
  -1 %.
- Scale: hero 80px / line-height 1.0 / tracking -3.2px; interior hero 64px;
  section heading 40px / -3 %; card titles 15–20px / 600; body 14–16px;
  lede 18px at `--ink-58`; captions 12–13px at `--ink-50`.
- Display headings use `background: linear-gradient(#fff, #a3b2b0)` clipped
  to text; the serif word overrides the fill with solid mint.

## Spacing and shape

- Content width 1200px (`.wrap`), 24px gutters (16px under 560px).
- Section padding 120px top/bottom (80px under 900px).
- Radius: buttons and chips 999px; tags 5px; small controls 8–10px; stat
  tiles 12px; cards 16px; app window and feature cards 20–24px.
- Nav 69px high, sticky, 72 % ground with 14px backdrop blur and a 6 %
  bottom hairline; active link gets a 1px mint underline on the nav edge.

## Light and depth

- Glows: radial mint at 14–18 % behind interior heroes, behind the hero app
  window (`0 0 120px rgba(110,231,200,.18)`), on the featured plan and the
  closing CTA card. One glow per viewport at most.
- The hero app window fades into the ground with a 240px gradient overlay.
- Cards lift 2px and tint their border mint on hover.

## Motion

- Page switch: 450ms fade-up. Sections: `.reveal` fade-up on scroll.
- Numbers count up once when revealed; sparklines draw in with
  `stroke-dashoffset`. Live elements (countdown, status dots) tick or pulse.
- All motion is disabled under `prefers-reduced-motion`.

## Voice

Calm and specific. Short sentences, real-looking numbers (`$48.2k`, `-35%`,
`2.1×`), operator language ("You approve; it executes."). No exclamation
marks, no superlatives.
