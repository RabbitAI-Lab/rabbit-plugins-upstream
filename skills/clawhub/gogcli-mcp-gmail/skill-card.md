## Description:

Helps agents read, organize, draft, and send Gmail messages through tools for threads, labels, attachments, bulk actions, and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams using an agent to manage Gmail can search mail, work with threads and attachments, prepare replies or forwards, organize messages, and manage mailbox settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Gmail read/write and settings access can expose or change sensitive mail and account settings.

Mitigation: Grant access only to an appropriate account; use a dedicated account or enable GOG_READONLY when only reads are needed.

Risk: Some destructive Gmail and settings deletions can be forced without a separate user-confirmation flow.

Mitigation: Review and explicitly approve destructive actions, especially deletion of labels, filters, drafts, and send-as aliases.

Risk: Stored Gmail credentials could be exposed on an insufficiently isolated host.

Mitigation: Use a secure keyring backend and strong host isolation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli dependency documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration guidance]

**Output Format:** [Structured Gmail data and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include message contents, attachment links, and local file paths.]

## Skill Version(s):

4.7.0 (source: server release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
