---
name: type-scale-generator
description: Use when generating a full typographic scale (H1-H6, body, caption) from a base font size and a mathematical ratio or historical scale — outputs CSS custom properties or Tailwind config, rounded to avoid subpixel rendering.
triggers:
  use_when:
    - user asks to generate a type scale
    - user asks for a font-size system based on a ratio (e.g. "minor third", "perfect fourth")
    - user asks to build h1-h6 sizes for a design system
    - user asks for a fluid/responsive type scale with clamp()
  do_not_use_for:
    - a single text style's line-height/tracking (see text-typesetting)
    - vertical rhythm between blocks (see vertical-spacing)
    - column width (see line-length-optimizer)
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: 1.0
  status: accepted
---

# Type Scale Generator

## Purpose

Generate a mathematically coherent set of font sizes from a base size and a ratio (or a historical fixed-step scale), rounded to avoid subpixel rendering artifacts, output as ready-to-use design tokens.

## When To Use

- Building a font-size system for a new design system or page.
- User names a musical/geometric ratio ("minor third", "1.25", "golden ratio") or asks for a scale without specifying one.
- Not for a single text style's line-height/tracking (`text-typesetting`) or spacing between elements (`vertical-spacing`).

## Inputs

- `base-size`: default `16px`.
- `scale-ratio`: one of the named/numeric ratios below, or `fibonacci` / `classic-garamond`.
- `steps`: how many sizes up (headings) and down (caption/small) from base — default 4 up, 1 down (covers body, small, h4, h3, h2, h1).
- `responsiveness`: static or fluid (`clamp()`).

## Outputs

- A named token map (CSS custom properties or Tailwind `fontSize` config, matching whichever convention the project already uses).
- Each value shown with its raw computed number and the rounded value actually used, so the rounding decision is auditable.

## Workflow

### Step 1 — Pick the ratio

**Musical/geometric ratios** (`size = base × ratio^step`):

| Ratio | Name | Character |
|---|---|---|
| `1.067` | Minor Second | Very compact — dense dashboards, data-heavy mobile UI. Pair with a small base (12–14px) so headings don't dominate. |
| `1.125` | Major Second | Standard for SaaS apps and complex dashboards — subtle, clean hierarchy. |
| `1.200` | Minor Third | Safe, universal default — works for both product UI and marketing pages. |
| `1.250` | Major Third | Blogs and marketing pages where headings need to clearly separate from body. |
| `1.333` | Perfect Fourth | Latin's recommended starting point for responsive web — very readable on desktop. |
| `1.414` | Augmented Fourth | Bold, dynamic, poster-like character. |
| `1.500` | Perfect Fifth | Aggressive — H1 becomes very large. Portfolio / product-launch pages. |
| `1.618` | Golden Ratio | Bringhurst's classic proportion. Grows extremely fast at higher steps — usually needs a smaller ratio on mobile breakpoints. |

**Non-linear / historical scales** (fixed steps, not a single multiplier):

- `fibonacci`: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...` — map directly to px or rem (e.g. body 13/21px, H1 55/89px). Use when the layout grid itself is Fibonacci-proportioned, so type and grid share the same logic.
- `classic-garamond`: `6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72` — the historical printer's type-size series (pre-digital, renaissance-era steps). Use when a project wants a traditional/editorial feel over a computed geometric curve; pick the nearest listed step rather than interpolating.

If the user doesn't specify, default to `1.200` (Minor Third) — safe, universal, per the table above.

### Step 2 — Compute steps

For geometric ratios: `size(step) = base-size × ratio^step`, where `step` is negative for sizes below base (caption/small) and positive above (headings). Show the raw (unrounded) result before applying Step 3.

For `fibonacci`/`classic-garamond`: pick the nearest sequence value to each target role rather than computing — these are lookup tables, not formulas.

### Step 3 — Edge-case & rounding guard

1. **Round every computed value to the nearest even integer or multiple of 4px** where reasonably close (e.g. `16 × 1.333 = 21.328` → round to `22px`, and prefer `24px` if the project's spacing grid is 4px/8px-based and a 4px-multiple is within ~1px). State which rounding was applied — don't silently pick one without showing the raw number.
2. **Minimum readability threshold** (Refactoring UI): UI body text must never go below `12px`, and never pair a sub-`12px` size with a font-weight below `400`. Flag and refuse to emit a token that violates this, rather than emitting it silently.
3. If `responsiveness: fluid`, wrap the two endpoint sizes (mobile base, desktop computed size) in a `clamp(min, preferred, max)` — compute `preferred` as a `vw`-based interpolation between the two breakpoints; state the breakpoints assumed.

### Step 4 — Output

Emit as CSS custom properties (or the project's existing token format if shown in the input):

```css
--text-sm: 0.833rem;   /* 13.33px → rounded 13px */
--text-base: 1rem;     /* 16px */
--text-md: 1.2rem;     /* 19.2px → rounded 20px */
--text-lg: 1.44rem;    /* 23.04px → rounded 24px */
```

## Figma Node Integration

When running with Figma access and asked to apply the scale to existing text styles:

- Read the file's existing type styles (`getLocalTextStylesAsync` or equivalent) to detect whether a scale is already in use, so the new scale doesn't silently fragment the system.
- Write new/updated Figma text styles with the rounded `fontSize` values from Step 3 — never the raw unrounded ratio output, since Figma renders fractional sizes with the same subpixel risk as CSS.
- Report the full token map before writing; only apply directly to the file on explicit request.

## Quality Checklist

- [ ] Ratio (or fibonacci/garamond) explicitly named in the output, not just numbers with no source.
- [ ] Every value shows raw computed number alongside the rounded value actually used.
- [ ] Rounding follows the even-integer/4px-multiple guard, not ad hoc.
- [ ] No token below 12px paired with weight < 400.
- [ ] Fluid scale (if requested) states the assumed breakpoints.
- [ ] Output format matches the project's existing token convention if one is shown in the input.

## References

- Bringhurst, R. (2012). *The Elements of Typographic Style* (4th ed.). Hartley & Marks — golden ratio and classical proportion systems in typography.
- Latin, M. (2017). *Better Web Typography for a Better Web*. — practical ratio recommendations for responsive web type scales (Perfect Fourth as a starting point).
- Santa Maria, J. (2014). *On Web Typography*. A Book Apart — musical-interval scales and the Fibonacci sequence as alternatives to a single fixed ratio.
- Kunz, W. (1998). *Typography: Macro- and Microaesthetics*. Niggli — historical printer's type-size series (Garamond-era steps).
- Felici, J. (2003). *The Complete Manual of Typography*. Adobe Press — traditional point-size series predating digital, arbitrary-precision scales.
- Wathan, A., Schoger, S. (2018). *Refactoring UI*. — minimum readable UI text size (12px floor) and its interaction with font weight.
- Related skills: [`text-typesetting`](../text-typesetting/README.md) (line-height/tracking per size), [`vertical-spacing`](../vertical-spacing/README.md) (rhythm between the blocks this scale produces).
