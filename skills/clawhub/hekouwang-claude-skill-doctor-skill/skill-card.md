## Description:

Checks Claude and Agent Skill packages for SKILL.md best-practice alignment, including trigger quality, length, progressive disclosure, externalized scripts, portability, and hardcoded secret risks, then produces a scorecard and prioritized repair guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill maintainers use this skill to audit Claude and Agent Skill directories, identify trigger, structure, portability, and safety issues, and receive prioritized repair guidance or proposed refactors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled scripts/run-all-doctors.sh can broaden a skill audit into local environment checks when explicitly run.

Mitigation: Review the command sequence and target path before running the script, and run it only in a workspace where local environment inspection is intended.

Risk: The optional trigger evaluation script invokes the Claude CLI, uses the current process environment, and can consume user quota.

Mitigation: Review scripts/trigger_eval.py before use, run it deliberately with a small evaluation set first, and confirm cost and environment assumptions before larger runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill)
- [Doctor suite reference](references/doctor-suite.md)
- [Skill writing vocabulary](references/skill-writing-vocab.md)
- [Trigger evaluation guide](references/trigger-eval.md)
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown and plain-text scorecards, optional JSON reports, and proposed file edits or shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The default checker is local and zero-dependency; optional trigger evaluation invokes the Claude CLI and can consume user quota.]

## Skill Version(s):

1.5.2 (source: frontmatter, changelog released 2026-08-12, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
