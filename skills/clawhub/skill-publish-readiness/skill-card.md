## Description:

Reviews ClawHub skill and plugin release candidates before publishing, checking completeness, consistency, environment declarations, security risks, and differentiation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ClawHub publishers use this skill to review local skill or plugin packages before release, identify blockers and risks, and receive a minimum fix path with validation or dry-run commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reviews local package files and may encounter secrets or sensitive configuration embedded in examples or metadata.

Mitigation: Use it on packages intended for review and redact credentials before review; follow its own checks for hardcoded tokens and credential-bearing URLs.

Risk: The skill can suggest ClawHub validation or publishing commands that affect release workflows.

Mitigation: Run validation and dry-run commands first, and require explicit confirmation before any real publishing action.

Risk: Publish-readiness guidance can miss registry, moderation, installation, or scanner state outside the supplied package evidence.

Mitigation: Treat the report as pre-publish guidance and verify final release status with platform validation, moderation results, inspect output, and isolated installation.

## Reference(s):

- [Security Review Guide](references/security_review_guide.md)
- [Differentiation Rubric](references/differentiation_rubric.md)
- [Consistency Rules](references/consistency_rules.md)
- [Publish Review Report Template](templates/publish_review_report.md)
- [Project Homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/skill-publish-readiness)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review report with prioritized findings, evidence matrix, minimum fix path, differentiation score, and validation or dry-run commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May branch output for skill or plugin packages; formal publishing actions require user confirmation.]

## Skill Version(s):

1.0.9 (source: frontmatter and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
