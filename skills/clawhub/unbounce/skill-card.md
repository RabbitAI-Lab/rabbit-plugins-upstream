## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and operations teams use this skill to work with Unbounce accounts through Maton, including listing account data, managing landing pages, tracking leads, and setting up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Unbounce business data, including leads, through an approved Maton connection.

Mitigation: Use OAuth where possible, choose least-privilege scopes, default to read/list operations, and confirm every write or new connection with the user.

Risk: Approved hosted functions and triggers can create persistent automations.

Mitigation: Require user-reviewed function code, deploy with DENY_ALL network policy unless a specific host is approved, and confirm trigger destinations and data flows before creation.

Risk: API keys and trigger payloads may expose sensitive business or personal data if logged or forwarded.

Mitigation: Prefer OAuth over long-lived API keys, never print or persist secrets, minimize forwarded event fields, and avoid third-party trigger destinations unless the user explicitly approves the endpoint.

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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API call guidance and Maton automation setup steps; write operations and persistent automation require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
