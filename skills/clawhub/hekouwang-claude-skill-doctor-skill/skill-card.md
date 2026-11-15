## Description:

Audits agent skills for trigger clarity, structure, portability, security hygiene, and host compatibility, then produces a scorecard and prioritized improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-skill authors use this skill to audit SKILL.md files and skill directories, then review a scorecard and prioritized fixes. Optional workflows extend checks to project documentation, local development environments, and model-based trigger evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trigger evaluation sends evaluation queries and the tested skill description to an external model service and can incur usage charges.

Mitigation: Do not include sensitive content in evaluation queries; use isolated credentials when appropriate, and run this optional workflow only when its data sharing and cost are acceptable.

Risk: The available security assessment is partial and medium-confidence, with unresolved environment-access and Docker-reference questions.

Mitigation: Review the remaining scanner questions that apply to your setup before using the relevant optional workflows.

## Reference(s):

- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill)
- [ClawHub release page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill)
- [Trigger evaluation guide](references/trigger-eval.md)
- [Doctor suite guide](references/doctor-suite.md)
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable scorecards and remediation guidance in text or Markdown, with optional machine-readable JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON reports include findings, scores, and a gate result. Optional model-based trigger evaluation should be calibrated with the documented A/B check before relying on its scores.]

## Skill Version(s):

1.8.6 (source: frontmatter and changelog, released 2026-11-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
