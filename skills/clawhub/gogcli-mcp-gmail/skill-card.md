## Description:

Connects an agent to Gmail to read and organize messages, manage drafts and attachments, send replies, and update mailbox settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an agent to work with Gmail can search and read mail, manage threads, labels, drafts and attachments, send replies, and manage account settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Gmail access can expose private messages and change mailbox or account settings.

Mitigation: Grant access only to accounts where this level of control is acceptable; use GOG_READONLY=1 when only reading is needed and avoid shared hosts for OAuth and keyring state.

Risk: Draft deletion and changes to filters, send-as aliases, or vacation settings can be destructive or persistent without a strong confirmation gate.

Mitigation: Manually review the target and effect of each such action before letting the agent proceed.

Risk: Attachments shared through signed links can be accessed without a credential until the link expires.

Mitigation: Avoid generating or sharing attachment links for sensitive mail unless necessary; treat generated links as secrets.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Gmail message text, structured tool responses, and attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attachments may be returned inline, as server-side files, or through time-limited download links.]

## Skill Version(s):

4.6.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
