# Output Format Specification

Specifies the exact format for each file in the generated style skill, using the three-layer token architecture.

## SKILL.md

### YAML Frontmatter (Machine-Parseable)

Every generated style skill MUST include a YAML frontmatter block with structured token data. This is for machine parsing AND human reading:

```yaml
---
name: brand-style-{name}
description: Reusable UI style skill extracted from {source}. Contains three-layer design tokens (P primitive + S semantic + C component) with evidence grading. Load this skill when generating UI matching the {name} visual language.
version: "1.0"
source: {url_or_path}
source_type: url | screenshot | project
extracted_at: {ISO date}
evidence_summary:
  defined: {count}      # grade D
  measured: {count}     # grade M
  inferred: {count}     # grade I
  assumed: {count}      # grade A
token_summary:
  primitive_colors: {count}
  semantic_colors: {count}
  component_colors: {count}
  primitive_typography: {count}
  semantic_typography: {count}
  primitive_spacing: {count}
  semantic_spacing: {count}
  components: {count}
theme_support: none | light_dark | multi_brand
---
```

### Body Structure

```markdown
# {Name} Design Style

[2-4 sentence overview: aesthetic, key characteristics, source, extraction method, evidence quality.]

## Token Architecture

This style uses a three-layer token system:

| Layer | Purpose | Count | Example |
|-------|---------|-------|---------|
| **Primitive** | Raw design materials | {N} | `color.blue.500`, `space.4`, `radius.md` |
| **Semantic** | Design roles | {N} | `color.action.primary`, `color.bg.surface` |
| **Component** | Per-component overrides | {N} | `button.primary.bg.default` |

## Quick Reference — CSS Variables

```css
:root {
  /* Primitive */
  --color-blue-500: #XXXXXX;
  --space-4: 16px;
  --radius-md: 4px;

  /* Semantic */
  --color-action-primary: var(--color-blue-500);
  --color-bg-surface: #FFFFFF;
  --color-text-primary: #XXXXXX;

  /* Component */
  --button-primary-bg-default: var(--color-action-primary);
}
```

## Theme Mappings (if applicable)

| Semantic Token | Light Theme | Dark Theme |
|---------------|-------------|------------|
| `color.bg.page` | `#F7F8FA` | `#17171A` |
| `color.bg.surface` | `#FFFFFF` | `#232324` |
| `color.text.primary` | `#1D2129` | `rgba(255,255,255,.9)` |

> Note: `color.bg.surface` (light) and `color.text.on.action` (dark) both resolve to `#FFFFFF` but MUST remain separate semantic tokens — they serve different roles and change independently.

## Using This Style

To generate UI matching this style:
1. **Reference semantic tokens** in component code, not primitive values
2. **Primitive tokens** are building materials — use only through semantic aliases
3. **Component tokens** exist only where semantic defaults don't fit

## References

- `references/colors.md` — Primitive color scales + Semantic color roles + Theme mappings
- `references/typography.md` — Primitive font scale + Semantic text roles
- `references/spacing.md` — Primitive spacing/radius/shadow scales + Semantic layout roles
- `references/components.md` — Component tokens, patterns, variants, and state mappings
- `references/known-gaps.md` — Unresolved discrepancies, exceptions, and assumptions needing review
```

## references/colors.md

MUST use three-layer structure with evidence column:

```markdown
# Color Palette — {Name}

> Extracted from: {source} | Evidence quality: {high/medium/low based on D+M vs I+A ratio}

## Primitive: Color Scales

### Blue Scale
| Token | Hex | Evidence | Notes |
|-------|-----|----------|-------|
| `color.blue.50` | `#E8F3FF` | D | Lightest |
| `color.blue.500` | `#165DFF` | D | Default interaction |
| `color.blue.900` | `#001B4D` | D | Darkest |

### Neutral/Gray Scale
| Token | Hex | Evidence | Notes |
|-------|-----|----------|-------|
| `color.gray.50` | `#F7F8FA` | D | Lightest |
| `color.gray.500` | `#86909C` | D | Mid-gray |
| `color.gray.900` | `#1D2129` | D | Near-black |

### Additional Color Scales
[Red, Green, Yellow, Orange, Purple, etc. — same format]

## Semantic: Design Roles

| Token | Maps To | Light Theme | Dark Theme | Evidence | Notes |
|-------|---------|-------------|------------|----------|-------|
| `color.action.primary` | `color.blue.500` | `#165DFF` | `#4080FF` | I | Buttons, links, focus rings |
| `color.action.primary.hover` | `color.blue.400` | `#4080FF` | `#5C9DFF` | I | Hover state |
| `color.action.primary.active` | `color.blue.600` | `#0E42D2` | `#2B6AE6` | I | Active/pressed state |
| `color.action.primary.disabled` | `color.blue.200` | `#BEDAFF` | `#4A6FA5` | I | Disabled state |
| `color.bg.page` | `color.gray.50` | `#F7F8FA` | `#17171A` | I | Page background |
| `color.bg.surface` | white | `#FFFFFF` | `#232324` | I | Card/panel background |
| `color.bg.surface.hover` | `color.gray.50` | `#F7F8FA` | `#2B2B2D` | I | Hovered surface |
| `color.text.primary` | `color.gray.900` | `#1D2129` | `rgba(255,255,255,.9)` | I | Headings, body |
| `color.text.secondary` | `color.gray.600` | `#4E5969` | `rgba(255,255,255,.7)` | I | Captions, descriptions |
| `color.text.tertiary` | `color.gray.500` | `#86909C` | `rgba(255,255,255,.5)` | I | Placeholders, hints |
| `color.text.disabled` | `color.gray.400` | `#C9CDD4` | `rgba(255,255,255,.3)` | I | Disabled text |
| `color.text.on.action` | white | `#FFFFFF` | `#FFFFFF` | I | Text on primary buttons |
| `color.border.default` | `color.gray.200` | `#E5E6EB` | `#353537` | I | Default borders |
| `color.status.success` | `color.green.500` | `#00B42A` | `#27C346` | I | Success |
| `color.status.warning` | `color.orange.500` | `#FF7D00` | `#FF9A2E` | I | Warning |
| `color.status.danger` | `color.red.500` | `#F53F3F` | `#F76560` | I | Error/danger |
| `color.status.info` | `color.blue.500` | `#165DFF` | `#4080FF` | I | Informational |

### Same-Value / Different-Semantic Alerts

| Value | Token A | Token B | Why Separate |
|-------|---------|---------|-------------|
| `#FFFFFF` | `color.bg.surface` (light) | `color.text.on.action` (both) | Different roles, change independently with theme |

## Component: Per-Element Tokens

| Token | Maps To | Evidence | Notes |
|-------|---------|----------|-------|
| `button.primary.bg.default` | `color.action.primary` | I | |
| `button.primary.bg.hover` | `color.action.primary.hover` | I | |
| `input.border.focus` | `color.action.primary` (20% alpha) | I | |

> Only tokens that genuinely differ from semantic defaults are listed here.
> Components that use semantic tokens directly (e.g., buttons using `color.action.primary`) are documented in components.md, not re-declared here.

## CSS Variables

```css
:root {
  /* === Primitive: Color Scales === */
  --color-blue-50: #E8F3FF;
  /* ... all primitives ... */

  /* === Semantic: Design Roles === */
  --color-action-primary: var(--color-blue-500);
  --color-bg-page: var(--color-gray-50);
  --color-bg-surface: #FFFFFF;
  --color-text-primary: var(--color-gray-900);
  /* ... all semantics ... */

  /* === Dark Theme Overrides === */
  [data-theme="dark"] {
    --color-action-primary: #4080FF;
    --color-bg-page: #17171A;
    --color-bg-surface: #232324;
    --color-text-primary: rgba(255, 255, 255, 0.9);
    /* ... all overrides ... */
  }
}
```
```

## references/typography.md

```markdown
# Typography — {Name}

> Extracted from: {source} | Evidence quality: {level}

## Primitive: Font Scale

### Font Families
| Token | Stack | Evidence | Notes |
|-------|-------|----------|-------|
| `font.family.primary` | `Inter, -apple-system, ...` | D | UI text |
| `font.family.mono` | `Menlo, Consolas, monospace` | D | Code |

### Size Scale
| Token | Size | Evidence |
|-------|------|----------|
| `font.size.xs` | 12px / 0.75rem | D |
| `font.size.sm` | 13px / 0.8125rem | D |
| `font.size.base` | 14px / 0.875rem | D |
| `font.size.lg` | 16px / 1rem | D |
| `font.size.xl` | 20px / 1.25rem | D |
| `font.size.2xl` | 24px / 1.5rem | D |
| `font.size.3xl` | 30px / 1.875rem | D |

### Weight Scale
| Token | Weight | Evidence |
|-------|--------|----------|
| `font.weight.normal` | 400 | D |
| `font.weight.medium` | 500 | D |
| `font.weight.semibold` | 600 | D |
| `font.weight.bold` | 700 | D |

### Line Height Scale
| Token | Value | Evidence |
|-------|-------|----------|
| `font.leading.tight` | 1.2 | D |
| `font.leading.normal` | 1.5715 | D |
| `font.leading.relaxed` | 1.8 | D |

## Semantic: Text Roles

| Token | Family | Size | Weight | Leading | Evidence | Usage |
|-------|--------|------|--------|---------|----------|-------|
| `text.heading.page` | primary | `font.size.3xl` | `font.weight.bold` | `font.leading.tight` | I | Page titles |
| `text.heading.section` | primary | `font.size.2xl` | `font.weight.semibold` | 1.3 | I | Section headings |
| `text.heading.card` | primary | `font.size.xl` | `font.weight.medium` | 1.3 | I | Card titles |
| `text.body` | primary | `font.size.base` | `font.weight.normal` | `font.leading.normal` | I | Body text |
| `text.body.small` | primary | `font.size.sm` | `font.weight.normal` | 1.5 | I | Secondary text |
| `text.caption` | primary | `font.size.xs` | `font.weight.normal` | 1.4 | I | Captions, meta |
| `text.code` | mono | `font.size.sm` | `font.weight.normal` | 1.5 | I | Code blocks |

## CSS Variables

```css
:root {
  --font-family-primary: Inter, -apple-system, ...;
  --font-size-base: 14px;
  --text-heading-page: 700 30px/1.2 var(--font-family-primary);
}
```
```

## references/spacing.md

```markdown
# Spacing & Sizing — {Name}

> Extracted from: {source} | Evidence quality: {level}

## Primitive: Spacing Scale

| Token | px | rem | Evidence |
|-------|----|-----|----------|
| `space.0` | 0 | 0 | D |
| `space.1` | 4px | 0.25rem | D |
| `space.2` | 8px | 0.5rem | D |
| `space.3` | 12px | 0.75rem | D |
| `space.4` | 16px | 1rem | D |
| `space.5` | 20px | 1.25rem | D |
| `space.6` | 24px | 1.5rem | D |
| ... | | | |

## Primitive: Radius Scale
| Token | Value | Evidence |
|-------|-------|----------|
| `radius.none` | 0 | D |
| `radius.sm` | 2px | D |
| `radius.md` | 4px | D |
| `radius.lg` | 8px | D |
| `radius.full` | 9999px | D |

## Primitive: Shadow Scale
| Token | CSS Box-Shadow | Evidence |
|-------|---------------|----------|
| `shadow.none` | `none` | D |
| `shadow.sm` | `0 1px 2px 0 rgba(0,0,0,.06)` | D |
| `shadow.md` | `0 4px 10px 0 rgba(0,0,0,.08)` | D |
| `shadow.lg` | `0 8px 24px 0 rgba(0,0,0,.12)` | D |

## Primitive: Z-Index Scale
| Token | Value | Evidence |
|-------|-------|----------|
| `z.base` | 0 | D |
| `z.dropdown` | 1000 | D |
| `z.sticky` | 1100 | D |
| `z.modal` | 1300 | D |
| `z.notification` | 1500 | D |

## Semantic: Layout Roles

| Token | Maps To | Evidence |
|-------|---------|----------|
| `space.container.padding` | `space.6` | I |
| `space.section.gap` | `space.8` | I |
| `space.card.padding` | `space.6` | I |
| `shadow.card` | `shadow.sm` | I |
| `shadow.overlay` | `shadow.lg` | I |

## Container Widths & Breakpoints

| Token | Value | Evidence |
|-------|-------|----------|
| `container.xs` | 480px | D |
| `container.sm` | 640px | D |
| `container.md` | 768px | D |
| `container.lg` | 1024px | D |
| `container.xl` | 1280px | D |
| `breakpoint.sm` | 640px | D |
| `breakpoint.md` | 768px | D |
| `breakpoint.lg` | 1024px | D |
| `breakpoint.xl` | 1280px | D |

## CSS Variables

```css
:root {
  --space-4: 16px;
  --radius-md: 4px;
  --shadow-sm: 0 1px 2px 0 rgba(0,0,0,.06);
  --container-padding: var(--space-6);
}
```
```

## references/components.md

```markdown
# Component Patterns — {Name}

> Extracted from: {source} | Evidence quality: {level}

Each component documents: visual description, token references, variants, states, and evidence grade.

## Button

**Description:** [1-2 sentences describing the visual appearance]

### Token References
| Property | Value | Evidence |
|----------|-------|----------|
| Height (default) | 32px | I |
| Height (small) | 28px | I |
| Height (large) | 36px | I |
| Padding (default) | `space.2` `space.4` | I |
| Border Radius | `radius.sm` | I |
| Font Size | `font.size.base` | I |
| Font Weight | `font.weight.normal` | I |

### Variants

#### Primary (Solid)
| State | Background | Text | Border | Evidence |
|-------|-----------|------|--------|----------|
| Default | `color.action.primary` | `color.text.on.action` | transparent | I |
| Hover | `color.action.primary.hover` | `color.text.on.action` | transparent | I |
| Active | `color.action.primary.active` | `color.text.on.action` | transparent | I |
| Focus | `color.action.primary` | `color.text.on.action` | `color.action.primary` (ring) | I |
| Disabled | `color.action.primary.disabled` | `color.text.on.action` (50% opacity) | transparent | I |

#### Secondary (Outlined)
| State | Background | Text | Border | Evidence |
|-------|-----------|------|--------|----------|
| Default | transparent | `color.text.primary` | `color.border.default` | I |
| Hover | `color.bg.surface.hover` | `color.action.primary` | `color.action.primary` | I |
| ... | | | | |

### Component Tokens
| Token | Value | Evidence |
|-------|-------|----------|
| `button.height.default` | 32px | I |
| `button.height.small` | 28px | I |
| `button.height.large` | 36px | I |

> Other properties use semantic tokens directly — no component token needed.
```

## references/known-gaps.md

```markdown
# Known Gaps & Exceptions — {Name}

> All unresolved discrepancies, assumptions needing review, and deliberate exceptions.

## Source Conflicts

| Issue | Source A | Source B | Resolution | Impact |
|-------|----------|----------|------------|--------|
| Font family | Docs: Nunito | Code: Inter | Used code (Inter) | Typography section |

## Unconfirmed Assumptions

| Token | Assumption | Reason | Action Needed |
|-------|-----------|--------|---------------|
| `color.blue.700-900` | Extrapolated from gradient | Only 50-600 found in source | Review against brand guidelines |

## Deliberate Exceptions

| Value | Location | Why Not a Token |
|-------|----------|-----------------|
| `#FF6B6B` | Hero gradient overlay | One-off decorative; doesn't repeat elsewhere |
```
