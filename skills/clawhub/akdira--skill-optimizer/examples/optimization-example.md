# Optimization Example: Before/After

This document shows a real optimization case study.

---

## Subject: `landing-page` Skill (Before Optimization)

### Original Score: 26/50

| Dimension | Score | Notes |
|-----------|-------|-------|
| Trigger Clarity | 3/5 | Basic triggers listed but no negative triggers |
| Structure | 4/5 | Good sections but missing error handling |
| Step Completeness | 3/5 | Steps reference external files (sections.md, copy.md) |
| Error Handling | 1/5 | Only "Red Flags" section, no error recovery |
| Input Validation | 2/5 | No input validation mentioned |
| Output Specification | 2/5 | "Conversion Checklist" but no output format |
| Examples | 2/5 | Formula shown but no full before/after example |
| Tool References | 3/5 | References sections.md, copy.md, optimization.md |
| Dependencies | 3/5 | Implicit (needs web framework) |
| Maintainability | 3/5 | Has version reference but no changelog |

### Identified Weaknesses

1. **[HIGH]** No error handling — what if the page doesn't convert?
2. **[HIGH]** No concrete full-page example (hero → CTA)
3. **[MEDIUM]** No output specification (what files to produce?)
4. **[MEDIUM]** No input validation (what info needed from user?)
5. **[LOW]** No negative triggers (when NOT to use this skill)

---

## Optimization Pass 1

### Edit 1: Add Error Handling Section ✅ ACCEPTED
```markdown
## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Page not converting | CTA not visible above fold | Move CTA into hero section |
| High bounce rate | Slow load time | Optimize images, reduce JS |
| Low mobile conversion | Not mobile-first | Test on mobile first, desktop second |
| Form abandonment | Too many fields | Reduce to 1-3 fields max |
```

**Reason:** Critical gap — most common failure mode has no guidance.

### Edit 2: Add Input Validation ✅ ACCEPTED
```markdown
## Before You Start

Gather these inputs:
- [ ] **Product/service name** — what are you selling?
- [ ] **Target audience** — who is this for?
- [ ] **Primary CTA** — what action should visitors take?
- [ ] **Social proof** — testimonials, logos, numbers?
- [ ] **Brand assets** — logo, colors, fonts?

**If missing:** Ask the user for these BEFORE starting.
```

**Reason:** Prevents starting without critical information.

### Edit 3: Add Concrete Example ✅ ACCEPTED
```markdown
## Full Example: SaaS Landing Page

**Hero:**
- Headline: "Close Deals 3x Faster with AI-Powered Proposals"
- Subhead: "Generate professional proposals in minutes, not days."
- CTA: "Start Free Trial" + "Watch Demo"
- Visual: Product screenshot with proposal being generated

**Problem Section:**
- "Still writing proposals in Google Docs?"
- "Average sales team spends 8 hours per proposal"
- "60% of proposals never get a response"

**Solution Section:**
- "AI analyzes your best-performing proposals"
- "Auto-generates customized proposals for each prospect"
- "Built-in tracking shows when prospects open, read, and sign"
```

**Reason:** Abstract formulas need concrete instantiation.

### Edit 4: Add Output Specification ✅ ACCEPTED
```markdown
## Deliverables

| Output | Format | Contents |
|--------|--------|----------|
| Landing page copy | Markdown | Hero + 5 sections + CTA |
| Wireframe spec | Description | Section layout, heights, visual notes |
| SEO meta | Text | Title tag + meta description |
| A/B test plan | Table | 3 variants to test post-launch |
```

**Reason:** Unclear what "done" looks like without output spec.

### Rejected Edit: Rewrite entire structure ❌ REJECTED
**Proposed:** Reorganize into taskflow format with explicit state machine.
**Rejected:** Too invasive. Original structure works well. Learning rate = max 4 edits.

---

## After Optimization

### New Score: 38/50 (+12)

| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Trigger Clarity | 3/5 | 3/5 | — |
| Structure | 4/5 | 4/5 | — |
| Step Completeness | 3/5 | 3/5 | — |
| Error Handling | 1/5 | 4/5 | +3 ✅ |
| Input Validation | 2/5 | 4/5 | +2 ✅ |
| Output Specification | 2/5 | 4/5 | +2 ✅ |
| Examples | 2/5 | 4/5 | +2 ✅ |
| Tool References | 3/5 | 3/5 | — |
| Dependencies | 3/5 | 3/5 | — |
| Maintainability | 3/5 | 3/5 | — |

### Validation Gate
- ✅ Score improved: 26 → 38 (+12)
- ✅ No functionality removed
- ✅ All edits bounded (additions only)
- ✅ No contradictions introduced
- ✅ Style consistent with original

**VERDICT: PASS — Optimization accepted**

---

## Key Takeaways

1. **Error handling was the biggest gap** — went from 1/5 to 4/5
2. **4 edits was the right limit** — the 5th proposed edit was correctly rejected as too invasive
3. **Score improved by 46%** (26 → 38) with just 4 bounded additions
4. **No rewrites needed** — all improvements were additive
5. **Concrete examples are high-leverage** — they improve both the "Examples" dimension AND make the skill more usable in practice

---

## Next Pass Candidates

For optimization pass 2, remaining weaknesses:
1. Trigger clarity (add negative triggers)
2. Step completeness (make referenced files inline or add navigation)
3. Maintainability (add version + changelog)
