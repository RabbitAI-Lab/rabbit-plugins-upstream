## Description:

Eventzilla (eventzilla.net). Use this skill for ANY Eventzilla request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and read Eventzilla organizer account data, including events, attendees, transactions, users, and ticket categories through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could run mutable code locally.

Mitigation: Use a trusted OOMOL installation path with version pinning or checksum/signature verification where available, inspect installer contents before execution, and run setup with ordinary user privileges.

Risk: Eventzilla attendee, transaction, ticket, organizer, and user data is routed through OOMOL for read operations.

Mitigation: Confirm that this data-routing path is acceptable before connecting the Eventzilla account and running read actions.

## Reference(s):

- [Eventzilla homepage](https://www.eventzilla.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Eventzilla skill page](https://clawhub.ai/oomol/skills/oo-eventzilla)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to validate action payloads before execution.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
