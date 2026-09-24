## Description:

Instantly API integration with managed OAuth for agents to manage cold email campaigns, leads, sending accounts, email sending, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect to Instantly through Maton OAuth, inspect campaign and lead data, and perform approved campaign, lead, account, email, analytics, function, or trigger workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the Instantly connection gives Maton access to the connected Instantly account within the provider-enforced scope.

Mitigation: Approve each connection separately, use least-privilege scopes when offered, and specify the target connection when more than one account is connected.

Risk: Write operations can change outreach campaigns, leads, accounts, analytics-related records, or send email.

Mitigation: Default to read and list calls first, then confirm the target resource, payload, and intended effect before POST, PUT, PATCH, DELETE, or send actions.

Risk: The raw API-key path exposes a long-lived Maton credential to the local environment.

Mitigation: Prefer OAuth through the Maton CLI; use raw HTTPS only when the CLI cannot be installed, and never print, persist, log, or pass the key on a command line.

Risk: Hosted functions, triggers, and destinations can create ongoing automation or persistent event forwarding.

Mitigation: Require user-authored or user-reviewed handlers, separate approval for each create/update/invocation, and restrictive network policy unless the user approves specific hosts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton homepage](https://maton.ai)
- [Instantly API V2 documentation](https://developer.instantly.ai/api-reference)
- [Instantly API introduction](https://developer.instantly.ai/)
- [Instantly Help Center](https://help.instantly.ai/)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with bash, JSON, Python, and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use Maton CLI or raw HTTPS; write, connection, function, trigger, and destination actions require explicit approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
