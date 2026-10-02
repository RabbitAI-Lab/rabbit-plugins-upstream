## Description:

Helps agents manage OneDrive files, folders, and sharing through Microsoft Graph using a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find, upload, download, organize, and share files in an authorized OneDrive account. They can also configure user-approved scheduled or event-driven OneDrive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected OneDrive account grants access to files and folders within its authorized scope.

Mitigation: Connect only the needed account, select the least privilege available, and review the access before approving it.

Risk: Writes, deletion, and public sharing links can change or expose files.

Mitigation: Confirm the target and effect of every write or sharing action, especially open links.

Risk: Hosted functions and triggers can continuously forward events from connected services to a destination.

Mitigation: Review each function, trigger, event source, and destination separately before approval; avoid forwarding sensitive events to untrusted hosts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/one-drive)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [OneDrive sharing and permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands, API examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an authorized connection; writes, sharing, and automations require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
