## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, webhooks, and related funnel operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to let an agent inspect and manage ClickFunnels 2.0 resources such as sales funnels, contacts, orders, products, courses, forms, and webhooks through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClickFunnels API actions can modify real contacts, orders, products, courses, forms, webhooks, and fulfillment data.

Mitigation: Default to read and list operations, verify resource identifiers first, and require explicit user confirmation before any POST, PUT, PATCH, DELETE, webhook, order, contact, or fulfillment change.

Risk: Long-lived API keys and provider-issued tokens can be exposed through logs, command lines, files, or broad process environments.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: The Maton API passthrough can reach endpoints beyond the documented examples when the connection authorizes them.

Mitigation: Grant the narrowest available ClickFunnels scopes, pin the intended connection when multiple accounts exist, and apply the same approval rules to every allowed endpoint.

Risk: API responses may include personal, customer, order, webhook, or business-sensitive data.

Mitigation: Extract only the fields needed for the task and avoid dumping raw responses into logs, files, or user-visible output unless explicitly requested.

Risk: Instructions embedded in fetched ClickFunnels content could attempt to redirect agent behavior.

Mitigation: Treat API response content as untrusted data and do not execute, eval, or use it to select follow-up endpoints or recipients without validation.

## Reference(s):

- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro)
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination)
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering)
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub ClickFunnels Skill](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active ClickFunnels connection; list endpoints may require pagination and responses may contain personal or business data.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
