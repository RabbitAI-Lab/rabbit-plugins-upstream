## Description:

Helps agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows for bug fixes, setup and safety hardening, reliability improvements, and adjacent skill ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, skill authors, maintainers, and agent users use this skill to turn validated demand for Skill Vetter-style workflows into concrete plans, checklists, analysis, code changes, or implementation support. It is intended for practical work on bug fixing, setup and safety hardening, reliability, and related skill workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit activation may route generic security, GitHub, first-issue, or bug-fix requests to this skill unexpectedly.

Mitigation: Review trigger terms and implicit invocation before deployment; narrow keywords or require explicit invocation where predictable routing is important.

Risk: Generated workflow guidance may be incomplete or mismatched when the user's outcome, constraints, inputs, or success criteria are unclear.

Mitigation: Have the agent restate the outcome, constraints, available inputs, success criteria, assumptions, and validation notes before relying on generated artifacts or changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan)
- [CI hardening issue signal](https://github.com/joncfrancisco/pzbot/issues/14)
- [Security update issue signal](https://github.com/JackZeng/LongView-Chromium/issues/14)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code, shell command, configuration, checklist, and validation-note sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, constraints, success criteria, remaining risks, and follow-up work when relevant.]

## Skill Version(s):

0.20260826.40329 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
