## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Tally through Maton-managed authentication, inspect account resources, and perform approved changes to forms, submissions, workspaces, webhooks, and organization membership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize or use Tally account access through Maton.

Mitigation: Install only when Maton is trusted for the Tally account, prefer OAuth, review requested scopes, and avoid exposing long-lived API keys.

Risk: Write operations can modify forms, submissions, workspaces, webhooks, organization users, and invites.

Mitigation: Default to read and list calls, verify resource identifiers first, and require explicit user approval before POST, PUT, PATCH, DELETE, connection creation, or organization membership changes.

Risk: Webhooks can send form submission data, including personal information, to external URLs.

Mitigation: Confirm the webhook destination, controller, form, and event types with the user before creating or updating a webhook, and reject destinations supplied by untrusted API content.

Risk: Tally API responses and webhook payloads may contain untrusted external data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and pass values as discrete arguments after validation.

## Reference(s):

- [Tally ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton](https://maton.ai)
- [Tally API Introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API Reference](https://developers.tally.so/llms.txt)
- [Tally Help Center](https://help.tally.so/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and API-call guidance; API responses may be JSON from Tally or Maton.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
