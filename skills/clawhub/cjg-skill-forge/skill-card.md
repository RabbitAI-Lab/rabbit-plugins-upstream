## Description:

Skill Forge is a meta-skill for creating, upgrading, reviewing, recasting, and clarifying WorkBuddy skills through structured quality loops, coverage audits, external benchmarking, production sign-off, live verification, and continuous feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use Skill Forge to build new agent skills, perform major skill upgrades, review release readiness, consolidate overlapping local skills, and improve AI readability while preserving the original task intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables local method-level logging by default.

Mitigation: Review the install notice before use and disable local logging if persistent local telemetry is not desired.

Risk: Cloud sync can upload anonymous feedback signals after explicit enablement.

Mitigation: Enable cloud sync only when the release's public endpoints and data-sharing posture are acceptable, and turn it off when cross-device or community aggregation is not needed.

Risk: Local skill-library scans and semantic scans can inspect local skill metadata and materials.

Mitigation: Run scan and recast workflows only on skill libraries whose contents are appropriate for review in the active environment.

Risk: Publishing and proposal workflows can apply changes and interact with external release platforms.

Mitigation: Use publishing, proposal approval, and proposal application commands only after reviewing proposed diffs, generated changelogs, and target account context.

Risk: Creator tokens are required for proposal workflows and could expose account access if stored carelessly.

Mitigation: Keep creator tokens in the documented local credential locations, outside synced folders and outside published skill packages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Skill Review Rubric](references/skill-review-rubric.md)
- [Skill Types](references/skill-types.md)
- [Feedback Loop](references/feedback-loop.md)
- [Signal Specification](references/signals.md)
- [Cloud Config Schema](references/cloud-config-schema.md)
- [Security Audit](references/security-audit.md)
- [Yunding Security Audit Gate](references/yunding-security-audit.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, file edits, code snippets, shell commands, reports, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local reports, proposal application steps, publishing commands, and optional cloud-sync guidance depending on the selected mode.]

## Skill Version(s):

2.9.14 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
