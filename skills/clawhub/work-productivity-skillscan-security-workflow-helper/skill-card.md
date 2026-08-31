## Description:

Helps agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixing, setup hardening, safety review, reliability improvement, and adjacent skill creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and AI-agent teams use this skill to turn SkillScan-style security and reliability needs into actionable plans, checklists, workflows, analysis, code changes, or decision support. It emphasizes local-hardware-friendly execution and visible validation against the user's success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation wording is broad enough that the skill may be selected for generic security or workflow requests.

Mitigation: Invoke the skill deliberately by name for SkillScan-style security workflow assistance, or narrow triggers before deployment.

Risk: The skill produces plans, checklists, analysis, commands, code, or configuration that may be incorrect for a user's environment.

Mitigation: Review outputs against the stated success criteria, test proposed commands or code in a controlled environment, and scan skill changes before deployment.

Risk: Security guidance can be incomplete if the user omits constraints, existing controls, or threat context.

Mitigation: State assumptions, ask only for missing information that materially changes the result, and list remaining risks or follow-up work.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter)
- [ClawHub SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [ClawHub AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [ClawHub PollyReach demand signal](https://clawhub.ai/skills/pollyreach)
- [Ask HN: Android /iOS mobile application Vulnerability Scanning](https://news.ycombinator.com/item?id=49498013)
- [Ask HN: Just finished building a security audit tool](https://news.ycombinator.com/item?id=49504798)
- [GitHub issue: Sprint Planning - 2026/08/31 (Week 36)](https://github.com/nisyuu/makasete-ai/issues/281)
- [GitHub issue: Media Plans with preview, diffs, drift, and rollback](https://github.com/jampat000/Deluno/issues/343)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, text, code snippets, shell commands, configuration, or structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, validation checks, remaining risks, and follow-up work when relevant.]

## Skill Version(s):

0.20260831.40551 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
