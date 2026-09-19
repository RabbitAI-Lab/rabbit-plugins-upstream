## Description:

MiniMax (minimax.io). Use this skill for ANY MiniMax request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to operate MiniMax through an OOMOL-connected account with schema-first command guidance for reads, writes, media generation, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts executed directly in a shell.

Mitigation: Review the oo CLI installation method before installing and prefer an official package manager, pinned release, or verified installer.

Risk: Write and destructive MiniMax actions can create or delete remote resources.

Mitigation: Confirm exact payloads for write actions and deletion targets before allowing the skill to run them.

## Reference(s):

- [MiniMax homepage](https://www.minimax.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-minimax)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands invoke the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
