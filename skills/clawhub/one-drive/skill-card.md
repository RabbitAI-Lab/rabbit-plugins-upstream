## Description:

Helps agents manage OneDrive files, folders, and sharing through a user-authorized Maton connection to Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find, upload, download, organize, and share files in an authorized OneDrive account. It also provides guidance for explicitly approved automation of those tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account may expose sensitive OneDrive files and personal information.

Mitigation: Use OAuth with the narrowest available scopes, connect only the account needed, and limit returned data to the task.

Risk: Writes, deletions, or public sharing links can change access or expose files beyond the current task.

Mitigation: Confirm each write, share, or delete action with the user; check the target account and sharing settings before proceeding.

Risk: Hosted functions, triggers, and forwarding destinations can continue acting on or sending data after a task ends.

Mitigation: Obtain explicit approval for automation and destinations, avoid embedding credentials, and review or remove unused automation.

## Reference(s):

- [ClawHub Microsoft OneDrive skill release](https://clawhub.ai/byungkyu/skills/one-drive)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [OneDrive developer documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Trigger source catalogs](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [OneDrive operations require a user-authorized connection and network access.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release; source metadata lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
