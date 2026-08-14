# Post-Generation Validation Checklist

After generating the output style skill, run these validations before presenting results to the user.

## 1. Format Validation

- [ ] **YAML frontmatter parses cleanly** — no syntax errors in the SKILL.md YAML block
- [ ] **All required fields present:** `name`, `description`, `version`, `source`, `source_type`, `extracted_at`, `evidence_summary`, `token_summary`
- [ ] **Evidence counts are integers** and sum matches the actual token counts
- [ ] **Token counts are integers** and match the actual number of tokens in each layer

## 2. Token Reference Validation

- [ ] **Every `{colors.xxx}` reference resolves** to a defined token in colors.md
- [ ] **Every `{typography.xxx}` reference resolves** to a defined token in typography.md
- [ ] **Every `{spacing.xxx}` / `{shadow.xxx}` / `{radius.xxx}` reference resolves**
- [ ] **No dangling references** — no token references that point to undefined tokens
- [ ] **No circular references** — tokens that reference each other in a loop (e.g., `A→B→A`)

## 3. Color Value Validation

- [ ] **All hex values are valid** (3, 6, or 8 hex digits, with or without `#`)
- [ ] **All alpha values are in valid range** (0–1 or 0%–100% or valid hex alpha)
- [ ] **No obviously wrong colors** — e.g., pure black/white that should be near-black/near-white
- [ ] **Dark theme values don't accidentally use light theme hex codes** (common pitfall)

## 4. Layer Consistency Validation

- [ ] **Every semantic token references a primitive token** (not a raw hex value or another semantic)
- [ ] **Every component token references a semantic token** (not a raw value or primitive directly)
- [ ] **No component token duplicates a semantic token** — if `card.bg` = `color.bg.surface`, card should just use the semantic token
- [ ] **Same-value/different-semantic pairs are separated** — e.g., `#FFFFFF` as page background AND inverse text are two different semantic tokens
- [ ] **Primitive tokens are named by what they ARE** (not where they're used) — `color.blue.500`, not `color.button`

## 5. Cross-Contamination Check

- [ ] **No tokens or brand names from other design systems** — no Material Design color names, no Tailwind default names, no Ant Design tokens
- [ ] **No "Lorem ipsum" or placeholder values** left in the output
- [ ] **No references to internal paths** from the extraction machine

## 6. Section Completeness

- [ ] **SKILL.md:** Token Architecture table, Quick Reference CSS block, Theme Mappings (if dark mode), References list
- [ ] **colors.md:** Primitive scales + Semantic roles + Component tokens + Same-value alerts + CSS variables
- [ ] **typography.md:** Primitive families/sizes/weights + Semantic text roles + CSS variables
- [ ] **spacing.md:** Primitive spacing/radius/shadow/z-index scales + Semantic layout roles + Breakpoints + CSS variables
- [ ] **components.md:** Each component has variants, states, token references, and evidence grades
- [ ] **known-gaps.md:** Exists and is not empty (at minimum, state "No unresolved gaps found")

## 7. Theme Validation (if applicable)

- [ ] **Light and dark theme mappings are defined** for all semantic tokens
- [ ] **Same-value traps are documented** — tokens with identical values in light theme but different dark theme mappings
- [ ] **Theme switching doesn't break semantic relationships** — a token that's "primary action" in light stays "primary action" in dark

## 8. Demo Page Validation (Optional but Recommended)

Generate a demo HTML page that exercises the tokens:

- [ ] **Page renders without errors** in a browser
- [ ] **All semantic color roles appear** — backgrounds, surfaces, text levels, actions, statuses
- [ ] **Typography hierarchy is visible** — headings through captions all present and correct
- [ ] **Component demos cover all variants and states** — buttons (all variants × all states), inputs, cards, etc.
- [ ] **Visual output matches the source's aesthetic** — if it looks completely different, the extraction has errors
- [ ] **Dark mode toggle works** (if applicable) and all colors shift correctly

## Validation Report Template

After running validations, output:

```
## Validation Report: brand-style-{name}

**Format:** ✅ YAML parses / ⚠️ {issue}
**References:** ✅ {N} references all resolve / ⚠️ {dangling tokens}
**Colors:** ✅ {N} hex values valid / ⚠️ {invalid values}
**Layers:** ✅ Primitive→Semantic→Component chain intact / ⚠️ {breaks}
**Contamination:** ✅ No foreign design system tokens / ⚠️ {foreign tokens}
**Sections:** ✅ All {N} sections present / ⚠️ {missing sections}
**Theme:** ✅ {N} theme mappings complete / ⚠️ {gaps}

**Files:** {path} — {lines} lines
**Tokens:** {P} primitive + {S} semantic + {C} component = {total} total
**Evidence:** {D} defined + {M} measured + {I} inferred + {A} assumed
**Known Gaps:** {count} items → see references/known-gaps.md
```
