## Description:

MiniMax lets agents operate MiniMax through an OOMOL-connected account for reading, creating, updating, deleting, model, token, video, and audio workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run MiniMax connector actions through OOMOL, including response creation, model lookup, token estimation, video generation and management, and text-to-audio synthesis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, change, or delete MiniMax resources through an OOMOL-connected account.

Mitigation: Review write and delete payloads with the user and get explicit approval before running state-changing actions.

Risk: The integration depends on OOMOL account connection and CLI setup for MiniMax access.

Mitigation: Install or reconnect only when the user intends to use OOMOL for MiniMax and trusts the integration.

## Reference(s):

- [MiniMax homepage](https://www.minimax.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub MiniMax skill](https://clawhub.ai/oomol/skills/oo-minimax)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is schema-first; state-changing MiniMax actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
