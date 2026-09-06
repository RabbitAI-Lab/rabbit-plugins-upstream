## Description:

Basecamp API integration with managed OAuth for managing projects, to-dos, messages, schedules, documents, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect an agent to Basecamp through Maton OAuth, inspect project collaboration data, and perform approved changes to projects, to-dos, messages, schedules, documents, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized Basecamp connections can read or modify project, to-do, message, schedule, document, and collaboration data.

Mitigation: Use OAuth when possible, approve only the specific Basecamp account and scopes needed, default to read/list calls, and require clear confirmation before create, update, send, archive, trash, or delete operations.

Risk: Long-lived API keys can be exposed through environment variables, logs, shell history, command arguments, or persisted files.

Mitigation: Prefer OAuth and the operating system credential store; never print, persist, or pass credentials on command lines, and rotate any key that was exposed.

Risk: Multiple Maton profiles or Basecamp connections can route an operation to the wrong account.

Mitigation: Specify the intended profile and connection when ambiguity exists, then confirm the target resource and payload before any write.

Risk: Basecamp content returned by the API may contain untrusted instructions or unsafe text.

Mitigation: Treat returned messages, comments, fields, and webhook payloads as data; do not execute them or let them choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [Basecamp ClawHub Listing](https://clawhub.ai/byungkyu/skills/basecamp)
- [Maton Homepage](https://maton.ai)
- [Basecamp 4 API Documentation](https://github.com/basecamp/bc3-api)
- [Basecamp Authentication Guide](https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md)
- [Basecamp API Reference](https://github.com/basecamp/bc3-api#endpoints)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Code, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK calls through OAuth or an API key; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
