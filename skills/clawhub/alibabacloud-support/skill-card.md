## Description:

Helps customers draft and manage Alibaba Cloud support tickets, including listing, creating, viewing, replying to, closing and rating tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Alibaba Cloud customers and support teams use this skill to prepare redacted ticket drafts, check ticket status and engineer replies, and manage individual support tickets through the Workorder API with confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine rule refresh can replace the installed skill code from an upstream source.

Mitigation: Review this update behavior before installation and avoid the skill where self-modifying code is not permitted.

Risk: Ticket operations use the configured aliyun CLI identity and can modify support tickets.

Mitigation: Use a least-privilege Alibaba Cloud identity and review each ticket preview before confirming a change.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sdk-team/skills/alibabacloud-support)
- [Alibaba Cloud support](https://www.aliyun.com/service)
- [Workorder API reference](artifact/references/api-reference.md)
- [Error handling contract](artifact/references/error-handling.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with redacted ticket drafts, previews, status summaries and ticket links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket changes require a preview and explicit confirmation; no automatic retry of uncertain writes.]

## Skill Version(s):

0.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
