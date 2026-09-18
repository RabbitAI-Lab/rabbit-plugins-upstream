## Description:

FFHub helps agents read, create, and update FFHub FFmpeg task data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect FFHub action schemas and list, retrieve, or create FFmpeg tasks in an OOMOL-connected FFHub account. It is intended for agent-assisted FFHub operations where write payloads are confirmed before task creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct shell execution of a remote oo CLI installer.

Mitigation: Use a safer verified installation method when available, or download and review the installer before execution.

Risk: The create_ffmpeg_task action changes FFHub state by creating a new FFmpeg task.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub FFHub Skill Page](https://clawhub.ai/oomol/skills/oo-ffhub)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [FFHub Homepage](https://ffhub.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
