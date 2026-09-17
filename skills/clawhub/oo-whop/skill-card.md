## Description:

Whop connector skill for searching and reading users, companies, memberships, and products through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve Whop authorized users, companies, memberships, and products through the OOMOL oo CLI without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified remote installer in the user's shell.

Mitigation: Download and inspect the installer before execution, and verify a published checksum or signature when available.

Risk: The connector can retrieve Whop account data such as users, companies, memberships, and products from the connected account.

Mitigation: Use only the listed read actions, confirm the intended account and scope, and avoid requesting data beyond the user's task.

## Reference(s):

- [Whop homepage](https://whop.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; live action schemas should be inspected before payload construction.]

## Skill Version(s):

1.0.3 (source: server evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
