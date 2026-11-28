---
name: bs-sticker-gifting-app-landing
description: Build a complete multi-page website with warm cream, oversized black type, coral and yellow stickers, playful gift-card artwork and bold product bands. Includes connected content pages and interactive controls, with a reusable visual system for new brands and content.
---

# Sticker Gifting App Landing

Build a complete website using warm cream, oversized black type, coral and yellow stickers, playful gift-card artwork and bold product bands.
The worked example is a fictional brand, Wishwell — Gifting made joyful, with 14 connected
routes. Its HTML is the visual blueprint, not a substitute for a framework
implementation. Start from the included template and preserve its design
relationships when replacing the content.

## Workflow

### 1. Establish the content and output location

Read the target repository and its instructions before writing. Identify
the brand, audience, page requirements and available content. Ask only for
information that blocks useful progress; draft clearly fictional examples
when the user has not supplied real business details.

Keep unrelated files and worktree changes intact. Put a standalone requested
site in an isolated directory when it does not belong in the existing app.
Do not silently migrate an existing application to another framework.

### 2. Choose the target stack

Honor an explicitly requested framework or starter, including Vue, React,
Astro, Next.js or a TypeScript starter. If none is specified, use **Next.js
App Router with TypeScript**. Do not ask the user to choose a stack merely
because the request omitted it.

Read references/framework-adaptation.md before implementation. Translate
the design into genuine components, content data and framework routes.
Never use an iframe or inject the entire template as raw HTML to claim a
framework port. The hash router exists only for the catalog demo.

### 3. Read and preserve the visual system

Read references/style-guide.md and references/visual-contract.md. Open
references/template.html and identify the hero anchors, section sequence,
container widths, typography ratios, image masks and signature shapes.

Preserve these structures: hero, sticker, gift, faq.
Keep the same visual hierarchy after changing the name and copy. New text
may require a line break or a small local adjustment, not a new design style.

### 4. Plan the complete page family

Read references/page-library.md and references/route-inventory.md. Inventory
every navigation item, card, category, article, product and form destination.
Create real content for the secondary pages before calling the site complete.

Each entity gets an ID, title, category, specific description and its own
image subject. Detail pages need useful sections and a clear return path.
A new page must be reachable from visible navigation or contextual links.
Remove links when removing a page. Keep the not-found route useful.

### 5. Build the structure in the selected framework

Use shared components for navigation, cards, buttons, forms and footer.
Keep content collections separate from visual components. Use semantic
headings, descriptive links and properly associated input labels.

Keep interaction state local to the component that owns it, except shared
cart or saved-item state. Use the selected framework’s router and conventions.
Implement both the default and empty states; do not stop at a static screenshot.

### 6. Create a rich, consistent image set

Read the image direction in references/visual-contract.md. Plan hero,
collection, detail, editorial and supporting images as distinct roles.
The worked example currently maps 9 source images.

Use owned assets or the host’s image tool. Match subject, lighting, palette
and crop to the design. Request one coherent scene per image, no watermarks
and no third-party logos. Review every generated image before use.

Do not use one image for unrelated products, projects or stories. Reusing
the same entity’s image on its card and detail page is appropriate; add
a different contextual or close-up image when a long page needs more depth.

Optimize photographs as high-quality WebP or an equivalent supported format.
Keep meaningful alt text and responsive dimensions. In the catalog demo
embed each image once and reuse its internal asset reference.

### 7. Preserve working interactions

Wire every apparent control to a visible result: menus, filters, tabs,
carousels, product options, cart quantities, forms and accordions.
Show active states and useful feedback. Provide a real no-results state.

The local demo validates inputs but does not send messages, reserve travel
or take payment. Do not claim that a real transaction occurred. Real
backend integrations belong in the generated application when requested.

### 8. Apply the icon grammar

Read references/icon-library.md. Keep interface marks as consistent inline
SVGs. No emoji, icon fonts, remote icon dependencies or copied brand marks.
Icon-only buttons need accessible names; decorative artwork stays hidden
from assistive technology.

### 9. Validate the artifact

Run the included scripts/validate-sticker.mjs against the finished demo.
For references/template.html, pass --allow-replace. Fix every reported
error. The validator checks self-containment, forbidden APIs, image tokens,
route links, size and the signature visual structures.

For a framework output, run that project’s appropriate type and build
checks. The catalog HTML validator does not validate framework source.
Check imports, routes, asset paths and the rendered content separately.

### 10. Review in a real browser

Open the home page and all linked routes at desktop, tablet and 390 px.
Compare the hero silhouette, heading scale, section rhythm and image crop
with the template. Check long titles, empty results and form validation.

Click the navigation, cards and every control. Confirm there is no
horizontal overflow, covered text, blank image or console error.
Respect reduced-motion settings and visible keyboard focus.

### 11. Deliver clearly

Provide the output path, the selected framework and a short account of
what was validated. Distinguish programmatic checks from browser review.
Do not claim deployment, publication or source-license clearance unless
those actions were actually completed and authorized.

## Catalog demo constraints

The catalog preview is a self-contained HTML file, under 20 MB, with inline
styles, scripts and embedded media. It must work in a sandboxed iframe with
allow-scripts only. No network requests, storage, cookies or top navigation.
These constraints do not force generated websites into a single HTML file.

## Files

- references/template.html: editable visual blueprint with image placeholders.
- references/style-guide.md: style-specific rules and composition.
- references/visual-contract.md: concrete tokens and fidelity requirements.
- references/page-library.md: page roles and content requirements.
- references/route-inventory.md: current complete route inventory.
- references/framework-adaptation.md: stack choice and component mapping.
- references/icon-library.md: icon and accessibility conventions.
- references/third-party-notices.md: attribution and provenance boundaries.
- scripts/validate-sticker.mjs: static demo and template validation.


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

<!-- reui:stack -->
#### Interface components come from ReUI

Every generic control in this template — buttons, text fields, selects,
radio groups, tabs, accordions, filter chips, the mobile menu panel — is a
[ReUI](https://reui.io) component, not a hand-written control. Keep it that
way in the generated project.

- Install from the official registry and use the real component source.
  ReUI is a React component system built on Radix primitives; in a
  Next.js/React project add components with the shadcn CLI
  (`npx shadcn@latest add @reui/button`, and so on) and import them from
  your `components/ui` directory. The MIT-licensed source also lives at
  https://github.com/keenthemes/reui.
- Do not substitute a native `<select>`, a hand-rolled popover, or a `div`
  with matching class names. If a control needs behaviour ReUI does not
  provide, build it explicitly and say so.
- Style through tokens, not forks. Point ReUI's custom properties
  (`--primary`, `--background`, `--border`, `--radius`, …) at this
  template's palette and keep its own control classes on the rendered
  elements. `references/reui-components.md` lists the mapping used here.
- In a non-React stack, check ReUI's real support before promising it.
  Astro can mount React islands; a Vue or Svelte project cannot use ReUI
  components directly — raise the conflict rather than switching stacks or
  silently swapping in another library.
<!-- /reui:stack -->

---

## More from Skillry

This skill is a free open-source website template from [Skillry](https://skillry.dev).

- Explore the full catalog of creative design, presentation, video, and web skills at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
