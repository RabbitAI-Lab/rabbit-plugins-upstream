# Rule 2 — Design System

## Theme source

The theme is created in `src/theme/create-theme.ts` and provided by `src/theme/theme-provider.tsx`. It uses `experimental_extendTheme` with CSS variables (`cssVarPrefix: ''`).

## Core values

- **Border radius:** `theme.shape.borderRadius = 8`
- **Primary font:** `"Public Sans Variable"`
- **Secondary / heading font:** `"Barlow"`
- **Font weights:** light 300, regular 400, medium 500, semi-bold 600, bold 700, extra-bold 800

## Typography scale

| Variant | Weight | Size | Notes |
|---------|--------|------|-------|
| `h1` | 800 | 40 / 52 / 58 / 64 | Barlow, hero only |
| `h2` | 800 | 32 / 40 / 44 / 48 | Barlow, section titles |
| `h3` | 700 | 24 / 26 / 30 / 32 | Barlow, card titles |
| `h4` | 700 | 20 / 20 / 24 / 24 | Sub-section titles |
| `h5` | 700 | 18 / 19 / 20 / 20 | Smaller titles |
| `h6` | 600 | 17 / 18 / 18 / 18 | Component titles |
| `subtitle1` | 600 | 16 | Emphasized body |
| `subtitle2` | 600 | 14 | Labels, chips |
| `body1` | 400 | 16 | Default body |
| `body2` | 400 | 14 | Dense body |
| `caption` | 400 | 12 | Hints, meta |
| `overline` | 700 | 12 | Uppercase labels |
| `button` | 700 | 14 | `textTransform: 'unset'` |

## Color usage

Use semantic colors: `primary`, `secondary`, `info`, `success`, `warning`, `error`.
Use neutrals: `grey`, `common`, `text`, `background`, `action`, `divider`.

Palette has channel extensions (`*.Channel`, `background.neutral`, `common.whiteChannel`, `common.blackChannel`). Use these with `varAlpha`.

## Shadows

Prefer `theme.customShadows`:

- `z1`, `z4`, `z8`, `z12`, `z16`, `z20`, `z24`
- `card`, `dialog`, `dropdown`
- `primary`, `secondary`, `info`, `success`, `warning`, `error`

Use `theme.shadows[N]` only when a standard MUI elevation is required.

## Spacing

Use `theme.spacing(n)` inside `sx` props. Common values:

- Page padding: `theme.spacing(1, 5, 8, 5)`
- Card padding: `theme.spacing(3)`
- Section gap: `theme.spacing(5)` or `theme.spacing(3)`
