# Skill Quality Rubric

Detailed scoring guide for the 10 quality dimensions. Each dimension scored 1-5.

---

## 1. Trigger Clarity (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No triggers defined |
| 2 | Vague triggers ("use when needed") |
| 3 | Basic keyword triggers listed |
| 4 | Specific triggers with context ("use when X AND Y") |
| 5 | Comprehensive triggers: keywords, phrases, negations ("don't use when Z"), and edge cases |

**What to look for:**
- Are trigger keywords specific enough to avoid false activation?
- Are common user phrasings covered?
- Are there negative triggers (when NOT to use)?

---

## 2. Structure (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No structure, wall of text |
| 2 | Some headings but inconsistent |
| 3 | Clear sections but missing some |
| 4 | Well-organized with all major sections |
| 5 | Excellent structure + logical flow + scannable + consistent formatting |

**What to look for:**
- Frontmatter with name + description?
- Overview → Steps → Examples → References flow?
- Consistent heading levels?
- Scannable (tables, bullets, code blocks)?

---

## 3. Step Completeness (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No steps or single vague instruction |
| 2 | Steps present but incomplete or unclear |
| 3 | All major steps present, some vague |
| 4 | Detailed steps with clear actions |
| 5 | Atomic steps, each with action + expected result + verification |

**What to look for:**
- Are steps in logical order?
- Is each step actionable (not just descriptive)?
- Can someone follow the steps without additional context?

---

## 4. Error Handling (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No error handling at all |
| 2 | Mentions "if it fails, try again" |
| 3 | Some error cases covered |
| 4 | Common errors + solutions documented |
| 5 | Comprehensive error matrix: error → cause → solution → prevention |

**What to look for:**
- Edge cases covered?
- Fallback paths documented?
- Troubleshooting section?
- "What to do when X goes wrong"?

---

## 5. Input Validation (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No input validation |
| 2 | Mentions checking inputs but no specifics |
| 3 | Lists required inputs |
| 4 | Validates inputs with specific checks |
| 5 | Input validation + clear error messages for invalid inputs + examples of valid/invalid |

**What to look for:**
- Required vs optional inputs specified?
- Format constraints documented?
- Validation steps before execution?

---

## 6. Output Specification (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No output specification |
| 2 | Vague output description |
| 3 | Output format described |
| 4 | Output format + examples + success criteria |
| 5 | Precise output spec + file paths + format + verification + example output |

**What to look for:**
- What does the skill produce?
- Where does output go?
- How to verify output is correct?

---

## 7. Examples (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No examples |
| 2 | One abstract example |
| 3 | Multiple examples but no context |
| 4 | Concrete examples with before/after |
| 5 | Rich examples: context → input → process → output → verification |

**What to look for:**
- Real-world scenarios?
- Before/after comparisons?
- Edge case examples?

---

## 8. Tool References (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No tool references |
| 2 | Tools mentioned but no versions/paths |
| 3 | Tools + basic usage |
| 4 | Tools + versions + paths + key flags |
| 5 | Complete tool reference: versions, paths, flags, alternatives, compatibility notes |

**What to look for:**
- Specific versions mentioned?
- Paths to tools/binaries?
- Command examples with flags?

---

## 9. Dependencies (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No dependencies listed |
| 2 | Some dependencies mentioned |
| 3 | All dependencies listed |
| 4 | Dependencies + install instructions + versions |
| 5 | Full dependency tree + install + verify + troubleshooting + alternatives |

**What to look for:**
- All prerequisites listed?
- Installation commands?
- Version requirements?
- How to verify dependencies are met?

---

## 10. Maintainability (1-5)

| Score | Criteria |
|-------|----------|
| 1 | No version info, hard to update |
| 2 | Basic version info |
| 3 | Version + changelog |
| 4 | Version + changelog + clear ownership |
| 5 | Full lifecycle: version, changelog, owner, review schedule, deprecation plan |

**What to look for:**
- Version number in frontmatter?
- Changelog or update history?
- Clear ownership (who maintains)?
- Easy to find and update specific sections?

---

## Scoring Summary

| Total Score | Quality Level | Action |
|-------------|---------------|--------|
| 45-50 | 🟢 Excellent | Minor polish only |
| 35-44 | 🟡 Good | Targeted improvements |
| 25-34 | 🟠 Fair | Significant optimization needed |
| 15-24 | 🔴 Poor | Major rewrite recommended |
| 10-14 | 🔴 Critical | Start from scratch |
