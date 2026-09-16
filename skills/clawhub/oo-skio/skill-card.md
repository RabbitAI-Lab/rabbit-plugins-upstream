## Description:

Skio (skio.com). Use this skill for ANY Skio request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to read Skio commerce data through an OOMOL-connected account, including orders, products, storefront users, and subscriptions. It is intended for users who need authenticated Skio data lookup without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through verified official instructions or a package with checksum or signature validation before using the connector.

Risk: The skill relies on OOMOL and connected Skio account access.

Mitigation: Use it only with accounts and permissions appropriate for the requested read operations, and resolve authentication or connection setup only after a command reports that it is needed.

## Reference(s):

- [Skio homepage](https://skio.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to fetch each action schema before running Skio connector requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
