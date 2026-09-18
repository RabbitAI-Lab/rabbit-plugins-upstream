## Description:

Short Menu enables agents to create, update, and delete Short Menu short links through the OOMOL short_menu connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Short Menu short links through an OOMOL-connected account. The skill is intended for link creation, update, and deletion workflows where write and destructive actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI from a trusted, verifiable source, inspect the installer before running it, and avoid elevated privileges unless required.

Risk: The skill can create, update, and delete Short Menu links.

Mitigation: Confirm the exact payload, target link, and expected effect with the user before write or destructive actions.

Risk: Connector input fields may change over time.

Mitigation: Inspect the live short_menu action schema before building each action payload.

## Reference(s):

- [Short Menu ClawHub skill page](https://clawhub.ai/oomol/skills/oo-short-menu)
- [Short Menu homepage](https://shortmenu.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before actions; write and destructive actions require explicit confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
