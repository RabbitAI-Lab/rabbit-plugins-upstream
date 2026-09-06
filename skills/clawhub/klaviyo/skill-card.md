## Description:

Klaviyo provides managed OAuth access through Maton for reading and managing Klaviyo marketing, customer, campaign, flow, event, metric, template, catalog, webhook, and account resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to let an agent work with Klaviyo customer data and marketing workflows through a Maton-managed connection. Typical tasks include listing and updating profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, webhooks, tags, coupons, images, forms, reviews, and account settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access customer data and marketing resources in the connected Klaviyo account.

Mitigation: Install only when that access is intended, prefer OAuth, choose the narrowest available Klaviyo scopes, and use read-only access where possible.

Risk: Write operations can send campaigns, create webhooks, change subscriptions, import data in bulk, delete resources, or otherwise affect customers and account state.

Mitigation: Require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Raw API responses may contain personal data such as names, email addresses, phone numbers, message content, or event details.

Mitigation: Retrieve only fields needed for the task, avoid dumping full responses, and do not write raw responses to logs or files unless the user specifically requests it.

Risk: Using a Maton API key instead of OAuth exposes a long-lived credential to the process environment.

Mitigation: Prefer OAuth; when an API key is unavoidable, never print, log, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: Multiple Maton profiles or Klaviyo connections can cause actions to target the wrong account.

Mitigation: List active connections first and specify the intended connection or profile before performing state-changing work.

## Reference(s):

- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [Klaviyo Developer Portal](https://developers.klaviyo.com/en)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Klaviyo API paths, Maton CLI commands, request payloads, response-field guidance, and confirmation prompts for write operations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
