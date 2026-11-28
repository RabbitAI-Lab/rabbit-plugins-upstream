# Framework adaptation

The template is a single HTML file only because the catalog preview needs
one. Real projects use the requested framework's routes, components and
state.

## Decide the stack

1. An explicit user request wins (Next.js, React + Vite, Vue/Nuxt, Svelte/
   SvelteKit, Astro, plain HTML).
2. Inside an existing repository, read the signals: `package.json`
   dependencies, `next.config.*`, `nuxt.config.*`, `svelte.config.*`,
   `astro.config.*`, existing `components/` or `src/routes/`. Build in that
   stack and follow its styling convention (CSS Modules, Tailwind, global
   CSS, scoped styles).
3. No repository and no preference: Next.js App Router with TypeScript.
4. Ask one short question only when signals conflict.

## Mapping

| Template | Framework |
| --- | --- |
| `:root` custom properties | global tokens file (CSS variables or Tailwind theme extension with the same values) |
| `<header class="nav">` / `<footer>` | `SiteNav` / `SiteFooter` in the root layout |
| `<section data-page="x">` | route `/`, `/pricing`, `/resources`, `/events`, `/changelog` |
| hash router + `.on` class | framework router and links; active link from the current path |
| repeated cards and rows | components fed by typed data arrays (`plans`, `events`, `releases`, `articles`) |
| inline icon sprite | one `Icon` component rendering Lucide paths (`lucide-react` / `lucide-vue-next` / `lucide-svelte`) plus a small `BrandMark` for integrations |
| `toast()` | a single toast/notification component in the layout |
| inline `<script>` interactions | component state (`useState`, `ref`, stores); only interactive parts become client components |
| embedded data-URI images | files in `public/` (or the framework asset pipeline) with width/height and alt text |
| embedded fonts | the framework font loader (`next/font/google` for Geist, Geist Mono, Instrument Serif) or self-hosted files |

## Rules

- Keep every visual value identical: colours, opacities, sizes, radii,
  spacing, glows, gradients, motion timings.
- Server-render static content; hydrate only the toggle, filters, search,
  countdown, accordions, forms and the bento interactions.
- Countdown targets and prices come from data, not hard-coded markup.
- Provide page metadata, a not-found route and a README with install, dev
  and build commands.
- Never wrap the template in an iframe or inject it as raw HTML.
