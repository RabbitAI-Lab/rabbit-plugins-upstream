## Description:

TicketSource helps an agent search and read TicketSource account data through OOMOL's ticket_source connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users with OOMOL-connected TicketSource accounts use this skill to retrieve events, performance dates, and venues. The skill also guides agents to inspect live action schemas before sending connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review or verify the installer through OOMOL's official installation documentation, avoid elevated shells, and do not let an agent run the installer automatically.

Risk: The connected TicketSource account may expose private business event data.

Mitigation: Use the skill only with an authorized OOMOL-connected account and limit returned event, performance, and venue data to the user's request.

Risk: Connector action inputs and outputs may change over time.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing or sending JSON payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ticket-source)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [TicketSource Homepage](https://www.ticketsource.co.uk/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schemas before payload construction.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
