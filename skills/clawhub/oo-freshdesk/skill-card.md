## Description:

This skill helps agents operate Freshdesk through OOMOL's oo CLI to search and read account, ticket, and conversation data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer users can use this skill to inspect Freshdesk account details, retrieve tickets, list tickets, and review ticket conversations through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review and verify the OOMOL installer source before use; prefer a pinned, signed, or checksum-verified installation path.

Risk: Connector capabilities may be broader than the listed read-only Freshdesk actions if a live schema exposes additional actions.

Mitigation: Keep usage to the listed read-only actions unless the live schema and explicit user approval justify broader access.

## Reference(s):

- [Freshdesk homepage](https://www.freshworks.com/freshdesk/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Freshdesk skill page](https://clawhub.ai/oomol/skills/oo-freshdesk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses generally guide oo CLI schema inspection and read-only Freshdesk connector calls.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
