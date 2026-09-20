## Description:

Faktoora (faktoora.com). Use this skill for ANY Faktoora request - reading, creating, updating, and deleting data. Whenever a task involves Faktoora, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Faktoora projects through an OOMOL-connected account, including reading, creating, updating, deleting, attaching, and detaching project resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes running a remote installer script directly in a shell.

Mitigation: Review the oo CLI installer source first or use an OOMOL installation path that supports version pinning and integrity verification.

Risk: The skill can create, update, attach, detach, and delete Faktoora project resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Faktoora skill listing](https://clawhub.ai/oomol/skills/oo-faktoora)
- [Faktoora homepage](https://faktoora.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
