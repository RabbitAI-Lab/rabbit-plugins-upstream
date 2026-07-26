# Design Systems Guide

> Pick the right foundation. Do not invent CSS for things that have an official package.

---

## When to Use a Real Design System

If the brief reads as one of these, install and use the **official** package:

| Brief reads as… | Reach for | Install |
|-----------------|-----------|---------|
| Microsoft / enterprise SaaS / dashboards | Fluent UI | `npm i @fluentui/react-components` |
| Google-ish UI, Material-flavored product | Material Web | `npm i @material/web` |
| IBM-style B2B / enterprise analytics | Carbon | `npm i @carbon/react @carbon/styles` |
| Shopify app surfaces | Polaris | `npm i @shopify/polaris` |
| Atlassian / Jira-style product | Atlaskit | `npm i @atlaskit/*` |
| GitHub-style devtool / community page | Primer | `npm i @primer/css` or `@primer/react-brand` |
| Public-sector UK service | GOV.UK Frontend | `npm i govuk-frontend` |
| US public-sector / trust-first | USWDS | `npm i @uswds/uswds` |
| Modern accessible React foundation | Radix Themes | `npm i @radix-ui/themes` |
| Modern SaaS (own the components) | shadcn/ui | `npx shadcn@latest add ...` |
| Tailwind-based modern SaaS / AI marketing | Tailwind v4 | `npm i tailwindcss@4` |

### Honesty Rule
If the brief reads as one of the systems above:
- Install and use the **official** package
- Do not recreate its CSS by hand
- Do not import a system's tokens but then override 90% of them

### One System Per Project
Do not mix Fluent React with Carbon in the same tree. Do not import shadcn/ui components into a Material 3 app.

---

## When the Brief Is an Aesthetic, Not a System

For these directions, there is **no single official package**. Build with native CSS + Tailwind + a maintained component library.

### Glassmorphism / "Frosted Glass"
```css
.glass-card {
  backdrop-filter: blur(16px) saturate(180%);
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.15);
}
```
Provide solid-fill fallback for `prefers-reduced-transparency`.

### Bento (Apple-style Tile Grids)
```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-flow: dense;
  gap: 1rem;
}
.bento-card-large { grid-column: span 2; grid-row: span 2; }
.bento-card-wide { grid-column: span 2; }
```
No single library owns this. Use CSS Grid with mixed cell sizes.

### Brutalism
- Native CSS, monospace fonts, raw borders
- No border-radius (all 90-degree corners)
- High-contrast light or dark modes
- Visible compartmentalization with solid borders

### Editorial / Magazine
- Serif type for headlines (only when justified by brief)
- Asymmetric grid, generous whitespace
- No library — pure CSS

### Dark Tech / Hacker
- Mono + accent neon (single color)
- Terminal motifs, ASCII decorations
- CRT scanlines via repeating-linear-gradient

### Aurora / Mesh Gradients
```css
.aurora-bg {
  background: 
    radial-gradient(ellipse at 20% 30%, rgba(120, 80, 200, 0.4) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 70%, rgba(50, 150, 200, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 50%, rgba(200, 100, 150, 0.2) 0%, transparent 70%);
}
```
SVG or layered radial gradients. No library.

---

## Apple Liquid Glass (Special Note)

Apple documents Liquid Glass for Apple platforms only. **There is no official `liquid-glass.css`.**

Web implementations are approximations using:
- `backdrop-filter`
- Layered borders
- Highlight overlays

Label clearly as approximation in code comments.

---

## Stack Defaults (When No System Is Chosen)

### Framework
- **React or Next.js** — default to Server Components (RSC)
- **RSC SAFETY:** Global state works ONLY in Client Components
- **INTERACTIVITY ISOLATION:** Components using Motion, scroll listeners, or pointer physics MUST be `'use client'`

### Styling
- **Tailwind v4** (default) — do NOT use `tailwindcss` plugin in postcss.config.js
- Use `@tailwindcss/postcss` or the Vite plugin

### Animation
- **Motion** (formerly Framer Motion) — import from `motion/react`
- `import { motion } from "motion/react"`
- The `framer-motion` package still works as legacy alias

### Fonts
- Always use `next/font` (Next.js) or self-host with `@font-face` + `font-display: swap`
- Never link Google Fonts via `<link>` in production

### State
- Local `useState` / `useReducer` for isolated UI
- Global state ONLY for deep prop-drilling avoidance (Zustand, Jotai, or React context)
- **NEVER** use `useState` for continuous values (mouse position, scroll progress) — use Motion's `useMotionValue` / `useTransform` / `useScroll`

---

## Responsiveness & Layout Mechanics

### Breakpoints
Standardize: `sm 640`, `md 768`, `lg 1024`, `xl 1280`, `2xl 1536`

### Container
Contain page layouts using `max-w-[1400px] mx-auto` or `max-w-7xl`

### Viewport Stability
- **NEVER** use `h-screen` for full-height Hero sections
- **ALWAYS** use `min-h-[100dvh]` to prevent layout jumping on mobile (iOS Safari address bar)

### Grid over Flex-Math
- **NEVER** use complex flexbox percentage math (`w-[calc(33%-1rem)]`)
- **ALWAYS** use CSS Grid (`grid grid-cols-1 md:grid-cols-3 gap-6`)

---

## Dependency Verification (Mandatory)

Before importing ANY 3rd-party library, check `package.json`. If the package is missing, output the install command first. **Never** assume a library exists.

---

*This guide is part of the frontend-design skill v2.0.0*
