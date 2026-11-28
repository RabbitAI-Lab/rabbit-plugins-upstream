# Pre-delivery checklist

Walk this list before handing over. Every box must be true.

## Premium UI

- [ ] Inter Tight display with -0.02 to -0.03em tracking, Inter text, Geist Mono for IDs and code; fonts from the fontsource CDN (template only), the `@fontsource-variable/*` packages or `next/font/google` (framework project), or inlined as data URIs (single-file build) or served from `fonts/` (deployed static site).
- [ ] Sand ground, mint bands, near-black ink, one lane-green accent; no stray accent colors outside product UI.
- [ ] Hero keeps its fixed composition: one-line 54px headline (127px from the top at 1440x900), 34px muted subtitle, 2x2 feature notes, two 40px buttons, "1 of 3" indicator, product frame top-aligned on the right. No added pills, stats, floating cards or washes.
- [ ] No purple, violet or indigo anywhere (labels, team dots and roadmap bars included); section h2 at most 48px.
- [ ] At least eight different section layouts; no three image-and-text splits in a row; two-tone headings used at most twice.
- [ ] Radius scale, hairline borders and warm layered shadows are consistent.
- [ ] Every clickable element has hover, `:active` press, `:focus-visible`, and disabled/loading/success states where relevant.
- [ ] Sticky header gains a backdrop on scroll; nav shows the current section or route.

## Imagery

- [ ] The product is HTML/CSS/SVG with believable data, never a photo or generated screenshot.
- [ ] Photos only in customer, story, team and avatar slots; one art direction across all of them.
- [ ] Faces are never cropped; `object-position` set per image; no text, logos or screens in photos.
- [ ] Every `<img>` has alt, width/height, lazy loading below the fold and `decoding="async"`.
- [ ] Customer wordmarks are fictional and typeset; integrations are named by category.

## Motion

- [ ] Content is visible without JavaScript; reveals run once; hero animates within a second.
- [ ] Auto-advancing tabs run one loop and pause on hover, focus and offscreen.
- [ ] One marquee only; nothing loops next to reading text.
- [ ] Reduced motion makes everything instant and static.

## Completeness

- [ ] Every nav, footer, card and CTA link reaches a section or a route with real content.
- [ ] Routes: pricing, changelog, sign-in, sign-up, demo, security, customer story, company, privacy, terms, 404.
- [ ] Forms: empty submit shows inline errors, invalid email explains the fix, valid input shows loading then success, toast confirms.
- [ ] Filters and searches reach an empty state with a way back.
- [ ] Billing switch updates every price on the page and in the comparison table.
- [ ] Theme toggle switches every surface, including product UI; choice persists (guarded storage).
- [ ] Numbers agree across sections (see the section inventory).

## Responsiveness

- [ ] Checked at 360, 390, 768, 1024, 1440 and 1920 px; no horizontal scroll anywhere.
- [ ] Mobile has its own layout: stacked hero (32px headline at 122px, product frame under the indicator), tab titles only, one-plan comparison picker.
- [ ] Touch targets are at least 44px.

## Accessibility

- [ ] Landmarks, skip link, one h1 per view, focus moves to the h1 on route change.
- [ ] Labels above inputs; `aria-invalid` and `aria-describedby` on errors.
- [ ] Tabs, switches, radiogroups and accordions expose roles and states; arrow keys work in tab lists.
- [ ] Mobile sheet traps focus and closes on Esc; menus close on Esc and outside click.
- [ ] Text contrast at least 4.5:1 in both themes.

## Performance and sandbox

- [ ] Zero console errors and zero network requests in a self-contained build.
- [ ] Works inside `<iframe sandbox="allow-scripts">`: routes, anchors, forms, copy buttons.
- [ ] No `alert/confirm/prompt/window.open`; storage wrapped in try/catch.
- [ ] Each asset referenced once; built demo under 5 MB.
- [ ] `node scripts/validate-template.mjs <your built index.html>` passes (`--files` for a deployed site with `images/` and `fonts/` beside it, a folder path for a framework port); no Tracklane sample names remain.
