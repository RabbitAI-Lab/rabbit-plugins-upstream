## Description:

Read and organise the mailbox owner's mail through the mail CLI, including syncing, searching, reading, managing messages and rules, and drafting or sending messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Mailbox owners use the skill to search and organise mail, manage messages and rules, and draft or send requested messages through a configured account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox contents and exported messages or attachments may expose private information to people who can access the shared mail store or output folders.

Mitigation: Limit access to the shared store and exported files to intended users, and choose a private output folder for exports.

Risk: Sending mail or applying bulk changes can affect recipients or many messages.

Mitigation: Use the intended mailbox profile, review dry-run or preview details, and proceed only with the owner's explicit request and approval.

## Reference(s):

- [Mail Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-mail)
- [Publisher profile: wirecat](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files]

**Output Format:** [JSON command results, with exported messages or attachments as files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sync and search results can be partial; the skill provides continuation guidance.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
