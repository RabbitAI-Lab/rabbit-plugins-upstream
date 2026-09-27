## Description:

Accesses Zoom through Maton's managed OAuth integration to manage meetings, webinars, recordings, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an authorized Zoom account and perform scoped Zoom API tasks such as scheduling meetings, managing webinars, listing recordings, retrieving user information, and building approved Maton automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Zoom account data and create, update, or delete meetings, webinars, recordings, registrants, functions, triggers, and destinations after authorization.

Mitigation: Use OAuth where possible, keep scopes narrow, default to read and list calls, and confirm every write, destructive action, new connection, or automation with the user.

Risk: Trigger destinations can create persistent forwarding of event data, including personal, financial, source-code, or workspace content from connected services.

Mitigation: Forward only the minimum required fields, prefer Maton-controlled destinations, avoid credentials in destination payloads or headers, and require explicit approval for any third-party host.

Risk: Raw API keys and raw response bodies can expose long-lived credentials or sensitive Zoom data.

Mitigation: Prefer the Maton CLI credential store and OAuth flow, avoid printing or logging secrets, and extract only the response fields needed for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-api)
- [Maton](https://maton.ai)
- [Zoom API Documentation](https://developers.zoom.us/docs/api/)
- [Zoom REST API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom OAuth Scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-authorized Zoom access.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
