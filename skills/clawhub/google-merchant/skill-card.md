## Description:

Helps agents manage Google Merchant Center products, inventories, data sources, promotions, and account settings through Maton with user-approved writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and their agents use this skill to inspect and manage Google Shopping catalog and account data through an authorized Merchant Center connection. It also guides user-approved automations for connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes or deletions could affect the wrong Merchant Center resources.

Mitigation: Start with read operations and obtain explicit approval for each write using exact account and resource identifiers.

Risk: Hosted functions and triggers can keep acting on connected data after the initial request.

Mitigation: Review the function, trigger, scope, and duration with the user before enabling automation.

Risk: Webhook destinations and notification subscriptions may continuously disclose event data.

Mitigation: Confirm destination URLs and data flow; avoid third-party webhook hosts unless the user controls and trusts them.

## Reference(s):

- [Google Merchant Center skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton](https://maton.ai)
- [Google Merchant API reference](https://developers.google.com/merchant/api/reference/rest)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized Maton connection and network access for live operations.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
