## Description:

X (Twitter) connector that lets an agent read, search, create, update, and delete X account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, search, post, message, manage lists, and upload media through an OOMOL-connected X account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask the agent to run remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation method and script contents before allowing installation.

Risk: The skill can post, delete, send DMs, follow, mute, manage lists, and upload media through the connected X account.

Mitigation: Require the agent to show the exact payload and expected effect, then obtain explicit approval before write or destructive actions.

Risk: Using the connector routes account activity through OOMOL as an intermediary.

Mitigation: Install only when that intermediary relationship is acceptable for the account and task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [X homepage](https://x.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read results from X actions and proposed payloads for write or destructive actions.]

## Skill Version(s):

1.0.5 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
