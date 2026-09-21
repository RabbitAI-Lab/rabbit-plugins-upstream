## Description:

元审 yotta-vetter helps agents and developers perform a structured pre-installation safety review of skills using source, code, permission, and risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent users use this skill before installing or evaluating unknown skills to produce an initial vetting report and decide what needs human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a material scanner bypass risk.

Mitigation: Use the skill only as an initial review aid and manually inspect reviewed skill files, especially exempt basenames such as audit_rules.py, vetter_rules.py, verify_rules.py, and hardening_rules.py.

Risk: The security evidence flags installation behavior that users should review before trusting it.

Mitigation: Pin the npm package version during installation and avoid bulk or global installation unless adding the skill to every listed agent is intended.

Risk: The skill produces review guidance rather than an install approval authority.

Mitigation: Require human confirmation of findings and permissions before installing or trusting a reviewed skill.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Project homepage](https://github.com/YottaMeta/yotta-vetter)
- [Four-phase vetting checklist](references/checklist.md)
- [SKILL VETTING REPORT template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text, Markdown reports, and optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review and report output only; final install decisions require human confirmation.]

## Skill Version(s):

0.2.5 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
