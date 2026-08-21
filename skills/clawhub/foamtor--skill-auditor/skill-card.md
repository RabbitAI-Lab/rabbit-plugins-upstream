## Description:

Audits SKILL.md instruction-following quality, detects the skill type, scores applicable compliance dimensions, and suggests improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foamtor](https://clawhub.ai/user/foamtor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and team leads use this skill to audit SKILL.md files for instruction-following structure, quality gates, and improvement opportunities before publishing or adopting agent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local Python script over a SKILL.md and nearby skill directory structure.

Mitigation: Install only if that local file access matches your review workflow, and review the script before use in sensitive workspaces.

Risk: Audit findings are quality guidance, not a security guarantee or automatic fixer.

Mitigation: Treat the report as advisory, review proposed changes manually, and run any normal security or policy review required before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/foamtor/skills/skill-auditor)
- [Server-Resolved GitHub Repository](https://github.com/Foamtor/skill-auditor)
- [Agent Skills Standard](https://agentskills.io)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report with optional JSON from a local Python audit script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads an existing SKILL.md and nearby skill directory structure; findings are quality guidance and do not automatically fix the skill.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
