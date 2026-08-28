## Description:

Eraser (eraser.io). Use this skill for ANY Eraser request - reading, creating, updating, and deleting data. Whenever a task involves Eraser, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Eraser action schemas and manage Eraser files and diagrams through an OOMOL-connected account. It supports reading content, creating and updating files or diagrams, generating diagrams from DSL or prompts, and archiving or deleting selected content after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, archive, and delete Eraser content in a connected account.

Mitigation: Review and approve exact payloads before write, archive, or delete actions; explicitly confirm the target before destructive diagram deletion.

Risk: The skill operates through OOMOL-connected Eraser credentials.

Mitigation: Install only if you trust OOMOL and want the agent to operate your connected Eraser account.

## Reference(s):

- [Eraser homepage](https://www.eraser.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eraser)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Code]

**Output Format:** [Markdown responses with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Eraser DSL, Markdown file content, or action payloads for user confirmation before write or destructive actions.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
