## Description:

Detrack helps agents read, create, update, and delete Detrack delivery and collection data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to manage Detrack jobs and depots through OOMOL's oo CLI. It supports read workflows plus confirmed create, update, and delete actions for delivery or collection jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute downloaded code.

Mitigation: Use verified official installation steps, inspect downloads before execution, and do not pipe remote installer scripts directly into a shell.

Risk: Create, update, and delete actions can change or remove Detrack operational data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: The connector depends on trusted OOMOL and Detrack account access.

Mitigation: Install and use the skill only when the publisher and connected account permissions are trusted for the intended workspace.

## Reference(s):

- [ClawHub Detrack skill listing](https://clawhub.ai/oomol/skills/oo-detrack)
- [Detrack homepage](https://www.detrack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
