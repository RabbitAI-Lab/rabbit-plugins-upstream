## Description:

Helps agents work with Klaviyo marketing and customer data through a Maton-managed connection, including profiles, campaigns, flows, and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to inspect and manage Klaviyo customer profiles, lists, campaigns, flows, and other email-marketing resources through an authorized connection. Optional hosted functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive Klaviyo business and customer data could exceed the task's needs.

Mitigation: Use OAuth with only the required account and least-privilege scopes; revoke unused connections.

Risk: Writes and automation can change marketing data or trigger customer communications.

Mitigation: Default to read-only operations and confirm each write, connection, or automation with the user before execution.

Risk: Webhook or trigger destinations can continue forwarding data after setup.

Mitigation: Confirm each destination and its data flow separately, and remove destinations when no longer needed.

## Reference(s):

- [Klaviyo API documentation](https://developers.klaviyo.com/en/reference/api_overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [ClawHub Klaviyo release](https://clawhub.ai/byungkyu/skills/klaviyo)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Klaviyo connection.]

## Skill Version(s):

1.2.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
