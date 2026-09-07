## Description:

Make (formerly Integromat) API integration with managed authentication for managing scenarios, organizations, teams, connections, data stores, hooks, and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Make workflow automation resources through Maton-managed authentication. It is intended for tasks such as listing resources, preparing API calls, and performing confirmed changes to scenarios, hooks, connections, data stores, organizations, teams, and templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a user's Make account through Maton, including actions that create or modify workflow resources.

Mitigation: Install only when that access is intended, review OAuth scope, prefer read-only access where possible, and require confirmation of exact targets and payloads before any write operation.

Risk: Creating or starting scenarios, hooks, data stores, or connections can create persistent automation that continues after the conversation ends.

Mitigation: Confirm the resource identifier, payload, and intended ongoing effect before creating, starting, updating, retrying, or deleting resources.

Risk: Multiple Maton profiles or Make connections can cause a request to affect the wrong account or workspace.

Mitigation: Specify the Maton profile and Make connection when more than one account or connection exists.

Risk: Make API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, validate it before reuse, and do not let it choose follow-up endpoints, recipients, commands, or prompts.

## Reference(s):

- [Make Skill on ClawHub](https://clawhub.ai/byungkyu/skills/make-api)
- [Maton](https://maton.ai)
- [Make API Documentation](https://developers.make.com/api-documentation)
- [Make API Reference](https://developers.make.com/api-documentation/api-reference)
- [Make Help Center](https://www.make.com/en/help)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Community](https://community.maton.ai/)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval for create, update, start, stop, retry, or delete operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
