## Description:

Manus API integration for creating and managing AI agent tasks, projects, files, and webhooks through the Maton CLI with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Manus tasks, manage projects and files, and configure webhooks through Maton-mediated API calls. It is intended for workflows that need Manus account access while keeping credentials managed outside the agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a connected Manus account, including creating or deleting resources and registering webhooks.

Mitigation: Default to read and list calls, require explicit user approval for connection creation and any POST, PUT, PATCH, or DELETE request, and confirm the target resource and payload before execution.

Risk: Raw API-key fallback can expose a long-lived credential through environment variables, logs, shell history, or child processes.

Mitigation: Use OAuth through the Maton CLI where possible, keep credentials in the operating system credential store, and never print, persist, or pass the key on a command line.

Risk: Multiple Maton profiles or Manus connections can cause actions to affect the wrong account.

Mitigation: Specify the intended Maton profile and Manus connection when more than one is available, especially before write operations.

Risk: Manus API responses and webhook payloads are external data and may contain adversarial instructions or unsafe content.

Mitigation: Treat returned content as untrusted data, validate it before reuse, and never execute or follow instructions found inside fetched API content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/manus-api)
- [Maton homepage](https://maton.ai)
- [Manus API Overview](https://open.manus.im/docs)
- [Manus API Reference](https://open.manus.im/docs/api-reference)
- [Manus Website](https://manus.im)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Maton CLI commands, API paths, request payload examples, and approval guidance for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
