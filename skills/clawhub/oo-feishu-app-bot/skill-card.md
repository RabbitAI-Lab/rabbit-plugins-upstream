## Description:

Feishu App Bot (open.feishu.cn) helps agents read, create, update, and delete Feishu App Bot data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Feishu App Bot from an agent, including reading, creating, updating, searching, and deleting chats, messages, Drive files, Docs, Sheets, Base data, Calendar events, Tasks, OKRs, Wiki content, Slides, Mail, Whiteboards, and meetings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can ask users to run internet-downloaded installer scripts for the oo CLI.

Mitigation: Review the install steps carefully and prefer a verified official package or a pinned, checksum-verified release.

Risk: Write and destructive actions can change or remove Feishu data.

Mitigation: Confirm exact payloads, targets, and expected effects before allowing write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feishu App Bot homepage](https://open.feishu.cn)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running actions and to require confirmation for write or destructive Feishu operations.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
