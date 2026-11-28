# Visual system

Grid-Paper Beverage Brand Site uses white graph paper, heavy condensed display type, outlined product cards, a rotated photo fan and playful flavor colors.

## Reference hierarchy

The included template is the visual source of truth. Preserve the first-screen
composition, section order and image treatment before changing copy. Do not
replace the signature hero with a generic headline-and-button layout.

## Tokens extracted from the working template

- `--ground`: `#e8e8e6`
- `--paper`: `#ffffff`
- `--ink`: `#181818`
- `--muted`: `#5d5d59`
- `--accent`: `#ffe447`
- `--on-accent`: `#181818`
- `--tint`: `#f5f2ec`
- `--line`: `#272727`
- `--card-radius`: `18px`

## Composition rules

- Keep the hero silhouette, relative headline scale and image anchors.
- Preserve the original content width and the relationship between full-bleed
  sections and inset cards. Read the template CSS for exact breakpoint values.
- Keep these signature structures: `oat-hero`, `oat-fan`, `oat-story`, `oat-recipes`.
- Let supporting pages reuse typography, controls and surfaces while giving
  each item its own content and imagery. Do not repeat the home hero on every page.
- Use the template's type families or a licensed, locally bundled equivalent
  with comparable width and weight. Check line breaks after changing fonts.

## Image direction

The example maps 12 source images. Assign one clear subject to each
product, project, destination or story. Reuse that subject only for the same
entity's card and detail page. Additional detail photographs should show a
different view, material, activity or context. Never use a single hero image
as the thumbnail for unrelated items.

Use coherent lighting, palette and photographic or illustrative treatment.
Generate original subjects without third-party logos, branded packaging or
watermarks. Match the crop to the displayed frame and check the subject at
mobile width. CSS cropping of a multi-subject sheet is not a new source image.

## Responsive behavior

At desktop widths retain the original asymmetric composition and card rhythm.
At tablet widths reduce columns before shrinking type excessively. At 390 px
stack content in reading order, keep controls at least 44 px high, and keep
forms and cards within the viewport. Decorative overlaps may move but must
not cover a heading, label or primary action.

## Interaction and motion

Preserve hover, focus, selected, loading or confirmation, empty and error
states where they exist. Respect reduced-motion preferences. Menus close
after navigation; the active page is visible and every other page is hidden.
Forms validate required fields and explain what happened. Local demo forms
do not claim a real submission, reservation or payment.

## Avoid

- Unrelated colors, stock gradient substitutions or a generic SaaS layout.
- Stretched images, repeated thumbnails for different entities or blank media.
- Source names, logos, testimonials or claims copied into the new brand.
- Decorative controls that look clickable but have no visible result.


## Reference fidelity revision

Use white 22 px graph paper with barely visible gray rules, ink outlines, a cream compact header, blue label stickers and yellow action buttons. The hero is a compact two-line mixed-case condensed heading (62 px desktop, 43 px mobile), one line of monospace support copy, and five overlapping rounded photo cards with distinct lifestyle, product and food images. Add a blue speech note, a yellow sparkle and a green smile sticker. Do not return to an oversized uppercase headline, yellow full-page ground or three huge packaging photos. The product rail follows immediately: four cards visible on desktop, six products reachable by arrows/scroll, full-width Add to cart pills, one cobalt highlighted card. Follow with the outlined split story, three vivid recipe tiles, two-column FAQ, centered newsletter, shaped photo strip and rounded footer. All controls, photos and tiles link to their corresponding route; product shelf controls scroll the existing cards.


## Refinement v2

Retain the white graph paper, outlined photo collage, cheerful shelf colours and condensed headings from the reference refinement. Product photographs and recipe heroes use complete 3:2 framing. Keep the same cream/cobalt/yellow photographic family. Recipes use short actual preparation steps, without generic design paragraphs. Forms max 640px, fields 48px, textarea 128px; checkout summary 285px alongside the form and first on mobile. Preserve the shopping-cart icon and matching multipack pricing.


### Shopping bag entrance
Use a compact 44px icon-only shopping bag or cart button in the header. Do not render “Bag (0)”, “Cart (0)”, parentheses, or a text label. Hide the quantity badge for an empty cart; show and update it only for positive quantities. Preserve an accessible label and keyboard focus.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
