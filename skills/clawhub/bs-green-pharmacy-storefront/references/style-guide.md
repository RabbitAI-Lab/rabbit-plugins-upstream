# Green pharmacy style guide

The page must feel like a bright, friendly pharmacy counter: a lime hero that
holds a smiling pharmacist, pastel tiles that sort people by need, calm grey
product cards, and a dark-green footer that ends in a giant lime wordmark.
Cheerful in colour, clinical in alignment.

## Tokens (locked)

| Token | Value | Job |
| --- | --- | --- |
| `--lime` | `#c2f364` | hero frame, active nav pill, open FAQ item, footer band, membership tile |
| `--lime-deep` | `#a3dc3c` | lime button hover |
| `--forest` | `#0f3b2e` | footer, active filter chips, brand mark, check icons |
| `--navy` | `#1b1a4e` | every heading, primary buttons, prices, cart summary panel |
| `--ink` / `--muted` / `--soft` | `#13132b` / `#5c6170` / `#8a8f9c` | body, secondary, meta text |
| `--line` / `--panel` | `#e6e8ee` / `#f3f5f8` | hairlines; product cards, FAQ pills, quiet cards |
| `--mint` `--yellow` `--peach` `--pink` `--sky` `--orange` `--aqua` `--lilac` | pastel set | category tiles, promo tiles, service cards, page headers, avatars |
| `--r-hero` / `--r-card` / `--r-tile` / `--r-ui` | `32px` / `20px` / `16px` / `12px` | frames, cards, tiles, inputs |
| `--shadow` / `--shadow-lift` | soft navy shadows | floating cards, hovered product cards |

Rules:

- **Lime is a surface, navy is the voice.** Lime never carries body text
  smaller than 12px; headings on lime are always navy. Navy never becomes a
  background for large areas except the cart summary.
- **One pastel per tile.** Each category, promo or service tile takes exactly
  one pastel from the set. Never gradient two pastels together; never put two
  tiles of the same pastel side by side.
- **Product cards are grey, product photos are white.** The `--panel` card
  holds a white image well with the product centred and 10% padding. The
  cereal feature is the one allowed exception (aqua well, cover-fit photo).
- **Deals wear yellow.** The percentage-off pill is always `--yellow` with
  navy text, top-right of the image well, and the old price is struck through
  in `--soft`.

## Type

- Single grotesk stack: `"Helvetica Neue", Helvetica, Arial, sans-serif`.
  Do not load web fonts.
- Hero display word: 800 weight, `clamp(64px, 10.5vw, 184px)`, letter-spacing
  `-.05em`, line-height `.86`, one or two words, always navy.
- Hero support copy: 12px, uppercase, `.06em` tracking, 700 weight.
- Section titles: 800 weight, 28–40px, two lines with a manual break
  ("Today's best deals / for you").
- Inner page headers: 800 weight, `clamp(36px, 5.4vw, 64px)` on a pastel frame.
- Cards: 14px 600 names, 11px meta, 16px 800 prices. Body copy 14–15px at
  400 in `--muted`.

## Signature moves

- **The lime hero frame.** A 32px-radius lime panel with a three-column grid:
  giant word across the top, uppercase copy and two round badges bottom-left,
  the pharmacist portrait rising from the bottom edge in the middle column,
  the white upload-prescription card and a navy pill button bottom-right.
- **Six pastel category tiles.** Square photos of people or hands on flat
  pastel backgrounds, label underneath, hover lifts the tile 4px.
- **Two-up service cards.** A yellow card with a dashed drop zone and a peach
  card with a pointing pharmacist; both end in a navy pill plus a round icon
  button.
- **Monogram brand discs.** Fictional brands are two-letter monograms in a
  96px pastel disc; one disc is inverted (forest with lime type) for rhythm.
- **Tabbed trending grid.** Category chips above a four-column product grid;
  the active chip is forest with white text.
- **Promo tiles with a masked figure.** Title top-left, offer bottom-left in
  26px, a person photo masked from transparent to opaque on the right half.
- **Cereal feature banner.** Aqua frame with a centred label, split copy and
  photo, hairline fact list, navy price button, and two flavour bars in
  yellow and peach bleeding to the frame edges.
- **FAQ pills.** Grey rounded rows; the open row turns lime and rotates its
  chevron.
- **Footer band.** Forest footer with five columns, then a lime band with the
  cross icon and the wordmark at up to 168px.

## Motion

- `.reveal` elements fade and rise 18px when 8% visible, once.
- Product cards lift 4px and scale the photo 5% on hover; buttons rise 1px.
- The add-to-cart button flips to navy for 900ms after a click and a navy
  toast slides in from the bottom.
- Everything respects `prefers-reduced-motion`.

## Voice

- Plain, warm and specific: "2-hour delivery in the city", not "fast
  shipping". Second person. No exclamation marks except in the trending
  heading's sibling copy if the buyer wants one.
- Every product gets a real blurb, three benefits, usage advice and four
  detail rows. Never leave a product with a one-line description.
- Safety lines are honest ("Always read the label", emergency guidance on the
  consultation page).

## Do / don't

- Do keep the pharmacist portraits on flat lime, peach or yellow backgrounds
  that match the tile behind them.
- Do keep prices to two decimals with a dollar sign; keep sale badges to whole
  percentages.
- Don't use real pharmaceutical brand names, real product names or real
  people. Don't use store badges with real platform logos; use the text
  "Download for iOS / Android" chips.
- Don't add a second accent hue; the pastels are tile colours, not brand
  colours.
- Don't use emoji, dingbats or icon fonts anywhere. Every icon is an inline
  SVG from the sprite.


## Current refinement standard

Preserve the lime hero, oversized two-word heading, delivery portrait, pastel category photos and forest-green footer. Reduce the homepage recommended grid to four visible products per selected category. Keep the full catalog and every product reachable.

Use short product names above the price; put strengths and pack details in the details table. Keep descriptions concise. Do not invent efficacy, dosage or verification claims for new products; use supplied product information. General navigation and purchase controls use the same line-icon family. Original Apple and Android marks identify platform buttons only; license and original SVGs are included under brand-icons/.

32 active images follow two roles: colorful studio portraits for categories and services, soft white-background pack shots for products. Show complete products with contain sizing inside square media frames. Keep the pharmacy interior on the about page; do not add unrelated staged skincare products to a specific product case.

Forms have 48px fields, 128px textareas and 16px radio controls, with a maximum 720px form card. Pair fields on desktop and stack on mobile. Checkout totals align labels left and amounts right. The mobile cart uses a compact thumbnail, clear quantity control and a separate remove action.

Cart thumbnails must read the live hydrated product image when rendering the cart. Do not cache an absent src before the image hydration script has run. Validate a populated cart, quantity changes, totals and mobile rendering. Respect the selected framework and default to Next.js App Router + TypeScript.


### Shopping bag entrance
Use a compact 44px icon-only shopping bag or cart button in the header. Do not render “Bag (0)”, “Cart (0)”, parentheses, or a text label. Hide the quantity badge for an empty cart; show and update it only for positive quantities. Preserve an accessible label and keyboard focus.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
