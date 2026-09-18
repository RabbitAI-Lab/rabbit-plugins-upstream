## Description:

TicketSource (ticketsource.co.uk). Use this skill for TicketSource requests that search and read data from a connected TicketSource account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TicketSource event data through an OOMOL-connected account. It supports reading individual events and listing events, performance dates, and venues after checking the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Run setup only when the oo CLI is intentionally needed, and prefer a signed or checksum-verified installer before executing the installer.

Risk: The skill depends on an OOMOL-connected TicketSource account and server-side credentials.

Mitigation: Use the documented connection flow only after an auth or connection failure, and avoid handling raw TicketSource tokens directly.

## Reference(s):

- [TicketSource skill page](https://clawhub.ai/oomol/skills/oo-ticket-source)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [TicketSource homepage](https://www.ticketsource.co.uk/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
