## Description:

Enables agents to read, organize, draft, send, and manage Gmail messages, threads, labels, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent with Gmail can search and read mail, manage threads and labels, prepare and send replies, and handle attachments or bulk mailbox actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some destructive Gmail delete actions may run without separate confirmation of the specific target.

Mitigation: Review the exact message or draft targets before permitting delete tools, especially on important accounts.

Risk: Write tools can change mailbox contents or send messages when only read access is needed.

Mitigation: Set GOG_READONLY=1 for read-only use and keep GOG_FILE_ROOTS narrow.

Risk: Signed attachment URLs allow access without a Google login, while Drive delivery creates files.

Mitigation: Treat attachment URLs as temporary bearer secrets and choose Drive delivery only when file creation is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Links]

**Output Format:** [Structured Gmail tool responses, attachment files, or download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Signed attachment links expire after one hour.]

## Skill Version(s):

4.6.3 (source: ClawHub release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
