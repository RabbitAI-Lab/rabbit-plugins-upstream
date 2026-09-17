## Description:

Chattermill (chattermill.com) lets an agent read, create, update, and delete Chattermill data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and operations teams use this skill to inspect Chattermill action schemas and run read, search, create, update, and delete actions against connected Chattermill projects through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use the skill only after independently trusting and verifying the installer source, or prefer official package-manager or signed-release installation steps when available.

Risk: Requests are routed through OOMOL with server-side credential handling.

Mitigation: Use the connector only when routing Chattermill requests through OOMOL is acceptable for the intended workspace and data.

Risk: Write and destructive actions can modify or permanently delete Chattermill data.

Mitigation: Inspect the live action schema first and confirm the exact payload, target, and effect before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chattermill)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Chattermill homepage](https://chattermill.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/chattermill.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the oo CLI when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
