## Description:

Enables agents to read, create, and update Google Forms through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate Google Forms through an OOMOL-connected account, including retrieving forms and responses, creating forms, applying batch updates, and changing publish settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code.

Mitigation: Install the oo CLI only from a verified package, pinned release, or inspected download before using the skill.

Risk: Google Forms write actions can create forms, apply batch updates, or change publish and response settings.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Google Forms skill page](https://clawhub.ai/oomol/skills/oo-googleforms)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Forms](https://workspace.google.com/products/forms/)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns JSON responses from oo CLI actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
