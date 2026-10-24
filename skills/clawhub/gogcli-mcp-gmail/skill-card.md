## Description:

Connects an agent to Gmail for reading, organizing, drafting, sending, and managing messages, attachments, labels, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and agents with authorized Gmail accounts use this connector to search and read mail, organize threads and labels, manage drafts and attachments, and perform approved sending or settings changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad mailbox access can expose private messages or make unintended changes.

Mitigation: Grant access only to intended accounts and use read-only mode when searching or reading is sufficient.

Risk: Sending, autoreplies, permanent deletion, and forwarding filters can have irreversible or external effects.

Mitigation: Review message previews and confirmation prompts before authorizing these actions.

Risk: Attachment file access and persistent Google authentication state increase local data exposure.

Mitigation: Keep allowed file roots narrow and protect stored authentication credentials.

## Reference(s):

- [gogcli prerequisite](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Guidance]

**Output Format:** [Gmail tool responses with message content, metadata, status reports, and optional attachment files or links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some operations modify mailbox contents or settings, send messages, or download attachments.]

## Skill Version(s):

4.8.1 (source: server release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
