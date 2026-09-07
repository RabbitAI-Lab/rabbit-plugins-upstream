## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, webhooks, and related sales-funnel automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect an agent to a ClickFunnels account through Maton, inspect account resources, and perform approved changes to contacts, products, orders, courses, forms, webhooks, and marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the skill gives an agent access to the connected ClickFunnels account through Maton.

Mitigation: Use OAuth where possible, connect only the needed account and scopes, and revoke unused connections promptly.

Risk: POST, PUT, PATCH, and DELETE calls can modify or delete ClickFunnels data, trigger workflows, or affect customer-facing operations.

Mitigation: Default to read and list calls, then require explicit user approval after reviewing the exact resource, payload, and intended effect.

Risk: Multiple Maton profiles or ClickFunnels connections can cause operations to target the wrong account.

Mitigation: Verify the active profile and specify the intended connection before any change.

Risk: API responses may contain personal data or credentials.

Mitigation: Return only the fields needed for the task, avoid logging raw responses, and never print, store, or transmit credentials outside the approved Maton flow.

## Reference(s):

- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro)
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination)
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering)
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized ClickFunnels connection; write operations require explicit user approval.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
