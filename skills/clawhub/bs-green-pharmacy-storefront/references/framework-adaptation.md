# Framework adaptation and visual fidelity

## Selection

An explicit user framework/starter wins. With no explicit selection, use
Next.js App Router and TypeScript. Do not ask a stack question by default.
Inspect package.json and project rules before writing. Work inside the named
starter when requested; do not overwrite or migrate unrelated applications.
Use the repository's existing package manager and compatible dependency
versions. For a fresh Next.js application, resolve current stable versions
from official documentation at execution time rather than pinning stale ones.

## Design contract

Read template.html and style-guide.md first. Extract actual color tokens,
font families/fallbacks, headline/body ratios, content width, section spacing,
border radii, stroke weights, image aspect ratios and decorative treatments.
Make a section-by-section checklist before implementation. The reference is
the visual specification, not inspiration for a different generic landing page.
Keep a copy of this checklist in the generated application's README.

## Next.js default

Use app/layout.tsx for document metadata and the shared shell, app/page.tsx
for the home route, and real app/<section>/page.tsx or dynamic detail routes.
Keep typed project/product/article collections in a data module. Extract
named header, footer, hero, card and section components from the template.
Use next/link for internal links. Use server components for static content;
mark only interactive menus, filters, tabs, forms and carts with use client.
Use React state and native form validation instead of document-wide selectors.
Provide meaningful metadata, a not-found route, local images with width/height
and descriptive alt text, and a README with install/dev/build instructions.
Use CSS variables or the project's styling system without altering visual
values. Preserve the original CSS when it is the most faithful translation.

## Other stacks

- React: typed reusable components, the starter's router, hooks for state.
- Vue: SFC components, script setup with TypeScript when supported, Vue Router
  for multiple pages, refs/computed values for interactive controls.
- Astro: file-based pages, reusable .astro components and scoped client islands
  only for controls requiring state; keep article and product content static.
- TypeScript starter: follow its build tool, entry points, router and CSS
  conventions. TypeScript describes the language, not a replacement framework.
- An explicitly requested standalone HTML output remains supported.

## Image coverage

Create an image plan before implementation. Every distinct product, project,
article and gallery item needs appropriate unique art. Listing cards may reuse
that same item's lead image on its own detail page, but unrelated items must
not share it. Use separate hero, editorial/detail, process and supporting
images. Avoid filling empty space with random photographs, stretching one
asset across unrelated roles, or counting alternate crops as new images.
Generate new images with the host image tool where needed. Keep art direction
consistent within the site: lighting, palette, subject, material and rendering.
Deliver generated project images as local files, never hotlinks. The catalog
demo embeds high-quality WebP images and has no network dependencies.

## Interaction and content contract

Every navigation link must lead to a populated page. Preserve mobile menu,
active route, keyboard focus, hover states and reduced-motion support. Detail
pages must contain specific content rather than repeated generic paragraphs.
Filters change the displayed items and expose an empty result state; sort
controls reorder results. A cart supports add/remove/quantity/totals, including
empty state. Forms validate fields and show a clear local demo confirmation.
Do not imply an email was delivered, a booking confirmed, or payment charged
unless a real backend was explicitly requested and connected. Keep real
payments, account services and order processing out of an unconnected demo.

## Verification

Build the generated framework project with its package manager. Walk every
route, test controls and browser back/forward, check empty/invalid states,
and inspect desktop and mobile screenshots at 1920, 1280 and 390 px widths.
Compare section order, image composition and type scale against template.html.
Resolve visual drift before delivery; a successful build does not prove
fidelity. Demo sandbox restrictions apply to examples/demo.html only, not to
framework-native routing. Never replace framework components with an iframe.

<!-- reui:framework -->
## ReUI component layer

Generic interface controls are ReUI components. This is a requirement of the
output, not a styling suggestion, and it survives the stack choice.

### Mapping

| Template element | ReUI component |
| --- | --- |
| CTA / link button | `Button` (use `asChild` to render an `<a>`) |
| Text, email, phone field | `Input` inside `Field` + `FieldLabel` |
| Long-form field | `Textarea` |
| Dropdown choice | `Select` + `SelectTrigger` / `SelectContent` / `SelectItem` |
| Single choice from a visible set | `RadioGroup` + `RadioGroupItem` |
| Opt-in / agreement | `Checkbox` |
| Filter chips, size or billing switches | `ToggleGroup` + `ToggleGroupItem` |
| Save / wishlist toggle | `Toggle` |
| Sectioned panels | `Tabs` + `TabsList` / `TabsTrigger` / `TabsContent` |
| FAQ and process lists | `Accordion` + `AccordionItem` / `AccordionTrigger` |
| Mobile navigation panel | `Sheet` + `SheetContent` |
| Modal | `Dialog` + `DialogContent` |
| Validation messaging | `FieldError`, `FieldDescription`, `aria-invalid` |

Physical or illustrative motion — tape, torn paper, doodles, parallax and
similar template-specific effects — stays in bespoke CSS. ReUI covers the
interface layer, not the artwork.

### Keeping the template's look

Two mechanisms, in this order:

1. **Token mapping.** ReUI reads its chrome from custom properties. Point
   them at the template palette so components inherit its colour, radius and
   type rather than ReUI's defaults.
2. **The template's own CSS.** Rendered controls keep their original class
   names, so existing rules — including contextual ones like `.nav .btn` —
   continue to apply. Do not delete that CSS and re-implement it in
   component files.

The component implementations are never forked per template. If two
templates look different, that difference lives in tokens and template CSS.

### Accessibility expectations

Radix gives these components roving focus, typeahead, focus trapping and
focus restoration. Keep them: do not replace a trigger with a `div`, do not
strip `aria-*` attributes, and do not remove the visible focus ring. Verify
keyboard operation of every control — arrow keys in tabs and selects,
Enter/Space to activate, Escape to dismiss, and focus returning to the
trigger afterwards.
<!-- /reui:framework -->
