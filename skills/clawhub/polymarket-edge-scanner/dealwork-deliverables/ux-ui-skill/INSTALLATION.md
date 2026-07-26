# Installation & Usage Guide

This package contains a reusable UX/UI skill for generating Minimal UI / MUI-themed Next.js TypeScript code in Claude and Codex.

## Package contents

```
.
├── SKILL.md                 # Main instruction file for Claude
├── .codex.md                # Codex instruction file
├── INSTALLATION.md          # This file
├── rules/                   # Detailed rule modules
│   ├── 01-identity.md
│   ├── 02-design-system.md
│   ├── 03-components.md
│   ├── 04-layout.md
│   ├── 05-forms.md
│   ├── 06-animations.md
│   ├── 07-responsive.md
│   └── 08-accessibility.md
├── examples/                # Prompt → output examples
│   ├── prompt-dashboard-card.md
│   ├── output-dashboard-card.tsx
│   ├── prompt-user-form.md
│   └── output-user-form.tsx
└── sample/                  # Runnable Next.js sample
    └── src/
        ├── app/dashboard/support/page.tsx
        └── sections/support/
            ├── view.tsx
            ├── components/
            │   ├── stat-card.tsx
            │   └── recent-users.tsx
            └── hooks/
                └── use-sample-data.ts
```

## Claude setup

1. Open your Claude project or conversation.
2. Go to **Project settings** → **Skills**.
3. Upload `SKILL.md` (or paste its contents into the project instructions).
4. For best results, also upload the `rules/` folder so Claude can reference detailed modules.
5. Start prompting with features you want built.

Example prompt:

```text
Build a dashboard analytics page at /dashboard/analytics with:
- a header "Analytics overview"
- four stat cards (Total users, Revenue, Orders, Bounce rate)
- a recent orders data grid
All using Minimal UI / MUI components.
```

## Codex setup

1. Open your Codex workspace or project.
2. Add `.codex.md` to the project root or paste it into the system instructions.
3. Optionally include the `rules/` files for deeper context.
4. Prompt Codex with the feature you want.

## Applying to an existing next.ts project

1. Copy the skill files into the root of your Minimal UI Next.js project (next to `package.json`).
2. Verify the project uses the same conventions:
   - `src/theme/styles` helpers exist.
   - `src/layouts/dashboard` exists.
   - `src/components/hook-form` wrappers exist.
   - Absolute imports use `src/*`.
3. If your project is the `starter-next-ts` variant, some components may not exist. Generate only what is available, or copy the needed component from the full `next-ts` variant.
4. When prompting, reference the specific route and feature name so the generated files land in the right place.

## How to test the sample

1. Copy the contents of `sample/src/` into your Minimal UI Next.js project's `src/` folder.
2. Make sure your project has `DashboardContent` available in `src/layouts/dashboard`.
3. Keep the page under `src/app/dashboard/`. The sidebar and header come from `src/app/dashboard/layout.tsx`;
   a page placed outside that tree renders with no shell. Optionally add `/dashboard/support` to your nav config.
4. Run `npm run dev` or `yarn dev` and visit `http://localhost:<port>/dashboard/support`.

## Tips for best results

- Be specific about the route (`/dashboard/<feature>` vs `/blank/<feature>`).
- Mention whether the page needs form validation, data tables, dialogs, or animations.
- Ask the model to reuse existing project components before creating new ones.
- Review generated code for any missing imports or unavailable components in the starter variant.
