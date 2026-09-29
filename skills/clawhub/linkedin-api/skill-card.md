## Description:

Helps agents use LinkedIn through a connected Maton account to retrieve profile and organization information, share content, and manage advertising workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can guide an agent to read LinkedIn account information, prepare and share posts, or manage campaigns through their approved connection. The skill also describes optional scheduled or event-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an unintended LinkedIn account could grant Maton access to its data and actions.

Mitigation: Confirm the intended account and obtain explicit approval before creating a connection.

Risk: Posts, account changes, and advertising budget changes can have public or financial consequences.

Mitigation: Default to reading; review each write and budget change with the user before proceeding.

Risk: Hosted functions, triggers, or third-party destinations may run actions or send data unexpectedly.

Mitigation: Review and approve each automation and destination; use external recipients only when the user controls and trusts the host.

Risk: Local execution workflows can run commands on the user's machine.

Mitigation: Review and explicitly approve local --exec workflows before running them.

## Reference(s):

- [ClawHub LinkedIn skill](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [LinkedIn API documentation](https://learn.microsoft.com/en-us/linkedin/)
- [LinkedIn Marketing API documentation](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection; advertising actions may require additional LinkedIn permissions.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
