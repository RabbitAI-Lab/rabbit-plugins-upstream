## Description: <br>
Audits Claude or Agent Skill directories for SKILL.md trigger quality, size, progressive disclosure, externalized scripts, portability, and hardcoded-secret risks, then returns a scorecard and prioritized repair guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and skill authors use this skill to review Claude or Agent Skill packages before release or installation. It combines deterministic checks with qualitative review to produce a scorecard, prioritized fixes, and optional restructuring guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for a broad range of skill-review, audit, linting, optimization, or restructuring prompts. <br>
Mitigation: Install it only when an opinionated Agent Skill auditor is desired, and review its output before applying suggested changes. <br>
Risk: The optional trigger-evaluation workflow can call the Claude CLI and consume the user's own API or CLI quota. <br>
Mitigation: Run trigger evaluation only when trigger quality needs empirical testing, and start with a small query set before larger evaluations. <br>
Risk: The skill scans local skill directories and can inspect files in the target package. <br>
Mitigation: Run it only against skill directories the user intends to inspect. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill) <br>
- [README](README.md) <br>
- [Skill writing vocabulary](references/skill-writing-vocab.md) <br>
- [Trigger evaluation guide](references/trigger-eval.md) <br>
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown reports, optional JSON audit output, prioritized guidance, and proposed code or shell command changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The zero-dependency checker runs locally; optional trigger evaluation can call the Claude CLI and consume the user's own API or CLI quota.] <br>

## Skill Version(s): <br>
1.4.1 (source: frontmatter and CHANGELOG, released 2026-08-01) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
