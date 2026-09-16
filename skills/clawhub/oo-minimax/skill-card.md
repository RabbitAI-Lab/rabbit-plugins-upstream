## Description:

Use this skill for MiniMax requests, including reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MiniMax through an OOMOL-connected account, including model discovery, response creation, token estimation, video workflows, and text-to-audio synthesis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer scripts that can be piped directly into a shell.

Mitigation: Do not run the installer automatically; use a trusted package manager or download and verify the installer contents and integrity before execution.

Risk: The skill can create, modify, or delete MiniMax resources through connector actions.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub MiniMax Skill Release](https://clawhub.ai/oomol/skills/oo-minimax)
- [MiniMax Homepage](https://www.minimax.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before running MiniMax actions and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
