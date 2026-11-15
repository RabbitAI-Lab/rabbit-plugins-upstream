## Description:

Audits a local Hermes skill before ClawHub export and guides fixes to both the local and public versions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blueboyzx](https://clawhub.ai/user/blueboyzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers publishing or updating a Hermes skill use it to check accuracy, metadata, staging, and security before export, then verify the local and public copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit instructions include running bundled scripts on real inputs before a security review, and the available scan is partial.

Mitigation: Review scripts before running them; use copied or synthetic inputs in an isolated environment without credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/blueboyzx/skills/skill-export-audit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown audit findings, workflow guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and commands depend on the supplied skill tree and current registry state.]

## Skill Version(s):

1.1.0 (source: artifact frontmatter; server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
