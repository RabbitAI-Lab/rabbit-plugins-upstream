## Description:

Pushsafer enables agents to list Pushsafer devices and groups and send push notifications through an OOMOL-connected Pushsafer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to inspect Pushsafer devices or groups and send notifications through an already connected OOMOL Pushsafer account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send push notifications through the connected Pushsafer account.

Mitigation: Confirm the exact send_message payload, recipient, and notification contents with the user before execution.

Risk: Setup commands can install the oo CLI or modify authentication and account-connection state.

Mitigation: Run setup only when an auth, connection, billing, or missing-CLI error shows it is needed and the user trusts OOMOL and the connector.

## Reference(s):

- [ClawHub Pushsafer skill page](https://clawhub.ai/oomol/skills/oo-pushsafer)
- [Pushsafer homepage](https://www.pushsafer.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
