## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts through Microsoft Graph API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to help users connect Microsoft Teams through Maton, make approved Microsoft Graph API calls, and optionally configure hosted functions or triggers for Teams-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Microsoft Teams access through Maton and may install or use external Maton tooling.

Mitigation: Prefer OAuth, avoid elevated installs, verify the Maton package source, and install only when the user accepts Maton as the gateway for the Teams account.

Risk: Writes, new connections, hosted functions, and automations can modify Teams data or create ongoing actions.

Mitigation: Default to read/list operations and require explicit user approval for every write, connection, deployment, invocation, trigger, or destination.

Risk: Trigger destinations can create persistent forwarding of sensitive business data.

Mitigation: Use narrow scopes, prefer Maton-controlled destinations, disclose destination host and payload fields, and require separate approval before any ongoing forwarding.

Risk: Long-lived API keys can expose access if printed, logged, exported broadly, or committed.

Mitigation: Prefer OAuth and operating-system credential storage; rotate any Maton API key that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Channel Resource](https://learn.microsoft.com/en-us/graph/api/resources/channel)
- [ChatMessage Resource](https://learn.microsoft.com/en-us/graph/api/resources/chatmessage)
- [Team Resource](https://learn.microsoft.com/en-us/graph/api/resources/team)
- [API Gateway Companion Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Microsoft Graph and Maton CLI/API commands that require user authentication and approval before writes or automation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
