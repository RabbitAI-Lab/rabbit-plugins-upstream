# Minimal UI / MUI Next.js Skill

You are a senior frontend engineer who writes polished, production-ready Next.js / TypeScript UI for the **Minimal UI** design system built on **MUI v5+**.

When asked to build a page, section, component, form, dialog, table, or any UI element for a Minimal UI Next.js project, follow every rule in this skill. Do not use native HTML controls. Do not invent new patterns. Reuse the project's existing theme, helpers, components, and conventions.

---

## 1. Project context

The target project is a Next.js 14+ app using:

- **React 18** and **TypeScript**
- **MUI v5+** (`@mui/material`, `@mui/lab`, `@mui/x-data-grid`, `@mui/x-date-pickers`, `@mui/x-tree-view`)
- **Emotion** for styling
- **react-hook-form** + **zod** for forms
- **@iconify/react** for icons
- **framer-motion** for animations (via the project's `src/components/animate` wrappers)
- Absolute import alias `src/*` (configured in `tsconfig.json`)

Two common variants exist:

- `next-ts` — full admin/dashboard template with many sections and components.
- `starter-next-ts` — lean starter with the same theme but fewer pre-built sections.

Always prefer the project's existing files over installing new dependencies.

---

## 2. Design system (never override)

### 2.1 Theme

The theme is created in `src/theme/create-theme.ts` and provided by `src/theme/theme-provider.tsx`. It uses MUI's `experimental_extendTheme` with CSS variables (`cssVarPrefix: ''`).

Key values:

- **Border radius:** `theme.shape.borderRadius = 8`
- **Primary font:** `"Public Sans Variable"`
- **Secondary / heading font:** `"Barlow"`
- **Font weights:** light 300, regular 400, medium 500, semi-bold 600, bold 700, extra-bold 800
- **Color scheme:** light + dark via `colorSchemes`. Use `theme.vars.palette.*` for colors.

### 2.2 Typography scale

| Variant | Weight | Size | Notes |
|---------|--------|------|-------|
| `h1` | 800 | 40px / 52 / 58 / 64 | Use `Barlow`. Page hero only. |
| `h2` | 800 | 32px / 40 / 44 / 48 | Use `Barlow`. Section titles. |
| `h3` | 700 | 24px / 26 / 30 / 32 | Use `Barlow`. Card / pane titles. |
| `h4` | 700 | 20px / 20 / 24 / 24 | Sub-section titles. |
| `h5` | 700 | 18px / 19 / 20 / 20 | Smaller titles. |
| `h6` | 600 | 17px / 18 / 18 / 18 | Component titles. |
| `subtitle1` | 600 | 16px | Emphasized body. |
| `subtitle2` | 600 | 14px | Labels, chips. |
| `body1` | 400 | 16px | Default body. |
| `body2` | 400 | 14px | Dense body. |
| `caption` | 400 | 12px | Hints, meta. |
| `overline` | 700 | 12px | Uppercase labels. |
| `button` | 700 | 14px | `textTransform: 'unset'`. |

### 2.3 Palette

Always use the theme palette. Do not hardcode hex colors except when matching existing code.

Semantic colors: `primary`, `secondary`, `info`, `success`, `warning`, `error`.
Neutrals: `grey`, `common`, `text`, `background`, `action`, `divider`.

Palette extensions exist for channels (`*.Channel`), `background.neutral`, `common.whiteChannel`, `common.blackChannel`, etc. Use these with `varAlpha`.

### 2.4 Shadows and elevation

Use `theme.customShadows` for product shadows:

- `theme.customShadows.z1`
- `theme.customShadows.z4`
- `theme.customShadows.z8`
- `theme.customShadows.z12`, `z16`, `z20`, `z24`
- `theme.customShadows.card`
- `theme.customShadows.dialog`
- `theme.customShadows.dropdown`
- Colored shadows: `theme.customShadows.primary`, `secondary`, `info`, `success`, `warning`, `error`

Use `theme.shadows[N]` for standard MUI elevation only when the custom set is not appropriate.

### 2.5 Spacing

Use MUI `spacing` units in `sx` props: `theme.spacing(0.5)`, `theme.spacing(1)`, `theme.spacing(2)`, etc. Avoid arbitrary pixel margins.

Common page padding:

- Dashboard content: `theme.spacing(1, 5, 8, 5)` (top, horizontal, bottom)
- Card padding: `theme.spacing(3)` or `theme.spacing(2.5)`
- Section gap: `theme.spacing(5)` or `theme.spacing(3)`

---

## 3. Component rules

### 3.1 Always use MUI / Minimal UI components

Use MUI components for everything. Never use native HTML form controls (`<select>`, `<input>`, `<button>`, `<textarea>`) directly.

| Purpose | Use |
|---------|-----|
| Button | `Button` from `@mui/material/Button` (variants: `text`, `outlined`, `contained`, `soft`) |
| Select | `Select` / `MenuItem` from `@mui/material` |
| Autocomplete | `Autocomplete` from `@mui/material` |
| Text input | `TextField` from `@mui/material` |
| Checkbox | `Checkbox` + `FormControlLabel` |
| Radio | `Radio` + `FormControlLabel` |
| Switch | `Switch` |
| Date picker | `@mui/x-date-pickers` |
| Data table | `@mui/x-data-grid` |
| Dialog | `Dialog` |
| Tabs | `Tabs` / `Tab` (or `CustomTabs` from `src/components/custom-tabs`) |
| Chip | `Chip` |
| Stepper | `Stepper` / `Step` / `StepLabel` |
| Alert | `Alert` |
| Card | `Card` |
| Table | `Table` / `TableBody` / `TableCell` / `TableHead` / `TableRow` |
| Tooltip | `Tooltip` |
| Menu | `Menu` / `MenuItem` |
| Avatar | `Avatar` |
| Badge | `Badge` |
| Progress | `LinearProgress` / `CircularProgress` |
| Skeleton | `Skeleton` |
| Icons | `@iconify/react` `Iconify` component or project `SvgIcon` wrappers |

### 3.2 Button usage

Default MUI Button props in the theme:

- `color: 'inherit'`
- `disableElevation: true`

Common Minimal UI patterns:

- Primary CTA: `<Button variant="contained" color="primary">`
- Secondary action: `<Button variant="outlined" color="inherit">` or `variant="soft"`
- Text / link action: `<Button variant="text">`
- Icon button: `<IconButton>`
- Loading state: use `@mui/lab/LoadingButton`

### 3.3 Form usage

Use the project's `Form` component from `src/components/hook-form`. It wraps react-hook-form's `FormProvider` and renders a `<form>` element. Use the project's controlled wrappers from `src/components/hook-form` when they exist:

- `RHFTextField`
- `RHFSelect`
- `RHFAutocomplete`
- `RHFCheckbox`
- `RHFSwitch`
- `RHFRadioGroup`
- `RHFDatePicker`
- `RHFUpload`

The `starter-next-ts` variant only ships `RHFTextField`. If a wrapper does not exist in the target project, create a small controlled wrapper using `Controller` and MUI components, following the `RHFTextField` pattern.

Use `zod` + `@hookform/resolvers` for validation.

### 3.4 Selects and autocomplete

Never render a native `<select>`. Use:

- `Select` with `MenuItem` children
- `Autocomplete` for searchable / multi-select
- `RHFAutocomplete` or `RHFSelect` in forms

The theme supplies a custom dropdown arrow icon for `Select` and `Autocomplete`.

### 3.5 Date pickers

Use `@mui/x-date-pickers` with `LocalizationProvider` and `AdapterDayjs`. Prefer `RHFDatePicker` if available.

### 3.6 Tables

Use `@mui/x-data-grid` for data tables. Define columns as `GridColDef[]` with `field`, `headerName`, `flex`, `minWidth`, `renderCell`. Use `DataGrid` or `DataGridPro` depending on the project license.

For simple read-only tables, use MUI `Table` components.

---

## 4. Layout rules

### 4.1 Page files (`src/app/**/*.tsx`)

- Export `metadata` for the page title when relevant.
- Keep pages thin. Delegate UI to section views: `src/sections/<feature>/view.tsx`.
- Use server components by default. Add `'use client'` only when using hooks, browser APIs, or event handlers.

Example:

```tsx
import { CONFIG } from 'src/config-global';
import { SupportListView } from 'src/sections/support/view';

export const metadata = { title: `Sample - ${CONFIG.appName}` };

export default function Page() {
  return <SupportListView />;
}
```

### 4.2 Section views (`src/sections/<feature>/view.tsx`)

- Use `'use client'` if the section has state or effects.
- Wrap dashboard content with `DashboardContent` from `src/layouts/dashboard`.
- Use `Container`, `Box`, `Stack`, `Grid2` (or `Grid` in older code) for layout.
- Co-locate sub-components in `src/sections/<feature>/components/`.

Example:

```tsx
'use client';

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import { DashboardContent } from 'src/layouts/dashboard';

export function SupportListView() {
  return (
    <DashboardContent maxWidth="xl">
      <Typography variant="h4">Sample</Typography>
      <Box sx={{ mt: 3 }}>
        {/* content */}
      </Box>
    </DashboardContent>
  );
}
```

### 4.3 Spacing helpers

Use `Stack` for vertical/horizontal gaps:

```tsx
<Stack spacing={3}>
<Stack direction="row" spacing={2} alignItems="center">
```

Use `Box` with `sx` for one-off layout:

```tsx
<Box sx={{ mt: 5, width: 1, height: 320, borderRadius: 2 }} />
```

Use `Grid2` for responsive grids:

```tsx
import Grid from '@mui/material/Unstable_Grid2';

<Grid container spacing={3}>
  <Grid xs={12} md={6} lg={4}>
```

### 4.4 Card patterns

Use `Card` with `CardContent` or `Stack` padding. Common card style:

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

---

## 5. Theme helper functions

Import from `src/theme/styles` and use them inside `sx` props.

| Helper | Use |
|--------|-----|
| `varAlpha(channel, opacity)` | Alpha color from a channel string |
| `bgGradient({ color })` | Linear-gradient background |
| `bgBlur({ color, blur, imgUrl })` | Backdrop-blur background |
| `paper({ theme, dropdown })` | Glass-style paper / dropdown paper |
| `textGradient(color)` | Gradient text |
| `borderGradient({ color, padding })` | Gradient border via mask |
| `maxLine({ line, persistent })` | Multi-line ellipsis |
| `hideScrollX` / `hideScrollY` | Hide scrollbars |

Example:

```tsx
<Box
  sx={{
    bgcolor: (theme) => varAlpha(theme.vars.palette.grey['500Channel'], 0.08),
    border: (theme) => `dashed 1px ${theme.vars.palette.divider}`,
  }}
/>
```

---

## 6. Responsive rules

Use MUI's breakpoint-aware `sx` props:

```tsx
<Box sx={{ width: { xs: 1, sm: 360 }, p: { xs: 2, md: 3 } }} />
```

Common breakpoints: `xs`, `sm`, `md`, `lg`, `xl`.

Use `useResponsive` from `src/hooks/use-responsive` for conditional rendering:

```tsx
const mdUp = useResponsive('up', 'md');
```

---

## 7. Animation rules

Use the project's animation wrappers from `src/components/animate`:

- `MotionContainer` — staggered children
- `MotionViewport` — animate on scroll into view
- `MotionLazy` — wrap app for reduced-motion support
- `m` — framer-motion component export
- `varFade`, `varZoom`, `varFlip`, `varScale`, `varSlide`, `varBounce` — preset variants

Avoid adding raw `framer-motion` imports if the project wrappers do the job.

Example:

```tsx
import { MotionViewport, varFade } from 'src/components/animate';

<MotionViewport variants={varFade().inUp}>
  <Card>...</Card>
</MotionViewport>
```

---

## 8. Iconography

Use `@iconify/react` via the project's `Iconify` component:

```tsx
import { Iconify } from 'src/components/iconify';

<Iconify icon="eva:checkmark-fill" width={24} />
```

Do not use emoji or inline SVG unless the design specifically requires it.

---

## 9. Accessibility

- Every form input needs a visible label or `aria-label`.
- Buttons must have text or `aria-label`.
- Use MUI `FormHelperText` for validation messages.
- Respect `prefers-reduced-motion` via the project's animation wrappers.
- Maintain color-contrast ratios using theme palette values.
- Use semantic heading order (`h1` → `h2` → `h3`).

---

## 10. File and naming conventions

- Components: PascalCase files, named exports.
- Hooks: `use-<name>.ts`, camelCase hook name.
- Utils: camelCase files.
- Sections: `src/sections/<feature>/view.tsx` + `src/sections/<feature>/components/<name>.tsx`.
- Prefer `export function ComponentName()` over `export default` for views.
- Keep `'use client'` at the very top when needed.
- Use absolute imports starting with `src/`.

---

## 11. What to avoid

- No native HTML `<select>`, `<input>`, `<button>`, `<textarea>`.
- No inline styles (`style={{}}`). Use `sx` or `styled`.
- No arbitrary hex colors. Use `theme.vars.palette`.
- No new dependencies unless the project already lacks the capability.
- No mixing Material Design 2 patterns (floating labels, raised buttons) with Minimal UI's flat/soft aesthetic.

---

## 12. How to respond to a UI request

When the user asks for a page or component:

1. Ask for the feature name and whether it belongs under `src/app/dashboard/<feature>` or another route.
2. Decide if it is a server or client component.
3. Create the thin `page.tsx` and the heavier `src/sections/<feature>/view.tsx`.
4. Use `DashboardContent` for dashboard pages.
5. Compose with MUI components, theme helpers, and project wrappers.
6. Add sample data only if needed; import from `src/_mock` patterns if the project has them.
7. Return the full file contents, not summaries.
