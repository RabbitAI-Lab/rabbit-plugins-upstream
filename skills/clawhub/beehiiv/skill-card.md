## Description:

beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to connect an agent to beehiiv through Maton, list or manage newsletter resources, and create approved automations around subscriber, post, segment, and publication workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a beehiiv connection that reaches newsletter account data through the user's authorization.

Mitigation: Install it only for intended beehiiv work, choose the narrowest available authorization scopes, and confirm every new connection before it is created.

Risk: Write operations, hosted functions, triggers, or external destinations can change newsletter data or keep moving subscriber and event data automatically.

Mitigation: Review each requested write, function, trigger, and destination before approval, especially flows that run unattended or send data to another service.

Risk: Raw HTTP fallback and long-lived Maton API keys can expose credentials if handled casually.

Mitigation: Prefer OAuth through the Maton CLI and credential store; use raw HTTP only where the CLI cannot be installed and avoid exporting or logging MATON_API_KEY.

## Reference(s):

- [ClawHub beehiiv Skill](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton Homepage](https://maton.ai)
- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, JSON examples, and API endpoint descriptions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for authenticated beehiiv operations through Maton; responses may include newsletter and subscriber data depending on the user's authorized connection.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
