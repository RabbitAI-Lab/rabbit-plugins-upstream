## Description:

Use this skill for Crustdata requests by searching and reading company data through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search, identify, enrich, and autocomplete company data in Crustdata through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running remote installer scripts directly in a shell.

Mitigation: Use official, versioned installation instructions and verify installers before executing them.

Risk: Crustdata access is brokered through OOMOL-connected account credentials.

Mitigation: Install only when using OOMOL as the credential broker is acceptable for the account and data involved.

## Reference(s):

- [Crustdata homepage](https://crustdata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Crustdata skill on ClawHub](https://clawhub.ai/oomol/skills/oo-crustdata)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Crustdata connector responses as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
