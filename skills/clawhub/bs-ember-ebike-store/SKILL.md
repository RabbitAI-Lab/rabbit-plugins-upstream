---
name: bs-ember-ebike-store
description: Build a complete multi-page website with an orange photographic hero, bold condensed headings, dark cycling category cards and tactile component details. Includes connected content pages and interactive controls, with a reusable visual system for new brands and content.
---

# Ember E-Bike Store

Build a complete website using an orange photographic hero, bold condensed headings, dark cycling category cards and tactile component details.
The worked example is a fictional brand, Ember Cycle, with 33 connected
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

Preserve these structures: bike-hero, bike-controls, bike-categories, data-carousel.
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
The worked example currently maps 15 source images.

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

Run the included scripts/validate-design.mjs against the finished demo.
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
- scripts/validate-design.mjs: static demo and template validation.


### Shopping bag entrance
Use a compact 44px icon-only shopping bag or cart button in the header. Do not render “Bag (0)”, “Cart (0)”, parentheses, or a text label. Hide the quantity badge for an empty cart; show and update it only for positive quantities. Preserve an accessible label and keyboard focus.


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
