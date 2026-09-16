## Description:

TextCortex (textcortex.com). Use this skill for ANY TextCortex request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TextCortex through an OOMOL-connected account, including chat completions and model discovery. The skill guides agents to inspect live action schemas before running TextCortex connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer an official, version-pinned installer or package manager path with checksum or signature verification, and inspect the exact payload before running setup commands.

Risk: The create_chat_completion action is tagged as write-capable and can create TextCortex chat completions through the connected account.

Mitigation: Confirm the exact payload and intended effect with the user before running write-tagged connector actions.

## Reference(s):

- [ClawHub TextCortex Skill Page](https://clawhub.ai/oomol/skills/oo-textcortex)
- [TextCortex Homepage](https://textcortex.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
