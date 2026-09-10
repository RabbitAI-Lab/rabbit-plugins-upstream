## Description:

Klaviyo API integration with managed OAuth for accessing and managing customer profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, webhooks, tags, coupons, images, forms, reviews, and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to work with Klaviyo accounts through Maton-managed authentication for customer data, campaigns, flows, events, metrics, catalogs, webhooks, and related marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform writes, sends, deletes, webhook changes, and bulk subscription changes through the connected Klaviyo account.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user confirmation before any modifying operation.

Risk: Maton API keys and provider-issued tokens can be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, never display credential values, and use environment-based API keys only when the CLI cannot be installed.

Risk: The Maton API passthrough can reach endpoints beyond the documented examples when the connection permits them.

Mitigation: Use the least Klaviyo scopes needed, specify the intended connection when multiple accounts exist, and apply the same confirmation rules to every endpoint.

Risk: Klaviyo API responses can include personal data and untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and avoid dumping raw responses unless the user explicitly needs them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)
- [Maton Homepage](https://maton.ai)
- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [Klaviyo Developer Portal](https://developers.klaviyo.com/en)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash, HTTP, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain customer or marketing data; extract only fields needed for the user task.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
