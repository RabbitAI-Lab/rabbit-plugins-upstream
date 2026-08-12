## Description:

MiniMax (minimax.io). Use this skill for ANY MiniMax request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate MiniMax through an OOMOL-connected account, including model discovery, token estimation, response creation, and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create MiniMax responses or video generation tasks in the connected account.

Mitigation: Confirm the exact payload and expected account effect with the user before running write-tagged actions.

Risk: Destructive actions can delete MiniMax video generation tasks.

Mitigation: Confirm the target task and obtain explicit user approval before running destructive actions.

Risk: The skill depends on a trusted OOMOL account and MiniMax connection.

Mitigation: Use only trusted connections and review payloads carefully before approving write or destructive commands.

## Reference(s):

- [ClawHub MiniMax skill](https://clawhub.ai/oomol/skills/oo-minimax)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [MiniMax homepage](https://www.minimax.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector JSON results and execution identifiers returned by the oo CLI.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
