## Description:

Helps QianWen users diagnose issues and manage support tickets, including creating, viewing, replying to, closing, and rating them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

QianWen users and support teams use this skill to troubleshoot model-service issues and manage support tickets from a conversation, including follow-ups and escalation to human support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored or ambient QianWen credentials may grant access to ticket data, including in shared-account environments.

Mitigation: Review the active account and its ticket access before use; avoid installing where indirect triggers or shared sessions could expose tickets.

Risk: The skill can create, reply to, close, or rate tickets without an executable confirmation safeguard.

Mitigation: Require the agent to show the final draft, ticket ID, and intended action and obtain explicit user approval before each write.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sdk-team/skills/alibabacloud-qianwenai-support)
- [QianWen support portal](https://platform.qianwenai.com/home/support)
- [QianWen support API reference](artifact/references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and Markdown with ticket drafts, statuses, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report ticket details and support replies; ticket-changing actions should follow explicit user confirmation.]

## Skill Version(s):

0.0.2 (source: ClawHub release metadata and bundled manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
