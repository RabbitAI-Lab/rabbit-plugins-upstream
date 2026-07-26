# Anti-Slop Checklist

> LLM-generated design output clusters around a few defaults. This checklist helps you identify and avoid them.

---

## Banned Fonts (As Defaults)

### Hard Bans
- **Inter** as display font — it's a body font, not a headline
- **Roboto, Arial, Open Sans, Helvetica** — generic system fonts
- **Fraunces** — the #1 LLM-favorite display serif
- **Instrument_Serif** — the #2 LLM-favorite display serif

### When Inter Is Acceptable
- User explicitly asks for "neutral" / "standard" / "Linear-style"
- Public-sector / accessibility-first sites
- Dashboard body text (not headlines)

### Recommended Alternatives
| Use Case | Recommended Fonts |
|----------|-------------------|
| Sans display (headlines) | Geist Display, Outfit, Cabinet Grotesk, Satoshi, ABC Diatype, Söhne Breit |
| Sans body | Geist, Inter Tight, Switzer, Plus Jakarta Sans |
| Mono (code/data) | Geist Mono, JetBrains Mono, IBM Plex Mono |
| Serif (only when justified) | PP Editorial New, GT Sectra, Tiempos Headline, Recoleta, Cormorant Garamond |

### Serif Discipline
Serif is **discouraged as default**. "It feels creative / premium / editorial" is NOT a reason to reach for serif.

**Serif is only acceptable when:**
- The brand brief literally names a serif font, OR
- The aesthetic family is genuinely editorial / luxury / publication / manuscript / heritage / vintage AND you can articulate why this specific serif fits

**For everything else**, default to sans-serif display. Sans display fonts are not "boring" — they are the default for the same reason black is the default in fashion.

---

## Banned Layouts (As Defaults)

### The "AI SaaS Landing" Template
- Centered hero over dark mesh gradient
- Three equal feature cards in a row
- Generic glassmorphism on everything
- Infinite-loop micro-animations everywhere

### The "AI Purple" Aesthetic
- Purple-to-blue gradients on white backgrounds
- Near-black background with single bright acid-green accent
- "AI purple" is the most common AI design fingerprint

### The "Newspaper" Default
- Broadsheet-style layout with hairline rules
- Zero border-radius everywhere
- Dense newspaper-like columns

### What To Do Instead
- Read the brief and choose layout based on content, not defaults
- Break symmetry with offset margins, mixed aspect ratios
- Use asymmetric grids, masonry, or horizontal scroll
- Vary border-radius: tighter on inner elements, softer on containers

---

## Banned Icons

### Discouraged As Default
- **Lucide** — the "default" AI icon choice
- **Feather** — thin-line generic
- **FontAwesome** — dated
- **Material Icons** — too Google-specific

### Recommended Alternatives (Priority Order)
1. `@phosphor-icons/react` — versatile, multiple weights
2. `hugeicons-react` — modern, distinctive
3. `@radix-ui/react-icons` — clean, technical
4. `@tabler/icons-react` — consistent stroke width

### Rules
- **One icon family per project** — do not mix Phosphor with Lucide
- **Standardize strokeWidth globally** (e.g., 1.5 or 2.0)
- **Never hand-roll SVG icons** — install a library or compose from primitives

---

## Banned Content Patterns

### Placeholder Names
- "John Doe", "Jane Smith" — use diverse, realistic names
- "Acme Corp", "Nexus", "SmartFlow" — invent contextual brand names
- "Lorem ipsum" — write real draft copy

### AI Copywriting Clichés
Never use these words/phrases:
- "Elevate", "Seamless", "Unleash", "Next-Gen"
- "Game-changer", "Delve", "Tapestry"
- "In the world of...", "Unlock the power of"
- "Revolutionary", "Cutting-edge", "State-of-the-art"

### Fake Data
- Perfect round numbers: `99.99%`, `50%`, `$100.00`
- Use organic, messy data: `47.2%`, `$99.00`, `+1 (312) 847-1928`

### Emoji Policy
- Discouraged by default in code, markup, and visible text
- Replace symbols with icon-library glyphs
- **Override:** allow emojis only when user explicitly asks for playful / chat-style / social-native vibe

---

## Banned Technical Patterns

### CSS Anti-Patterns
- `h-screen` for full-height Hero — use `min-h-[100dvh]` instead
- Complex flexbox percentage math (`w-[calc(33%-1rem)]`) — use CSS Grid
- Arbitrary z-index values like `z-[9999]` — establish a z-index scale
- Animating `top`, `left`, `width`, `height` — use `transform` and `opacity`

### React Anti-Patterns
- `useState` for continuous values (mouse position, scroll progress) — use Motion's `useMotionValue`
- Global state for everything — only for deep prop-drilling avoidance
- Not isolating client components — wrap providers in `"use client"`

### Dependency Issues
- Importing libraries not in package.json — always verify first
- Mixing design systems (Fluent + Carbon in same tree) — one system per project

---

## Pre-Output Audit

Before delivering, scan your code for:

1. **Font check** — Are you using Inter/Fraunces/Instrument_Serif as default?
2. **Layout check** — Is this the "centered hero + three cards" template?
3. **Color check** — Did you default to purple gradients?
4. **Icon check** — Are you using Lucide without justification?
5. **Content check** — Any "Lorem ipsum" or "Acme Corp"?
6. **Technical check** — Using `h-screen` or animating layout properties?

If any of these trigger, revise before delivering.

---

## The Variance Mandate

**Never generate the exact same layout or aesthetic twice in a row.** Dynamically combine different layout archetypes and texture profiles based on the design read. Reach past defaults deliberately.

---

*This checklist is part of the frontend-design skill v2.0.0*
