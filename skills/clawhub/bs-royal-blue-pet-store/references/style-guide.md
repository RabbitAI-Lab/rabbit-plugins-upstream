# Visual system

Royal Blue Pet Store uses a royal-blue frame, blue serif headings, a golden-retriever hero, category tiles and seasonal pet banners.

## Reference hierarchy

The included template is the visual source of truth. Preserve the first-screen
composition, section order and image treatment before changing copy. Do not
replace the signature hero with a generic headline-and-button layout.

## Tokens extracted from the working template

- `--ground`: `#1646a3`
- `--paper`: `#fff`
- `--ink`: `#17243b`
- `--muted`: `#788190`
- `--accent`: `#2357bb`
- `--on-accent`: `#fff`
- `--tint`: `#f1f4f7`
- `--line`: `#e5e9ef`
- `--card-radius`: `18px`
- `--shell-radius`: `28px`
- `--button-radius`: `7px`

## Composition rules

- Keep the hero silhouette, relative headline scale and image anchors.
- Preserve the original content width and the relationship between full-bleed
  sections and inset cards. Read the template CSS for exact breakpoint values.
- Keep these signature structures: `pet-hero`, `pet`, `spring`, `wishlist`.
- Let supporting pages reuse typography, controls and surfaces while giving
  each item its own content and imagery. Do not repeat the home hero on every page.
- Use the template's type families or a licensed, locally bundled equivalent
  with comparable width and weight. Check line breaks after changing fonts.

## Image direction

The example maps 9 source images. Assign one clear subject to each
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


### Shopping bag entrance
Use a compact 44px icon-only shopping bag or cart button in the header. Do not render “Bag (0)”, “Cart (0)”, parentheses, or a text label. Hide the quantity badge for an empty cart; show and update it only for positive quantities. Preserve an accessible label and keyboard focus.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
