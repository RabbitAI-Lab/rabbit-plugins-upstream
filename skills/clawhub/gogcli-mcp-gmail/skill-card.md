## Description:

Connects an agent to Gmail for reading, organizing, drafting, sending, and managing messages, attachments, and mailbox settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and developers using Gmail-connected agents can search and organize mail, work with drafts and attachments, and manage Gmail settings. Write and administrative actions require careful review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft, label, filter, and send-as deletions may run without a user-bound confirmation step.

Mitigation: Require a person to confirm the specific target before each deletion.

Risk: Broad Gmail access can send mail or change mailbox settings, with long-lived authentication.

Mitigation: Use read-only mode for inspection, safeguard authentication, and review recipients and changes before writes.

Risk: Attachment exports and signed download links can expose sensitive files.

Mitigation: Keep GOG_FILE_ROOTS narrow and avoid signed links for sensitive attachments unless necessary.

Risk: Updating a draft can overwrite text unique to another copy.

Mitigation: Compare and merge draft copies before updating; use the sibling-content check when available.

## Reference(s):

- [gogcli command-line tool](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration guidance]

**Output Format:** [Gmail content and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attachments may be returned inline, as file paths, or as time-limited signed links.]

## Skill Version(s):

4.8.0 (source: server-resolved release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
