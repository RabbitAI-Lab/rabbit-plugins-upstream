# Visual system

Lime-Frame Designer Portfolio uses a lime outer frame, a white inner card, a centered portrait, small proof cards and a dark statistics band.

## Reference hierarchy

The included template is the visual source of truth. Preserve the first-screen
composition, section order and image treatment before changing copy. Do not
replace the signature hero with a generic headline-and-button layout.

## Tokens extracted from the working template

- `--lime`: `#d4f56a`
- `--lime-deep`: `#b9e04a`
- `--lime-soft`: `#eefbc8`
- `--card`: `#ffffff`
- `--panel`: `#f3f3f1`
- `--panel-deep`: `#e9e9e6`
- `--ink`: `#141414`
- `--muted`: `#5f5f5f`
- `--soft`: `#9a9a9a`
- `--line`: `#e6e6e2`
- `--dark`: `#232323`
- `--dark-2`: `#2f2f2f`
- `--on-dark`: `#f5f5f2`
- `--on-dark-muted`: `#a8a8a3`
- `--r-sheet`: `22px`
- `--r-card`: `22px`
- `--r-tile`: `16px`
- `--r-pill`: `999px`
- `--frame`: `10px`
- `--font`: `"Helvetica Neue",Helvetica,Arial,sans-serif`
- `--shadow-card`: `0 18px 40px -22px rgba(20,20,20,.28)`
- `--shadow-float`: `0 30px 60px -30px rgba(20,20,20,.35)`
- `--ease`: `cubic-bezier(.2,.7,.2,1)`

## Composition rules

- Keep the hero silhouette, relative headline scale and image anchors.
- Preserve the original content width and the relationship between full-bleed
  sections and inset cards. Read the template CSS for exact breakpoint values.
- Keep these signature structures: `hero`, `portrait`, `stats`, `work`.
- Let supporting pages reuse typography, controls and surfaces while giving
  each item its own content and imagery. Do not repeat the home hero on every page.
- Use the template's type families or a licensed, locally bundled equivalent
  with comparable width and weight. Check line breaks after changing fonts.

## Image direction

The example maps 10 source images. Assign one clear subject to each
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

Keep the lime outer frame, white rounded canvas, central portrait and restrained dark/lime controls. Favor short headings and one-sentence service descriptions. Show unique client wordmarks in a compact static grid; never repeat the full list under reduced motion. The nine active assets share natural studio lighting, neutral materials and a restrained lime/sage family. Portfolio media keeps its square composition with contain; portrait uses a 4:5 crop aligned to the top so the head remains visible. Do not insert unrelated website photography into the gardening-app case. Labels for fictional clients remain fictional; platform icons must only identify a platform actually present. Fields are 48px and textarea 128px, with a 660px maximum form width. Confirmation is hidden until submission.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
