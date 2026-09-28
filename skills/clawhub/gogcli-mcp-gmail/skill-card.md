## Description:

Provides Gmail tools for reading and organizing messages, managing drafts and attachments, sending mail, and changing account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using an agent to work with Gmail can read and organize conversations, prepare and send drafts, handle attachments, and manage labels or settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some permanent deletions and account-settings changes can run without a separate user-confirmation step.

Mitigation: Review the exact action and affected messages or settings before invoking destructive tools; restrict access where possible.

Risk: Broad Gmail read/write/settings access and stored Google authentication data expose sensitive mail and credentials.

Mitigation: Use GOG_READONLY=1 for read-only or shared deployments and protect the authentication and data directories.

Risk: Anyone holding a signed attachment link may access the attachment until the link expires.

Mitigation: Treat signed links as sensitive and share them only with intended recipients.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli project](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Gmail tool responses with message content, metadata, and attachment files or links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attachment delivery may return inline content, a file path, or a signed link.]

## Skill Version(s):

4.5.2 (source: ClawHub release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
