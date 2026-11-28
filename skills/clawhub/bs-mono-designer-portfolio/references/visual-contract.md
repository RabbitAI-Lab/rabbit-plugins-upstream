# Visual system

Mono Designer Portfolio uses black-and-white editorial hierarchy, oversized condensed type, a portrait-led introduction and a dense poster grid.

## Reference hierarchy

The included template is the visual source of truth. Preserve the first-screen
composition, section order and image treatment before changing copy. Do not
replace the signature hero with a generic headline-and-button layout.

## Tokens extracted from the working template

- `--ground`: `#e9e9e9`
- `--ground-2`: `#f2f2f2`
- `--paper`: `#f8f8f8`
- `--ink`: `#262626`
- `--ink-2`: `#333333`
- `--muted`: `#5c5c5c`
- `--soft`: `#8a8a8a`
- `--line`: `rgba(0,0,0,.09)`
- `--grid`: `rgba(255,255,255,.72)`
- `--white`: `#ffffff`
- `--shadow-poster`: `0 18px 36px -20px rgba(0,0,0,.45),0 2px 6px rgba(0,0,0,.07)`
- `--shadow-poster-hover`: `0 30px 50px -22px rgba(0,0,0,.55),0 4px 10px rgba(0,0,0,.08)`
- `--r-tile`: `16px`
- `--font`: `"Avenir Next",Avenir,"Segoe UI",system-ui,-apple-system,"Helvetica Neue",Helvetica,Arial,sans-serif`
- `--font-mono`: `"SF Mono",Menlo,Consolas,"Liberation Mono",monospace`
- `--wrap`: `1240px`

## Composition rules

- Keep the hero silhouette, relative headline scale and image anchors.
- Preserve the original content width and the relationship between full-bleed
  sections and inset cards. Read the template CSS for exact breakpoint values.
- Keep these signature structures: `hero`, `portrait`, `work`, `poster`.
- Let supporting pages reuse typography, controls and surfaces while giving
  each item its own content and imagery. Do not repeat the home hero on every page.
- Use the template's type families or a licensed, locally bundled equivalent
  with comparable width and weight. Check line breaks after changing fonts.

## Image direction

The example maps 11 source images. Assign one clear subject to each
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


## Refinement v2

Use the monochrome grid-paper shell as a quiet exhibition frame. Keep biography and service descriptions concise; case studies use a short brief, approach and outcome. Display the eight selected posters at their full 2:3 ratio, including on mobile; never stretch or crop the artwork to fill a shallow card. Portfolio subjects can differ, but maintain consistent poster scale, frame and captions. The ten active assets include the grayscale designer portrait, eight posters and a monochrome studio photograph. Avoid unrelated product still lifes on case pages. Use authentic Photoshop, Illustrator and Figma marks for their software positions; drawing and printing use consistent line icons, not invented two-letter badges. Fields are 48px high, textareas at least 128px. Keep the mobile hero title on one line.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
