## Description:

Operate SeaTable through an OOMOL-connected account to read, create, update, and delete table data with the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other external users use this skill to work with SeaTable bases from an agent session, including listing rows, fetching metadata, appending rows, updating rows, and deleting rows after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI, which could be high-impact if run automatically or without user review.

Mitigation: Do not let an agent run the installer automatically; have the user review official installation instructions or verified releases and explicitly approve any setup command.

Risk: The skill can update or delete SeaTable data through write and destructive connector actions.

Mitigation: Require user confirmation of the exact payload, target rows, and expected effect before running write or destructive actions.

## Reference(s):

- [SeaTable homepage](https://seatable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SeaTable skill on ClawHub](https://clawhub.ai/oomol/skills/oo-seatable)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output should inspect live connector schemas before constructing payloads and should preserve confirmation steps for write and destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
