## Description:

Helps agent users, skill authors, maintainers, and teams create practical vetting-style workflows, checklists, analyses, or implementation support for improving skill reliability, safety, setup, and adjacent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and agent users use this skill to turn a skill-vetting or reliability request into a concrete workflow, checklist, analysis, code change, or decision aid. It is intended for practical support around bug fixing, setup hardening, safety review, and adjacent skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms may cause the skill to influence ordinary security, GitHub, vetting, or bug-fix conversations unintentionally.

Mitigation: Review and narrow trigger rules before installation where possible, prefer explicit invocation for sensitive work, and verify the skill's recommendations before applying them.

Risk: Workflow, checklist, or implementation guidance could be incomplete or misleading for a specific codebase or operational environment.

Mitigation: Validate outputs against local success criteria, scan proposed changes, and keep assumptions, limits, and follow-up risks visible in the final response.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent)
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github)
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan)
- [Ask HN: Do you route only certain websites through a VPN?](https://news.ycombinator.com/item?id=49583757)
- [Ask HN: Are we normalizing surveillance in the name of safety?](https://news.ycombinator.com/item?id=49586069)
- [User-guide-driven development with coding agents](https://news.ycombinator.com/item?id=49579372)
- [How do you filter noise from signal in programming resources?](https://news.ycombinator.com/item?id=49580521)
- [GitHub issue: feature branch CI and pre-PR review](https://github.com/kouitic/jstock_advisor/issues/230)
- [GitHub issue: random sort bug](https://github.com/mealie-recipes/mealie/issues/8324)
- [GitHub issue: OpenClaw ecosystem daily](https://github.com/96loveslife/big_model_radar/issues/451)
- [GitHub issue: HEIC photo rejection bug](https://github.com/paro-studio/web/issues/94)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260907.40414 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
