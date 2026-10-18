## Description:

Helps agents manage EdgeOne Makers projects, deployments, and environment variables through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect EdgeOne Makers projects and deployments, manage environment variables, and request project or deployment changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup suggests running an unverified remote installer directly in a shell.

Mitigation: Review the installer source or use a verified package-manager or signed release installation before using the CLI.

Risk: Write and destructive actions can change configuration or delete project data.

Mitigation: Approve these actions only after confirming the exact project, payload, and effect.

## Reference(s):

- [EdgeOne Makers skill release](https://clawhub.ai/oomol/skills/oo-edgeone-makers)
- [EdgeOne Makers product](https://edgeone.ai/zh/products/pages)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text, with JSON action results when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project, deployment, log, or environment variable details.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
