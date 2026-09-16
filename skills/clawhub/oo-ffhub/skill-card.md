## Description:

FFHub (ffhub.io). Use this skill for reading, creating, and updating FFHub task data through the OOMOL-connected FFHub connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect FFHub action schemas and run FFmpeg task actions, including creating tasks and checking task status or task lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes commands that execute remote installer scripts directly in a shell.

Mitigation: Use an installation path that lets the user review and verify the installer before execution.

Risk: The skill can create FFHub FFmpeg tasks that change account state or consume service credits.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [FFHub homepage](https://ffhub.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ffhub)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can be run directly; write actions require user confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
