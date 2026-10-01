## Description:

Helps agents access and manage Google Merchant Center products, inventory, promotions, data sources, and reports through an authenticated Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and developers use this skill to inspect Google Merchant Center data and, with explicit approval, manage product listings, inventory, promotions, data sources, and account settings or set up recurring tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes can change or delete Merchant Center products, inventory, promotions, data sources, or account settings.

Mitigation: Default to reading data and confirm each write with the user and exact resource identifiers before execution.

Risk: Functions, triggers, destinations, and notification subscriptions can continue processing or sending data until removed.

Mitigation: Obtain separate approval for ongoing automation, limit access and destinations to what is needed, and remove it when no longer required.

Risk: Account authorization and webhook destinations may grant broad access or expose business data.

Mitigation: Use the narrowest available scopes and confirm any destination and the data it will receive before connecting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Merchant API reference](https://developers.google.com/merchant/api/reference/rest)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an authenticated connection; writes and new automation require explicit user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
