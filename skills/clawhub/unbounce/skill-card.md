## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an Unbounce account through Maton, inspect accounts, pages, leads, domains, users, and related resources, and run approved changes or automations against the connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Homebrew installation path is not tied to the reviewed CLI release, while the CLI may later handle OAuth, API keys, hosted functions, persistent triggers, and Unbounce business data.

Mitigation: Prefer the pinned npm CLI path, or verify the exact Homebrew formula and artifact before using the skill with credentials or business data.

Risk: Writes, function deployments, trigger destinations, and local event handlers can modify data or create persistent data flows.

Mitigation: Require explicit approval after confirming the target, payload, data flow, destination, and duration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/unbounce)
- [Maton Homepage](https://maton.ai)
- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
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

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe API calls that return account, landing page, lead, domain, page group, and user data from the connected Unbounce account.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
