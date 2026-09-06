## Description:

Qwen (qwen.ai). Use this skill for ANY Qwen request - reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Qwen services through the OOMOL oo CLI, including document analysis, image generation and translation, speech generation and recognition, and custom voice management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that can execute downloaded scripts on the user's machine.

Mitigation: Install the oo CLI manually from trusted OOMOL documentation, review installer contents before execution, and avoid letting an agent run pipe-to-shell commands blindly.

Risk: The skill can invoke write and destructive Qwen connector actions, including custom voice creation and deletion.

Mitigation: Review the live action schema and exact payload, then require explicit user approval before running write or destructive actions.

Risk: Using the skill routes Qwen account access through OOMOL as the broker.

Mitigation: Install only when the user accepts OOMOL as the broker for their Qwen account and has connected the intended account and scopes.

## Reference(s):

- [Qwen homepage](https://qwen.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qwen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON data and execution metadata from the oo connector.]

## Skill Version(s):

1.0.0 (source: server evidence release version and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
