## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to inspect and manage ClickFunnels 2.0 account data and marketing automation workflows through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete ClickFunnels business data through Maton for the connected account.

Mitigation: Prefer read and list operations first, and review the target resource, payload, and intended effect before approving any write or delete action.

Risk: Raw API passthrough can reach broad ClickFunnels API endpoints, including webhook changes with downstream side effects.

Mitigation: Use OAuth, connect only the needed ClickFunnels account, specify the connection when multiple accounts exist, and review webhook changes carefully.

Risk: Credentials or provider-issued tokens could be exposed if handled outside the Maton credential flow.

Mitigation: Use Maton OAuth where possible, avoid printing or persisting credentials, and send API keys only to api.maton.ai when a CLI fallback is required.

## Reference(s):

- [ClickFunnels Skill on ClawHub](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [Maton Homepage](https://maton.ai)
- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro)
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination)
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering)
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected ClickFunnels account.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
