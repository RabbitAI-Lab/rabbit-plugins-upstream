## Description:

Connects an agent to Gmail for reading, organizing, drafting, sending, and managing messages and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Gmail users and developers use this skill to let an agent search and read mail, manage threads and labels, work with drafts and attachments, and perform authorized mail actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can access and modify the configured Gmail account.

Mitigation: Use GOG_READONLY=1 when write access is unnecessary, avoid shared deployments with mutating access, and protect stored account data and the keyring password.

Risk: Some draft, label, filter, and send-as deletion tools may act without explicit human confirmation.

Mitigation: Require human review before destructive actions and verify the target before deletion.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or structured Gmail results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return message contents, attachment data or links, draft previews, and action results.]

## Skill Version(s):

4.5.1 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
