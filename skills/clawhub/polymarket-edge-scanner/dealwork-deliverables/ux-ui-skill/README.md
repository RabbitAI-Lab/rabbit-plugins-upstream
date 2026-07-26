# Minimal UI / MUI UX/UI Skill for Claude & Codex

A reusable, multi-file UX/UI skill package that teaches Claude and Codex to generate polished Next.js / TypeScript UI matching the **Minimal UI** design system.

## What is inside

- `SKILL.md` — main instruction file for Claude projects.
- `.codex.md` — instruction file for Codex workspaces.
- `INSTALLATION.md` — step-by-step setup for Claude, Codex, and existing Minimal UI projects.
- `rules/` — eight focused rule modules covering identity, design system, components, layout, forms, animations, responsiveness, and accessibility.
- `examples/` — two prompt-to-output examples:
  - Dashboard stat card
  - User edit form
- `sample/` — a Next.js / TypeScript support-ticket page (`/dashboard/support`) that demonstrates:
  - Tabs (`CustomTabs`)
  - Stat cards (`Card`, `Stack`, `Iconify`, `varAlpha`)
  - Data grid (`DataGrid` with toolbar)
  - Form with validation (`react-hook-form` + `zod`)
  - MUI `Select` (no native `<select>`)
  - `Autocomplete` with chips
  - `DatePicker`
  - `Switch`
  - Stepper
  - Buttons (`contained`, `outlined`, `soft`)
  - Alert feedback

## How to use

1. Add `SKILL.md` to your Claude project instructions (or `.codex.md` for Codex).
2. Optionally include the `rules/` folder for richer context.
3. Copy `sample/src/app/dashboard/support` and `sample/src/sections/support` into your Minimal UI Next.js project,
   keeping the paths exactly as they are. The route must stay under `src/app/dashboard/` to inherit the sidebar and header.
4. Run `npm run dev` / `yarn dev` and open `/dashboard/support`.

## Compatibility

The skill is written for both the full `next-ts` and the `starter-next-ts` Minimal UI variants:

- Uses MUI components directly so no custom wrapper dependency is required.
- Uses the project's `Form` component from `src/components/hook-form`.
- Uses helpers (`varAlpha`, `Iconify`, `Label`, `CustomTabs`, `DashboardContent`) that exist in both variants.
- The sample has been type-checked against `starter-next-ts` with `tsc --noEmit`.

## Deliverable checklist

- [x] Complete reusable skill/instruction file for Claude & Codex
- [x] Installation and usage guidance
- [x] Concrete rules for layout, spacing, typography, color, responsive behavior, states, accessibility, and component selection
- [x] No native HTML controls
- [x] Runnable Next.js / TypeScript sample following project conventions
- [x] Example prompt/output pairs
