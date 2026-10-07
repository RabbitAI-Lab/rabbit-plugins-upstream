## Description:

Guides agents in managing Box files, folders, sharing, and collaborations through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find, upload, download, organize, and share Box content through a connection they authorize. They can also configure approved automations that act on that connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a Box connection can grant access beyond the intended task.

Mitigation: Confirm the Box account and requested OAuth scopes with the user before connecting; choose only scopes needed for the task.

Risk: Uploads, public links, and collaborator changes may expose or alter sensitive content.

Mitigation: Ask for approval of the exact target and data before each write or sharing action; default to read-only operations.

Risk: Functions, triggers, webhooks, and destinations can make Box actions persistent or automatic.

Mitigation: Obtain explicit approval of the intended behavior and persistence before creating or changing automation.

## Reference(s):

- [Box skill on ClawHub](https://clawhub.ai/byungkyu/skills/box)
- [Maton](https://maton.ai)
- [Maton API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Box actions require a user-authorized connection; obtain approval before writes and automations.]

## Skill Version(s):

1.2.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
