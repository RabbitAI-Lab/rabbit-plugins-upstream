## Description:

Enables agents to read and manage Lemon Squeezy account data through OOMOL's Lemon Squeezy connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Lemon Squeezy stores, users, customers, products, variants, orders, subscriptions, and webhooks, and to create or update selected customers and webhooks with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer scripts directly in a shell.

Mitigation: Install the OOMOL CLI from a verified, versioned source and review the setup path before installation.

Risk: The skill can create, update, or delete Lemon Squeezy account data.

Mitigation: Use it only for intended Lemon Squeezy account work and require explicit user confirmation before creating, updating, or deleting customers or webhooks.

Risk: Action payloads can become stale if connector contracts change.

Mitigation: Inspect the live connector schema before constructing or running an action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lemon-squeezy)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Lemon Squeezy homepage](https://www.lemonsqueezy.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Lemon Squeezy connector results as JSON and should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
