## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Tally accounts through Maton-managed OAuth, including forms, submissions, workspaces, webhooks, and organization membership. It is best suited for tasks where the agent should read or list account data first, then ask for explicit approval before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton provides gateway access to the connected Tally account.

Mitigation: Use OAuth where possible, verify the intended Maton profile and Tally connection before use, request only needed scopes, and revoke unused connections.

Risk: Write, delete, organization membership, and invite operations can change data or account access.

Mitigation: Default to read and list operations first, then confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Webhooks can send respondent data, including personal information, to external URLs.

Mitigation: Confirm the destination URL, form, and event types with the user before creating or updating a webhook.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth; if an API key is unavoidable, do not print, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: Tally API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and keep follow-up endpoint or recipient choices under user control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Tally API Introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API Reference](https://developers.tally.so/llms.txt)
- [Tally Help Center](https://help.tally.so/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose API calls and request payloads; modifying operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
