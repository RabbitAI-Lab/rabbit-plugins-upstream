## Description:

Use this skill for TicketSource requests at ticketsource.co.uk, including searching and reading data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read TicketSource account data through the OOMOL TicketSource connector, including listing events, retrieving a specific event, and listing event dates or venues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting OOMOL to TicketSource grants the service access needed to retrieve TicketSource account data.

Mitigation: Install only when OOMOL should bridge to the TicketSource account, review the oo CLI installation source, and grant only TicketSource scopes the user is comfortable authorizing.

Risk: Connector commands can fail when the oo CLI is missing, authentication has expired, billing is stopped, or the TicketSource connection is unavailable.

Mitigation: Run first-time setup steps only after the matching command failure and reconnect or recharge through the documented OOMOL flows before retrying.

## Reference(s):

- [TicketSource homepage](https://www.ticketsource.co.uk/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [TicketSource skill page](https://clawhub.ai/oomol/skills/oo-ticket-source)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal operation uses read-only oo CLI connector actions and returns connector JSON responses.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
