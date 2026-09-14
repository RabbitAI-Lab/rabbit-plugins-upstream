## Description:

Zoom Admin API integration with managed OAuth for managing users, meetings, webinars, recordings, and account settings with admin-level access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and operations teams use this skill to administer Zoom workspaces through Maton-managed OAuth, including account users, meetings, webinars, recordings, and settings. It is intended for tasks where the user has explicitly authorized the target Zoom account and approved write operations or automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative Zoom access can affect users, meetings, webinars, recordings, transcripts, and account settings across the authorized Zoom workspace.

Mitigation: Install only when administrative Zoom access is intended, use least-privilege OAuth scopes where available, default to read and list operations, and confirm every write with the exact account, resource, payload, and expected effect.

Risk: Broad recording exports or full API responses can expose confidential or personal meeting data.

Mitigation: Avoid broad recording exports, extract only the fields needed for the task, and do not log, persist, or display raw responses unless the user explicitly asked for them.

Risk: Maton API keys and OAuth credentials grant access through the Maton gateway if mishandled.

Mitigation: Prefer OAuth, store credentials only through the Maton CLI or platform-supported credential stores, never print or persist API keys, and rotate any key that was exposed.

Risk: Hosted functions, triggers, and destinations can create persistent automation or event forwarding.

Mitigation: Require explicit approval for every automation setup, review destination hosts and transmitted fields, prefer Maton-controlled destinations, avoid third-party forwarding unless the user approves the exact host, and use denied outbound network policies for functions unless a task requires named hosts.

Risk: CLI or SDK package installation introduces supply-chain dependency on Maton distribution channels.

Mitigation: Use pinned versions reviewed with the release, check release notes before upgrades, and verify Maton CLI or SDK provenance before installing packages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoom API Overview](https://developers.zoom.us/docs/api/)
- [Zoom Meeting API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom User API Reference](https://developers.zoom.us/docs/api/rest/reference/user/methods/)
- [Zoom Account API Reference](https://developers.zoom.us/docs/api/rest/reference/account/methods/)
- [Zoom Rate Limits](https://developers.zoom.us/docs/api/rate-limits/)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, code snippets, JSON examples, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zoom API paths, Maton CLI commands, SDK snippets, OAuth connection steps, trigger setup guidance, and risk-aware confirmation prompts.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
