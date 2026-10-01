## Description:

Provides read-only Ticket Tailor data retrieval through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users with an OOMOL-connected Ticket Tailor box office use this skill to retrieve events, orders, and issued tickets through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad invocation rule for Ticket Tailor requests.

Mitigation: Use it for specific Ticket Tailor data retrieval tasks and avoid applying it to unrelated mentions of Ticket Tailor.

Risk: The artifact includes remote CLI install one-liners.

Mitigation: Prefer a verified or package-managed oo CLI installation path before connecting accounts or running commands.

Risk: Using the connector grants read access to Ticket Tailor events, orders, and issued tickets through OOMOL.

Mitigation: Install only when that access is acceptable for the connected account and intended workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ticket-tailor)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ticket Tailor Homepage](https://www.tickettailor.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns read-oriented Ticket Tailor data through the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
