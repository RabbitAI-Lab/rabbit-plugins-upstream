## Description:

Google Tag Manager API integration with managed OAuth for managing GTM accounts, containers, workspaces, tags, triggers, variables, environments, container versions, and user permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Google Tag Manager resources through Maton-managed OAuth, including account/container administration, workspace changes, publishing, environments, and user permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Tag Manager write operations can change account, container, workspace, environment, user-permission, or published-version state.

Mitigation: Default to read/list calls first, then get explicit user confirmation for the target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, publish, permission, or account-change operation.

Risk: Hosted functions and triggers can create persistent automation that acts through the user's approved connection.

Mitigation: Use only user-authored or user-reviewed handlers, scope triggers narrowly, prefer private destinations, and require separate approval before creating, updating, deploying, invoking, or attaching automation.

Risk: Maton API keys, OAuth credentials, and raw API responses can expose account access or sensitive business data.

Mitigation: Prefer OAuth-backed Maton CLI profiles, avoid exporting long-lived API keys, use the operating system credential store, and avoid logging or broadly copying raw response bodies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-tag-manager-api)
- [Maton Homepage](https://maton.ai)
- [Tag Manager API Overview](https://developers.google.com/tag-platform/tag-manager/api/v2)
- [Tag Manager API Reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest)
- [Tag Manager Concepts](https://developers.google.com/tag-platform/tag-manager/api/v2/devguide)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, HTTP/API examples, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and authenticated Google Tag Manager connection; default workflow is read/list before confirmed write operations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
