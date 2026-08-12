## Description:

Audits Agent Skill directories for SKILL.md structure, trigger quality, progressive disclosure, portability, script placement, and basic secret hygiene, then returns a scorecard and prioritized fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill maintainers use this skill to review Agent Skill packages, run deterministic checks, interpret structural issues, and plan concrete fixes before publishing or installing a skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional helper scripts have higher operational impact: trigger evaluation spends Claude CLI/API quota and inherits the local CLI environment, while the doctor-suite runner can inspect the local development environment through env-doctor.

Mitigation: Use check.py for normal reviews, and run trigger_eval.py or run-all-doctors.sh only as deliberate opt-in steps after confirming the target path, expected cost, and local environment exposure.

Risk: Audit results and refactoring suggestions can be incomplete or misleading if applied without review.

Mitigation: Review findings before changing a skill, apply edits intentionally, and rerun the checker after modifications.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill)
- [Project Homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill)
- [Doctor Suite Reference](references/doctor-suite.md)
- [Skill Writing Vocabulary](references/skill-writing-vocab.md)
- [Trigger Evaluation Reference](references/trigger-eval.md)
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Code, Guidance]

**Output Format:** [Markdown scorecards, JSON reports, shell commands, and refactoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized recommendations, optional command-line checks, and JSON output from check.py --json.]

## Skill Version(s):

1.5.1 (source: frontmatter, changelog released 2026-08-12, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
