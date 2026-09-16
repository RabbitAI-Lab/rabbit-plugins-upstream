## Description:

Fern enables agents to inspect schemas and run Fern connector actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Fern customers, payment accounts, transactions, and exchange-rate details through an OOMOL-connected Fern account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands from remote URLs.

Mitigation: Prefer an official, versioned installation method with checksum or signature verification, and review installers before execution.

Risk: Fern access depends on OOMOL as an intermediary for account credentials and connector execution.

Mitigation: Install only when OOMOL is an approved intermediary for Fern access and use appropriately scoped Fern connections.

## Reference(s):

- [ClawHub Fern skill page](https://clawhub.ai/oomol/skills/oo-fern)
- [Fern homepage](https://fernhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions inspect live schemas before payloads are constructed; listed actions are read-only.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
