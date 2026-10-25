---
name: skill-factory
description: The ultimate meta-skill for creating new OpenClaw skills from scratch. This skill transforms any agent into a world-class skill architect capable of designing, building, and shipping legendary-tier skills. Use this skill whenever you need to create a new skill — whether for writing, coding, research, analysis, creative work, or any domain. The factory produces skills that are structured, intelligent, robust, and ready for production. Think of it as a "skill compiler" that takes a domain description and outputs a complete, elite-tier skill package.
metadata: '{"openclaw": {"emoji": "🏭", "requires": {"bins": []}}}'
---

## ⚠️ GUARDRAILS (Wajib — batasi otoritas)

Skill ini membantu membuat skill baru, tapi punya batas keras:

- **JANGAN** sentuh file token/secret/credential (`openclaw.json`, `models.json` berisi apiKey, env berisi token, `_meta.json` selain field `version`/`slug`).
- **Bukan** pengganti identitas agent — hanya panduan membuat skill untuk task tertentu.
- Ikuti ASK/STOP/VERIFY: konfirmasi sebelum overwrite file skill existing; verifikasi (secret-scan) sebelum klaim sukses.
- Satu skill per proses; jangan modifikasi skill lain tanpa instruksi eksplisit.


# 🏭 SKILL FACTORY — The Skill Architect

> **Identity**: You are a **Skill Architect** — a master craftsman who designs cognitive systems. You don't just write instructions; you architect minds.

> **Mission**: Transform any domain, task, or capability into a legendary-tier OpenClaw skill that elevates any agent to expert-level performance.

---

## ⚡ THE SKILL CREATION PROTOCOL

**When asked to create a new skill, execute this 7-phase protocol:**

```
PHASE 1: NEEDS ANALYSIS
  → Understand the domain deeply
  → Identify the target user
  → Define success criteria
  → Map the skill lifecycle

PHASE 2: ARCHITECTURE DESIGN
  → Design the skill structure
  → Define components and their relationships
  → Plan the reasoning engine
  → Design the output system

PHASE 3: CORE BUILDING
  → Write SKILL.md (the brain)
  → Define purpose, triggers, directives
  → Install reasoning protocols
  → Set quality standards

PHASE 4: REFERENCE BUILDING
  → Build reference materials
  → Frameworks, formulas, patterns
  → Best practices, standards
  → Examples and case studies

PHASE 5: TEMPLATE BUILDING
  → Create ready-to-use templates
  → Pre-writing and post-writing checklists
  → Decision trees and selection guides
  → Quick-start guides

PHASE 6: QUALITY ASSURANCE
  → Run the 10-dimension audit
  → Test with edge cases
  → Verify completeness
  → Polish to legendary tier

PHASE 7: PACKAGING & DELIVERY
  → Structure the skill folder
  → Write README.md
  → Create installation guide
  → Document known limitations
```

---

## 🎯 PHASE 1: NEEDS ANALYSIS

### Step 1.1: Domain Deep Dive

```
QUESTIONS TO ANSWER:
→ What domain does this skill cover? (be specific)
→ What tasks does it handle? (list all)
→ What is the complexity level? (simple / moderate / complex / wicked)
→ What expertise is required? (beginner / intermediate / advanced / expert)
→ What tools does it use? (if any)
→ What outputs does it produce?
```

### Step 1.2: User Persona Mapping

```
Define 3 user personas:

PERSONA 1: NOVICE
→ Skill level: Beginner
→ Needs: Hand-holding, examples, step-by-step
→ Pain points: Overwhelmed, doesn't know where to start
→ Success metric: Can complete basic tasks independently

PERSONA 2: COMPETENT
→ Skill level: Intermediate
→ Needs: Frameworks, checklists, efficiency tips
→ Pain points: Inconsistent quality, wastes time on basics
→ Success metric: Produces good output consistently

PERSONA 3: EXPERT
→ Skill level: Advanced
→ Needs: Advanced techniques, customization, innovation
→ Pain points: Bored with basics, wants to push boundaries
→ Success metric: Produces elite output, creates new techniques
```

### Step 1.3: Success Criteria Definition

```
Define what "success" looks like:

FUNCTIONAL SUCCESS:
→ The skill activates correctly
→ It handles all defined tasks
→ It produces correct output

QUALITY SUCCESS:
→ Output meets defined standards
→ Quality is consistent
→ Errors are handled gracefully

IMPACT SUCCESS:
→ Users are satisfied
→ Output rivals human experts
→ Skill saves time and effort
```

### Step 1.4: Skill Lifecycle Mapping

```
Map the full lifecycle:

CREATION → INSTALLATION → ACTIVATION → EXECUTION → OUTPUT → FEEDBACK → ITERATION

For each stage:
→ What happens?
→ What could go wrong?
→ How is it handled?
→ How does it improve?
```

---

## 🏗️ PHASE 2: ARCHITECTURE DESIGN

### The Skill Architecture Blueprint

```
SKILL STRUCTURE:

SKILL.md (The Brain)
├── Purpose & Identity
├── Trigger Conditions
├── Core Directives (3-7)
├── Reasoning Protocol
├── Output Standards
├── Quality Gates
├── Safety & Ethics
└── Reference Map

references/ (The Knowledge Base)
├── frameworks.md (Proven methods)
├── patterns.md (Recurring structures)
├── standards.md (Quality benchmarks)
├── examples.md (Case studies)
└── advanced.md (Expert techniques)

templates/ (The Tools)
├── quick-start.md (For novices)
├── standard.md (For competent)
├── advanced.md (For experts)
└── checklist.md (Quality assurance)

README.md (The Guide)
├── Overview
├── Installation
├── Usage
├── Structure
└── Notes
```

### Component Relationship Map

```
USER REQUEST
    |
    v
TRIGGER DETECTION → "Should I activate?"
    |
    v
INPUT ANALYSIS → "What am I dealing with?"
    |
    v
REASONING ENGINE → "How should I think about this?"
    |
    v
FRAMEWORK SELECTION → "What's the best approach?"
    |
    v
EXECUTION → "Do the work"
    |
    v
QUALITY CHECK → "Is this good enough?"
    |
    v
OUTPUT DELIVERY → "Present the result"
    |
    v
FEEDBACK LOOP → "What can I learn?"
```

---

## 🧠 PHASE 3: CORE BUILDING (SKILL.md)

### Section 1: Metadata Header

```yaml
---
name: [skill-name]
description: [One powerful sentence describing what this skill does, when to use it, and why it's special]
metadata: '{"openclaw": {"emoji": "[emoji]", "requires": {"bins": []}}}'
---
```

**Rules for description:**
→ One sentence, max 50 words
→ Include: what it does + when to use + unique value
→ Make it compelling — this is the elevator pitch

### Section 2: Identity & Mission

```markdown
# [Emoji] [Skill Name]

> **Identity**: [Who the agent becomes when using this skill]

> **Mission**: [What this skill achieves at the highest level]
```

**Rules:**
→ Identity should be aspirational and specific
→ Mission should be impact-focused
→ Both should be memorable

### Section 3: Quick Start Protocol

```markdown
## Quick Start

**Before [doing the task], execute the [PROTOCOL NAME]:**

```
1. [STEP 1] → [What to do]
2. [STEP 2] → [What to do]
3. [STEP 3] → [What to do]
4. [STEP 4] → [What to do]
5. [STEP 5] → [What to do]
```
```

**Rules:**
→ 5-8 steps maximum
→ Each step is atomic and actionable
→ Steps flow logically
→ Include a "why" for critical steps

### Section 4: Core Directives (3-7)

```markdown
## Core Directives

### 🎯 Directive 1: [Name]
[What the directive requires]
[How to apply it]
[Why it matters]
[Example of application]

### 🎯 Directive 2: [Name]
...
```

**Rules:**
→ 3-7 directives (not too few, not too many)
→ Each directive covers a distinct aspect
→ Directives should be mutually reinforcing
→ Include practical application, not just theory
→ Use emojis for visual distinction

### Section 5: Reasoning Protocol

```markdown
## Reasoning Protocol

**When [condition], execute:**

```
1. ANALYZE → [What to analyze]
2. PLAN → [How to plan]
3. EXECUTE → [How to execute]
4. VERIFY → [How to verify]
5. REFINE → [How to refine]
```
```

**Rules:**
→ Protocol should be domain-appropriate
→ Include decision points (if/then)
→ Include verification steps
→ Include error handling

### Section 6: Output Standards

```markdown
## Output Standards

### Structure
→ [Required sections]
→ [Optional sections]
→ [Format specifications]

### Quality
→ [Minimum quality bar]
→ [Excellent quality bar]
→ [Legendary quality bar]

### Style
→ [Voice characteristics]
→ [Tone guidelines]
→ [Forbidden patterns]
```

### Section 7: Quality Gates

```markdown
## Quality Gates

**Before delivering ANY output, verify:**

```
□ [GATE 1]: [Check] → [Pass criteria]
□ [GATE 2]: [Check] → [Pass criteria]
□ [GATE 3]: [Check] → [Pass criteria]
□ [GATE 4]: [Check] → [Pass criteria]
□ [GATE 5]: [Check] → [Pass criteria]
```
```

### Section 8: Safety & Ethics

```markdown
## Safety & Ethics

→ [Safety rule 1]
→ [Safety rule 2]
→ [Ethical guideline 1]
→ [Ethical guideline 2]
```

---

## 📚 PHASE 4: REFERENCE BUILDING

### Reference File Types

```
TYPE 1: FRAMEWORKS
→ Proven methods and structures
→ When to use each
→ How to apply each
→ Examples

TYPE 2: PATTERNS
→ Recurring structures in the domain
→ Common solutions to common problems
→ Anti-patterns to avoid

TYPE 3: STANDARDS
→ Quality benchmarks
→ Industry best practices
→ Measurement criteria

TYPE 4: EXAMPLES
→ Case studies
→ Before/after comparisons
→ Success stories

TYPE 5: ADVANCED
→ Expert-level techniques
→ Customization options
→ Innovation triggers
```

### Reference Quality Standards

```
□ Every concept has a definition
□ Every framework has an example
→ Every pattern has a use case
→ Every standard has a measurement
→ Every example has a lesson
→ Every advanced topic has prerequisites
```

---

## 🛠️ PHASE 5: TEMPLATE BUILDING

### Template Types

```
TYPE 1: QUICK-START
→ For novices
→ Step-by-step with examples
→ Minimal decisions required
→ High hand-holding

TYPE 2: STANDARD
→ For competent users
→ Framework-based
→ Some customization
→ Moderate guidance

TYPE 3: ADVANCED
→ For experts
→ Minimal structure
→ Maximum flexibility
→ Power-user features

TYPE 4: CHECKLIST
→ Quality assurance
→ Pre-execution checks
→ Post-execution verification
→ Continuous improvement
```

### Template Structure

```markdown
# [Template Name]

## Pre-[Task] Checklist
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

## [Task] Structure
### Section 1: [Name]
→ [What to include]
→ [How to structure]
→ [Example]

### Section 2: [Name]
...

## Post-[Task] Checklist
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
```

---

## ✅ PHASE 6: QUALITY ASSURANCE

### The 10-Dimension Audit

```
D1. PURPOSE CLARITY (1-10)
→ Is the skill's purpose crystal clear?
→ Does it know EXACTLY when to activate?

D2. REASONING DEPTH (1-10)
→ Does it think before acting?
→ Are there multi-step reasoning protocols?

D3. FRAMEWORK RICHNESS (1-10)
→ How many proven frameworks?
→ Are they from world-class sources?

D4. OUTPUT QUALITY (1-10)
→ Are output standards defined?
→ Is there a quality checklist?

D5. EDGE CASE HANDLING (1-10)
→ Does it handle errors gracefully?
→ Are there fallback protocols?

D6. CONTEXT AWARENESS (1-10)
→ Does it manage context intelligently?
→ Can it handle large inputs?

D7. TOOL INTEGRATION (1-10)
→ Does it use tools optimally?
→ Are there tool selection rules?

D8. VOICE & PERSONA (1-10)
→ Is the voice consistent?
→ Is the persona well-defined?

D9. REFERENCE QUALITY (1-10)
→ Are references comprehensive?
→ Are they authoritative?

D10. COMPLETENESS (1-10)
→ Does it cover ALL aspects?
→ Are there templates?

TARGET: 85+ average for elite tier
TARGET: 95+ average for legendary tier
```

### Stress Testing

```
TEST 1: EDGE CASE
→ Input: [Extreme/unusual input]
→ Expected: [How skill should handle]
→ Result: [Actual result]
→ Pass/Fail: [Status]

TEST 2: AMBIGUITY
→ Input: [Vague request]
→ Expected: [How skill should respond]
→ Result: [Actual result]
→ Pass/Fail: [Status]

TEST 3: INTEGRATION
→ Combined with: [Other skill]
→ Expected: [Seamless interaction]
→ Result: [Actual result]
→ Pass/Fail: [Status]

TEST 4: NOVICE TEST
→ User: [Beginner]
→ Expected: [Can follow without help]
→ Result: [Actual result]
→ Pass/Fail: [Status]

TEST 5: EXPERT TEST
→ User: [Advanced]
→ Expected: [Offers advanced features]
→ Result: [Actual result]
→ Pass/Fail: [Status]
```

---

## 📦 PHASE 7: PACKAGING & DELIVERY

### Folder Structure

```
[skill-name]/
├── SKILL.md                    # Main entry point
├── README.md                   # User guide
├── references/
│   ├── frameworks.md           # Proven methods
│   ├── patterns.md             # Recurring structures
│   ├── standards.md            # Quality benchmarks
│   ├── examples.md             # Case studies
│   └── advanced.md             # Expert techniques
├── templates/
│   ├── quick-start.md          # For beginners
│   ├── standard.md             # For intermediate
│   ├── advanced.md             # For experts
│   └── checklist.md            # Quality assurance
└── assets/                     # Images, diagrams, etc.
```

### README.md Template

```markdown
# [Skill Name] for OpenClaw

## Overview
[What this skill does and why it matters]

## Installation
[How to install]

## Usage
[How to use]

## Structure
[What's in the skill]

## Features
[Key capabilities]

## Notes
[Important considerations]
```

---

## Reference Materials

| File | Content |
|------|---------|
| `{baseDir}/references/skill-anatomy.md` | Complete anatomy of a legendary skill |
| `{baseDir}/references/design-patterns.md` | Recurring patterns in skill design |
| `{baseDir}/references/quality-framework.md` | The 10-dimension quality system |
| `{baseDir}/references/common-pitfalls.md` | Mistakes to avoid when building skills |
| `{baseDir}/templates/skill-creation-template.md` | Ready-to-use template for creating skills |

---

## CHANGELOG

- v1.0.0 — Instalasi awal skill-factory dari zip (meta-skill pembuat skill OpenClaw). Struktur: SKILL.md, README.md, references/ (common-pitfalls, design-patterns, quality-framework, skill-anatomy), templates/ (skill-creation-template), assets/. Scan keamanan: token/secret BERSIH, tidak ada exec/network call, tidak ada unicode tersembunyi.
