## Description:

Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed Notion write operations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Notion workspace content, run Notion API calls, and configure approved Notion automations through a managed OAuth connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a Notion connection can expose workspace data available to the connected account.

Mitigation: Install only when the user is comfortable granting Maton access to the intended Notion workspace, prefer least-privilege scopes, and confirm the connection before use.

Risk: Write, deletion, trigger, hosted function, or destination actions can change data or create ongoing data flows.

Mitigation: Require explicit confirmation of the exact Notion connection, target resource, payload, destination, and intended effect before executing sensitive actions.

Risk: Forwarding Notion or trigger data to third-party URLs can disclose private workspace content.

Mitigation: Avoid third-party forwarding URLs unless the user understands what data will be sent, to which host, and for how long.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Maton homepage](https://maton.ai)
- [Notion API Introduction](https://developers.notion.com/reference/intro)
- [Notion Search](https://developers.notion.com/reference/post-search.md)
- [Notion Query Database](https://developers.notion.com/reference/post-database-query.md)
- [Notion Get Page](https://developers.notion.com/reference/retrieve-a-page.md)
- [Notion Create Page](https://developers.notion.com/reference/post-page.md)
- [Notion Update Page](https://developers.notion.com/reference/patch-page.md)
- [Append Block Children](https://developers.notion.com/reference/patch-block-children.md)
- [Notion Filter Reference](https://developers.notion.com/reference/post-database-query-filter.md)
- [Notion LLM Reference](https://developers.notion.com/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Notion API request guidance, Maton CLI commands, hosted function examples, trigger configuration, and security handling notes.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
