## Description:

Brave Search provides managed-authentication access for web, image, news, video, local POI, autosuggest, spellcheck, and summarizer searches through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to run privacy-focused Brave Search queries and retrieve search, image, news, video, location, and summary results through a managed Maton connection. It is suited to read/list search workflows and scheduled checks that the user explicitly approves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure through long-lived API keys or inherited environment variables.

Mitigation: Prefer OAuth login, avoid exposing MATON_API_KEY, and keep credentials in the supported credential store whenever possible.

Risk: Over-broad account or connection access during search, functions, or automations.

Mitigation: Keep connections narrowly scoped, prefer read/list calls, and confirm new connections or write-like operations with the user before proceeding.

Risk: Hosted functions, triggers, destinations, or local event handlers can create persistent or unattended data flows.

Mitigation: Review each function, trigger, destination, and local --exec handler before approval; keep destinations on approved Maton endpoints unless the user explicitly names and approves another host.

Risk: Location headers and search responses can reveal personal or sensitive information.

Mitigation: Send only the fields required for the task, avoid logging raw responses, and use precise location headers only when the user explicitly needs location-specific results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Maton Homepage](https://maton.ai)
- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Brave Search result data returned through the user's authorized Maton connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
