## Description:

Feishu App Bot helps agents read, create, update, and delete Feishu/Lark resources through an OOMOL-connected Feishu App Bot account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to operate Feishu/Lark chats, messages, Drive, Wiki, Base, Sheets, Slides, tasks, calendars, mail, and meetings through a connected Feishu App Bot account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Feishu App Bot may have broad read and write scopes across Feishu resources.

Mitigation: Install only when the granted OOMOL connection scopes are acceptable and review the target, action, and payload before execution.

Risk: Some state-changing actions may not be tagged as write or destructive in the skill text.

Mitigation: Require explicit review for any action that could alter, recall, overwrite, revert, move, sort, or delete Feishu content, even if it appears untagged.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot)
- [Feishu App Bot homepage](https://open.feishu.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses when executed.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
