# Visual system

Sticker Gifting App Landing uses warm cream, oversized black type, coral and yellow stickers, playful gift-card artwork and bold product bands.

## Reference hierarchy

The included template is the visual source of truth. Preserve the first-screen
composition, section order and image treatment before changing copy. Do not
replace the signature hero with a generic headline-and-button layout.

## Tokens extracted from the working template

- `--ink`: `#1e3a5f`
- `--ink-deep`: `#132a47`
- `--body`: `#2f3f55`
- `--muted`: `#5b6b82`
- `--sky`: `#b8ced7`
- `--sky-light`: `#b8ced7`
- `--cream`: `#f7f4ee`
- `--paper`: `#ffffff`
- `--mint`: `#cfe6cd`
- `--pink`: `#f3a9c2`
- `--butter`: `#f6d97b`
- `--tangerine`: `#f4a24f`
- `--powder`: `#c4d8ee`
- `--dark`: `#2b2b2e`
- `--dark-2`: `#3a3a3e`
- `--lilac`: `#c9bbea`
- `--lilac-deep`: `#5a3f8f`
- `--lime`: `#9dc23f`
- `--coral`: `#f08a7a`
- `--line`: `rgba(30,58,95,.12)`
- `--r-band`: `36px`
- `--r-card`: `28px`
- `--r-ui`: `999px`
- `--serif`: `"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif`
- `--sans`: `"Avenir Next",Avenir,"Segoe UI",system-ui,-apple-system,sans-serif`
- `--shadow-sticker`: `0 6px 14px rgba(20,40,70,.14),0 1px 0 rgba(255,255,255,.7) inset`
- `--shadow-card`: `0 20px 50px rgba(20,40,70,.16)`
- `--shadow-phone`: `0 40px 80px rgba(20,40,70,.35),0 8px 20px rgba(20,40,70,.2)`
- `--wrap`: `1180px`
- `--w`: `78px`

## Composition rules

- Keep the hero silhouette, relative headline scale and image anchors.
- Preserve the original content width and the relationship between full-bleed
  sections and inset cards. Read the template CSS for exact breakpoint values.
- Keep these signature structures: `hero`, `sticker`, `gift`, `faq`.
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


## Current refinement standard

Retain the source rhythm: pale blue sticker hero and phone, pastel feature mosaic, lilac gift tiles, charcoal cash section, green photographic CTA. Use one softened-blue (#b8ced7) hero scene with a complete phone, not two repeated phone bands. Keep the main heading short and the phone illustration proportional.

One short lead per section; features explain one benefit in one sentence. Keep the legal information readable without hiding its content. Do not use fabricated popularity badges as visual filler.

Card artwork belongs to a warm matte illustration family. The arcade card uses parchment, dusty blue, coral and yellow gouache, never a glossy neon render. Product photographs share simple solid-color studio settings; everyday cards use warm natural lighting. Illustrations and photographed products have distinct consistent roles. Use square gift-card artwork at its full 1:1 ratio on both list and detail pages.

Use bundled original Apple and Android SVGs for the corresponding platform buttons. UI controls and stickers retain their existing coherent icon systems. No third-party brand names in the fictional gift shop. Devicon provenance and license are under brand-icons/.

Form fields are 48px high with a 128px textarea, forms maximum 560px. Phone inputs and paired fields stack naturally on mobile. Local demo confirmation must say no message was sent. Preserve all routes, filters, amount controls and plan tabs. Respect the requested framework; default to Next.js App Router + TypeScript.


### Complete phone hero
The home hero uses a left-aligned headline and CTA alongside one complete phone showing the greeting card. Surround the phone with two illustrated gift cards and a few stickers. Both gift cards link to their matching detail pages; occasion arrows and the Send link remain functional. Never crop the phone to its top edge, use a fixed-height peek container, or repeat the same phone in an immediately adjacent section. At mobile width, place the copy above a proportionally smaller but complete phone; keep the greeting artwork contained and all controls inside the viewport. The feature mosaic follows the hero directly.


### Physical gift card in the closing CTA
The hand-held card must have a designed, printed face: a recognizable brand mark, gift-card label and realistic card edges, perspective and thumb occlusion. Never use a blank white placeholder. Preserve the lime-green photographic background and empty left area for the heading. The current user-requested example uses a generated Starbucks gift-card mockup; use the requested brand for future projects rather than assuming a merchant partnership.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
