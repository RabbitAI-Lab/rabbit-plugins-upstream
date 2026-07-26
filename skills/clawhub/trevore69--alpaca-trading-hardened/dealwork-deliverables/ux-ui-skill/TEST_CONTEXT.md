# Test Context

Everything below was run against the `next-ts` project from the Google Drive archive you supplied
(`MinimalUI_v6` -> `Minimal_TypeScript_v6.1.0` -> `next-ts`). No starter, substitute repo, or mocked
environment was used.

## Target

| Item | Value |
|---|---|
| Project | `Minimal_TypeScript_v6.1.0/next-ts` (from your Drive archive) |
| Next.js | 14.2.5 (App Router) |
| MUI | 5.16.7 |
| Node | v22.23.1 |
| Package manager | npm (project's existing `package-lock.json`) |
| Dev port | 8082 (the project's own `next dev -p 8082`) |
| Final route | `/dashboard/support` |

## Prompt used to generate the page

```
Using the Minimal UI next-ts project, generate a support ticket management page.

Placement:
- The page must live at src/app/dashboard/support/page.tsx so it inherits DashboardLayout
  (sidebar + header) from src/app/dashboard/layout.tsx.
- page.tsx stays thin: export metadata, render a view from src/sections/support/view.
- The view wraps its content in DashboardContent from src/layouts/dashboard.

Purpose:
- One real business purpose: triage and manage inbound support tickets.
- Page header via CustomBreadcrumbs (heading + links + a primary "New ticket" action).
- Four summary figures, status tabs with counts, search + priority filter.
- A ticket table: subject/reference, requester, priority, status, last updated, row actions.

Workflows:
- Dialog: "New ticket" — subject, requester email, priority, description; Cancel / Create.
- Menu: per-row overflow — View details, Assign to me, Mark as resolved, Delete.
- Delete routes through the project's ConfirmDialog.

Conventions:
- Reuse the project's own components: Label, Iconify, Scrollbar, CustomBreadcrumbs,
  ConfirmDialog, usePopover/CustomPopover, useBoolean, useSetState, toast,
  and the src/components/table primitives (useTable, TableHeadCustom, TablePaginationCustom).
- Typography: use existing variants only. Page title = CustomBreadcrumbs heading (h4).
  Do not use h1/h2/h3 (Barlow display sizes) for a dashboard page title.
- No native HTML controls. No custom design system. No meta commentary about the implementation.
```

## Typography rule (verified in your theme, not assumed)

Read directly from `src/theme/core/typography.ts`:

- `secondaryFont` = **Barlow**, applied to `h1`, `h2`, `h3` **only**.
- `primaryFont` = **Public Sans Variable**, used for `h4`, `h5`, `h6`, `subtitle*`, `body*`, and all UI text.
- The page therefore uses `h4` for the page title and for stat numerals, and `subtitle2`/`body2`/
  `caption` beneath. Nothing in the page uses `h1`–`h3`, which is why the type ramp stays restrained.

## Commands run

```bash
cd Minimal_TypeScript_v6.1.0/next-ts
npm install --no-audit --no-fund            # 1190 packages, exit 0
npm run dev                                 # next dev -p 8082
npx tsc --noEmit                            # 0 errors in the added files
npx eslint "src/sections/support/**/*.{ts,tsx}" "src/app/dashboard/support/**/*.tsx"   # exit 0
npm run build                               # next build
```

## Interaction tests

Driven with a real headless Chrome session against the running dev server, not by inspection:

| Check | Result |
|---|---|
| `GET /dashboard/support/` | HTTP 200 |
| Dashboard shell (sidebar + header) inherited from layout | pass |
| Dialog: focus lands on Subject on open | pass |
| Dialog: Create disabled until subject + requester email present | pass |
| Dialog: Create adds the ticket to the top of the table | pass |
| Dialog: closes on Escape and on Cancel | pass |
| Menu: opens from row overflow button | pass |
| Menu: items = View details / Assign to me / Mark as resolved / Delete | pass |
| Menu: "Assign to me" sets row status to In progress | pass |
| Menu: closes after selection and on Escape | pass |

## Authentication flag used for testing

To view `/dashboard` without signing in, the project's own supported flag was used:

- File: `src/config-global.ts`
- Original value: `auth: { method: 'jwt', skip: false, ... }`
- Temporary value during screenshots: `skip: true`
- **Restored to `skip: false` before packaging.**

This is the project's documented flag, not a workaround, and no other auth code was touched.

## Screenshots

All screenshots in `screenshots/` were captured from this running project at `localhost:8082`,
at the route above, from the exact code in `sample/`. Viewports: desktop 1440px wide, mobile 375px.
No mockups, composites, or edited images.
