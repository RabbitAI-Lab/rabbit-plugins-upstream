## Description:

Reviews ClawHub skills and plugins before release, from a fast launch checklist to deep evidence-based validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ClawHub publishers use this skill before publishing skills or plugins to check release readiness, evidence quality, consistency, security posture, and next dry-run commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated publish or dry-run commands may be unsafe if placeholders, paths, owners, or quoted arguments are copied without review.

Mitigation: Check inserted values, quote or pass arguments safely, and keep formal publishing behind explicit user confirmation.

Risk: A readiness report can overstate release status when dry-run, registry, moderation, or isolated install evidence is missing.

Mitigation: Keep evidence boundaries explicit and separate local validation, dry-run, registry visibility, moderation, and install proof.

Risk: Sensitive release environments may be affected by unexpected CLI behavior or unreviewed dependency changes.

Mitigation: Use a pinned or reviewed ClawHub CLI version for sensitive release workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/skill-publish-readiness)
- [OpenClaw publisher homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [Consistency rules](references/consistency_rules.md)
- [Security review guide](references/security_review_guide.md)
- [Differentiation rubric](references/differentiation_rubric.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quick or deep review sections, evidence boundaries, severity labels, and dry-run commands.]

## Skill Version(s):

2.0.0 (source: frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
