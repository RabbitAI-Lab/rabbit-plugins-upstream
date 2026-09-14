## Description:

Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, and managing document content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Google Docs through Maton-managed authentication, perform read/list operations, and make user-approved document changes or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Maton-mediated access to the selected Google Docs account.

Mitigation: Use OAuth where possible, grant only the account and scopes needed for the task, and revoke unused connections.

Risk: Write operations and automations can modify documents or create ongoing actions.

Mitigation: Approve each write, connection, function, trigger, or destination explicitly after reviewing the target, payload, and intended effect.

Risk: Trigger destinations can create persistent event forwarding.

Mitigation: Keep destinations on Maton-controlled endpoints unless the user intentionally approves a specific external host and data flow.

Risk: Package installs in the instructions are not independently hash-verified.

Mitigation: Use an isolated environment for the CLI and upgrade pinned tools deliberately after reviewing release notes.

## Reference(s):

- [ClawHub Google Docs Skill](https://clawhub.ai/byungkyu/skills/google-docs)
- [Maton Homepage](https://maton.ai)
- [Google Docs API Overview](https://developers.google.com/docs/api/how-tos/overview)
- [Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Request Types](https://developers.google.com/docs/api/reference/rest/v1/documents/request)
- [Document Structure](https://developers.google.com/docs/api/concepts/structure)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for authenticated Google Docs access through Maton.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
