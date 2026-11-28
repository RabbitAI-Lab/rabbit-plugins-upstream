# Lime-frame style guide

The page must feel like a white sheet resting on a lime desk: one bright
frame, one calm sheet, one confident person in the middle. Colour is
rationed; confidence comes from scale and spacing.

## Tokens (locked)

| Token | Value | Job |
| --- | --- | --- |
| `--lime` | `#d4f56a` | the page frame, primary pills, icon discs, CTA band |
| `--lime-deep` | `#b9e04a` | nav underline, hover tint, the 404 number |
| `--lime-soft` | `#eefbc8` | tinted chips, featured testimonial, result tiles |
| `--card` | `#ffffff` | the sheet, cards |
| `--panel` | `#f3f3f1` | portrait card, value tiles, form fields |
| `--panel-deep` | `#e9e9e6` | image fallbacks |
| `--ink` | `#141414` | headings, body, dark buttons |
| `--muted` | `#5f5f5f` | secondary text |
| `--soft` | `#9a9a9a` | meta lines, the grey half of headings |
| `--line` | `#e6e6e2` | hairlines, card borders |
| `--dark` / `--dark-2` | `#232323` / `#2f2f2f` | stats band, footer, hover of dark buttons |
| `--on-dark` / `--on-dark-muted` | `#f5f5f2` / `#a8a8a3` | text on dark surfaces |
| `--r-sheet` / `--r-card` / `--r-tile` | `30px` / `22px` / `16px` | sheet, cards, inner tiles |
| `--frame` | `18px` (10px on phones) | the visible lime border |

Rules:

- **The frame is the brand.** Body background is lime; the sheet is white
  with `--r-sheet` corners and clips its children. Never paint lime
  panels inside the sheet except the CTA band and small chips.
- **Grey does the talking.** Every long heading has a second fragment in
  `--soft` (`<span class="grey">`), and the role reads "Digital" in ink
  over "Designer" in grey. This is the signature typographic move.
- **Rounded everywhere.** Cards 22px, tiles 16px, buttons and chips are
  full pills, avatars and icon buttons are circles. No square corners.
- **Dark is warm-black.** Stats band and footer use `--dark`, rounded,
  with `--on-dark-muted` for labels and 1px `#3e3e3e` dividers.

## Type

- Single face: `"Helvetica Neue", Helvetica, Arial, sans-serif`, weights
  300 to 800. No web fonts.
- Hero name: uppercase, 800, `clamp(46px, 5.6vw, 70px)`, line-height
  0.95, letter-spacing -0.035em, on two lines.
- Role: uppercase, 700, 30 to 38px, second word 500 in `--soft`.
- Section titles: 700, `clamp(28px, 3.6vw, 42px)`, letter-spacing -0.02em,
  preceded by an uppercase eyebrow with a lime dot.
- Page titles: `clamp(40px, 6vw, 72px)`, letter-spacing -0.03em.
- Body 16px / 1.55 in `--muted`; meta 12 to 13px in `--soft`.

## Signature moves

1. **Portrait card**: `--panel` card, 16px padding, photo with `--r-tile`
   corners and a 1:1.05 ratio, a column of four white circular social
   buttons overlapping the top-right of the photo, and a centred
   "Available for new projects" line with a pulsing green dot.
2. **Pill buttons with a disc**: text on the left, a 36px circle on the
   right holding an arrow; the disc rotates 45 degrees on hover and the
   button lifts 2px. Lime pill with black disc for primary, black pill with
   lime disc for secondary, hairline pill for tertiary.
3. **Wordmark marquee**: grey text wordmarks in four typographic flavours
   (bold grotesk with a small outline glyph, serif, mono, wide uppercase)
   scrolling slowly with masked edges; pauses on hover; static wrap under
   reduced motion.
4. **Collaboration split**: a two-tone headline and two contact items with
   circular hairline icons on the left, two 0.86-ratio rounded mockups on
   the right that lift on hover.
5. **Stats band**: dark rounded panel, centred two-tone headline, a small
   rounded studio thumbnail with a lime play disc, three numbers with
   hairline dividers that count up when scrolled into view.
6. **Plus accordion**: hairline rows, a grey circular plus that turns lime
   and rotates 45 degrees when open; panel animates with grid rows.

## Motion

Reveal: 22px rise and fade over 0.7s with a soft ease, staggered 80ms per
sibling. Counters ease out over 1.4s. Marquee 32s linear loop. Hover:
cards lift 4px and gain a soft shadow; covers scale 1.04 over 0.7s. All
motion collapses under `prefers-reduced-motion`.

## Voice

First person, warm and direct. Short sentences with concrete numbers
(weeks, prices, counts). Headlines make a promise and the grey fragment
adds the condition. No superlatives, no jargon, no exclamation marks.

## Do / don't

- Do keep the hero to three columns on desktop and stack portrait first
  on phones.
- Do give every list a lime check disc and every card an arrow disc.
- Do keep testimonial stars as stroked stars with lime fill.
- Don't add a second accent, gradients on buttons, or coloured headings.
- Don't use pure black backgrounds, square corners or drop shadows on text.
- Don't leave any `href="#"` or a page without a designed body.


## Refinement v2

Keep the lime outer frame, white rounded canvas, central portrait and restrained dark/lime controls. Favor short headings and one-sentence service descriptions. Show unique client wordmarks in a compact static grid; never repeat the full list under reduced motion. The nine active assets share natural studio lighting, neutral materials and a restrained lime/sage family. Portfolio media keeps its square composition with contain; portrait uses a 4:5 crop aligned to the top so the head remains visible. Do not insert unrelated website photography into the gardening-app case. Labels for fictional clients remain fictional; platform icons must only identify a platform actually present. Fields are 48px and textarea 128px, with a 660px maximum form width. Confirmation is hidden until submission.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
