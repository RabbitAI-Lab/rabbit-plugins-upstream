---
name: skill-optimizer
description: "Systematically analyze, score, and optimize OpenClaw skill documents (SKILL.md files). Adapted from Microsoft SkillOpt research — treats skill docs as trainable state with validation-gated edits. Use when improving skill quality, auditing skills, onboarding new skills, or batch-optimizing workspace skills."
version: "1.0.0"
author: "Finn (adapted from Microsoft SkillOpt)"
references:
  - "https://arxiv.org/abs/2605.23904"
  - "https://github.com/microsoft/skillopt"
---

# Skill Optimizer 🔬

Systematic skill document optimization for OpenClaw, adapted from Microsoft SkillOpt research.

> **Core insight:** Skills are the "weights" of a frozen agent. Optimize them with the same discipline as neural network training — rollout, reflect, aggregate, select, update, gate — but in text space, without retraining the model.

## When to Use

- Skill execution is inconsistent or frequently fails
- Want to systematically improve skill quality (not just ad-hoc fixes)
- Onboarding new skills and want to validate quality before deployment
- Auditing existing skills for completeness and best practices
- Batch-optimizing multiple skills across the workspace
- Preparing skills for ClawHub publication

## Core Concepts (from SkillOpt)

| SkillOpt Concept | Our Adaptation |
|---|---|
| **Skill document = trainable state** | SKILL.md is the "model" we optimize |
| **Rollout** | Execute skill with test scenarios, capture results |
| **Reflect** | Analyze execution patterns, identify weaknesses |
| **Aggregate** | Combine multiple improvement suggestions |
| **Select (learning rate)** | Limit edits per pass to prevent overfitting |
| **Update** | Apply bounded edits to SKILL.md |
| **Validation gate** | Only accept edits that demonstrably improve quality |
| **Slow update** | Gradual improvement across optimization passes |
| **Meta skill** | Cross-skill patterns extracted as reusable heuristics |
| **best_skill.md** | The optimized SKILL.md artifact |

## Quality Dimensions (Scoring Rubric)

Every skill is scored on 10 dimensions (1-5 each, max 50):

| # | Dimension | What to Check |
|---|-----------|---------------|
| 1 | **Trigger Clarity** | Are activation triggers specific and comprehensive? |
| 2 | **Structure** | Does it follow consistent sections (Overview → Steps → Examples)? |
| 3 | **Step Completeness** | Are all steps present, ordered, and actionable? |
| 4 | **Error Handling** | Does it handle edge cases, failures, and exceptions? |
| 5 | **Input Validation** | Does it validate inputs before execution? |
| 6 | **Output Specification** | Are expected outputs clearly defined? |
| 7 | **Examples** | Are there concrete before/after examples? |
| 8 | **Tool References** | Are tools/commands referenced correctly with versions? |
| 9 | **Dependencies** | Are prerequisites and dependencies documented? |
| 10 | **Maintainability** | Is it easy to update? Version controlled? |

## Workflow

### Mode 1: Analyze (Read-Only)

```
Input: skill name or path to SKILL.md
Output: quality score + detailed analysis
```

**Steps:**
1. Read the SKILL.md file
2. Parse structure: frontmatter, sections, steps, examples
3. Score each of the 10 quality dimensions
4. Identify specific weaknesses with line references
5. Generate analysis report

**Command pattern:**
```
Analyze skill: <skill-name>
```

### Mode 2: Optimize (Read + Write)

```
Input: skill name or path to SKILL.md
Output: optimized SKILL.md + diff report
```

**Steps:**
1. **Analyze** — Run full analysis (Mode 1)
2. **Backup** — Copy original to `SKILL.md.bak`
3. **Propose** — Generate specific edits for each weakness
4. **Select** — Apply learning rate: max 4 edits per pass (SkillOpt default)
5. **Update** — Apply edits to SKILL.md
6. **Gate** — Re-score the skill. Only accept if score improves.
7. **Report** — Show before/after diff + score comparison

**Learning Rate Control:**
- Default: max 4 edits per optimization pass
- If more than 4 improvements needed → prioritize by impact
- Rejected edits go to a buffer for next pass
- Prevents overfitting / over-editing in one pass

**Command pattern:**
```
Optimize skill: <skill-name>
```

### Mode 3: Batch Optimize

```
Input: list of skills or "all"
Output: optimization report for all skills
```

**Steps:**
1. List all skills in workspace
2. Score each skill (quick analysis)
3. Rank by improvement potential (lowest scores first)
4. Optimize top N skills (default: 3)
5. Generate batch report

**Command pattern:**
```
Batch optimize skills [top N]
```

### Mode 4: Compare

```
Input: skill name
Output: before/after comparison
```

**Steps:**
1. Read current SKILL.md and SKILL.md.bak (if exists)
2. Generate side-by-side diff
3. Show score comparison
4. List accepted/rejected edits

**Command pattern:**
```
Compare skill: <skill-name>
```

## Optimization Strategies

### Strategy 1: Structural Completion
**Problem:** Skill is missing critical sections.
**Fix:** Add missing sections based on template.
**Impact:** High (foundational)

### Strategy 2: Trigger Expansion
**Problem:** Triggers are too narrow, skill doesn't activate when needed.
**Fix:** Expand trigger keywords based on common usage patterns.
**Impact:** Medium-High

### Strategy 3: Error Path Addition
**Problem:** Skill only covers happy path.
**Fix:** Add error handling, fallback paths, and troubleshooting.
**Impact:** High

### Strategy 4: Example Enhancement
**Problem:** Abstract instructions without concrete examples.
**Fix:** Add before/after examples for each major step.
**Impact:** Medium

### Strategy 5: Dependency Documentation
**Problem:** Prerequisites not documented, causes setup failures.
**Fix:** Add clear dependency list with versions and install commands.
**Impact:** Medium

### Strategy 6: Output Specification
**Problem:** Unclear what the skill should produce.
**Fix:** Add explicit output format, file paths, success criteria.
**Impact:** Medium

### Strategy 7: Step Decomposition
**Problem:** Steps are too large or vague.
**Fix:** Break complex steps into smaller, atomic actions.
**Impact:** Medium

### Strategy 8: Cross-Reference Enhancement
**Problem:** Skill doesn't reference related skills or tools.
**Fix:** Add links to related skills, tools, and documentation.
**Impact:** Low-Medium

## Validation Gate Rules

An edit is ONLY accepted when:
1. ✅ The quality score improves (or stays same with no regressions)
2. ✅ No existing functionality is removed
3. ✅ The edit is bounded (add/delete/replace, not full rewrite)
4. ✅ The edit doesn't introduce contradictions
5. ✅ The edit maintains consistent tone and style

If the gate rejects an edit:
- Log it to the rejected-edit buffer
- Try alternative formulation in next pass
- If 3+ rejections on same issue → flag for human review

## Meta Skill Extraction

After optimizing 5+ skills, extract cross-skill patterns:

1. **Common weaknesses** — what do most skills lack?
2. **Common strengths** — what do the best skills have?
3. **Structural patterns** — what sections work best?
4. **Anti-patterns** — what should skills NEVER do?

Store patterns in `references/meta-skill-patterns.md`.
Use patterns to improve the scoring rubric and optimization strategies.

## Output Format

### Analysis Report
```markdown
# Skill Analysis: [skill-name]

## Score: [X]/50

### Dimension Scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| Trigger Clarity | 3/5 | ... |
| ... | ... | ... |

### Weaknesses (Priority Order)
1. [HIGH] Missing error handling in Step 3
2. [MEDIUM] No examples for main workflow
3. [LOW] Triggers could be more specific

### Strengths
- Clear step-by-step structure
- Good tool references

### Recommended Edits
1. Add error handling section after Step 5
2. Add example for common use case
3. Expand trigger keywords
```

### Optimization Report
```markdown
# Optimization Report: [skill-name]

## Before → After
- Score: [X]/50 → [Y]/50 (+[Z])
- Edits applied: [N]
- Edits rejected: [M]

## Changes Made
### Edit 1: [Type] [Section]
- Before: [original text]
- After: [new text]
- Reason: [why this improves the skill]

## Validation
- [✅/❌] Score improved
- [✅/❌] No functionality removed
- [✅/❌] Edits bounded
- [✅/❌] No contradictions
- [✅/❌] Style consistent
```

## Integration with AAR

After optimizing a skill:
1. Run the skill on a real task
2. Note any failures or friction points
3. Feed findings back into next optimization pass
4. This creates a continuous improvement loop (like SkillOpt epochs)

## References

- **Paper:** [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904)
- **GitHub:** [microsoft/SkillOpt](https://github.com/microsoft/skillopt) (15.5K stars)
- **Key insight:** Train skills like neural networks — epochs, learning rates, validation gates — without touching model weights
- **Results:** 41% → 80% accuracy (spreadsheet), 33% → 72% accuracy (document)
- **Our adaptation:** Text-space optimization for OpenClaw SKILL.md files with LLM-driven analysis
