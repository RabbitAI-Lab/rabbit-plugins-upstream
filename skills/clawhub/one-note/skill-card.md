## Description:

OneNote API integration with managed OAuth via Microsoft Graph for accessing and managing notebooks, sections, section groups, and pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to connect a Microsoft OneNote account through Maton and manage notebooks, sections, section groups, and page content. It is also used to build approved OneNote automations with hosted functions and event or schedule triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneNote connections can expose notebook and page content through authorized Microsoft Graph scopes.

Mitigation: Use OAuth, review requested OneNote scopes, prefer read and list calls first, and revoke unused connections promptly.

Risk: Write operations can create or modify notebooks, sections, section groups, and pages.

Mitigation: Confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Hosted functions can run approved OneNote actions unattended under the deploying account identity.

Mitigation: Use only user-authored or user-reviewed handlers, approve deploys and invocations separately, and use DENY_ALL network policy unless specific outbound hosts are approved.

Risk: Triggers and destinations can create persistent automatic forwarding of event data.

Mitigation: Create destinations only after explicit approval of the host, payload fields, persistence, and credential handling; minimize forwarded fields and remove destinations when they are no longer needed.

Risk: API keys are long-lived credentials and environment variables can leak to child processes.

Mitigation: Prefer OAuth and credential-store backed CLI profiles; use raw HTTP with MATON_API_KEY only when the CLI cannot be installed and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Microsoft OneNote Skill](https://clawhub.ai/byungkyu/skills/one-note)
- [Maton](https://maton.ai)
- [OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [Page HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code examples, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-scoped guidance and commands for Maton CLI, raw HTTP fallback, Microsoft Graph OneNote endpoints, hosted functions, and trigger setup.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
