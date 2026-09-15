## Description:

The airfocus skill lets an agent read, create, update, and delete airfocus data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage airfocus profiles, workspaces, and items from an agent while relying on OOMOL-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Review the installer path before installing; prefer a verified package or downloaded, inspected, version-pinned artifact.

Risk: Write and delete actions can change or permanently remove airfocus data.

Mitigation: Approve write or delete actions only after checking the exact workspace, item, and payload.

## Reference(s):

- [airfocus homepage](https://airfocus.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [airfocus skill on ClawHub](https://clawhub.ai/oomol/skills/oo-airfocus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can trigger read, write, and destructive connector actions after schema inspection and required user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
