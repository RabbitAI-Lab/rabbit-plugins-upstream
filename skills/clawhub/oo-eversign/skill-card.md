## Description:

Xodo Sign (eversign.com). Use this skill for ANY Xodo Sign request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Xodo Sign through an OOMOL-connected account. It supports inspecting live action schemas, creating documents from files or templates, retrieving documents and audit logs, listing businesses/documents/templates, reassigning signers, and sending reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running unverified internet installer scripts directly in Bash or PowerShell.

Mitigation: Prefer an official signed package or a pinned download with checksum or signature verification before installing the oo CLI.

Risk: Write actions can create documents, reassign signers, or send reminders in Xodo Sign.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running a write action.

## Reference(s):

- [Xodo Sign homepage](https://eversign.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Xodo Sign actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
