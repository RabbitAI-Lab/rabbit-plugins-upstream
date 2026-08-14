# Extraction Checklist

Comprehensive checklist for extracting design tokens from any source. Each item should be tagged with an evidence grade and a target token layer.

## Evidence Grades

| Grade | Label | Meaning |
|-------|-------|---------|
| **D** | 已定义 (Defined) | Found in CSS variables, theme config, or design token files |
| **M** | 已测量 (Measured) | Confirmed from source code or browser computed styles |
| **I** | 有依据的归纳 (Inferred) | Reasonably deduced from patterns across multiple components |
| **A** | 暂时假设 (Assumed) | Best guess; MUST be reviewed by user |

## Token Layers

| Layer | Purpose | Naming Rule |
|-------|---------|-------------|
| **Primitive** | Raw materials (color scales, spacing steps, font sizes) | Name what it IS: `color.blue.500`, `space.4`, `radius.md` |
| **Semantic** | Design roles (backgrounds, text, actions, statuses) | Name what it DOES: `color.action.primary`, `color.bg.page` |
| **Component** | Per-component overrides | Name what it's FOR: `button.primary.bg.default`, `input.border.focus` |

## Colors

For each color discovered, record:

- [ ] **Hex value** (e.g., `#3B82F6`) — include alpha channel if used (e.g., `#165DFF14`)
- [ ] **Evidence grade:** D (from CSS variable) / M (from computed style) / I (from visual sampling) / A (assumed)
- [ ] **Target layer:** Primitive (raw color) → Semantic (role) → Component (per-element)
- [ ] **Current role(s):** What elements use this color (buttons, headings, backgrounds, borders, icons)
- [ ] **Theme variation:** If source has light/dark mode, document both — different themes may map to the same primitive
- [ ] **Same-value warning:** If this hex value also appears in a DIFFERENT semantic role, flag it — they must become separate semantic tokens

### Extraction Methods by Source

**URL:** Extract from CSS `color`, `background-color`, `border-color`, `--*` variables (D), Tailwind `bg-*`, `text-*` classes (D), computed styles (M)
**Screenshot:** Identify dominant colors by visual sampling (I); accent, surface, and text colors are more reliable than subtle variations
**Project:** Parse theme configs (D), CSS variables (D), design token JSON (D), SCSS `$variables` (D), computed styles from browser (M)

### Three-Layer Organization

```markdown
## Primitive: Color Scales (evidence: D)

| Token | Hex | Evidence | Notes |
|-------|-----|----------|-------|
| `color.blue.50` | `#E8F3FF` | D | Lightest blue |
| `color.blue.100` | `#BEDAFF` | D | |
| ... | | | |
| `color.blue.500` | `#165DFF` | D | Default interaction blue |
| `color.blue.600` | `#0E42D2` | D | Hover state |
| ... | | | |
| `color.blue.900` | `#001B4D` | D | Darkest blue |
| `color.gray.50` | `#F7F8FA` | D | Lightest gray |
| ... | | | |
| `color.gray.900` | `#1D2129` | D | Darkest gray |

## Semantic: Design Roles (evidence: I)

| Token | Maps To | Light Theme | Dark Theme | Evidence |
|-------|---------|-------------|------------|----------|
| `color.action.primary` | `color.blue.500` | `#165DFF` | `#4080FF` | I |
| `color.action.primary.hover` | `color.blue.400` | `#4080FF` | `#5C9DFF` | I |
| `color.bg.page` | `color.gray.50` | `#F7F8FA` | `#17171A` | I |
| `color.bg.surface` | white | `#FFFFFF` | `#232324` | I |
| `color.text.primary` | `color.gray.900` | `#1D2129` | `rgba(255,255,255,.9)` | I |
| `color.text.secondary` | `color.gray.600` | `#4E5969` | `rgba(255,255,255,.7)` | I |

## Component: Per-Element Tokens (evidence: I)

| Token | Maps To | Evidence |
|-------|---------|----------|
| `button.primary.bg.default` | `color.action.primary` | I |
| `button.primary.bg.hover` | `color.action.primary.hover` | I |
| `input.border.focus` | `color.action.primary` (20% alpha) | I |
```

## Typography

For each font/level, record:

- [ ] **Evidence grade** — D (from theme config/CSS variable), M (from computed style), I (from visual), A (assumed)
- [ ] **Font family** — Primary, secondary, monospace; note source (Google Fonts, system stack, `@font-face`)
- [ ] **Size scale** — Document in rem with px fallback, note if rem base is 16px or other
- [ ] **Weight usage pattern** — 400 for body, 500-600 for headings, 700+ for hero
- [ ] **Line-height pattern** — Headings usually 1.1-1.3, body 1.5-1.6
- [ ] **Letter-spacing** — Negative for large headings, normal for body

### Three-Layer Organization

```markdown
## Primitive: Font Scale (evidence: D)

| Token | Size | Evidence |
|-------|------|----------|
| `font.size.xs` | 12px / 0.75rem | D |
| `font.size.sm` | 13px / 0.8125rem | D |
| `font.size.base` | 14px / 0.875rem | D |
| `font.size.lg` | 16px / 1rem | D |
| `font.size.xl` | 20px / 1.25rem | D |
| `font.size.2xl` | 24px / 1.5rem | D |
| `font.size.3xl` | 30px / 1.875rem | D |
| `font.weight.normal` | 400 | D |
| `font.weight.medium` | 500 | D |
| `font.weight.semibold` | 600 | D |
| `font.weight.bold` | 700 | D |

## Semantic: Text Roles (evidence: I)

| Token | Font | Size | Weight | Line-Height | Evidence |
|-------|------|------|--------|-------------|----------|
| `text.heading.page` | primary | `font.size.3xl` | `font.weight.bold` | 1.2 | I |
| `text.heading.section` | primary | `font.size.2xl` | `font.weight.semibold` | 1.3 | I |
| `text.heading.card` | primary | `font.size.xl` | `font.weight.medium` | 1.3 | I |
| `text.body` | primary | `font.size.base` | `font.weight.normal` | 1.5715 | I |
| `text.body.small` | primary | `font.size.sm` | `font.weight.normal` | 1.5 | I |
| `text.caption` | primary | `font.size.xs` | `font.weight.normal` | 1.4 | I |

### Extraction Methods by Source

**URL:** Extract from CSS `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`; Tailwind `text-*`, `font-*`; computed styles
**Screenshot:** Identify font category (sans-serif/serif/mono), gauge size hierarchy visually (I/A grade)
**Project:** Parse theme config `fontFamily`, `fontSize`; CSS variables; global defaults
```

## Spacing & Sizing

- [ ] **Evidence grade** per value
- [ ] **Base unit** — Usually 4px / 0.25rem; verify from the actual scale
- [ ] **Spacing scale** — Values used for padding, margin, gap; note any gaps in the scale
- [ ] **Border radius scale** — `none` / `sm` / `md` / `lg` / `full`; note which components use each
- [ ] **Shadow scale** — Full CSS box-shadow strings; note color, offset, blur, spread, and opacity
- [ ] **Z-index layers** — Page content, sticky headers, overlays, modals, tooltips, notifications
- [ ] **Container widths** — Max-width for content containers
- [ ] **Responsive breakpoints** — `sm` / `md` / `lg` / `xl` / `2xl` with actual px values

### Three-Layer Organization

```markdown
## Primitive: Spacing Scale (evidence: D)

| Token | Value | Evidence |
|-------|-------|----------|
| `space.0` | 0 | D |
| `space.1` | 4px | D |
| `space.2` | 8px | D |
| `space.3` | 12px | D |
| `space.4` | 16px | D |
| `space.5` | 20px | D |
| `space.6` | 24px | D |
| `space.8` | 32px | D |
| `space.12` | 48px | D |

## Primitive: Radius Scale (evidence: D)

| Token | Value | Evidence |
|-------|-------|----------|
| `radius.none` | 0 | D |
| `radius.sm` | 2px | D |
| `radius.md` | 4px | D |
| `radius.lg` | 8px | D |
| `radius.full` | 9999px | D |

## Primitive: Shadow Scale (evidence: D)

| Token | CSS | Evidence |
|-------|-----|----------|
| `shadow.sm` | `0 1px 2px 0 rgba(0,0,0,.06)` | D |
| `shadow.md` | `0 4px 10px 0 rgba(0,0,0,.08)` | D |
| `shadow.lg` | `0 8px 24px 0 rgba(0,0,0,.12)` | D |

## Semantic: Layout Roles (evidence: I)

| Token | Maps To | Evidence |
|-------|---------|----------|
| `space.container.padding` | `space.6` | I |
| `space.section.gap` | `space.8` | I |
| `shadow.overlay` | `shadow.lg` | I |
```

## Layout

- [ ] **Layout mode** — Centered single-column, multi-column grid, full-width sections
- [ ] **Grid system** — Column count, gap, responsive behavior
- [ ] **Section patterns** — Hero, features, CTA, footer; note recurring structure
- [ ] **Evidence grade** for layout patterns (usually I — inferred from observation)

## Component Patterns

For each recurring component, record:

- [ ] **Component name**
- [ ] **Visual description** — 1-2 sentences
- [ ] **Key CSS properties** — padding, border-radius, shadows, colors, typography
- [ ] **Variants** — primary/secondary, sm/md/lg/hover/active/disabled/focus
- [ ] **Token references** — Which semantic tokens this component uses
- [ ] **Component tokens** — Only if the component has values that differ from semantic defaults
- [ ] **Evidence grade** — Usually I (inferred from pattern repetition)
- [ ] **Drift check** — Does the same component type appear with different values across pages?

### Component Token Decision Flow

```
Does the component value equal a semantic token?
  YES → Use the semantic token directly. Do NOT create a component token.
  NO  → Is this value unique to this component and stable across instances?
           YES → Create a component token.
           NO  → Investigate: is this component drift or a bug?
```

```yaml
Button:
  Variants:
    Primary:
      bg.default:   → color.action.primary        # semantic — no component token needed
      bg.hover:     → color.action.primary.hover    # semantic — no component token needed
      bg.active:    → color.action.primary.active   # semantic — no component token needed
      bg.disabled:  → color.action.disabled          # semantic — no component token needed
      text:         → color.text.on.action           # semantic — no component token needed
      padding:      → space.2 space.4               # uses primitive directly (common pattern)
      radius:       → radius.md                     # uses primitive directly
      height:       32px                            # component token — unique to buttons
    Secondary:
      bg:           transparent
      border:       → color.border.default
      text:         → color.text.primary
      height:       32px                            # component token — matches primary
  Evidence: I
  Drift check: Button height consistent across all pages? Non-standard sizes in modals?
```

## Interactions & Motion

- [ ] **Hover states** — Color shift, scale, shadow change, underline animation; note duration
- [ ] **Focus rings** — Color, width, offset; `:focus` vs `:focus-visible`
- [ ] **Transitions** — Duration (ms), easing curves (ease, ease-in-out, custom cubic-bezier)
- [ ] **Animations** — Keyframe names, duration, iteration
- [ ] **Reduced motion** — Does the source provide `prefers-reduced-motion` alternatives?
- [ ] **Evidence grade** — D (from CSS), M (from observed behavior), I (inferred)

## Don't Forget

### Same-Value / Different-Semantic Traps

For every color, ask: "Could this same hex value mean different things in different contexts?"

| Value | Context A | Context B | Same Token? |
|-------|-----------|-----------|-------------|
| `#FFFFFF` | Page background (light theme) | Inverse text (dark theme) | **NO** — separate semantic tokens |
| `#165DFF` | Primary button | Link text | **Maybe** — depends on whether they should always change together |
| `#1D2129` | Primary text (light) | Page background (dark) | **NO** — different semantic roles |

### Frequency ≠ Importance Checklist

Before upgrading a value to a token, ask:
1. Does it appear across multiple pages/components? (if no → likely local exception)
2. Would changing it break the design? (if no → low priority)
3. Does it have a clear semantic role? (if no → may be accidental)
4. Would it need to change with theme? (if yes → must be semantic token)
5. Is it tied to a specific component's identity? (if yes → component token)
