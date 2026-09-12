## Description:

Manus is an agent skill for using the Manus AI Agent API through Maton to create and manage tasks, projects, files, and webhooks with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Manus AI agent tasks, projects, files, and webhooks from an agent session while keeping credentials managed through Maton. It is intended for read/list workflows by default and requires confirmation before creating connections or changing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived API keys can be exposed when the raw API-key fallback is used.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and use the raw API-key path only when the CLI cannot be installed.

Risk: Write, delete, file upload, webhook, and connection operations can modify user data or account state.

Mitigation: Default to read and list calls, verify identifiers first, and obtain explicit user confirmation for every connection creation or mutating request.

Risk: Multiple Maton profiles or Manus connections can route a request to the wrong account.

Mitigation: Specify the intended profile or connection when more than one is available and apply least-privilege scope selection during authorization.

Risk: Manus API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, do not execute it, and avoid interpolating it into shell commands or follow-up requests without validation.

## Reference(s):

- [ClawHub Manus Skill](https://clawhub.ai/byungkyu/skills/manus-api)
- [Maton Homepage](https://maton.ai)
- [Manus API Overview](https://open.manus.im/docs)
- [Manus API Reference](https://open.manus.im/docs/api-reference)
- [Manus Website](https://manus.im)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for connection creation or mutating API calls.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
