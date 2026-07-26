## Description: <br>
Klaviyo API integration with managed OAuth for accessing profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and marketing teams use this skill to query and manage Klaviyo customer profiles, campaigns, flows, events, metrics, catalogs, webhooks, and related marketing resources through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive marketing and customer data in the connected Klaviyo account. <br>
Mitigation: Install only if you trust Maton with the Klaviyo account, keep MATON_API_KEY secret, and use an account with the minimum practical Klaviyo permissions. <br>
Risk: Write, send, webhook, bulk subscription, suppression, or import operations can change customer data or marketing behavior. <br>
Mitigation: Confirm the exact resource, ID, account, and intended effect with the user before executing any sensitive or mutating operation. <br>
Risk: Requests may target the wrong Klaviyo account when multiple OAuth connections exist. <br>
Mitigation: Use the Maton-Connection header to select the intended connection whenever more than one Klaviyo account is available. <br>


## Reference(s): <br>
- [ClawHub Klaviyo Skill](https://clawhub.ai/byungkyu/skills/klaviyo) <br>
- [Klaviyo API Documentation](https://developers.klaviyo.com) <br>
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview) <br>
- [Klaviyo Developer Portal](https://developers.klaviyo.com/en) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with API endpoint descriptions and Python/bash code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Klaviyo account.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
