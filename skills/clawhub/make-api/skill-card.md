## Description:

Make (formerly Integromat) API integration with managed authentication for managing scenarios, organizations, teams, connections, data stores, hooks, and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to manage Make resources and build user-approved workflow automations through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can modify Make data or create persistent resources such as scenarios, hooks, and data stores.

Mitigation: Require explicit user approval before every create, update, start, stop, or delete action, including the target resource, payload, and intended effect.

Risk: Hosted functions run with the deploying Maton account's available connections.

Mitigation: Use user-authored or user-reviewed handlers, provide a least-privilege summary before deployment or invocation, and prefer DENY_ALL network policy unless the user approves specific external hosts.

Risk: Long-lived API keys can be exposed through environment variables or child processes.

Mitigation: Prefer OAuth and the operating system credential store; use raw HTTP or MATON_API_KEY only where the CLI cannot be installed.

Risk: Persistent trigger destinations can continuously forward future event data to a URL.

Mitigation: Confirm the destination URL, data fields, persistence, cadence, and credential handling separately before creating or updating a destination.

## Reference(s):

- [Make API Documentation](https://developers.make.com/api-documentation)
- [Make API Reference](https://developers.make.com/api-documentation/api-reference)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/make-api)
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

**Output Type(s):** [Shell commands, API calls, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Make API paths, Maton CLI commands, and user approval prompts.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
