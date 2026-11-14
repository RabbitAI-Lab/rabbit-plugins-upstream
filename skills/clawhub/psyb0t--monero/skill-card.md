## Description:

Operate a user-run docker-monero instance to inspect node and wallet state, manage wallets, and send explicitly approved XMR payments through REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

People running docker-monero use this skill to check node sync status, inspect wallet balances and transactions, obtain receiving addresses, and initiate user-approved XMR transfers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending XMR is irreversible and may move real funds.

Mitigation: Require explicit approval for the destination and amount, perform a dry run to show fees, and disable transfers or enable read-only mode unless sends are needed.

Risk: Bearer tokens and wallet passwords can be exposed over insecure connections.

Mitigation: Connect only to the user's instance over localhost, HTTPS, or private networking; do not expose tokens over plain HTTP.

Risk: Using an unpinned container image can change software handling funds unexpectedly.

Mitigation: Pin the Docker image digest for funds-bearing deployments rather than using the latest tag.

## Reference(s):

- [docker-monero setup guide](references/setup.md)
- [docker-monero project documentation (skill-linked homepage)](https://github.com/psyb0t/docker-monero)
- [ClawHub Monero skill listing](https://clawhub.ai/psyb0t/skills/monero)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-configured docker-monero endpoint and bearer token; transfers require explicit user approval.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
