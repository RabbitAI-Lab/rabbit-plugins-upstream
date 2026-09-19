## Description:

Eventzilla helps agents search and read Eventzilla organizer account data through OOMOL's oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and event-operations agents use this skill to retrieve Eventzilla events, attendees, ticket categories, transactions, organizers, and sub-organizers through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and irm-to-iex installer commands that execute remote code without pinning or verification.

Mitigation: Review the installer path before installation, prefer official versioned OOMOL installation guidance or a package manager, and run remote installer commands only after trusting the endpoint and understanding their effect.

Risk: The skill depends on an authenticated OOMOL Eventzilla connection and may fail when authentication, connection scope, credentials, or billing are not ready.

Mitigation: Run setup or connection recovery only after a matching command failure, then resolve sign-in, Eventzilla connection, credential, scope, or billing errors before retrying.

## Reference(s):

- [Eventzilla Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-eventzilla)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Eventzilla Homepage](https://www.eventzilla.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with oo CLI command examples and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; normal supported actions are read-only get and list operations.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
