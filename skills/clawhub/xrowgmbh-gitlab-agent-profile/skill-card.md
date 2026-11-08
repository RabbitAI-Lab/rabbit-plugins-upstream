## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to update a GitLab agent profile with monthly contribution charts and a public proof file summarizing merged work and direct owner commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback can automatically download and run an unpinned package with the process's GitLab access and filesystem privileges.

Mitigation: Review the package source and intended tool access, pin a reviewed package version, and run with only the credentials and filesystem access needed for the update.

Risk: The scan was partial because five local references were unresolved, leaving evidence about those references incomplete.

Mitigation: Resolve and review the referenced files, and confirm the skill's required tools and access scope before installation.

## Reference(s):

- [GitLab Agent Profile release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile on ClawHub](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [SVG and WebP contribution charts, a JSON proof file, and Markdown instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The proof file includes public counted records and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.132.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
