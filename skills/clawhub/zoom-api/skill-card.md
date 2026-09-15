## Description:

Zoom API integration with managed OAuth for managing meetings, webinars, recordings, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Zoom through Maton-managed OAuth: schedule and manage meetings, manage webinars, retrieve recordings, and inspect user profiles. It can also guide approved hosted functions or scheduled/event-driven automations that call Zoom actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the Maton CLI or SDKs introduces supply-chain exposure.

Mitigation: Verify Maton and the package source before installation, and keep the reviewed CLI or SDK version pinned until deliberately upgraded.

Risk: Zoom OAuth access can expose meetings, webinars, recordings, and user profile data from the connected account.

Mitigation: Prefer OAuth over long-lived API keys, grant only task-required scopes, specify the intended connection when multiple accounts exist, and revoke unused connections.

Risk: Write operations can create, change, cancel, or delete Zoom resources and may notify external participants.

Mitigation: Default to read/list calls, then require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE operations.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding event data after setup.

Mitigation: Review every function, trigger, and destination before creation; keep destinations on approved platform URLs where possible; minimize forwarded fields; and remove automations that are no longer needed.

Risk: Using raw HTTP with MATON_API_KEY can leak a long-lived credential through logs, shell history, child processes, or files.

Mitigation: Use raw HTTP only when the CLI cannot be installed, read the key from the process environment, never print or persist it, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Zoom Skill](https://clawhub.ai/byungkyu/skills/zoom-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed API calls and automation steps that require user approval before execution.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
