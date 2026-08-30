## Description:

Schedule and manage social media posts, uploads, analytics, account connection, and social inbox moderation across major platforms using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, agencies, and developers use this skill to operate PostFast from an agent workflow: schedule posts, upload media, manage drafts, inspect analytics, connect social accounts, and triage or moderate social inbox conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live posting and moderation actions, including irreversible comment deletion, without requiring explicit confirmation.

Mitigation: Configure the agent or operator workflow to ask for explicit approval before deleting comments, deleting scheduled posts, sending replies, private-replying, or posting publicly; prefer drafts, pending approval, hide, or snooze when intent is uncertain.

Risk: Using the skill gives PostFast access to the connected accounts and media managed through the workspace.

Mitigation: Install only when the operator trusts PostFast with those connected accounts and media, and scope API-key access to the intended workspace.

## Reference(s):

- [PostFast](https://postfa.st)
- [ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [PostFast API Reference](references/api-reference.md)
- [Media Specifications by Platform](references/media-specs.md)
- [Platform-Specific Controls Reference](references/platform-controls.md)
- [Media Upload Flow](references/upload-flow.md)
- [PostFast Skill Examples](examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with curl commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTFAST_API_KEY and connected social accounts; actions can publish, schedule, delete, reply to, or moderate social content through the PostFast API.]

## Skill Version(s):

1.17.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
