## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and handling templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access WATI through Maton for WhatsApp contact lookup, message sending, template workflows, and related account operations. It is intended for tasks where the agent should prefer read/list calls and get explicit user approval before creating connections or performing writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send WhatsApp messages, including bulk and template messages, through the connected WATI account.

Mitigation: Confirm the exact account, connection, recipients, payload, and intended effect before approving any write or connection creation.

Risk: Long-lived API keys may be exposed if used instead of OAuth.

Mitigation: Prefer OAuth through the Maton CLI and avoid printing, storing, exporting, or passing API keys unless the CLI cannot be used.

Risk: Requests may affect the wrong WATI account when multiple Maton profiles or connections exist.

Mitigation: Pin the intended profile or connection before making calls, especially before POST, PUT, PATCH, or DELETE requests.

## Reference(s):

- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Maton CLI, raw HTTP, Python SDK, or JavaScript SDK calls; write operations require user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
