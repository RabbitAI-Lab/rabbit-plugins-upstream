# Rule 7 — Responsive Design

Use MUI's breakpoint-aware `sx` props and the `useResponsive` hook.

## Breakpoint values in sx

```tsx
<Box sx={{ width: { xs: 1, sm: 360 }, p: { xs: 2, md: 3 } }} />
```

Breakpoints: `xs` (0), `sm` (600), `md` (900), `lg` (1200), `xl` (1536).

## Grid

Use `Grid2` from `@mui/material/Unstable_Grid2` (or `Grid` from `@mui/material` in older code):

```tsx
import Grid from '@mui/material/Unstable_Grid2';

<Grid container spacing={3}>
  <Grid xs={12} md={6} lg={4}>
    <Card>...</Card>
  </Grid>
</Grid>
```

## useResponsive hook

```tsx
import { useResponsive } from 'src/hooks/use-responsive';

const mdUp = useResponsive('up', 'md');
const smDown = useResponsive('down', 'sm');
```

Use it for conditional rendering, not for styles that `sx` breakpoints can handle.

## Verification breakpoints

Test every dashboard page at these widths before delivering:

- **Desktop:** 1440px or wider — sidebar expanded, content sits to the right with no clipping.
- **Tablet:** 768px — sidebar collapsed or hidden, content reflows cleanly.
- **Mobile:** 375px — single-column layout, no horizontal scroll.

Common checks:

- No content is hidden behind the sidebar at desktop.
- Headings and stat cards are not cut off.
- Tables and data grids scroll horizontally inside their container, not the page.
- Cards do not overflow the viewport on mobile.
