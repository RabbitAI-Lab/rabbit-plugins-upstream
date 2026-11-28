# Tracklane style guide

Warm, approachable and precise. A sand canvas with mint bands, near-black ink,
calm tracking-tight headlines and the product itself as the main visual. The
warmth comes from the palette and the photography; the precision comes from
type, hairlines and believable product UI.

## Tokens (`:root`, light)

| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `#F5F2EC` | Page sand ground |
| `--bg-2` | `#EEEAE2` | Deeper sand band (evaluate, customers) |
| `--mint` | `#E2ECE5` | Mint band (cycles, CTA, highlights) |
| `--mint-2` | `#D2E3D8` | CTA gradient end |
| `--surface` | `#FFFFFF` | Cards, app window, inputs |
| `--surface-2` | `#FBFAF7` | App sidebar |
| `--surface-3` | `#F6F4EF` | App canvas, wells |
| `--ink` | `#16181B` | Headlines, primary text |
| `--ink-2` | `#34383D` | Body text on surfaces |
| `--muted` | `#5E6369` | Secondary text (5.1:1 on sand) |
| `--sub-ink` | `#6B6963` | Warm grey of the two-tone hero subtitle |
| `--faint` | `#8C9095` | Decorative only, never body copy |
| `--line` / `--line-2` | `rgba(40,34,24,.10/.16)` | Hairlines |
| `--accent` | `#1E7A57` | Lane green: the single accent |
| `--accent-ink` | `#13583F` | Accent text on light fills |
| `--accent-soft` | `#DCEBE2` | Accent tint fills |
| `--btn` / `--btn-ink` | `#16181B` / `#F8F6F1` | Primary buttons |

Product-only semantic colors (status, labels, roadmap bars): `--st-progress`
amber, `--st-review` blue, `--st-done` green, `--st-teal` (`#2B7F8C`, the Infra
label and the Mobile team), `--st-red`. They never appear in marketing chrome.

No purple anywhere: no violet or indigo (hue 235 to 300) backgrounds, washes,
glows, gradients, headline words, label colors or team colors, in either theme.

Dark theme (`[data-theme="dark"]`) redefines every token: ground `#121311`,
mint band `#131B17`, surfaces `#1A1B19`, ink `#EEECE7`, accent `#55C495`, light
buttons on dark. Persist the choice in storage (guarded) and keep both themes
at AA contrast.

## Typography

Fonts: Inter Tight (variable), Inter (variable) and Geist Mono (variable). The
template loads them from the fontsource CDN. In a framework project install
`@fontsource-variable/inter-tight`, `@fontsource-variable/inter` and
`@fontsource-variable/geist-mono` or use `next/font/google` (`Inter_Tight`,
`Inter`, `Geist_Mono`); the single-file build inlines the three woff2 files as
data URIs (`scripts/inline-assets.mjs`), and a deployed static site serves them
from `fonts/` beside the page.

- Display: **Inter Tight** variable, weight 620 (hero headline 650).
- Text and UI: **Inter** variable, 400 to 600.
- Mono: **Geist Mono** for issue IDs, keys, code, dates in tables, eyebrow pill text.

| Role | Size | Line height | Tracking |
| --- | --- | --- | --- |
| Hero h1 (650) | `clamp(2rem, 4.4vw, 3.375rem)`: 54px desktop, 32px phone | 1.05 | -0.021em |
| Hero subtitle (500, `--sub-ink`) | `clamp(1.375rem, 2.9vw, 2.125rem)`: 34px / 22px | 1.2 | -0.014em |
| H2 | `clamp(2rem, 1.3rem + 2.2vw, 3rem)`: max 48px | 1.06 | -0.03em |
| FAQ aside h2 | `clamp(1.75rem, 1.4rem + 1vw, 2.0625rem)`: max 33px | 1.06 | -0.025em |
| Page h1 (routes) | `clamp(2.25rem, 1.5rem + 2.4vw, 3.375rem)`: max 54px | 1.04 | -0.032em |
| H3 / card title | `clamp(1.25rem, 1.1rem + .4vw, 1.5rem)` | 1.2 | -0.022em |
| Lead | `clamp(1.0625rem, 1rem + .3vw, 1.25rem)` | 1.55 | 0 |
| Body | 16px | 1.6 | 0 |
| Small / meta | 13 to 14.5px | 1.5 | 0 |
| Metric numbers | `clamp(2.75rem, 2rem + 2.2vw, 3.5rem)` (small cards max 48px) | 1 | -0.04em, tabular |

Scale ceiling: nothing on the page is set larger than the 54px hero headline
(price figures stay at 56px inside plan cards). Do not enlarge the hero.

Rules: `text-wrap: balance` on headings, 58 to 66ch measure for leads and
prose, tabular numerals for prices, metrics and tables. The two-tone heading
(ink sentence, then a muted sentence in the same h2) is a signature; use it at
most twice per page. Tile titles use the same move at body size: a bold
lead-in followed by muted text.

## Layout

- Container 1240px plus `clamp(20px, 4vw, 40px)` gutters; section padding
  `clamp(88px, 10vw, 140px)`.
- Hero: see "Hero anatomy" below. Plain sand ground, no gradient or wash; the
  logo marquee sits on the same sand directly under it.
- Section families used on the home page (keep at least eight): split hero with
  bleeding product, logo marquee, asymmetric metric cards (one tall + two
  stacked), 12-column bento (7/5 then 5/4/3), vertical tabs + panel on the mint
  band, copy + terminal split, three-step evaluation track, sticky heading +
  2x3 fact grid, portrait quote carousel + story card, pricing cards + strip,
  sticky aside + accordion, CTA card with inline form.
- Mobile is designed, not squashed: single columns, tabs collapse to titles,
  bento tiles stack, the comparison table switches to a one-plan picker.

## Hero anatomy (fixed composition)

The hero is a quiet split layout with exactly these elements, in this order.
Keep the composition, scale and vertical position; refine only polish.

1. Left column (`1fr`, copy max 640px), top-aligned with the frame:
   - h1 "Plan less, ship more" on one line, 54px / 650, no period. Its top sits
     about 63px under the 64px header (127px from the page top at 1440x900,
     122px at 390x844).
   - Subtitle 14px below: one muted 34px sentence, max 620px, three lines on
     desktop.
   - Feature notes 36px below: a 2x2 grid (max 560px, 20px gaps) of icon +
     15px title + 13.5px muted line (Custom issue flows, Cycle milestones,
     Cross-team projects, Progress insights). Under 520px the icon sits above
     the title.
   - Buttons 32px below, 40px tall: "Start free" (primary) and a secondary
     button that carries the release note ("Tracklane 2.0 ships cycle
     automation" with an arrow). No separate announcement pill.
   - View indicator 28px below, centered under the copy: "1 of 3 - Board"
     (the separator is a drawn 11px rule, not a dash character) over three
     26 x 3px bars. The bars are the real tablist ("Product views") that drives
     the product window; the active bar fills as the auto-advance runs.
2. Right column (`0.74fr`): the product frame, aspect 573 / 386 (573 x 386px at
   1440), 12px radius, hairline + one soft warm shadow, extending 65px past the
   container edge. Inside, the product window is laid out at 900 x 606px (620 x
   418px without the sidebar on phones) and scaled to the frame width
   (`--s`, set from script), so it reads like a crisp product screenshot. The
   in-app Board / Cycle / Roadmap switch mirrors the indicator and is not
   interactive.
3. Under 980px the frame moves below the indicator (44px gap) and bleeds off
   the right edge, rounded on the left only.

Do not add stat strips, floating cards, badges, extra paragraphs, a larger
type size or a background wash to the hero.

## Radius, borders, shadows

- Radius scale: 6 (chips, kbd), 10 to 13 (buttons, inputs), 14 (inner panels),
  20 (tabs, small cards), 28 (section cards, bento tiles, plans), 36 (story
  card, CTA). Buttons are rounded rectangles, never pills; chips and badges are
  pills.
- Borders are hairlines drawn with `box-shadow: 0 0 0 1px var(--line)` so they
  never shift layout.
- Shadows are warm-tinted and layered: `--sh-1` (hairline + 1px), `--sh-2`
  (raised card), `--sh-3` (app window, popular plan, code panel), `--sh-pop`
  (menus, toasts). No pure black shadows on light ground.

## Component anatomy

- **Header**: 64px, transparent at top, sand blur backdrop + hairline after
  scroll. Brand mark (ink rounded square with three lanes and a green dot) +
  wordmark. Nav: Product (dropdown with six items and a changelog footer),
  Customers, Pricing, Changelog, Company. Actions: theme toggle, Sign in (ghost),
  Start free (primary). Active state is a 1.5px accent underline.
- **Product window**: sidebar (workspace switcher, search with shortcut,
  inbox/views, team groups, current user), top bar (breadcrumb, cycle date pill,
  static view switch mirroring the hero indicator, avatar stack, filter), canvas in
  `--surface-3` with white cards. Issue card: mono ID + avatar, two-line title,
  priority glyph, label chip with color dot, estimate.
- **Metric card**: icon + label, a large (max 56px) number with a smaller unit, one-line
  definition, a small visual (bars, sparkline, cycle dots). Sources go in one
  footnote under the grid.
- **Bento tile**: bold lead-in title, then a working UI panel aligned to the
  bottom. At least two tiles carry a tint (mint, sand) and one is dark ink.
- **Cycles tab**: icon, title, description; active tab is a white card with a
  progress bar along its bottom edge.
- **Plan card**: name (+ "Most popular" badge), description, rolling price with
  unit text, full-width CTA, note, feature list with check icons. The popular
  plan has a mint gradient and a 1.5px ink ring.
- **Forms**: label above input, 46px inputs, 11px radius, inline error with
  alert icon under the field, loading spinner inside the button, success panel
  with icon, heading, echo of the email, and a reset action.

## Do

- Show the product working: real IDs, dates, owners and counts that add up.
- Keep one accent; let sand, mint and ink do the rest.
- Put trust in specifics: audit log rows, data regions, retention, response times.
- Keep every link and button functional.

## Don't

- No generated screenshots or laptop photos for the product.
- No real company logos; integrations by category only.
- No purple, violet or indigo in any role; no gradients toward blue-violet, neon
  glows, glassmorphism or grain.
- No oversized display type: headings stay at or below the scale above.
- No eyebrow labels above every section, no em dashes, no emoji.
- No section inversions to dark in the light theme (the single dark bento tile
  and the code panel are components, not sections).
