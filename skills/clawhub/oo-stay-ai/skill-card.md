## Description:

Stay AI lets agents inspect action schemas and run read actions for account settings, orders, and subscriptions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Stay AI account settings, subscriptions, and orders without handling raw Stay AI credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified pipe-to-shell installer commands that can execute arbitrary remote code.

Mitigation: Review the installer source before use; avoid curl | bash or PowerShell iex unless the source is trusted, and prefer a pinned, signed, or checksum-verified installation method when available.

## Reference(s):

- [ClawHub Stay AI skill page](https://clawhub.ai/oomol/skills/oo-stay-ai)
- [Stay AI homepage](https://stay.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
