# Rule 4 — Layout

## Route placement (most important rule in this file)

The dashboard shell (sidebar + header) is applied by `src/app/dashboard/layout.tsx`, **not** by
`DashboardContent`. A page only gets the sidebar and header if its route sits inside the
`src/app/dashboard/` tree.

```
src/app/dashboard/<route>/page.tsx   ✅ inherits DashboardLayout: sidebar, header, spacing
src/app/<route>/page.tsx             ❌ no shell — DashboardContent renders bare on a blank page
```

`DashboardContent` does **not** add the sidebar. It is only the content container inside the shell.
Putting a dashboard page outside `src/app/dashboard/` produces a page with no sidebar and no header,
with content flush to the left edge of the viewport. This is the single most common way to generate a
"broken" looking page, and it cannot be fixed with styling.

Verify placement before styling anything:

```bash
# the generated page must be under this path
ls src/app/dashboard/<route>/page.tsx
```

Never recreate the sidebar or header inside the page to compensate. Move the route instead.

## Page files

Keep `src/app/**/*.tsx` thin. Export `metadata` and delegate UI to a section view.

```tsx
import { CONFIG } from 'src/config-global';
import { SupportListView } from 'src/sections/support/view';

export const metadata = { title: `Sample - ${CONFIG.appName}` };

export default function Page() {
  return <SupportListView />;
}
```

## Section views

Place page-level UI in `src/sections/<feature>/view/` and re-export it from `view/index.ts`.

- Use `'use client'` only when needed.
- Wrap dashboard pages with `DashboardContent` from `src/layouts/dashboard`.
- Co-locate sub-components in `src/sections/<feature>/components/`.

## Layout primitives

- `Box` for one-off containers and `sx` styling.
- `Stack` for vertical/horizontal flow with gaps.
- `Grid2` (or `Grid`) for responsive grids.
- `Container` for centered max-width content.

Examples:

```tsx
<Stack spacing={3}>
<Stack direction="row" spacing={2} alignItems="center">
<Grid container spacing={3}>
  <Grid xs={12} md={6} lg={4}>
```

## Card patterns

```tsx
<Card>
  <CardContent>
    <Typography variant="h6">Title</Typography>
    <Typography variant="body2" sx={{ color: 'text.secondary' }}>
      Description
    </Typography>
  </CardContent>
</Card>
```

## Dashboard layout (critical)

Dashboard pages must never clip content behind the sidebar. Follow these rules exactly.

### Use `DashboardContent`

Every dashboard page must be wrapped in `DashboardContent` from `src/layouts/dashboard`. It already accounts for the sidebar width and header height.

```tsx
import { DashboardContent } from 'src/layouts/dashboard';

export function PageView() {
  return (
    <DashboardContent maxWidth="xl">
      {/* page content */}
    </DashboardContent>
  );
}
```

- `maxWidth` can be `xl`, `lg`, `md`, `sm`, `xs`, or `false` for full width.
- Do not add manual left margins such as `ml: '280px'` to offset the sidebar.
- Do not use `position: fixed` or `absolute` for the main content area.

### Avoid fixed widths that collide with the sidebar

Do not set explicit pixel widths on outer containers unless they are inside a flex item that already respects the available space. Prefer percentage or flex-based layouts.

Bad:
```tsx
<Box sx={{ width: 1440 }}>...</Box>
```

Good:
```tsx
<Box sx={{ width: '100%' }}>...</Box>
```

### Overflow and spacing

- Keep the page `Stack` as the first child of `DashboardContent`.
- Use `spacing={3}` or `spacing={5}` for vertical rhythm.
- Wide tables: wrap in `Scrollbar` and set a `minWidth` on the `Table` so the table scrolls
  horizontally inside its card instead of overflowing the page:
  `<Scrollbar sx={{ minHeight: 444 }}><Table sx={{ minWidth: 960 }}>`.
  The page itself must never scroll horizontally.
- Stat cards and charts should use responsive grids, not fixed columns.

### Visual hierarchy

- Page title: use `CustomBreadcrumbs heading="..."`, which renders `h4` (Public Sans). Do not use
  `h1`/`h2`/`h3` for a dashboard page title — those are Barlow display sizes meant for marketing
  pages, and they are the main cause of a page reading as a generic AI dashboard.
- Metric numerals in stat cards: `h4`. Do not exceed `h4`; oversized numerals break the type ramp.
- Section title inside card: `variant="h6"`.
- Card padding: `theme.spacing(3)`.
- Gap between cards: `theme.spacing(3)`.
- Never let headings or card content touch the sidebar edge. If content appears clipped, the page is missing `DashboardContent` or using a fixed width.
