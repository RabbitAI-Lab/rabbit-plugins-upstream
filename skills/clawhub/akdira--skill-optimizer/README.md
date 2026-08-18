# Skill Optimizer 🔬

> Train agent skills like neural networks — with epochs, learning rates, and validation gates — but without touching model weights.

Systematic skill document optimization for OpenClaw, adapted from [Microsoft SkillOpt](https://github.com/microsoft/skillopt) research.

## What is This?

SkillOpt (Microsoft Research, 2026) proved that you can dramatically improve AI agent accuracy by optimizing the **skill documents** (text SOPs) that guide agent behavior — without retraining the model itself. Their approach lifted accuracy from 41% → 80% on spreadsheet tasks and 33% → 72% on document tasks.

This skill adapts SkillOpt's methodology for OpenClaw's skill system. It treats each `SKILL.md` file as a "trainable parameter" and optimizes it through:

1. **Analyze** — Score the skill across 10 quality dimensions
2. **Propose** — Generate specific, bounded edits
3. **Gate** — Only accept edits that improve the score
4. **Report** — Show before/after comparison

## Quick Start

### Analyze a Skill
```
"Analyze skill: email-marketing-2"
```
Returns a quality score (0-50) with detailed breakdown.

### Optimize a Skill
```
"Optimize skill: email-marketing-2"
```
Creates backup, proposes edits, validates improvement, generates report.

### Batch Optimize
```
"Batch optimize skills"
```
Scores all workspace skills, optimizes the lowest-scoring ones first.

### Compare Before/After
```
"Compare skill: email-marketing-2"
```
Shows diff between current and backup versions.

## How It Works

### The SkillOpt Pipeline (Adapted)

```
┌─────────┐    ┌─────────┐    ┌───────────┐    ┌────────┐    ┌────────┐    ┌──────┐
│ Analyze │───→│ Propose │───→│ Select    │───→│ Update │───→│ Gate   │───→│ Report│
│ (Score) │    │ (Edits) │    │ (LR clip) │    │ (Edit) │    │ (Test) │    │       │
└─────────┘    └─────────┘    └───────────┘    └────────┘    └──────┘    └──────┘
     ↑                                                                    │
     └────────────────── Slow Update (next pass) ─────────────────────────┘
```

| SkillOpt Concept | Our Adaptation |
|---|---|
| Rollout (execute tasks) | Analyze skill structure + execution patterns |
| Reflect (analyze trajectories) | Score 10 quality dimensions, identify weaknesses |
| Aggregate (merge patches) | Combine related improvements |
| Select (learning rate) | Max 4 edits per pass (prevents overfitting) |
| Update (apply to doc) | Edit SKILL.md with bounded changes |
| Gate (validate) | Re-score, only accept improvements |
| Slow update | Gradual improvement across passes |
| Meta skill | Cross-skill patterns → better rubric |

### Quality Dimensions

Each skill is scored on 10 dimensions (1-5 each, max 50):

1. **Trigger Clarity** — Are activation triggers specific and comprehensive?
2. **Structure** — Consistent sections (Overview → Steps → Examples)?
3. **Step Completeness** — All steps present, ordered, actionable?
4. **Error Handling** — Edge cases, failures, exceptions covered?
5. **Input Validation** — Inputs validated before execution?
6. **Output Specification** — Expected outputs clearly defined?
7. **Examples** — Concrete before/after examples?
8. **Tool References** — Tools/commands referenced correctly?
9. **Dependencies** — Prerequisites documented?
10. **Maintainability** — Easy to update? Version controlled?

## Optimization Strategies

| Strategy | Problem | Impact |
|---|---|---|
| Structural Completion | Missing critical sections | 🔴 High |
| Trigger Expansion | Triggers too narrow | 🟠 Medium-High |
| Error Path Addition | Only happy path covered | 🔴 High |
| Example Enhancement | Abstract without examples | 🟡 Medium |
| Dependency Documentation | Prerequisites unclear | 🟡 Medium |
| Output Specification | Unclear expected output | 🟡 Medium |
| Step Decomposition | Steps too large/vague | 🟡 Medium |
| Cross-Reference Enhancement | No links to related skills | 🟢 Low-Medium |

## Validation Gate

An edit is ONLY accepted when ALL conditions are met:
- ✅ Quality score improves (or stays same with no regressions)
- ✅ No existing functionality is removed
- ✅ Edit is bounded (add/delete/replace, not full rewrite)
- ✅ No contradictions introduced
- ✅ Consistent tone and style maintained

Rejected edits are buffered for alternative formulation in the next pass.

## File Structure

```
skills/skill-optimizer/
├── SKILL.md                          # Main instructions (this skill)
├── README.md                         # This file
├── scripts/
│   ├── analyze-skill.sh             # Helper: parse + score skill structure
│   └── cron/
│       └── skill-optimizer-cron.sh  # Weekly cron job script
├── templates/
│   ├── skill-quality-rubric.md      # Detailed scoring rubric
│   └── optimized-skill-template.md  # Template for well-structured skills
├── references/
│   ├── skillopt-paper.md            # Paper summary + key concepts
│   └── meta-skill-patterns.md       # Cross-skill optimization patterns
└── examples/
    └── optimization-example.md      # Before/after optimization case study
```

## Cron Job — Automated Weekly Optimization

Automatically analyze and optimize skills on a weekly schedule.

### Setup

Register the cron job in OpenClaw:

```bash
openclaw cron add \
  --name "skill-optimizer-weekly" \
  --cron "0 3 * * 1" \
  --tz "Asia/Jakarta" \
  --message "Run skill-optimizer weekly cron: execute the cron script, review the report, and optimize the top 3 lowest-scoring skills." \
  --model "qwencloud/qwen3.6-flash" \
  --timeout-seconds 1800 \
  --session isolated
```

### What It Does

1. **Scans** all skills in `~/.openclaw/workspace/skills/`
2. **Analyzes** each skill (structure, sections, completeness)
3. **Scores** skills using the 10-dimension rubric
4. **Identifies** skills that need improvement (score < 35)
5. **Generates** a weekly report: `tmp/skill-optimization-cron-YYYY-MM-DD.md`
6. **Commits** any optimization changes to git

### Schedule

- **When:** Every Monday at 03:00 WIB (Asia/Jakarta)
- **Model:** qwen3.6-flash (budget-friendly)
- **Timeout:** 30 minutes max
- **Session:** Isolated (won't interfere with main chat)

### Manual Run

```bash
# Run the cron script manually
./scripts/cron/skill-optimizer-cron.sh

# Or trigger via OpenClaw
openclaw cron run skill-optimizer-weekly
```

### Report Format

Reports are saved to `tmp/skill-optimization-cron-YYYY-MM-DD.md` and include:
- Per-skill scores and metrics (words, sections, code blocks)
- Missing sections identification
- Overall statistics (total skills, analyzed, needs improvement)
- Recommended next steps

## Integration with Finn's Workflow

### With AAR (After Action Review)
After optimizing a skill, use it on a real task. Feed AAR findings back into the next optimization pass. Creates a continuous improvement loop.

### With Self-Improving Skill
The meta-skill extraction (cross-skill patterns) feeds into the self-improving skill's knowledge base.

### With Skill Workshop
Optimized skills can be submitted to the Skill Workshop for review and publication.

## Credits

- **Original research:** [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904) — Yang et al., Microsoft Research, 2026
- **Reference implementation:** [github.com/microsoft/skillopt](https://github.com/microsoft/skillopt) (15.5K+ stars)
- **Adaptation for OpenClaw:** Finn 🐺, PT Akdira Labs International

## License

Same as parent workspace. SkillOpt is MIT licensed.
