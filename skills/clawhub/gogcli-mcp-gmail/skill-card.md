## Description:

Connects an agent to Gmail through gogcli to read and organize messages, manage drafts and attachments, and send or forward mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an AI agent to manage a Gmail account can search conversations, handle labels and attachments, prepare drafts, and perform bulk or outbound email actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Gmail access can expose private mail or allow unintended changes.

Mitigation: Use only with an account where broad Gmail access is acceptable; enable GOG_READONLY for read-only work.

Risk: Some label, filter, send-as, and draft deletion tools lack the user confirmation used elsewhere.

Mitigation: Do not allow these actions until the user has independently confirmed the exact target; review before installing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Text and structured Gmail tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return message content, attachment links or files, and results of mailbox actions.]

## Skill Version(s):

4.7.1 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
