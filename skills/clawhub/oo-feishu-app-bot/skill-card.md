## Description:

Feishu App Bot enables an agent to read, create, update, and delete Feishu App Bot data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Feishu App Bot resources, including messages, chats, Drive, Wiki, documents, spreadsheets, Slides, calendars, tasks, OKRs, and Base apps. It is suited to connected-account workflows that need schema-checked oo CLI calls and careful review of write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected Feishu App Bot account with broad read, write, and delete capabilities.

Mitigation: Review the intended action, target resource, and payload before approval, especially for actions marked write or destructive.

Risk: The setup instructions include remote CLI installer commands that pipe downloaded scripts to a shell.

Mitigation: Prefer verifying or manually installing the oo CLI before running installer commands.

Risk: Incorrect connector payloads can modify or remove real Feishu workspace data.

Mitigation: Inspect the live action schema with the oo CLI before constructing payloads and use the least-privilege connected account practical for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feishu App Bot Homepage](https://open.feishu.cn)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before sending payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.7 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
