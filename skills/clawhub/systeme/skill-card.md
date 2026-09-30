## Description:

Helps agents manage Systeme.io contacts, tags, course and community access, and subscriptions through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and developers use this skill to manage Systeme.io customer records, course and community access, and subscriptions. They can also plan user-approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account connections and write operations can change customer records, subscriptions, and paid access.

Mitigation: Use the intended account and least-privilege connection; verify targets and get explicit user approval before connecting or writing.

Risk: Tag changes can trigger messaging, while deleting a tag or custom field can affect many contacts.

Mitigation: Explain downstream effects, confirm the exact resource and scope with the user, and prefer reads before changes.

Risk: Triggers and destinations can continuously forward event data or run unattended actions.

Mitigation: Require separate approval for automations and destinations; review event fields, destination ownership, and persistence before activation.

Risk: Credentials and API responses may expose account access or customer information.

Mitigation: Use secure credential storage, never print or embed secrets, and include only task-relevant customer data in outputs.

## Reference(s):

- [Systeme.io API reference](https://developer.systeme.io/reference)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Systeme.io skill listing](https://clawhub.ai/byungkyu/skills/systeme)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize API responses; avoid exposing unnecessary customer data.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
